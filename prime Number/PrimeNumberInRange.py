Tg = int(input("Enter Upper Range: "))

for x in range(2, Tg):
    for i in range(2,x):
        if(x%i==0):
            break
    else:
        print(x)