words=input("enter words seperated by spaces:").split()
longest=max(words,key=len)
print("longest word:",longest)
print("length of the longest word:",len(longest))
