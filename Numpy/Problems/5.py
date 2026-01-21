import numpy as np

arr = np.ones([5, 5])
arr[1:4, 1:4] = 0
print(arr)

'''5. Write a Python program to create a 2d array with 1 on the border and 0 inside.
Expected Output:
Original array:
[[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]
[ 1. 1. 1. 1. 1.]]

1 on the border and 0 inside in the array
[[ 1. 1. 1. 1. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 0. 0. 0. 1.]
[ 1. 1. 1. 1. 1.]]'''