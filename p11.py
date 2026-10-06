names=input("enter first names seperated by space:").split()
count=0
for name in names:
    count=count+name.lower().count('a')
print("numberof ocuurences of 'a':",count)
