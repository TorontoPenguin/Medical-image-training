import math
import os
import random
import shutil
import time
import warnings

import torch
import torch.backends.cudnn as cudnn
import torch.distributed as dist
import torch.multiprocessing as mp
import torch.nn as nn
import torch.nn.parallel
import torch.optim
import torch.utils.data
import torch.utils.data.distributed
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.tensorboard import SummaryWriter

import models
from ops.config import parser
from training.schedule import lr_setter
from training.train import train
from training.validate import validate
from utilis.meters import AverageMeter
from utilis.saving import save_checkpoint

best_acc1 = 0


def main():
    args = parser.parse_args()
    if args.concat:
        args.sum = False
    # if args.dataset == "PACS":
    #     args.classes_num = 7
    # elif args.dataset == "VLCS":
    #     args.classes_num = 5
    # else:
    #     args.classes_num = 20
    dataset_classes = {
    "PACS": 7,
    "VLCS": 5,
}

    if args.dataset in dataset_classes:
        args.classes_num = dataset_classes[args.dataset]

    args.log_path = os.path.join(args.log_base, args.dataset, "log.txt")

    if not os.path.exists(os.path.dirname(args.log_path)):
        os.makedirs(os.path.dirname(args.log_path))

    if args.seed is not None:
        import numpy as np
    
        random.seed(args.seed)
        np.random.seed(args.seed)
        torch.manual_seed(args.seed)
        torch.cuda.manual_seed_all(args.seed)

    cudnn.deterministic = True
    cudnn.benchmark = False

    if args.gpu is not None:
        warnings.warn('You have chosen a specific GPU. This will completely '
                      'disable data parallelism.')

    if args.dist_url == "env://" and args.world_size == -1:
        args.world_size = int(os.environ["WORLD_SIZE"])

    args.distributed = args.world_size > 1 or args.multiprocessing_distributed

    ngpus_per_node = torch.cuda.device_count()
    main_worker(ngpus_per_node, args)


