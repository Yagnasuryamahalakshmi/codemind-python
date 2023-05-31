n=int(input())
a=len(str(n))
temp=n
s=0
while temp!=0:
    rem=temp%10
    s+=rem**a
    temp//=10
    a-=1
if s==n:
    print("True")
else:
    print("False")