# 🧬 Breast Cancer Diagnostic: PCA & Clustering Analysis
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![Docker](https://img.shields.io/badge/Container-Docker-blue.svg)](https://www.docker.com/)

This project performs a comprehensive exploration of the **UCI Breast Cancer Wisconsin (Diagnostic) Dataset**. By leveraging **Principal Component Analysis (PCA)** and **K-Means Clustering**, we reduce complex biological features into interpretable dimensions to identify patterns between malignant and benign samples .

---

## 🚀 Key Features
*   **Data Standardization**: Implements `StandardScaler` to normalize high-dimensional medical data .
*   **Dimensionality Reduction**: Utilizes **PCA** to condense 30 features into 10 principal components, capturing over **95% of total variance** .
*   **Unsupervised Learning**: Applies **K-Means Clustering** to segment data points based on their geometric distribution in the PCA space .
*   **Performance Metrics**: Evaluates clustering quality using **Silhouette Score** and **Adjusted Rand Index (ARI)** .
*   **Containerization**: Ready for deployment via **Docker**.

---

## 🛠️ Technical Stack
*   **Data Handling**: `Pandas`, `NumPy` 
*   **Visualization**: `Matplotlib`, `Seaborn` 
*   **ML Engine**: `Scikit-Learn` (PCA, KMeans, Metrics) 
*   **Deployment**: `Docker`

---

## 📊 Analysis Pipeline

### 1. Feature Engineering & PCA
The project scales the 30 input features and extracts the most significant components:
*   **PC1** explains ~44.27% of variance .
*   **PC2** explains ~18.97% of variance .
*   **Top 10 components** account for a cumulative **95.16%** of the dataset's information .

### 2. Clustering Results
We partitioned the PCA-transformed data into 2 clusters (aligning with the Benign/Malignant nature of the target) :
*   **Silhouette Score**: `0.358` — Indicates reasonable cluster separation in high-dimensional space .
*   **Adjusted Rand Index (ARI)**: `0.671` — Demonstrates a strong correlation between the unsupervised clusters and the actual diagnostic labels .

---

## 📂 Project Structure
```bash
├── models/
│   ├── kmeans_model.pkl    # Serialized K-Means model
│   ├── pca.pkl             # Serialized PCA transformer
│   └── scaler.pkl          # Serialized StandardScaler
├── Breast-Cancer.ipynb     # Original Analysis & Research 
├── main.py                 # Application Entry Point
├── predict.py              # Prediction Logic & Interface
├── Dockerfile              # Containerization Script
├── requirements.txt        # Project Dependencies
└── README.md               # Project Documentation
