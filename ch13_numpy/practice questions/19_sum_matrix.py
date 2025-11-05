#Compute row-wise and column-wise sums of a matrix.
import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.sum(arr, axis=0))  # Column-wise
print(np.sum(arr, axis=1))  # Row-wise