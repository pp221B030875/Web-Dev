import math

a = int(input())
b = int(input())

for i in range(a,b):
    n = math.sqrt(i)
    if(n*n == i):
        print(i)