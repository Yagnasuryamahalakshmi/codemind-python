def rev(n):
    rev=0
    while n:
            r=n%10
            n=n//10
            rev=rev*10+r
    return rev
n=int(input())
rev=rev(n)
print(rev)
    