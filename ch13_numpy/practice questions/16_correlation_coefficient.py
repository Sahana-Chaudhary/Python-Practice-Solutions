#Find correlation coefficient between two arrays.

import numpy as np
a=np.array([4,6,8,4,2])
b=np.array([2,5,8,9,3])
print(np.corrcoef(a,b))