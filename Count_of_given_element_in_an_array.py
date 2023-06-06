n=int(input())
arr=list(map(int,input().split()))
z=int(input())
c=0
for i in arr:
    if i==z:
        c+=1
print(c)