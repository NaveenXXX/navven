ch=input("CHOICE:")
if ch in ('1','2','3','4','5'):
    x=int(input("X="))
    n=int(input("n="))
    if(ch=='1'):
        pow=x**n
        print("pow(x,n)=",pow)
    elif(ch=='2'):
        add=x+n
        print("add(x,n)=",add)
    elif(ch=='3'):
        sub=x-n
        print("sub(x,n)=",sub)
    elif(ch=='4'):
        mul=x*n
        print("mul(x,n)=",mul)
    else:
        div=x/n
        print("div(x,n)=",div)
        
    
