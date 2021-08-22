from array import *

values = array("i", [3, 5, 6, 7, 2, 9])

x = int(input("Enter Target Number: "))

for i in range(len(values)):
    if values[i]==x:
        print("Number Found.")
        break
else:
    print("Number Not Found.")
