import os
import torch


def save_checkpoint(
    state,
    is_best,
    log_path,
    epoch=0,
    filename="checkpoint.pth.tar"
):
    # 如果当前epoch不是更好的验证结果，
    # 什么都不保存
    if not is_best:
        return

    save_dir = os.path.dirname(log_path)

    os.makedirs(
        save_dir,
        exist_ok=True
    )

    best_path = os.path.join(
        save_dir,
        "model_best.pth.tar"
    )

    # 直接覆盖该次运行此前的最佳模型
    torch.save(
        state,
        best_path
    )

    print(
        "=> 验证集最佳模型已更新："
        f"epoch={state.get('epoch')}，"
        f"path={best_path}"
    )