def main_worker(ngpus_per_node, args):
    global best_acc1

    if args.gpu is not None:
        print("Use GPU: {} for training".format(args.gpu))

    # if args.distributed:
    #     if args.dist_url == "env://" and args.rank == -1:
    #         args.rank = int(os.environ["RANK"])
    #     if args.multiprocessing_distributed:
    #         args.rank = args.rank * ngpus_per_node + gpu
    #     dist.init_process_group(backend=args.dist_backend, init_method=args.dist_url,
    #                             world_size=args.world_size, rank=args.rank)

    if args.pretrained:
        print("=> using pre-trained model '{}'".format(args.arch))
        model = models.__dict__[args.arch](pretrained=True, args=args)
    else:
        print("=> creating model '{}'".format(args.arch))
        model = models.__dict__[args.arch](args=args)

    # print('Freezing cnn parameters')
    # for param in model.parameters():
    #     param.requires_grad = False
    # model.fc1.weight.requires_grad = True
    # model.fc1.bias.requires_grad = True
    # print('Done')

    num_ftrs = model.fc1.in_features
    model.fc1 = nn.Linear(num_ftrs, args.classes_num)
    nn.init.xavier_uniform_(model.fc1.weight, .1)
    nn.init.constant_(model.fc1.bias, 0.)

    if args.distributed:
        if args.gpu is not None:
            torch.cuda.set_device(args.gpu)
            model.cuda(args.gpu)
            args.batch_size = int(args.batch_size / ngpus_per_node)
            args.workers = int((args.workers + ngpus_per_node - 1) / ngpus_per_node)
            model = torch.nn.parallel.DistributedDataParallel(model, device_ids=[args.gpu])
        else:
            model.cuda()
            model = torch.nn.parallel.DistributedDataParallel(model)
    elif args.gpu is not None:
        torch.cuda.set_device(args.gpu)
        model = model.cuda(args.gpu)
    else:
        # DataParallel will divide and allocate batch_size to all available GPUs
        if args.arch.startswith('alexnet') or args.arch.startswith('vgg'):
            model.features = torch.nn.DataParallel(model.features)
            model.cuda()
        else:
            model = torch.nn.DataParallel(model).cuda()

    # define loss function (criterion) and optimizer
    criterion = nn.CrossEntropyLoss().cuda(args.gpu)
    criterion_train = nn.CrossEntropyLoss(reduction="none").cuda(args.gpu)

    optimizer = torch.optim.SGD(model.parameters(), args.lr,
                                momentum=args.momentum,
                                weight_decay=args.weight_decay)

    # optionally resume from a checkpoint
    if args.resume:
        if os.path.isfile(args.resume):
            print("=> loading checkpoint '{}'".format(args.resume))
            if args.gpu is None:
                checkpoint = torch.load(
                args.resume,
                map_location=f"cuda:{args.gpu}" if args.gpu is not None else "cpu", weights_only=False,)
            else:
                loc = 'cuda:{}'.format(args.gpu)
                checkpoint = torch.load(args.resume, map_location=loc)
            model.load_state_dict(checkpoint['state_dict'])
            
            args.start_epoch = 0
            best_acc1 = 0
            
            print("=> checkpoint loaded successfully")
            # print("=> loaded checkpoint '{}' (epoch {})"
            #       .format(args.resume, checkpoint['epoch']))
        else:
            print("=> no checkpoint found at '{}'".format(args.resume))

    cudnn.benchmark = False

    traindir = os.path.join(args.data, 'train')
    valdir = os.path.join(args.data, 'val')
    test_root = args.test_data if args.test_data else args.data
    testdir = os.path.join(test_root, "test")
    # train_dataset = datasets.ImageFolder(
    #     traindir,
    #     transforms.Compose([
    #         transforms.RandomResizedCrop(224, scale=(args.min_scale, 1.0)),
    #         transforms.RandomHorizontalFlip(),
    #         transforms.ColorJitter(.4, .4, .4, .4),
    #         transforms.RandomGrayscale(args.gray_scale),
    #         transforms.ToTensor(),
    #         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    #     ]))

    train_dataset = datasets.ImageFolder(
    traindir,
    transforms.Compose([
        transforms.Grayscale(
            num_output_channels=3
        ),
        transforms.Resize((224, 224)),
        transforms.RandomRotation(5),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ]))

    if args.distributed:
        print("initializing distributed sampler")
        train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset)
    else:
        train_sampler = None

    train_loader = torch.utils.data.DataLoader(
        train_dataset, batch_size=args.batch_size, shuffle=(train_sampler is None),
        num_workers=args.workers, pin_memory=True, sampler=train_sampler, drop_last=True)

    # val_loader = torch.utils.data.DataLoader(
    #     datasets.ImageFolder(valdir, transforms.Compose([
    #         transforms.Resize((224, 224)),
    #         transforms.ToTensor(),
    #         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

    #     ])),
    #     batch_size=args.batch_size, shuffle=False,
    #     num_workers=args.workers, pin_memory=True)

    val_loader = torch.utils.data.DataLoader(
    datasets.ImageFolder(
        valdir,
        transforms.Compose([
            transforms.Grayscale(
                num_output_channels=3
            ),
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])
    ),
    batch_size=args.batch_size,
    shuffle=False,
    num_workers=args.workers,
    pin_memory=True)
    
    # test_loader = torch.utils.data.DataLoader(
    #     datasets.ImageFolder(testdir, transforms.Compose([
    #         transforms.Resize((224, 224)),
    #         transforms.ToTensor(),
    #         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

    #     ])),
    #     batch_size=args.batch_size, shuffle=False,
    #     num_workers=args.workers, pin_memory=True)

    test_loader = torch.utils.data.DataLoader(
    datasets.ImageFolder(
        testdir,
        transforms.Compose([
            transforms.Grayscale(
                num_output_channels=3
            ),
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])
    ),
    batch_size=args.batch_size,
    shuffle=False,
    num_workers=args.workers,
    pin_memory=True)

    log_dir = os.path.dirname(args.log_path)
    print('tensorboard dir {}'.format(log_dir))
    tensor_writer = SummaryWriter(log_dir)

    if args.evaluate:
        validate(test_loader, model, criterion, 0, True, args, tensor_writer)
        return

    for epoch in range(args.start_epoch, args.epochs):
        if args.distributed:
            train_sampler.set_epoch(epoch)
        lr_setter(optimizer, epoch, args)

        train(train_loader, model, criterion_train, optimizer, epoch, args, tensor_writer)

        val_acc1 = validate(val_loader, model, criterion, epoch, False, args, tensor_writer)
        # Test is evaluated once for reporting only.  It must not be used to
        # choose the checkpoint.
        test_acc1 = validate(
            test_loader,
            model,
            criterion,
            epoch,
            True,
            args,
            tensor_writer
        )

        is_best = val_acc1 > best_acc1
        best_acc1 = max(val_acc1, best_acc1)

        # This block must stay inside the epoch loop.  saving.py decides
        # whether to write the checkpoint from is_best, so only the current
        # validation-best model is retained.
        if (
            not args.multiprocessing_distributed
            or (
                args.multiprocessing_distributed
                and args.rank % ngpus_per_node == 0
            )
        ):
            save_checkpoint(
                {
                    "epoch": epoch + 1,
                    "arch": args.arch,
                    "state_dict": model.state_dict(),
                    "best_acc1": best_acc1,
                    "optimizer": optimizer.state_dict(),
                    "dataset": args.dataset,
                    "seed": args.seed,
                    "epochp": args.epochp,
                    "classes_num": args.classes_num,
                    "class_to_idx": train_dataset.class_to_idx,
                },
                is_best,
                args.log_path,
                epoch
            )

    tensor_writer.close()


if __name__ == '__main__':
    main()
