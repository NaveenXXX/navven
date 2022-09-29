n=int(input("enter the total user:"))
if(n<=0):
    print("enter proper input")
else:
    m=int(input("enter the staff user:"))
    if(n<=m):
        print("invalid")
    else:
        p=m/3
        a=n-(m+p)
        print("total student user=",a)
