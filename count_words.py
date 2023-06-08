s=input().split()
v='aeiou'
con='bcdfghjklmnpqrstvwxyz'
c=0
for word in s:
    if word [0].lower() in v and word[-1][-1].lower() in con:
        c+=1
print(c)