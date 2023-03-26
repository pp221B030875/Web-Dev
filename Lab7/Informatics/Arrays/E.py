n = int(input())
array = input().split(' ')
ok = False
for i in range(n-1):
    num1 = int(array[i])
    num2 = int(array[i+1])
    if(num1 < 0 and num2 < 0):
        ok = True
        break
    elif(num1 >= 0 and num2 >= 0):
        ok = True
        break
if(ok):
    print("YES")
else:
    print("NO")
    