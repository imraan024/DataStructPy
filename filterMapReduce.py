from functools import reduce
num = [3, 5, 3, 7, 1, 6]


odd = list(filter(lambda n: n%2==1, num))
double = list(map(lambda n: n*2, num))
sum = reduce(lambda a, b: a+b, odd)



print(odd)
print(double)
print(sum)