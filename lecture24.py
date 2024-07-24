"""
Correlation

Definition:

· Correlation measures the strength and direction of a linear relationship between two variables. The correlation coefficient (Pearson's r)
ranges from -1 to 1.

Use Case:

· Correlation analysis is used in finance to determine the relationship between different financial assets, helping in portfolio diversification.
"""


import pandas as pd
import numpy as np

# Generate sample data
data = {
'Age': np.random.normal(30, 10, 100).astype(int),
'Annual Income (K$)': np.random.normal(50, 20, 100).astype(int),
'Spending Score (1-100)': np.random.randint(1, 100, 100),
'Years with Company': np.random.normal(5, 2, 100).astype(int)

# Create DataFrame
df = pd.DataFrame(data)

df


#Correlation Matrix
pip install tabulate

from tabulate import tabulate
correlation_matrix = df.corr()

# Print the correlation matrix as a table
print(tabulate(correlation_matrix, headers='keys', tablefmt='grid', numalign="right", floatfmt=".2f"))
