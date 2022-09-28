m=int(input("initial number:"))
n=int(input("final number:"))
k=int(input("no. of skipping value"))
for i in range(m,n+1,k+1):
    if(m>=n or k<0):
        print("invalid")
    else:
        print(i)
