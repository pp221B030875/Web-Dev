def min(a, b, c, d):
    cur = a
    if(cur > b):
        cur = b
    if(cur > c):
        cur = c
    if(cur > d):
        cur = d
    return cur
    
nums = input().split(' ')

print(min(int(nums[0]),int(nums[1]),int(nums[2]),int(nums[3])))