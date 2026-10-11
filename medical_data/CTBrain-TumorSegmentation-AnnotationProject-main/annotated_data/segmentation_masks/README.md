# 🧠 CT Brain Tumor – Segmentation Mask Annotations

This folder contains **pixel-wise segmentation masks** for 50 CT brain tumor images, exported from **CVAT** in PNG format.  
The masks are provided in both **class-level** and **object-level** formats, suitable for semantic and instance segmentation tasks.

## 📘 Folder Overview
- **File 1:** `50_ct_brain_tumor_annotated_in_segmentation_mask_CLASS-png_format.zip`  
  - Semantic segmentation masks where all tumor regions share a single label ID.
- **File 2:** `50_ct_brain_tumor_annotated_in_segmentation_mask_OBJECT-png_format.zip`  
  - Instance segmentation masks where each tumor object has a unique ID.
- **File 3:** `labelmap.txt` – defines class labels and corresponding pixel IDs.
- **Tool Used:** CVAT 1.1  
- **Images Annotated:** 50 CT brain PNG images  
- **Classes:** Tumor, Background  

## 🧩 Format Description
Each segmentation mask is a **PNG image** of the same size as the original CT image.  
- Pixel values correspond to label IDs defined in `labelmap.txt`.  
- Background pixels = 0, Tumor regions = non-zero values.  
- Mask colors are grayscale, optimized for machine readability.

Example labelmap:
0: background
1: tumor

## 🧠 Applications
- Deep learning segmentation models (U-Net, SegNet, DeepLabV3, etc.)
- Medical image visualization and dataset validation  
- Integration with COCO/YOLO datasets for multi-format training

Example usage:
```python
import cv2
mask = cv2.imread("mask_0001.png", cv2.IMREAD_GRAYSCALE)
unique_labels = set(mask.flatten())
print(unique_labels)
🧾 Notes

Both class-level and object-level masks are included for versatility.

All masks align perfectly with the raw CT images in pixel dimensions.

labelmap.txt ensures reproducibility and consistency across projects.

Author: Dr. Pradeep AI
Project: Medical-AI-Data-Annotation
Module: CT Brain Tumor – Segmentation Masks
