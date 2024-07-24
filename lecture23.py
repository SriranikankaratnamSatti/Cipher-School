#Descriptive Statistics - Mean

import pandas as pd

# Sample data
data = {
'Age': [25, 30, 35, 50, 28, 40, 50, 60, 32, 45],
'Salary': [50000, 1200000, 70000, 60000, 80000, 55000, 85000, 90000, 1500000, 62000]

}

df = pd.DataFrame(data)

# Mean
mean_age = df['Age'].mean()
mean_salary = df['Salary'].mean()

print("Mean Age:", mean_age)
print("Mean Salary:", mean_salary)

#Descriptive Statistics - Median

# Median
median_age = df['Age'].median()
median_salary = df['Salary'].median()

print("Median Age:", median_age)
print("Median Salary:", median_salary)

#Descriptive Statistics - Mode

# Mode
mode_age = df['Age'].mode()[0]
mode_salary = df['Salary'].mode()[0]

print("Mode Age:", mode_age)
print("Mode Salary:", mode_salary)

#Descriptive Statistics - Standard Deviation
"""
Definition:

. The standard deviation measures the amount of variation or dispesion in a set of values. It indicates how much the values
differ from the mean.

Use Case:

. Standard deviation is used in finance to measure the risk or volatility of an investment.
"""


#Descriptive Statistics - Variance
"""
Definition:

. The variance measures the dispersion of a set of values. It is the average of the squared differences from the mean.

Use Case:

· Variance is used in finance to assess the spread between numbers in a dataset, such as investment returns.
"""

# Variance
var_age = df['Age'].var()
var_salary = df['Salary'].var()

print("Variance Age:", var_age)
print("Variance Salary:", var_salary)

#Probability Distributions - Normal Distribution
"""
Definition:

. The normal distribution is a continuous probability distribution that is symmetrical around the mean. It is also known as the Gaussian
distribution.

Use Case:

· The normal distribution is used in finance to model returns on investment and in quality control to monitor product defects.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Normal Distribution
mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)

# Plotting the histogram
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma . np.sqrt(2 * np.pi)) . np.exp(-(bins - mu) ** 2 / (2 * sigma ** 2)), linewidth=2, color='r')
plt.title('Normal Distribution')
plt.show()

#Probability Distributions - Binomial Distribution
"""
Definition:

. The binomial distribution is a discrete probability distribution that models the number of successes in a fixed number of trials, with each
trial having two possible outcomes.

Use Case:

· The binomial distribution is used in quality control to model the number of defective items in a batch of products.
"""
# Binomial Distribution
n, p = 10, 0.5
binomial = np.random.binomial(n, p, 1000)

# Plotting the histogram
plt.hist(binomial, bins=10, density=True, alpha=0.6, color='b')
plt.title('Binomial Distribution')
plt.show()


#Quartiles
"""
Definition

Quartiles are values that divide a dataset into four equal parts. They are used to understand the distribution of the data and are particularly
useful in identifying the spread and the presence of outliers.

Key Points

1. Q1 (First Quartile): The median of the lower half of the dataset (25th percentile).
2. Q2 (Second Quartile or Median): The median of the dataset (50th percentile).
3. Q3 (Third Quartile): The median of the upper half of the dataset (75th percentile).
4. IQR (Interquartile Range): The difference between the third and first quartiles (IQR = Q3- Q1). IQR is used to measure the spread of the
middle 50% of the data.
"""

import numpy as np

# Sample data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate Quartiles
Q1 = np.percentile(data, 25)
Q2 = np.median(data)
Q3 = np.percentile(data, 75)
IQR= Q3 -Q1

print(f"Q1: {Q1}")
print(f"Q2 (Median): {Q2}")
print(f"Q3: {Q3}")
print(f"IQR: {IQR}")


#Z-Scores
"""
Definition

A Z-score (or standard score) measures how many standard deviations an element is from the mean. It is used to identify outliers and to
compare different data points from different normal distributions.

Interpretation

· A Z-score of 0 indicates that the data point's score is identical to the mean score.
· A Z-score of 1.0 indicates a value that is one standard deviation from the mean.
. Z-scores can be positive or negative, indicating whether they are above or below the mean and by how many standard deviations.
"""
import numpy as np

# Sample data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Calculate Z-scores
z_scores = [(x - mean) / std_dev for x in data]
