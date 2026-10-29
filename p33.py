n=int(input("enter a number"))
temp=n
digits=len(str(n))
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**digits
    temp=temp//10
if sum==n:
    print("armstrong no")
else:
    print("not an armstrong")
