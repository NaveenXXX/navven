print("enter the age:")
n=input()
if(n>=18):
    print("eligible to vote")
elif(n<0):
    print("invalid")
else:
    a=18-n
    print("you are allowed to vote after",a,"years") 
