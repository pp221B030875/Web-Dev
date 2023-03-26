n = input()
ok = False
res = ""
for i in range(len(n)):
    if(n[len(n)-1-i] == '0' and not ok):
        continue
    ok = True
    res += n[len(n)-1-i]
print(res)
    