n = int(input())
array = input().split(' ')
sum = 0
for i in range(n):
    if(int(array[i])> 0):
        sum += 1
print(sum)