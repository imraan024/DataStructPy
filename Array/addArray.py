from numpy import *

arr1 = array([2, 4, 6, 1, 8])
arr2 = array([7, 34, 7, 2, 3])

arr3 = array([0, 0, 0, 0, 0])

for i in range(len(arr3)):
     arr3[i] = arr1[i]+arr2[i]


print(arr3)