def poww(a,n):
    temp = a
    for i in range(n-1):
        a *= temp
    return a

a = int(input())
n = int(input())
print(poww(a,n))