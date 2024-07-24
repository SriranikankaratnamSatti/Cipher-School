#Feature Engineering & Selection
"""
Feature Engineering Methods

1. Handling Missing Values

Imputation: Fill missing values using mean, median, mode, or other appropriate values.

Example:

| Feature 1 | Feature 2 | Feature 3 |
|-----------|-----------|-----------|
| 0.1       | 0.2       | NaN       |
| 0.2       | NaN       | 0.6       |
| NaN       | 0.6       | 0.7       |

After imputation:

| Feature 1 | Feature 2 | Feature 3 |
|-----------|-----------|-----------|
| 0.1       | 0.2       | 0.65      |
| 0.2       | 0.4       | 0.6       |
| 0.15      | 0.6       | 0.7       |

2. Encoding Categorical Variables

One-Hot Encoding: Transform categorical variables into a set of binary columns.

Example:

| Color |
|-------|
| Red   |
| Blue  |
| Green |

After one-hot encoding:

| Color_Red | Color_Blue | Color_Green |
|-----------|------------|-------------|
| 1         | 0          | 0           |
| 0         | 1          | 0           |
| 0         | 0          | 1           |

3. Feature Scaling

Min-Max Scaling: Scale features to a specified range, typically [0, 1].

Example:

| Feature 1 | Feature 2 |
|-----------|-----------|
| 10        | 100       |
| 20        | 200       |
| 30        | 300       |

After min-max scaling:

| Feature 1 | Feature 2 |
|-----------|-----------|
| 0         | 0         |
| 0.5       | 0.5       |
| 1         | 1         |

4. Feature Creation

Polynomial Features: Generate new features by taking polynomial combinations of existing features.

Example:

| Feature 1 | Feature 2 |
|-----------|-----------|
| 1         | 2         |
| 3         | 4         |
| 5         | 6         |

After creating polynomial features (degree=2):

| Feature 1 | Feature 2 | Feature 1^2 | Feature 2^2 | Feature 1*Feature 2 |
|-----------|-----------|-------------|-------------|----------------------|
| 1         | 2         | 1           | 4           | 2                    |
| 3         | 4         | 9           | 16          | 12                   |
| 5         | 6         | 25          | 36          | 30                   |

Feature Selection Methods

1. Variance Thresholding

Explanation: This method removes all features whose variance does not meet a certain threshold. By default, it eliminates all zero-variance features, which are features that have the same value in all samples.

Example:

| Feature 1 | Feature 2 | Feature 3 | Constant |
|-----------|-----------|-----------|----------|
| 1         | 2         | 3         | 1        |
| 1         | 3         | 4         | 1        |
| 1         | 4         | 5         | 1        |
| 1         | 5         | 6         | 1        |
| 1         | 6         | 7         | 1        |

In this example, 'Feature 1' and 'Constant' have low or zero variance.

2. Correlation Matrix Filtering

Explanation: This method calculates the correlation matrix for the dataset features and removes one of each pair of highly correlated features to reduce redundancy.

Example:

| Feature 1 | Feature 2 | Feature 3 | Feature 4 |
|-----------|-----------|-----------|-----------|
| 1         | 2         | 2         | 5         |
| 2         | 4         | 4         | 6         |
| 3         | 6         | 6         | 7         |
| 4         | 8         | 8         | 8         |
| 5         | 10        | 10        | 9         |

In this example, 'Feature 2' and 'Feature 3' are highly correlated with 'Feature 1'.

3. Domain Knowledge

Explanation: This approach relies on field expertise to manually select the most relevant features. It leverages human understanding to identify which features are likely to be important.

Example:

| Age | Salary | Height | Weight |
|-----|--------|--------|--------|
| 25  | 50000  | 5.5    | 150    |
| 30  | 60000  | 6.0    | 160    |
| 35  | 70000  | 5.8    | 170    |
| 40  | 80000  | 5.9    | 180    |
| 45  | 90000  | 6.1    | 190    |

In this table, 'Age' and 'Salary' might be selected based on domain knowledge indicating their importance."""

# Code Examples

#Handling Missing Values

import pandas as pd
from sklearn.impute import SimpleImputer

# Sample data
data = {
    'Feature1': [1.0, 2.0, None, 4.0, 5.0], 
    'Feature2': [2.0, None, 4.0, 5.0, None], 
    'Feature3': [None, 3.0, 3.5, 4.0, 4.5]
}
df = pd.DataFrame(data)

# Handling missing values
imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print("After Imputation:\n", df_imputed)


#Encoding Categorical Variables

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample data
data = {
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']
}
df = pd.DataFrame(data)

# Encoding categorical variables
encoder = OneHotEncoder(sparse=False)
encoded_categories = encoder.fit_transform(df[['Color']])
df_encoded = pd.DataFrame(encoded_categories, columns=encoder.get_feature_names_out(['Color']))
df = pd.concat([df, df_encoded], axis=1).drop('Color', axis=1)
print("After One-Hot Encoding:\n", df)


#Feature Scaling

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Sample data
data = {
    'Feature1': [10, 20, 30, 40, 50],
    'Feature2': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)

# Feature scaling
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print("After Min-Max Scaling:\n", df_scaled)


#Feature Creation

import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

# Sample data
data = {
    'Feature1': [1, 2, 3, 4, 5], 
    'Feature2': [2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

# Feature creation
poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(df)
df_poly = pd.DataFrame(poly_features, columns=poly.get_feature_names_out(['Feature1', 'Feature2']))
print("After Creating Polynomial Features:\n", df_poly)


#Variance Thresholding

from sklearn.feature_selection import VarianceThreshold

# Sample data
data = {
    'Feature1': [1, 1, 1, 1, 1], 
    'Feature2': [2, 3, 4, 5, 6], 
    'Feature3': [3, 4, 5, 6, 7], 
    'Constant': [1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# Variance thresholding
selector = VarianceThreshold(threshold=0)
df_selected = selector.fit_transform(df)
print("After Variance Thresholding:\n", df_selected)


#Correlation Matrix Filtering

import pandas as pd

# Sample data
data = {
    'Feature1': [1, 2, 3, 4, 5], 
    'Feature2': [2, 4, 6, 8, 10], 
    'Feature3': [2, 4, 6, 8, 10], 
    'Feature4': [5, 6, 7, 8, 9]
}
df = pd.DataFrame(data)

# Correlation matrix
corr_matrix = df.corr()
print("Correlation Matrix:\n", corr_matrix)

# Identify highly correlated features
threshold = 0.9
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper.columns if any(upper[column] > threshold)]
df_re
