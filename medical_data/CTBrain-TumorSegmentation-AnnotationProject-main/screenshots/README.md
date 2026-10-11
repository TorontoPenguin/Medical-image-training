# 📸 CT Brain Tumor Segmentation – Screenshots and Documentation

This folder contains **visual documentation and supporting materials** for the **CT Brain Tumor Segmentation Dataset**.  
The screenshots and PDFs illustrate every major stage of the data preparation, annotation, and export workflow in **CVAT**.

## 📘 Folder Overview
- **screenshots_png_images/** – Contains 26 PNG screenshots captured during dataset creation and annotation in CVAT.  
- **01_project_overview.pdf** – Overview of dataset structure, project purpose, and annotation strategy.  
- **02_raw_data_preannotation_preview.pdf** – Visualization of the original CT scans before annotation.  
- **03_annotated_sample_data.pdf** – Examples of annotated tumor regions with masks and polygons.  
- **04_export_settings_and_data.pdf** – Summary of export settings used for generating YOLO, COCO, and CVAT XML outputs.  
- **.keep** – Maintains folder structure in GitHub.  

## 🧩 Purpose
The screenshots and PDFs provide:
- Transparent **proof of work** for annotation quality and process accuracy.  
- Step-by-step visualization of how segmentation data was created.  
- Easy reference for clients, collaborators, or researchers replicating the process.  

## 🧠 Usage
These visuals can be used for:
- Presentation and reports demonstrating dataset pipeline design.  
- Quick understanding of image quality and annotation coverage.  
- Cross-checking between raw images and annotated masks.

Example:
```python
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("screenshots_png_images/annotation_sample_01.png")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
🧾 Notes

All screenshots correspond to the 50 CT brain tumor images in the raw data folder.

Each PDF serves as a compact documentation reference.

The folder ensures full reproducibility and validation transparency.

Author: Dr. Pradeep AI
Project: Medical-AI-Data-Annotation
Module: CT Brain Tumor Segmentation – Screenshots & Visual Documentation
