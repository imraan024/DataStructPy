from array import *


def fibonacci(a):
    y = array("i", [])

    print("Fibonacci Series : ", end="")
    for i in range(a):
        if i == 1:
            x = 1
            y.append(x)
            print(y[i], end=" ")
        elif i == 0:
            x = 0
            y.append(x)
            print(y[i], end=" ")
        elif i == 1:
            x = 1
            y.append(x)
            print(y[i], end=" ")
        elif i == 2:
            x = 1
            y.append(x)
            print(y[i], end=" ")
        else:
            x = y[i - 1] + y[i - 2]
            y.append(x)
            print(y[i], end=" ")


tg = int(input("Enter target number: "))
if tg < 0:
    print("Number is less then Zero.")
else:
    fibonacci(tg)
