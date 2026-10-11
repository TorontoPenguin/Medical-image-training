# 🧠 CT Brain Tumor Segmentation — Annotation Project

A curated dataset of **50 CT brain scans** annotated for **tumor segmentation** using **CVAT**.  
This project demonstrates a structured medical computer vision annotation pipeline — ready for AI model training, validation, and healthcare research.

---

## 📘 Overview

| Attribute | Description |
|------------|--------------|
| **Modality** | CT (Computed Tomography) |
| **Region of Interest** | Brain |
| **Condition** | Tumor / Neoplastic lesion |
| **Dataset Size** | 50 CT slices |
| **Annotation Tool** | [CVAT – Computer Vision Annotation Tool](https://cvat.org/) |
| **Annotation Type** | Polygonal / Mask Segmentation |
| **Export Formats** | COCO JSON, Pascal VOC XML, Segmentation PNG |
| **Task Type** | Semantic Segmentation |
| **Purpose** | Medical image segmentation training, validation, and benchmarking |

This dataset provides both **polygonal and pixel-level segmentation** annotations for brain tumor detection, formatted for interoperability across deep learning frameworks.

---

## 📁 Folder Structure

50_ct_brain_tumor_annotation_project/
├── annotated_data/ # COCO, VOC, and mask exports from CVAT
│ ├── COCO/
│ ├── VOC/
│ └── segmentation_masks/
│
├── raw_data/ # Original 50 CT brain slices (.png)
├── metadata/ # Dataset descriptors and mapping files
├── screenshots/ # Visual documentation (proofs and exports)
└── README.md # This documentation file

---

## 🧩 Annotation Schema

| Class ID | Label | Description |
|-----------|--------|-------------|
| 0 | `background` | Non-tumor tissue or cranial structures |
| 1 | `tumor` | Visible tumor or abnormal lesion region |

Each exported format (COCO, VOC, Mask PNG) maintains a **unified class mapping** for consistent downstream model integration.

---

## ⚙️ Dataset Workflow Summary

| Step | Description |
|------|-------------|
| **1. Raw Data Preparation** | 50 CT scans curated, standardized to 512×512 resolution |
| **2. Annotation in CVAT** | Manual segmentation using polygon and brush tools |
| **3. Multi-format Export** | Data exported in COCO, VOC, and PNG mask formats |
| **4. Visual Proofing** | Annotation previews saved as screenshots and PDFs |
| **5. Documentation** | Metadata and labeling schema organized for reproducibility |

---

## 🧠 Applications

- Training segmentation models (U-Net, DeepLabV3+, Mask R-CNN)  
- Clinical image annotation workflow demonstration  
- Dataset structuring and cross-format conversion testing  
- Educational or research AI projects in neuroimaging  

---

## 🧰 Recommended Tools

| Task | Tools |
|------|--------|
| Annotation | CVAT |
| Visualization | FiftyOne, OpenCV, matplotlib |
| Model Training | MONAI, PyTorch Lightning, TensorFlow |
| Evaluation | Dice, IoU, Precision, Recall metrics |

---

## 🔗 Cross-References

| Folder | Description |
|---------|-------------|
| [`raw_data/`](./raw_data) | Original unannotated CT images |
| [`annotated_data/`](./annotated_data) | Segmentation data in COCO, VOC, and PNG formats |
| [`metadata/`](./metadata) | Dataset-level descriptors and schema info |
| [`screenshots/`](./screenshots) | Annotation proof and export verification visuals |

---

## 📸 Screenshot Previews

Annotation documentation includes:
- `01_project_overview.pdf`  
- `02_raw_data_preview.pdf`  
- `03_annotated_sample.pdf`  
- `04_export_formats_summary.pdf`

These files visually illustrate dataset creation and segmentation consistency.

---

## 📜 License

Licensed under the **MIT License**.  
© 2025 Dr. Pradeep Shanmugam — *MedDataForAI (Udyam Registered MSME, Government of India)*  

---

## 💡 Citation (APA Style)

Shanmugam, P. (2025). *CT Brain Tumor Segmentation — Medical AI Data Annotation Project.*  
Available at: [https://github.com/drpradeepAI/CTBrainTumorSegmentation-AnnotationProject](https://github.com/drpradeepAI/CTBrainTumorSegmentation-AnnotationProject)

---

## 🧾 Version Control

| Version | Date | Description |
|----------|------|-------------|
| **v1.0** | Nov 2025 | Initial release – 50 annotated CT brain scans (COCO, VOC, Mask PNG) |
| **v1.1 (Planned)** | 2026-Q1 | Addition of dataset cards and auto-metadata exports |

---

⭐ *If this project helps your research or workflow, please consider starring the repository!*
