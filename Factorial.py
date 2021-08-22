
def factorial(a):

    if a == 0:
        return 1
    else:
        return a * factorial(a-1)


tg = int(input("Enter target number: "))
fact = factorial(tg)
print(fact)
