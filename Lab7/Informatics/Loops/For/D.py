import re 
x = input()
d = input()
list = re.findall(d,x)
print(len(list))