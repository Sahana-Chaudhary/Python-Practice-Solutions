#Generate a 4x4 matrix with random numbers and replace the max value with 0.

import numpy as np
arr=np.random.randint(1,100,(4,4))
arr[arr==arr.max()] =0
print(arr)