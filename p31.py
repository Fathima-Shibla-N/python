n=int(input("enter a no:"))
i=1
print("factor are:")
while i<=n:
    if n%i==0:
        print(i,end="")
    i+=1
