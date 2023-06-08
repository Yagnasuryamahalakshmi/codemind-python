s=input()
c=0
sp="~`!@#$%^&*()_+-=[]''""{}\|?/.,<>"
for i in s:
    if i in sp:
        c+=1
print(c)