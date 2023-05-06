mc=int(input())
c=list(map(int,input().split()))
ec=int(input())
l=[]
for i in range(len(c)):
    if c[i]+ec>=max(c):
        l.append(True)
    else:
        l.append(False)
print(*l)