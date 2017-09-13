## Learning Python 

# contains notes and codes learnt in the Udemy Python course 'Learning Python for Data Analysis and Visualisation' 
# link: https://www.udemy.com/learning-python-for-data-analysis-and-visualization/learn/v4/content 

import numpy as np # import the package needed to process arrays 
list1 = [1,2,3,4,5]
list2 = [4,6,2,7,5]
array1 = np.array(list1)
lists = [list1,list2]
arrays = np.array(lists)
arrays.shape       # returns the dimension of the matrix 

np.eye(5)     # identity matrix 
np.zeros(5)   # vector of zeros of length 5 

# arithmetic operations on arrays 
arrays * arrays    # NOT a matrix multiplication 
arrays **3

# in order to change a list entries, a new copy has to be made if you would like the original list intact 
list1 = np.arange(11)
list_copy = np.copy(list1)
list_copy[:5] = 99

arr2d = np.array(([5,10,15],[20,25,30],[35,40,45],[1,2,3]))
arr2d[1][2]    # 2nd row and 3rd column entry 
arr2d[1]       # all elements of 2nd row 
arr_2d.shape[a]    # a = 0 shows the number of rows and a = 1 the number of columns 
