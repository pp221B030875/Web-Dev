n = int(input('n = '))
sum = 0

while(True):
    i = n%10
    sum += i
    n -= i
    n /= 10
    if(n == 0):
        break
print(sum)