n=int(input())
l=list(map(int,input().split()))
for i in range(0,n-1):
    if l[i]>=l[i+1]:
        print("no")
        break
else:
    print("yes")