#Introduction to Plotly
#Definition: Plotly is a graphing library that makes interactive,publication-quality graphs online.
#It Supports a wide variety of charts,including line plots,scatter plots,bar charts,histograms,heatmaps,and more.
#plotly is particularly useful for creating interactive visualization that can be embedded in web application and shared online.

#Key Features of Plotly

#1. Interactivity: Plotly charts are interactive by default, allowing users to zoom, pan, and hover over data points to get more information.
#2. Wide Range of Chart Types: Plotly supports a variety of chart types, including basic plots, statistical plots, 3D plots, and map.
#3. Customization: Extensive options to customize the appearance and behavior of charts.
#4. Integration: Easy integration with web applications and other libraries like Dash for building interactive dashboards.



import pandas as pd
sales_data = {
  'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02','2023-01-03'],
  'Region': ['North', 'South', 'East', 'West','North'],
  'Product': ['Product A', 'Product B', 'Product C', 'Product A','Product B'],
  'Sales': [1000,1500,2000,2500,3000],
  'Quantity': [50,60,70,80,90],
  'Profit': [200,300,400,500,600]
}

df = pd.DataFrame(sales_data)
print(df)
#The above data is same as written in sir's csv file


#Now install p  lotly
pip install plotly
import pandas as pd

#Load the dataset
df = pd.read_csv('sales_data.csv')
print(df.head())


#Creating a Line Plot
import plotly.express as px

#Create a line plot
fig = px.line(df, x='Date', y='Sales', title ='Sales Trend Over Time', markers=True)
fig.show()


#Create a Bar Chart
fig = px.bar(df, x='Region', y='Sales', title ='Sales by region', color='Region')
fig.show()


#Creating a Scatter Plot
fig = px.scatter(df, x='Sales', y='Profit', title ='Sales vs Profit', color='Region', size='Quantity', hover_data=['Product'])
fig.show()


#Creating a Histogram
fig = px.histogram(df, x='Sales', title ='Distribution of Sales',nbins=10)
fig.show()


#Create a Pie Chart
fig = px.pie(df, values='Sales', names='Product', title='Sales Distribution by Product')
fig.show()


#Create an interactive line Plot
fig = px.line(df, x='Date', y='Sales', title ='Interactive Sales Trend Over Time', markers=True, color='Region', hover_data=['Product', 'Quantity', 'Profit'])
fig.show()


#Will mark states of USA
import plotly.express as px

# Sample data
data = {
'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
'State': ['NY', 'CA', 'IL', 'TX', 'AZ'],
'Population': [8419000, 3980400, 2716000, 2328000, 1690000]

# Creating the DataFrame
df = pd.DataFrame(data)

# Create a geographical map
fig = px.choropleth(df, locations='State', locationmode='USA-states', color='Population', scope='usa', title='Population by State')
fig.show()

"""
Real-Life Use Cases

1. Sales Performance Analysis:

· Line Plot: Track sales trends over time to identify peak periods and dips.
· Bar Chart: Compare sales performance across different regions.
Pie Chart: Analyze the contribution of different products to total sales.
2. Customer Analysis:

· Scatter Plot: Visualize the relationship between customer spending (sales) and profitability (profit).
· Histogram: Understand the distribution of customer purchases.

3. Operational Efficiency:

· Heatmap: Identify correlations between operational metrics, such as sales, quantity, and profit, to optimize operations.
"""
