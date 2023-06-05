n=int(input())
x=str(n)
a=len(x)
if x.startswith("0"):
    print("Invalid")
elif a==10:
    print("Valid")
else:
    print("Invalid")
