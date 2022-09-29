import statistics
n=int(input("enter the length:"))
a=[]
for i in range(n):
    b=int(input("enter element:"))
    a.append(b)
 
print("\nMean: ", statistics.mean(a))
print("Median: ", statistics.median(a))
print("Mode: ", statistics.mode(a))
