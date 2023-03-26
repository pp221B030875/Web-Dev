v = int(input())
t = int(input())

dist = v*t

if(dist > 109):
    while(dist > 109):
        dist -= 109
elif(dist < 0):
    while(dist < 0):
        dist+=109

print(dist)
    