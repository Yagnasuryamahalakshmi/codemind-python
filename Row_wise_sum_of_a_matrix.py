n,m=map(int,input().split())
l=[]
for i in range(n):
    mat=list(map(int,input().split()))
    l.append(mat)
x=[]
for i in range(n):
    s=0
    for j in range(m):
        s+=l[i][j]
    x.append(s)
print(*x)