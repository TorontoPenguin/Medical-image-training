# 🧠 CT Brain Tumor – COCO Format Annotation

This folder contains the **COCO 1.0 JSON annotation file** for the CT brain tumor segmentation dataset.

## 📘 File Overview
- **File:** `50_ct_brain_tumor_annotated_in_coco_1.0_json_format.json`
- **Format:** COCO (Common Objects in Context)
- **Tool Used:** CVAT 1.1
- **Images Annotated:** 50 CT brain images
- **Annotation Type:** Object detection and segmentation
- **Classes:** Tumor, Background

## 🧩 Usage
This COCO file can be directly used for:
- Object detection and segmentation model training (Detectron2, MMDetection, PyTorch)
- Dataset visualization using COCO API or CVAT viewer

Example:
```python
from pycocotools.coco import COCO
coco = COCO("50_ct_brain_tumor_annotated_in_coco_1.0_json_format.json")
🧠 Notes

Compatible with all COCO-based pipelines.

Derived from CVAT export for consistency and interoperability.

The file links directly to the original 50 CT scan images in the raw data folder.

Author: Dr. Pradeep AI
Project: Medical-AI-Data-Annotation
Module: CT Brain Tumor – COCO Format
