#Data Cleaning and Normalization
"""
Overview:
Data Cleaning:
Data cleaning is the process of detecting and correcting (or removing) errors and inconsistencies in data to enhance its quality. Typical tasks include dealing with missing values, eliminating duplicates, correcting mistakes, and ensuring uniformity in data formats.

Normalization:
Normalization involves scaling numerical data to a common range, often between 0 and 1, or transforming it to have a mean of 0 and a standard deviation of 1. This technique boosts the performance of machine learning models and ensures all features contribute equally.

Practical Applications:
Machine Learning Data Preparation:
Address missing values and remove duplicates to maintain clean data. Normalize features to enhance the efficiency of machine learning algorithms.
Financial Data Analysis:
Fix errors in transaction data and impute missing values. Normalize financial metrics to allow for comparisons across different scales.
Customer Data Management:
Maintain consistency in customer records and correct incorrect entries. Normalize customer age and income data for effective segmentation analysis.
"""

import pandas as pd
# Load the dataset
df = pd.read_csv('sample_data.csv')
print(df)

# Check for missing values
print(df.isnull().sum())
df.info()

# Remove rows with any missing values
df_cleaned = df.dropna()
print(df_cleaned)

# Fill missing values with specific values
df_filled = df.fillna({
    'Age': df['Age'].mean(),
    'Salary': df['Salary'].mean()
})
print(df_filled)

# Forward fill method to propagate the previous values forward
df_ffill = df.fillna(method='ffill')
print(df_ffill)
# Backward fill method to propagate the next values backward
df_bfill = df.fillna(method='bfill')
print(df_bfill)

# Add duplicate rows for demonstration
df = pd.concat([df, df.iloc[[0]], df.iloc[[1]]], ignore_index=True)
print('Before removing duplicates: \n', df)
# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()
print('After removing duplicates: \n', df_no_duplicates)

# Replace incorrect values in the 'Department' column
df_corrected = df.replace({'Department': {'HR': 'Human Resources', 'Sales': 'Sales'}})
print(df_corrected)

# Convert all department names to lowercase for consistency
df['Department'] = df['Department'].str.lower()
print(df)

# Apply Min-Max normalization using the formula
df_normalized = df.copy()
for col in ['Age', 'Salary']:
    df_normalized[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
  
# Print original and normalized values
print("Original DataFrame:")
print(df)
print("\nNormalized DataFrame:")
print(df_normalized)

"""
Definition:
Min-max normalization:
This technique rescales the values of a feature to a fixed range, usually [0, 1]. It transforms each value in the feature to fit within this range.

Formula:
The formula for min-max normalization is:

Xnormalized=X-Xmin/Xmax-Xmin
Where:

X is the original value.
X min is the minimum value in the feature.
X max is the maximum value in the feature.
X normalized is the normalized value.
"""
