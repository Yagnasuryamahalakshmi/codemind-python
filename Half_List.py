n=int(input())
l=list(map(int,input().split()))
p=[]
k=[]
for i in range(0,len(l)//2):
    p.append(l[i])
for i in range(len(l)//2,len(l)):
    k.append(l[i])
new=k[::-1]+p
 
print(*new)