#Data Manipulation and Analysis with NumPy
#NumPY is a fundamentak package for scientific computing with Python. It provides support for arrays, matrices,and a large collection of mathematical function to operate on these data structure. NumPy arrays are more efficient and provide better performance for numerical operations compared to pyhton's built -in lists.

#First install the library -------->>>>>>  #pip install library name
#then import the library where we have to use that library -------->>>>>> import library name

#create a NumPy Array from a list
import numpy as np
#Creating a 1d array from a list
arr1 = np.array([1,2,3,4,5])
print(arr1)

#create a 2D array from a list of lists
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)



#Creating Arrays with Functions
#create an array as zeros
zeros = np.zeros((3,4))
print(zeros)


#create an array of ones
ones = np.ones((3,4))
print(ones)


#Creating an array with a range of values
range_Arr = np.arange(start=10, stop=20, step=2) or range_Arr = np.arange(10,20,2) #20 will not print ,stop is exclusive
print(range_Arr)


#Creating an array with random values
random_arr = np.random.rand(3,3)
print(random_arr)


#Basic Array operation-Element-wise Operations
arr = np.array([1,2,3,4,5])

#Element-wise addition
print(arr + 2)

#Element-wise multiplication
print(arr * 2)

#Element-wise subtraction
print(arr - 2)

#Element-wise division
print(arr / 2)


#Basic Array Operations-MAthematical functions
arr = np.array([1,2,3,4,5])

#Square root
print(np.sqrt(arr))

#Exponential
print(np.exp(arr))

#Logarithim
print(np.log))

#Sine
print(np.sin(arr))

#cos
print(np.cos(arr))


#Indexing and Slicing-Indexing
arr = np.array([1,2,3,4,5])
#Accessing element
print(arr[0]) #First element
print(arr[-1]) #Last Element


#Indexing and Slicing-Slicing
arr = np.array([1,2,3,4,5])
#Slicing array
print(arr[1:4]) #Elements from index 1 to 4
print(arr[:3]) #First 3 elements
print(arr[2:]) #Elements from index 2 to end


#Indexing and Slicing-Advanced Indexing
arr = np.array([1,2,3,4,5])
#Boolean indexing
print(arr[arr>3])
#FAncy indexing
indices = [0,2,4]   
print(arr[indices])


#Reshaping anad Transposing-Reshaping Arrays
arr = np.array([[1,2,3],[4,5,6]])
#REshaping the array
reshaped = arr.reshape((3,2))
print(reshaped)


#Reshaping anad Transposing-Transposing Arrays
arr = np.array([[1,2,3],[4,5,6]])
#Transposing the array
transposed = arr.T
print(transposed)


#Aggregation Function-Sum and Mean
arr = np.array([[1,2,3],[4,5,6]])
#Sum of all elements
print(np.sum(arr))

#sum along columns
print(np.sum(arr, axis=0))

#sum along rows
print(np.sum(arr.axis=1))

#MEan of all elements
print(np.mean(arr))


#Aggregation Function - Min and Max

arr = np.array([[1,2,3],[4,5,6]])
#Minimum value
print(np.min(arr))

#Maximum value
print(np.max(arr))

#Index of Minimum value
print(np.argmin(arr))

#Index of Maximum value
print(np.argmax(arr))
