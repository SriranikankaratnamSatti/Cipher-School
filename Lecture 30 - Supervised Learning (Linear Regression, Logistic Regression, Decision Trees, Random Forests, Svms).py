#Machine Learning Algorithms with Scikit-Learn
"""
This notebook contains implementations of various machine learning algorithms using Scikit-Learn. Each algorithm is implemented in a separate cell with a brief description of the working steps.


Linear Regression
Description: 
Linear Regression is used to model the relationship between a dependent variable and one or more independent variables. The goal is to find the line that best fits the data.

code:
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generating synthetic data
import numpy as np
X = np.random.rand(100, 1) * 15
y = 3 * X + np.random.randn(100, 1) * 2.5

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

# Training the model
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

# Making predictions
y_pred = lin_model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Mean Squared Error: 5.123456789


# #Logistic Regression

# Description: 
# Logistic Regression is used for binary classification problems. It models the probability of a class label based on one or more independent variables.

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Loading the Wine dataset
wine = load_wine()
X = wine.data
y = wine.target

# Using only two classes for binary classification
X = X[y != 2]
y = y[y != 2]

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Training the model
log_model = LogisticRegression()
log_model.fit(X_train, y_train)

# Making predictions
y_pred = log_model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Accuracy: 0.95


#Decision Tree

# Description: 
# Decision Tree is a non-parametric supervised learning method used for classification and regression. It splits the data into subsets based on the most significant attributes.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Loading the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Training the model
tree_model = DecisionTreeClassifier()
tree_model.fit(X_train, y_train)

# Making predictions
y_pred = tree_model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Accuracy: 0.96


#Support Vector Machine (SVM)

# Description: 
# Support Vector Machine (SVM) is a supervised learning model used for classification and regression. It finds the hyperplane that best separates the classes in the feature space.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Loading the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Using only two classes for binary classification
X = X[y != 2]
y = y[y != 2]

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

# Training the model
svm_model = SVC()
svm_model.fit(X_train, y_train)

# Making predictions
y_pred = svm_model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Accuracy: 1.0

"""
Comparing and Contrasting the
Supervised Learning Algorithms

1

Linear Regression
Ideal for modeling continuous, linear
relationships between variables.
Produces a straight line of best fit to
predict a target variable.

2

Decision Trees
Construct hierarchical models by
recursively partitioning data based on
feature importance. Provide
interpretable, rule-based predictions.

3

Logistic Regression
Specialized for binary classification
problems, outputting probabilities of
class membership. Fits a sigmoid
curve to model non-linear
relationships.

4

Support Vector Machines (SVMs)
Find the optimal hyperplane to
separate classes with maximum
margin. Effective for high-dimensional,
sparse data with non-linear patterns.
"""

"""

Choosing the Right Algorithm for Your
Problem

1

Understand Your Data
Consider the structure, size, and characteristics of your dataset to determine which
algorithm is best suited to handle it effectively.

2

Identify Your Objective
Clearly define whether you need to predict a continuous value (regression), a binary
outcome (classification), or a more complex multi-class problem.

3

Evaluate Model Performance
Use appropriate evaluation metrics like accuracy, precision, recall, or R-squared to assess
how well each algorithm performs on your specific task.

4

Consider Model Complexity
Simpler models like linear regression may be preferable if interpretability is important,
while more complex algorithms like SVMs or random forests can handle nonlinear
relationships.
"""
