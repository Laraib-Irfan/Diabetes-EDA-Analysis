🩺 Diabetes EDA & Statistical Analysis

Exploratory Data Analysis and statistical analysis of a large-scale diabetes dataset to uncover patterns, relationships, outliers, and important factors associated with diabetes classification.

📌 About the Project

This project performs a comprehensive Exploratory Data Analysis (EDA) and statistical analysis on a diabetes dataset using Python.

The main goals are to:

Understand the structure and quality of the dataset

Identify missing values and duplicate observations

Explore feature distributions

Detect and analyze outliers

Examine relationships between features and diabetes

Compare diabetic and non-diabetic groups statistically

Identify the most important patterns before future predictive modeling

📊 Dataset

Detail

Description

Original Observations

100,000

Features

9

Target Variable

diabetes

Target Encoding

0 = No diabetes • 1 = Diabetes

Duplicate Rows Found

3,854

Rows After Duplicate Removal

96,146

🛠️ Tools & Libraries

Python — Core programming language

Pandas — Data manipulation and cleaning

NumPy — Numerical operations

Matplotlib — Data visualization

Seaborn — Statistical visualization

SciPy — Statistical testing

Jupyter Notebook — Interactive analysis environment

🔍 EDA Performed

✅ Dataset structure and shape analysis

✅ Missing/null value analysis

✅ Duplicate detection and removal

✅ Distribution analysis using histograms

✅ Correlation analysis

✅ Correlation heatmap

✅ Outlier detection using IQR

✅ Lower and upper outlier analysis

✅ Scatter plots

✅ Bar plots

✅ Target distribution analysis

✅ Gender vs diabetes analysis

✅ Smoking history vs diabetes analysis

✅ Glucose-range analysis

📈 Statistical Analysis

1. Hypothesis Test — Blood Glucose vs Diabetes

An independent two-sample Welch's t-test was performed to determine whether mean blood glucose levels differ between diabetic and non-diabetic groups.

Hypotheses:

H₀: There is no significant difference in mean blood glucose between the two groups.

H₁: There is a significant difference in mean blood glucose between the two groups.

Statistic

Result

Mean glucose — Non-diabetic

132.85

Mean glucose — Diabetic

194.09

T-statistic

-94.79

P-value

< 0.001

Decision

Reject H₀

Conclusion: There is a statistically significant difference in mean blood glucose levels between diabetic and non-diabetic groups.

2. T-Test — BMI by Diabetes Status

A Welch's independent two-sample t-test was also performed to compare mean BMI between diabetic and non-diabetic groups.

Statistic

Result

Mean BMI — Non-diabetic

26.89

Mean BMI — Diabetic

31.99

T-statistic

-60.27

P-value

< 0.001

Decision

Reject H₀

Conclusion: There is a statistically significant difference in mean BMI between diabetic and non-diabetic groups.

📊 Target Distribution

The target variable is imbalanced:

Class

Percentage

Non-diabetic (0)

91.5%

Diabetic (1)

8.5%

⚠️ The class imbalance should be considered in future machine-learning modeling. Accuracy alone may not be sufficient; metrics such as precision, recall, F1-score, ROC-AUC, and a confusion matrix should also be considered.

🔗 Correlation with Diabetes

Feature

Correlation with diabetes

Blood Glucose Level

0.42

HbA1c Level

0.40

Age

0.26

BMI

0.21

Hypertension

0.20

Heart Disease

0.17

Gender

-0.04

Key Observation

Blood glucose level and HbA1c level showed the strongest positive correlations with diabetes in this dataset.

Correlation indicates an association between variables; it does not prove causation.

🚨 Outlier Analysis

Outliers were identified using the Interquartile Range (IQR) method.

Feature

Total Outliers

Lower

Upper

Age

0

0

0

BMI

7,086

1,121

5,965

HbA1c Level

1,315

0

1,315

Blood Glucose Level

2,038

0

2,038

Important Findings

Most detected outliers were on the upper side.

All identified upper outliers for HbA1c belonged to diabetes = 1.

All identified upper outliers for blood glucose belonged to diabetes = 1.

BMI outliers occurred in both diabetic and non-diabetic groups.

Outliers were not automatically removed because a statistical outlier is not necessarily an incorrect observation.

📌 Blood Glucose vs Diabetes

The analysis showed the following mean blood glucose levels:

Non-diabetic: 132.85

Diabetic: 194.09

The diabetic group had an average glucose level approximately 61.24 units higher than the non-diabetic group.

In the analyzed glucose ranges, all observations above 200 mg/dL were classified as diabetes = 1.

⚠️ This is a pattern observed in this dataset and should not be interpreted as a universal medical diagnostic threshold.

🚬 Smoking History vs Diabetes

Smoking History

No Diabetes

Diabetes

No Info

95.94%

4.06%

Current

89.79%

10.21%

Ever

88.21%

11.79%

Former

83.00%

17.00%

Never

90.47%

9.53%

Not current

89.30%

10.70%

The former smoking-history category had the highest observed diabetes percentage at 17%.

This represents an association in the dataset and does not establish a causal relationship.

👤 Gender vs Diabetes

Gender

No Diabetes

Diabetes

0.0

90.25%

9.75%

1.0

92.38%

7.62%

The diabetes percentages were relatively similar across the two gender categories, and gender had an almost negligible correlation with diabetes (r = -0.04).

🔑 Key Findings

Data Quality

3,854 duplicate rows were identified.

After removing duplicates, 96,146 rows remained.

No important missing-value problem was identified.

Class Distribution

91.5% of observations were non-diabetic.

8.5% were diabetic.

Strongest Relationships

Blood glucose: r = 0.42

HbA1c: r = 0.40

Age: r = 0.26

BMI: r = 0.21

Statistical Findings

Mean glucose was 132.85 for non-diabetic observations and 194.09 for diabetic observations.

The glucose t-test was statistically significant (p < 0.001).

Mean BMI was 26.89 for non-diabetic observations and 31.99 for diabetic observations.

The BMI t-test was statistically significant (p < 0.001).


🎯 Conclusion

The EDA and statistical analysis show that blood glucose level and HbA1c level are the most strongly associated features with diabetes in this dataset. BMI also showed a statistically significant difference between diabetic and non-diabetic groups.

The analysis also revealed a strong class imbalance and several upper-side outliers, which are important considerations for future predictive modeling.

Overall, this project provides a solid foundation for moving from data exploration to machine-learning-based diabetes prediction.

🚀 Future Work

The next stage of the project can include:

Feature encoding

Train-test split

Feature scaling where appropriate

Machine learning model training

Logistic Regression

Decision Tree

Random Forest

Model comparison

Confusion matrix

Precision, Recall, F1-score

ROC-AUC analysis

Hyperparameter tuning

👨‍💻 Author

Laraib Irfan
