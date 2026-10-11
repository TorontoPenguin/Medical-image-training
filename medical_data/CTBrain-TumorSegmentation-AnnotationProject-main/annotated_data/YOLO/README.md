# 🧠 CT Brain Tumor – YOLO Format Annotation

This folder contains YOLO segmentation annotations for 50 CT brain tumor images, created and exported using **CVAT** in **YOLO TXT format**.

## 📘 Folder Overview
- **Main Folder:** `50_ct_brain_annotated_YOLO/`  
- **File Count:** 50 `.txt` annotation files (one per image)  
- **Compressed Version:** `50_ct_brain_tumor_annotated_in_yolo_txt_format.zip`  
- **Tool Used:** CVAT 1.1  
- **Format Type:** YOLO segmentation (bounding box + polygon)  
- **Classes:** Tumor, Background  

## 🧩 Usage
Each `.txt` file corresponds to a single CT image and contains normalized coordinates of the tumor region.  
File structure (YOLOv8-seg format):
<class_id> x1 y1 x2 y2 ... xn yn
where `x` and `y` are normalized between 0 and 1 relative to image width and height.

Example:
0 0.512 0.234 0.640 0.250 0.678 0.360 0.515 0.355

### Example Loading in Python
```python
with open("ct_0001.txt") as f:
    yolo_data = f.readlines()
print(yolo_data)
Applications

Training segmentation models like YOLOv8-seg, Ultralytics, or Roboflow pipelines

Bounding box & polygon-level tumor localization

Dataset interoperability with detection frameworks

🧾 Notes

The .zip file provides the entire YOLO annotation set for quick download.

All .txt files are paired with corresponding .png images in the raw data folder.

Each file defines one or more polygonal tumor masks per image.

Author: Dr. Pradeep AI
Project: Medical-AI-Data-Annotation
Module: CT Brain Tumor – YOLO Format
