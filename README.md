# 🩺 Diabetes EDA Analysis

Exploratory Data Analysis on a large-scale diabetes dataset to uncover patterns, correlations, and risk indicators associated with diabetes diagnosis.


---

## 📌 About the Project

This project performs a comprehensive **Exploratory Data Analysis (EDA)** on a diabetes dataset using Python. The goal is to understand the underlying structure of the data, identify data quality issues, and surface the features most strongly associated with a diabetes diagnosis — laying the groundwork for future predictive modeling.

---

## 📊 Dataset

| Detail | Description |
|---|---|
| **Observations** | 100,000 |
| **Features** | 9 |
| **Target Variable** | `diabetes` |
| **Target Encoding** | `0` = No diabetes &nbsp;•&nbsp; `1` = Diabetes |

---

## 🛠️ Tools and Libraries

- **Python** — core programming language
- **Pandas** — data manipulation and cleaning
- **NumPy** — numerical operations
- **Matplotlib** — static visualizations
- **Seaborn** — statistical data visualization
- **Jupyter Notebook** — interactive analysis environment

---

## 🔍 EDA Performed

- ✅ Missing value analysis
- ✅ Duplicate detection and removal
- ✅ Distribution analysis
- ✅ Correlation analysis
- ✅ Outlier detection
- ✅ Scatter plots
- ✅ Bar plots
- ✅ Target distribution analysis
- ✅ Categorical feature analysis

---

## 🔑 Key Findings

### Data Quality
- **3,854 duplicate rows** were identified and removed.
- Dataset size after cleaning: **96,146 rows**.

### Class Balance
The target variable is notably **imbalanced**:

| Class | Percentage |
|---|---|
| Non-diabetic (`0`) | 91.5% |
| Diabetic (`1`) | 8.5% |

> ⚠️ This imbalance should be accounted for in any future modeling step (e.g., via resampling, class weighting, or appropriate evaluation metrics like F1-score or AUC-ROC rather than raw accuracy).

### Correlation with Target
| Feature | Correlation with `diabetes` |
|---|---|
| Blood Glucose Level | **0.42** |
| HbA1c Level | **0.40** |

These two features show the strongest linear relationship with diabetes status, consistent with their clinical relevance as diagnostic markers.

### Outliers
- Most detected outliers were concentrated on the **upper side** of feature distributions.

### Notable Pattern
- All observations with **glucose levels above 200 mg/dL** were classified as `diabetes = 1`, suggesting a strong (possibly threshold-based) diagnostic cutoff embedded in the data.

---
