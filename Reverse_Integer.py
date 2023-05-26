n=int(input())
rev=0
c=0
if n<0:
    c=1
n=abs(n)
while(n!=0):
    r=n%10
    n=n//10
    rev=rev*10+r
if c==1:
    print("-"+str(rev))
    exit()
print(rev)
    