from array import *
len = int(input("Insert The number of length: "))

arr = array("i", [])

for i in range(len):
    x = int(input("Enter the values: "))
    arr.append(x)

print(arr)

for j in range(len):
    print(arr[j], end=" ")
