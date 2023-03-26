n = int(input())
array = input().split(' ')

i = 0
while(i < n/2):
    temp = array[i]
    array[i] = array[n - i - 1] 
    array[n - i - 1] = temp
    i+=1
    
for i in range(n):
    print(array[i], end = " ")