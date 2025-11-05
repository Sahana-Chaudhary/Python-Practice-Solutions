#Create a 1D array and reshape it into a 3x3 matrix.
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr.reshape(3,3))

#or
arr1=np.arange(1,10).reshape(3,3)
print(arr1)
