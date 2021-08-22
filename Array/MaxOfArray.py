from array import *
length = int(input("Enter the length of your array: "))

arr = array("i", [])

for i in range(length):
    x = int(input("Enter the values: "))
    arr.append(x)

y = 0
i = 0
while(i < length):
    if(arr[i] > y):
        y = arr[i]
        i = i + 1
    else:
        i = i + 1
        continue

print("Max value is ", y)




