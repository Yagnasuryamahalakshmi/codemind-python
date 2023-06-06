s=input().split()
l=[]
for i in s:
    if s.index(i)%2==0:
        l.append(i[::-1])
    else:
        l.append(i)
print(*l)