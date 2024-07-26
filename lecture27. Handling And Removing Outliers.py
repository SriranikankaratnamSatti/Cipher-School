#Handling and Removing Outliers
"""
Definition:

Outliers:  
Outliers are data points that significantly deviate from other observations. They may result from inherent data variability or experimental errors.

Handling Outliers:  
This process involves identifying outliers and deciding whether to remove or adjust them to enhance the accuracy of statistical analyses and machine learning models.

Use Cases in Real Life:

Financial Data Analysis:  
  Detect and eliminate outliers in financial transaction data to avoid fraudulent activities and improve the precision of financial models.
Customer Data Management:  
  Manage customer data by addressing outliers in age, income, and spending to create precise customer segments and optimize marketing strategies.
Health Data Analysis:  
  Identify and manage outliers in patient health records, such as blood pressure and cholesterol levels, to ensure accurate diagnosis and treatment plans.
  """

import pandas as pd
# Load the dataset
df = pd.read_csv('outliers_data.csv')
print(df)


### Visualizing Outliers using Boxplots
import matplotlib.pyplot as plt

# Boxplot to visualize outliers in the Age column
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.boxplot(df['Age'].dropna())
plt.title('Boxplot of Age')

# Boxplot to visualize outliers in the Salary column
plt.subplot(1, 2, 2)
plt.boxplot(df['Salary'].dropna())
plt.title("Boxplot of Salary")
plt.show()

# Capping the outliers using the IQR method
df_capped = df.copy() 
for column in ['Age', 'Salary']:
    Q1 = df_capped[column].quantile(0.25)
    Q3 = df_capped[column].quantile(0.75)
    IQR = Q3-Q1 
    lower_bound = Q1-1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR 
    df_capped[column] = df_capped[column].apply(lambda x: upper_bound if x > upper_bound else (lower_bound if x < lower_bound else x))
print('Data after capping outliers using IQR method:')
print(df_capped)

# Replacing the outliers with median values
df_replaced = df.copy() 
for column in ['Age', 'Salary']:
    Q1 = df_replaced[column].quantile(0.25)
    Q3 = df_replaced[column].quantile(0.75)
    IQR = Q3-Q1 
    lower_bound = Q1-1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR 
    median = df_replaced[column].median()
    df_replaced[column] = df_replaced[column].apply(lambda x: median if x > upper_bound or x < lower_bound else x)
print('Data after replacing outliers with median values:')
print(df_replaced)
