n = int(input())
array = input().split(' ')
sum = 0
for i in range(1,n-1):
    num1 = int(array[i-1])
    num2 = int(array[i+1])
    num3 = int(array[i])
    if(num1 < num3 and num2 < num3):
        sum += 1
print(sum)