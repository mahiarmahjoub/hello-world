## Learning Python 

# contains notes and codes learnt in the Udemy Python course 'Learning Python for Data Analysis and Visualisation' 
# by 
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

arr = np.arange(50).reshape((10,5))
arr_Trans = arr.T    # transpose 
np.dot(arr.T,arr)    # dot product of matrices 
arr3d = np.arange(50).reshape((5,5,2))    # create a 3d array 

# Universal array functions
arr = np.arange(11)
np.sqrt(arr)
A = np.random.randn(10)   # generate random numbers from normal dist
B = np.random.randn(10)
np.add(A,B)   # full list of arithmetic options available at: https://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs

# Processing arrays & plotting 
import numpy as np 
import matplotlib.pyplot as plt   # need this package for visualisation 
points = np.arange(-5,5,0.01)
dx,dy = np.meshgrid(points,points)   # create a mesh for plotting 3d 
z = (np.sin(dx) + np.sin(dy))
plt.imshow(z)    # plot 
plt.colorbar()
plt.title("Plot for sin(x)+cos(x)")

# manipulating arrays 
A = np.array([1,2,3,4])
B= np.array([100,200,300,400])
condition = np.array([True,True,False,False])
answer2 = np.where(condition,A,B)   # where TRUE, entries from A taken, otherwise, from B
# answer2 = [1,2,300,400] will be the outcome 

from numpy.random import randn
arr = randn(5,5)
arr_pos = np.where(arr<0,0,arr)  # replace negative entries with 0, otherwise, leave untouched 
arr_pos.sum()   # sum of all entries - outcome is a scalar
arr_pos.sum(0)  # sum of entries from each column 
arr_pos.mean()  # the same can be done for mean, std etc. 
arr_pos.std()

arr_pos.sort()  # if arr_pos needs to be preserved, np.copy into a new vector and sort the latter

# array input and output 
arr = np.arange(5)
np.save('my_array',arr)   # saves as a .npy file 
np.load('my_array.npy')

arr = np.array([[1,2,3],[4,5,6]])
np.savetxt('my_test_text.txt',arr,delimiter=',')
arr = np.loadtxt('my_test_text.txt',delimiter = ',')

# Pandas 

import pandas as pd
from pandas import Series,DataFrame   # since we use Series, DataFrame a lot, we import them directly as opposed to np.Series every time

ww2_cas = Series([8700000,4300000,3000000,2100000,400000],index=['USSR','Germany','China','Japan','USA'])
ww2_cas.values   # returns the scalars only 
ww2_cas.index    # returns the labels for each value 
ww2_cas['USA']   # calls the value for the corresponding index of the entry 
ww2_cas[ww2_cas > 400000].index    # show which countries had more than 400000 casualties 
ww2_cas.name = "World War Two Casualties"
# you can also add Series together e.g. ww2_cas + ww2_cas will add the values 
ww2_cas.values.name = "Casualties"    # names the indices 

DataFrame(nfl_frame,columns=['Team','First Season','Total Games'])   # select only the said columns from the nfl_frame table
dframe = DataFrame(randn(25).reshape((5,5)),index=['A','B','D','E','F'],columns=['col1','col2','col3','col4','col5'])

dframe2 = dframe.reindex(['A','B','C','D','E','F'])    # adds an empty row 
new_columns = ['col1','col2','col3','col4','col5','col6']
dframe2.reindex(columns=new_columns)    # adds a new empty column 

# adds those names to the 1st and 5th row in 'Stadium column'
nfl_frame['Stadium'] = Series(["Levi's Stadium","AT&T Stadium"],index=[4,0]) 

# constructing dataframe from scratch - another way 
data = {'City':['SF','LA','NYC'],
        'Population':[837000,3880000,8400000]}
city_frame = DataFrame(data)

# if we have a DataFrame matrix named 'frame', then
frame.sort()
frame.mean()
frame.sum()    # takes the sum of each column 
frame.sum(axis=1)   # takes the sum of each row 
frame.describe()   # provides summary statistics for each column 
frame.plot()   # plots each column against the indices 

# filling or removing 'NA' or empty entries in a database
frame.isnull()   # returns a boalean of all the empty entries 
frame.dropna()   # gets rid of every row containing at least on NA
frame.dropna(how='all')   # only removes row where all entries is NA
frame.dropna(thresh=2)  # only removes rows with more than 2 NA
frame.fillna(1)   # fill all the NA with 1 

ser = Series(np.random.randn(6),index=[[1,1,1,2,2,2],['a','b','c','a','b','c']])   # multiple index levels 
dframe = ser.unstack()   # turns the multi-index series into a table 

frame = pd.read_csv('filename.csv')    # read 'filename.csv' into a DataFrame named frame 
frame = pd.read_table('filename.csv',sep=',')  # if a different separater is used 
frame.to_csv('mytextdata_out.csv')    # export 'frame' as a csv file 

 
