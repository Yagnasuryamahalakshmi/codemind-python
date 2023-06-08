n=int(input())
m=int(input())
a=[]
for i in range(n):
    s=list(map(int,input().split()))
    a.append(s)
s=0
for i in range(n):
    for j in range(m):
        s+=a[i][j]
print(s)
