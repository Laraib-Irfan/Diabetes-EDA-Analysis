import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
df=pd.read_csv("diabetes_dataset.csv")

# Quick structural checks before plotting or transforming the dataset
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Total rows containing at least one null value
null_rows = df.isnull().any(axis=1).sum()

# Total columns containing at least one null value
null_columns = df.isnull().any(axis=0).sum()

print("Total null rows:", null_rows)
print("Total null columns:", null_columns)

print(df.head(5))

# Distribution overview for all numeric columns
df.hist(figsize=(10,10),bins=20,rwidth=0.8)
plt.tight_layout()
plt.show()

# Encode categorical columns so they can be included in the correlation heatmap
df['gender']=df['gender'].map({'Male':0, 'Female':1})
df['smoking_history']=df['smoking_history'].map(
    {'never':0,
     'current':1,
     'former':2,
     'not cuurent':3,
     'No Info':4,
     'ever':5}
)
plt.figure(figsize=(10,10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.show()
plt.tight_layout()
plt.savefig('correlation_heatmap.png')

# Compare age distribution between encoded gender categories
plt.figure(figsize=(10,10))
sns.boxplot(x='gender',y='age',data=df)
plt.tight_layout()
plt.show()
plt.savefig('boxplot.png')

# Check spread and possible outliers across all numeric fields
plt.figure(figsize=(15,15))
sns.boxplot(data=df)
plt.xticks(rotation=45)
plt.show()

# Detect outliers in key continuous health indicators using the IQR rule
num_columns=df[['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']]
Q1=num_columns.quantile(0.25)
Q3=num_columns.quantile(0.75)
IQR= Q3-Q1
outliers=((num_columns<Q1-1.5*IQR)| (num_columns>Q3+1.5*IQR))
print(f"Number of outliers: {outliers.sum()}")

# Separate lower and upper outliers to understand which direction each feature skews
numeric_cols = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']

Q1 = df[numeric_cols].quantile(0.25)
Q3 = df[numeric_cols].quantile(0.75)
IQR = Q3 - Q1

lower_mask = df[numeric_cols].lt(Q1 - 1.5 * IQR)   #lt for less than 
upper_mask = df[numeric_cols].gt(Q3 + 1.5 * IQR)   # gt for greater than

print("Lower outliers:")
print(lower_mask.sum())

print("\nUpper outliers:")
print(upper_mask.sum())

# Inspect upper outlier limits against maximum observed values
for col in numeric_cols:
    upper_limit=Q3[col]+1.5*IQR[col]

    print(f"\n{col}")
    print(f"Upper limit:{upper_limit}")
    print(f"maximun value: {df[col].max()}")

# Compare diabetes counts among clinically important upper-outlier groups
hba1c_outliers=df[df["HbA1c_level"]>8.3]
bmi_outliers=df[df['bmi']>38.5]
glucose_outliers=df[df['blood_glucose_level']>247.5]
print(f"\n BMI outliers: {len(bmi_outliers)}")
print(bmi_outliers['diabetes'].value_counts())
print(f"\n HbA1c outliers: {len(hba1c_outliers)}")
print(hba1c_outliers['diabetes'].value_counts())
print(f"\n Glucose outliers: {len(glucose_outliers)}")
print(glucose_outliers['diabetes'].value_counts())


# Duplicate-row check before deciding whether cleaned analysis should drop repeats
duplicates=df.duplicated()
print(f"number of duplicates: {duplicates.sum()}")
print(df[df.duplicated()].head())

print(f"Total duplicated rows: {df.duplicated().sum()}")
print(f"Rows after removing duplicates: {df.drop_duplicates().shape[0]}")
print("original shape:",df.shape)

# Relationship between glucose, BMI, and diabetes diagnosis
plt.figure(figsize=(10,10))
sns.scatterplot(x='blood_glucose_level',hue='diabetes', y='bmi', data=df)
plt.title('Blood glucose level VS bmi')
plt.tight_layout()
plt.xlabel('Blood glucose level')
plt.ylabel('BMI')
plt.savefig('scatter_plot.png')
plt.show()

# Compare glucose levels between diabetic and non-diabetic groups
plt.figure(figsize=(10,10))
sns.boxplot(x='diabetes',y='blood_glucose_level',data=df)
plt.title('Blood glucose level VS diabetes')
plt.tight_layout()
plt.savefig('Blood glucose vs diabetes')
plt.show()


# Mean glucose level by diagnosis class
plt.figure(figsize=(10,10))
sns.barplot(x='diabetes',y='blood_glucose_level',data=df)
plt.title('Blood glucose level VS diabetes')
plt.tight_layout()
plt.savefig('Blood glucose vs diabetes barplot')
plt.show()

# Trend glucose levels by age while separating diabetes diagnosis
plt.figure(figsize=(10, 6))
sns.lineplot(x='age', y='blood_glucose_level', hue='diabetes', data=df, palette='husl')
plt.title('Glucose Levels over Age by Diagnosis')
plt.xlabel('Age')
plt.ylabel('Glucose')
plt.legend(title='Diagnosis')
plt.grid(True)
plt.tight_layout()
plt.show()

# Bucket glucose values to estimate diabetes percentage within each glucose range
bins=[0,100,120,140,160,180,200,220,240,260,300]
labels=['0-100','101-120','121-140','141-160',
    '161-180', '181-200', '201-220', '221-240',
    '241-260', '261-300']

df['glucose_range']=pd.cut(df['blood_glucose_level'],
                           bins=bins,
                           labels=labels)

diabetes_percentage = df.groupby(
    'glucose_range',
    observed=True
)['diabetes'].mean() * 100

print(diabetes_percentage)

plt.figure(figsize=(10,6))
sns.barplot(x=diabetes_percentage.index, y=diabetes_percentage.values)
plt.title('Percentage of diabetes cases by blood glucose level range')
plt.xlabel('Blood Glucose level range')
plt.ylabel('Percentage of diabetes cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('diabetes_percentage_by_glucose_level_range.png')
plt.show()

df['diabetes'].value_counts()
print(df['diabetes'].value_counts(normalize=True)*100)

# Percentage breakdowns for diabetes by categorical risk factors
print(pd.crosstab(df['gender'],df['diabetes'], normalize='index')*100)
print(pd.crosstab(df['smoking_history'], df['diabetes'], normalize='index')*100)
print(df['smoking_history'].value_counts())


