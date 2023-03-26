n = int(input())
i = -1
while(True):
    i+=1
    k = pow(2,i)
    if(k <= n):
        print(k , end = ' ')
    else:
        break
    