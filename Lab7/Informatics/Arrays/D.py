n = int(input())
array = input().split(' ')
sum = 0
for i in range(n-1):
    if(int(array[i])< int(array[i+1])):
        sum += 1
print(sum)