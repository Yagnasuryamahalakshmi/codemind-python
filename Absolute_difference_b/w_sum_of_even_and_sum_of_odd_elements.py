N=int(input())
arr=list(map(int,input().split()))
os=0
es=0
for i in arr:
    if i%2==0:
        es=es+i
    else:
        os=os+i
print(abs(es-os))