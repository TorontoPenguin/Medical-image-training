# 🧠 CT Brain Tumor – Raw Data
This folder contains the raw CT brain images used for tumor segmentation annotation in CVAT as part of the Medical AI Data Annotation Project.

## 📂 Folder Structure
raw_data/
├── 50_ct_brain_raw_data_png/                # Folder with 50 original CT brain images
│   ├── ct_0001.png
│   ├── ct_0002.png
│   └── ...
├── 50_ct_brain_tumor_raw_data_png_format.zip  # Compressed archive of all 50 images
└── .keep

## 🩻 Data Description
- Total Images: 50  
- Modality: CT (Computed Tomography)  
- Anatomical Region: Brain  
- Clinical Focus: Tumor segmentation  
- Format: PNG  
- Resolution: 512 × 512 pixels  
- Color Space: Grayscale (single channel)  
- Annotation Platform: CVAT 1.1  
- Annotation Type: Semantic segmentation (binary masks created separately)

## 🧾 File Naming Convention
Each CT image corresponds 1:1 with a segmentation mask file of the same index:

| Raw Image | Segmentation Mask |
|------------|------------------|
| ct_0001.png | mask_0001.png |
| ct_0002.png | mask_0002.png |
| ... | ... |

This structure ensures direct pairing between raw and mask data during preprocessing or model training.

## 🧰 Usage
You can use these CT images for:
- Deep learning segmentation model training (U-Net, nnU-Net, DeepLab, MONAI, etc.)
- Validation and benchmarking of AI segmentation pipelines
- Research and dataset augmentation tasks

To prepare the dataset:
1. Download `50_ct_brain_tumor_raw_data_png_format.zip`
2. Extract it using:
unzip 50_ct_brain_tumor_raw_data_png_format.zip
3. All 50 CT slices will be available inside `50_ct_brain_raw_data_png/`.

## 📘 Source
- Creator: Dr. Pradeep AI  
- Dataset: Medical-AI-Data-Annotation → Computer Vision → Radiology → CT Scans → Raw Data  
- Annotation Tool: CVAT  
- Purpose: Brain tumor segmentation model development and research dataset structuring.

## 🧩 Notes
- Each raw CT image has a corresponding segmentation mask in the `annotated_data/segmentation_masks/` folder.  
- Data is anonymized and formatted for use in AI/ML pipelines.  
- Recommended preprocessing: normalization, resizing (512×512), grayscale conversion (if needed).

**Author:** Dr. Pradeep AI  
**Project:** Medical-AI-Data-Annotation  
**Module:** CT Brain Tumor Segmentation (CVAT Annotation Workflow)
