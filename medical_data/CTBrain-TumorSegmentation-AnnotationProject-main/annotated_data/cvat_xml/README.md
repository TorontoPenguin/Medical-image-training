# 🧠 CT Brain Tumor – CVAT XML Format Annotation

This folder contains **CVAT XML annotations** for 50 CT brain tumor images.  
The file represents the original annotation format exported directly from **CVAT**, maintaining full annotation hierarchy and metadata.

## 📘 File Overview
- **File Name:** `50_ct_brain_tumor_annotated_in_cvat_xml_format.xml`  
- **Format Type:** CVAT XML (CVAT native export)  
- **Tool Used:** CVAT 1.1  
- **Images Annotated:** 50 CT brain slices  
- **Annotation Type:** Polygon-based segmentation  
- **Classes:** Tumor, Background  

## 🧩 Structure
Each annotation entry in this XML file includes:
- Image metadata (file name, width, height, frame ID)
- Object class (e.g., Tumor)
- Polygonal region coordinates  
- Shape attributes (frame-level object tracking ready)

Simplified example:
```xml
<image id="1" name="ct_0001.png" width="512" height="512">
  <polygon label="tumor" points="123.5,145.2;130.1,150.3;..."/>
</image>
Use Cases

Restoring projects in CVAT

Conversion to other formats (COCO, YOLO, Pascal VOC)
cvat-cli dump <task_id> --format "COCO 1.0" --output "converted_coco.json"
Notes

This XML file preserves the original annotations as exported from CVAT.

Suitable for re-importing into CVAT for modification or validation.

Each polygon corresponds to a segmented tumor region.

Author: Dr. Pradeep AI
Project: Medical-AI-Data-Annotation
Module: CT Brain Tumor – CVAT XML Format
