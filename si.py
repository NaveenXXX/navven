from math import factorial
p=int(input("enter the pinciple amount:"))
t=int(input("enter no. of years:"))
choice=str(input("is customer is senior citizen(y/n):"))
if choice in('n','y'):
    if choice =='n':
        r=10
    else:
        r=12
si=p*t*r/100
print("simple interest is:",si)
