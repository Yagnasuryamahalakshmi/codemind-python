n=int(input())
temp=n
rev=0
while n:#123 12 1 0
    r=n%10
    n=n//10
    rev=rev*10+r
if rev==temp:
    print("True")
else:
    print("False")