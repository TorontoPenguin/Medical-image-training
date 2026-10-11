# 🧾 Metadata – CT Brain Tumor Segmentation Dataset

This folder contains **metadata information** describing the dataset structure, image attributes, annotation formats, and dataset generation process for the **CT Brain Tumor Segmentation Project**.

## 📘 Overview
The metadata defines:
- Dataset hierarchy and folder organization  
- Number of images and annotation files  
- Data formats and annotation types  
- Label definitions and class mappings  
- Dataset creation environment and annotation tools  

## 🧩 Dataset Summary
| Property | Description |
|-----------|-------------|
| **Dataset Name** | CT Brain Tumor Segmentation |
| **Modality** | CT Scan |
| **Number of Images** | 50 |
| **Image Format** | PNG |
| **Annotation Formats** | COCO (JSON), YOLO (TXT), CVAT (XML), Segmentation Masks (PNG) |
| **Segmentation Classes** | Tumor, Background |
| **Resolution** | 512 × 512 pixels |
| **Color Space** | Grayscale |
| **Tool Used** | CVAT 1.1 |
| **Annotation Type** | Polygonal & Pixel-wise segmentation |
| **Source** | Curated clinical CT scan cases for educational & AI research use |
| **Author** | Dr. Pradeep AI |
| **License** | Research & Non-commercial educational use |

## 🧠 Folder Hierarchy
ct_scans/
├── raw_data/
│ └── 50_ct_brain_raw_data_png/
├── annotated_data/
│ ├── COCO/
│ ├── YOLO/
│ ├── cvat_xml/
│ └── segmentation_masks/
├── metadata/
├── screenshots/
└── README.md

## 🧩 Key Components
- **Raw Data:** Original CT images used for annotation  
- **Annotated Data:** Labeled data exported in multiple formats  
- **Metadata:** Summary and versioning info for dataset tracking  
- **Screenshots:** Documentation of annotation workflow  

## 🧬 Dataset Version
| Field | Value |
|--------|--------|
| **Dataset Version** | v1.0 |
| **Created On** | October 2025 |
| **Last Updated** | October 2025 |
| **Annotation Tool** | CVAT 1.1 |
| **Exporter Tools** | CVAT Exporter, LabelMe Converter |

## 🧩 Label Mapping
0 → Background
1 → Tumor

## 📊 Suggested Metadata Files
If applicable, you can later include:
- **metadata.csv** – Dataset summary in tabular format  
- **metadata.json** – Machine-readable metadata for API or ML pipelines  

Example `metadata.json` structure:
```json
{
  "dataset_name": "CT Brain Tumor Segmentation",
  "num_images": 50,
  "annotation_formats": ["COCO", "YOLO", "CVAT_XML", "Segmentation_Masks"],
  "classes": ["Tumor", "Background"],
  "created_by": "Dr. Pradeep AI",
  "tool": "CVAT 1.1",
  "version": "v1.0"
}
🧾 Notes

This metadata helps AI engineers, researchers, and clients understand dataset content without opening annotation files.

Ideal for dataset indexing in open repositories or private annotation portfolios.

Future updates can include data statistics, label counts, and validation splits.

Author: Dr. Pradeep AI
Project: Medical-AI-Data-Annotation
Module: CT Brain Tumor Segmentation – Metadata
