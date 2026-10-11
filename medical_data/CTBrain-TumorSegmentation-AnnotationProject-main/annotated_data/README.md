# 🧠 CT Brain Tumor – Annotated Data
This folder contains the annotated data for the 50 CT brain tumor segmentation project, created and exported from CVAT in multiple AI-compatible formats. These annotations represent pixel-level segmentation and bounding data for tumor regions in brain CT scans.

## 📂 Folder Structure
annotated_data/
├── COCO/                        # COCO JSON format for deep learning frameworks
│   └── 50_ct_brain_tumor_annotated_in_coco.json
├── YOLO/                        # YOLO segmentation in TXT format
│   ├── ct_0001.txt
│   ├── ct_0002.txt
│   └── ...
├── cvat_xml/                    # CVAT for images XML export format
│   └── 50_ct_brain_tumor_annotated_in_cvat.xml
├── segmentation_masks/           # Pixel-wise segmentation masks (semantic and instance)
│   ├── segmentation_class/
│   └── segmentation_object/
└── .keep

## 🧾 Annotation Details
- Annotation Tool: CVAT 1.1  
- Project Type: Medical Image Segmentation (CT Brain Tumor)  
- Annotation Task: Tumor detection and segmentation in brain CT images  
- Classes: Tumor, Background  
- Annotation Formats:  
  - COCO (.json): Object detection and segmentation annotations  
  - YOLO (.txt): Bounding box + segmentation polygon coordinates  
  - CVAT XML: Original CVAT export for interoperability  
  - Segmentation Masks: Class-wise and object-wise pixel masks for training

## 🧠 Data Description
- Total Annotated Images: 50  
- Modality: CT (Computed Tomography)  
- Target: Brain  
- Annotation Resolution: 512×512 pixels  
- Color Space: Grayscale (single channel)  
- Segmentation Type: Semantic and instance-level tumor masks  

## 🧩 Use Cases
This dataset can be directly used for:
- Training segmentation models (U-Net, DeepLab, nnU-Net, SegFormer, etc.)
- Object detection model fine-tuning (YOLOv8-seg, Detectron2, MMDetection)
- Validation or benchmarking of AI medical image workflows
- Dataset standardization or pipeline integration (COCO, CVAT, YOLO compatible)

## ⚙️ How to Use
1️⃣ YOLO Segmentation Format  
Each `.txt` file corresponds to a single CT image and follows YOLOv8 segmentation format:  
`<class_id> x1 y1 x2 y2 ... xn yn` where (x, y) are normalized polygon coordinates of the tumor.  

2️⃣ COCO Format  
Import directly into frameworks like Detectron2 or MMDetection:  
```python
from pycocotools.coco import COCO
coco = COCO("50_ct_brain_tumor_annotated_in_coco.json")
3️⃣ CVAT XML Format
Use for backup or reimport in CVAT to modify or verify annotations.

4️⃣ Segmentation Masks
Each image has corresponding mask files in two types:

segmentation_class: Class-wise semantic masks

segmentation_object: Instance-wise segmentation masks

🧬 Integration Tip

To train or visualize this dataset:

Clone the repository

Extract required annotation format folders

Load into your training framework (TensorFlow, PyTorch, MONAI, etc.)
Example:
dataset_path = "annotated_data/COCO/50_ct_brain_tumor_annotated_in_coco.json"
🧘 Notes

All data is anonymized and curated by Dr. Pradeep AI.

These annotations represent high-quality medical segmentation suitable for AI research, training, and benchmarking.

The dataset is designed for flexibility — supporting most major AI model formats.

The segmentation masks are derived directly from CVAT polygon data to ensure pixel-accurate representation.

Author: Dr. Pradeep AI
Project: Medical-AI-Data-Annotation
Module: CT Brain Tumor Segmentation (CVAT Annotation Workflow)
