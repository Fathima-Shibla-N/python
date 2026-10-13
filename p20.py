string=input("enter a string:")
if len(string)<3:
    print(string)
elif string.endswith("ing"):
    print(string+"ly")
else:
    print(string+"ing")
