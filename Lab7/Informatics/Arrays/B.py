n = int(input())
array = input().split(' ')

for i in range(n):
    if(int(array[i])%2 == 0):
        print(array[i] , end=' ')