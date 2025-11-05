#Replace elements greater than a value with a specific number.

import numpy as np
arr=np.array([[1,2,3,4],[1,2,3,4]])
arr[arr>2] = 10
print(arr)
