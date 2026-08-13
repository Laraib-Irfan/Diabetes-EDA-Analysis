# 🩺 Diabetes EDA & Statistical Analysis

Exploratory Data Analysis and statistical analysis of a large-scale diabetes dataset to uncover patterns, relationships, outliers, and important factors associated with diabetes classification.

## 📌 About the Project

This project performs a comprehensive EDA and statistical analysis on a diabetes dataset using Python to:

- Understand the structure and quality of the dataset
- Identify missing values and duplicate observations
- Explore feature distributions and detect outliers
- Examine relationships between features and diabetes
- Compare diabetic and non-diabetic groups statistically
- Identify key patterns before future predictive modeling

## 📊 Dataset

| Detail | Description |
|---|---|
| Original Observations | 100,000 |
| Features | 9 |
| Target Variable | `diabetes` (0 = No diabetes, 1 = Diabetes) |
| Duplicate Rows Removed | 3,854 |
| Rows After Cleaning | 96,146 |

## 🛠️ Tools & Libraries

Python • Pandas • NumPy • Matplotlib • Seaborn • SciPy 

## 🔍 EDA Performed

- Missing value & duplicate detection
- Distribution analysis (histograms, boxplots)
- Correlation analysis & heatmap
- Outlier detection using IQR
- Target, gender, and smoking-history distribution vs diabetes
- Glucose-range analysis

## 📈 Statistical Analysis

**Blood Glucose vs Diabetes (Welch's t-test)**
- Mean glucose — Non-diabetic: 132.85 | Diabetic: 194.09
- T-statistic: -94.79, p < 0.001 → Reject H₀ (significant difference)

**BMI vs Diabetes (Welch's t-test)**
- Mean BMI — Non-diabetic: 26.89 | Diabetic: 31.99
- T-statistic: -60.27, p < 0.001 → Reject H₀ (significant difference)

## 🔑 Key Findings

- **Class imbalance:** 91.5% non-diabetic vs 8.5% diabetic — accuracy alone won't be a sufficient metric for future modeling.
- **Strongest correlations with diabetes:** Blood glucose (0.42), HbA1c (0.40), Age (0.26), BMI (0.21).
- **Outliers:** Mostly on the upper side for BMI, HbA1c, and glucose; all upper outliers for HbA1c and glucose belonged to diabetic cases. Not removed, since they may reflect real observations.
- **Blood glucose > 200 mg/dL** was associated with diabetes = 1 in this dataset (not a diagnostic threshold).
- **Smoking history:** "Former" smokers had the highest observed diabetes rate (17%).
- **Gender:** Near-negligible correlation with diabetes (r = -0.04).

> Correlation indicates association, not causation.

## 🎯 Conclusion

Blood glucose and HbA1c levels are the features most strongly associated with diabetes in this dataset, with BMI also showing a statistically significant difference between groups. The dataset's class imbalance and upper-side outliers are important considerations for future predictive modeling.

## 🚀 Future Work

- Feature encoding, train-test split, and scaling
- Model training: Logistic Regression, Decision Tree, Random Forest
- Model evaluation: confusion matrix, precision/recall/F1, ROC-AUC
- Hyperparameter tuning

## 👨‍💻 Author

Laraib Irfan
