#Get unique elements from an array and their counts.
import numpy as np
arr=np.array([1,2,3,4,4,2,1])
values,counts=np.unique(arr,return_counts= True)
print(values,counts)