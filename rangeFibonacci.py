def fibonacci(x):
    a = 0
    b = 1
    if x <= 0:
        print("Negative number")
    elif x == 1:
        print(a)
    elif x <= 6:
        print(a)
        print(b)
        for i in range(2, x):
            c = a + b
            a = b
            b = c
            if c > x:
                break
            print(c)
    else:
        print(a)
        print(b)
        for i in range(2, x):
            c = a + b
            a = b
            b = c
            if c > x:
                break
            print(c)


tg = int(input("Enter target number: "))
fibonacci(tg)
