s=str(input("enter the string:"))
count=0
for i in s:
    if(i=='a' or i=='e'or i=='o'or i=='i' or i=='u' or
       i=='A' or i=='E' or i=='O' or i=='I' or i=='U'):
        count=count+1
print('no.of vowels are:',count)
