n,m=map(int,input().split())
l=[]
for i in range(n):
    mat=list(map(int,input().split()))
    l.append(mat)
x=[]
for i in range(m):
    s=0
    for j in range(n):
        s+=l[j][i]
        x.append(s)
print(max(*x))