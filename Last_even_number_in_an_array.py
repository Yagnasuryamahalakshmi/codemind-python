n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if i%2==0:
        l.append(i)
a=len(l)
print(l[a-1])