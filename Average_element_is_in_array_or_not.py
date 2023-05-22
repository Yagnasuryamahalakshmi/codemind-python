n=int(input())
arr=list(map(int,input().split()))
s=0
c=0
for i in arr:
    s=s+i
    if (s//n) in arr:
      c=1
if c==1:
    print('True')
else:
    print('False')