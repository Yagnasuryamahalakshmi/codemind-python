n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if i%2!=0:
      l.append(arr.index(i))
print(len(arr)-1)