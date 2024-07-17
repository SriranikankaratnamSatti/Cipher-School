#Working with Data using Pandas
#Pandas is a powerful and flexible open-source data analysis and manipulation library for python.
#It provides data structures like series (one-dimentional) and Data-Frame (two-Dimentional) that are efficient for handling large datasets.
#Pandas allows for data manipulation,aggregation and merging.

#USE case in real life
#Pandas can be used in various data analysis scenarios, such as customer data analysis, financial data analysis, and marketing campaign analysis.

#Creating a DataFrame from a Dictionary
pip install pandas
import pandas as pd
#creating a DataFrame from a Dictionary
data = {
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Age': [25,30,35],
  'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)


#Creating a DataFrame from a List of Dictionaries

data = [
  {'Name': 'Alice', 'Age': 25, "City': 'New York'},
  {'Name': 'Bob', 'Age': 30, "City': 'Los Angeles'},
  {'Name': 'Charlie', 'Age': 35, "City': 'Chicago'}
   ]
df = pd.DataFrame(data)


#Creating a DataFrame from a CSV File

#Assuming 'data.csv' is a csv file in the current directory
df = pd.read_csv('dataset.csv') #dataset.csv is file name
print(df)


#Viewing Data
#Displaying the first few rows
print(df.head()) #By default it will first 5 rows
print(df.head(10)) #now it will print top 10 rows

#Displaying the last few rows
print(df.tail())

#Getting information about the DataFrame
print(df.info())

#Descriptive Statistics
print(df.describe())

#Selecting Columns
#Selecting a single column
print(df['Name']) #will only print single column

#Selecting multiple columns
print(df[['Name','City']])

#Filtering Rows
#Filtering rows based on a condition
print(df[df['Age'] >30])

#Adding a new Column
df['Salary'] = [50000,60000,70000,80000,90000]
print(df)

#Modifying an Existing Columns
df['Age'] = df['Age'] + 1
print(df)

#Dropping Columns and Column
#Dropping a Column
df = df.drop(columns=['Salary'])
print(df)

#Dropping a Row
df = df.drop(index=1)
print(df)

#Grouping Data
#Grouping data by a column
grouped = df.groupby('City')
print(grouped['Age'].mean())

#Aggregating Data
#Aggregating Data using multiple functions
Aggregated = df.groupby('City').agg({'Age': ['mean', 'min', 'max']})

#merging DataFrames

df1 = pd.DataFrame({'ID':[1,2,3], 'Name':['Alice','Bob','Charlie']})
df2 = pd.DataFrame({'ID':[1,2,4], 'Salary':[50000,60000,70000]})

#Merging DataFrames on a Common Column
merger_df = pd.merge(df1, df2, on='ID', how='inner') #inner means intersection and outer means union
print(merger_df)


#Joining DataFrames
df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25,30]}, index=[0,1])
df2 = pd.DataFrame({'City': ['New York', 'Los Angeles']}, index=[0,2])

#Joining Dataframes on their index
joined_df = df1.join(df2, how = 'left')
print(joined_df)
