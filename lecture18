#Introduction to Matplotlib and Seaborn

#Matplotlib : Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. 
#It provides anobject-oriented API for embedding plots into applications using general-purpose GUI toolkits.


#Seaborn : Seaborn is a Python data visualization library based on Matplotlib.
#It provides a high-level interface for drawing attractive andinformative statistical graphics.


#Use Case in Real Life:

#Data Exploration: Create various plots to visualize data distributions and relationships between variables during the exploratory data analysis (EDA) phase.

#Statistical Analysis: Use visualizations to understand statistical properties of datasets, such as distribution plots, histograms, and pair plots to identify correlations and patterns.

#Business Reporting: Generate business reports with visualizations that provide insights into sales performance, customer behavior, and market trends.


pip install matplotlib #first install the matplotlib library
import matplotlib.pyplot as plt

#data
x = [1,2,3,4,5]
y = [2,3,5,7,11]

#Creating a line plot
plt.plot(x,y) #this will print simple solid line in the graph
plt.plot(x,y,linestyle="dotted",color = '#5D6D7E',linewidth ="7",marker="o",mfc="r",ms="10") or plt.plot(x,y,ls=":") #this will print dotted line
#Color will change the color of the line
#linewidth or lw will change the line width of the line
#in marker we can change the coordinated point to rectangle or circle and in different types of shaped also.
#mfc will change the marker color
#mec will change the marker boundary color 
#ms use to change the marker size at 1 it will small and it goes bigger and bigger 
plt.plot(x,y,linestyle="dashed") or plt.plot(x,y,ls="--") #this will print dashed line
plt.xlabel('X-axis')
plt.ylable('Y-axis')
plt.title('Simple Line Plot')
plt.show()

#example fo 2 line graph
import numpy as np
y1=np.array([3,5,3,8])
y2=np.array([1,9,7,4])
plt.plot(y1)
plt.plot(y2)
plt.show



#Creating a Simple Scatter Plot with MAtplotlib

#Data
x = [1,2,3,4,5]
y = [2,3,5,7,11]

#create a scatter plot
plt.scatter(x,y,color="red") #this will only show the marker points (coordinates points)
plt.xlabel('sales')
plt.ylable('price')
plt.title('Simple Scatter Plot')
plt.show()



#create a simple Bar Plot with Matplotlib
# Data
products = ['PC', 'TV', 'Ref', 'Micro']
sales = [4, 7, 1, 8]

# Creating a bar plot
plt.bar(products, sales, color="black",width=0.1) #it will create verticle ber graph
plt.barh(products, sales, color="black",width=0.1) #it will create horizontal ber graph. instead of bar I have written barh 
plt.xlabel('products')
plt.ylabel('Sales(in 1000s)')
plt.title('Simple Bar Plot')
plt.show()


#Create a Simple Histogram with Matplotlib
# Data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

#Creating a histogram
plt.hist(data, bins=4) 
plt.xlabel('Value']
plt.ylabel('Frequency')
plt.title('Simple Histogram')
plt.show()


#Creating Subplots with Matplotlib

# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2=[1, 4, 6, 8, 10]

# Creating subplots
fig, axs = plt.subplots(2)
axs[0].plot(x, y1)
axs[0].set_title('First Plot')
axs[1].plot(x, y2, 'tab:orang')
axs[1].set_title('Second Plot')

# Displaying the plot
plt.tight_layout()
plt.show()



#Adding Annotations with Matplotlib
# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Creating a plot with annotations
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot with Annotations')
plt.annotate('Peak', xy=(5, 11), xytext=(4, 10), arrowprops=dict(facecolor='black', shrink=0.05)) #it will show peak written at 4,10 and a arrow pointing at 5,11
plt.show()


#Creating a Simple Line Plot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

#Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

#Creating a line plot
sns.lineplot(x=x, y=y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt. title('Simple Line Plot with Seaborn')
plt.show()


#Creating a Simple Scatter Plot with Seaborn
# Data
x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]

#Creating a Scatter plot
sns.scatterplot(x=x1, y=y1)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt. title('Simple Scatter Plot with Seaborn')
plt.show()


#Creating a Simple BAr Plot with Seaborn
# Data
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

#Creating a bar plot
sns.barplot(x=categories, y=values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Plot with Seaborn')
plt.show()


#Create a Simple Histogram with Seaborn
#Data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

#Creating a histogram
sns.histplot(data, bins=4) 
plt.xlabel('Value']
plt.ylabel('Frequency')
plt.title('Simple Histogram with Seaborn')
plt.show()


#Creating a Pair Plot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris #Search about iris dataset

iris = load_iris()
iris_data = sns.load_dataset("iris")

#Creating a pair plot
sns.pairplot(iris_data, hue='species')
plt.title('Pair Plot with Seaborn')
plt.show()


#Creating a Heatmap with Seaborn
import numpy as np

#Data
data = np.random.rand(10, 12)
sns.heatmap(data)
plt. title('Heatmap with Seaborn')
plt.show()
