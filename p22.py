numbers=[-2,3,-5,6,8,-1]
positive=[n for n in numbers if n>0]
print(positive)

n=int(input("enter N:"))
squares=[i*i for i in range(1,n+1)]
print(squares)

word=input("enter a word:")
vowels=[ch for ch in word if ch in 'aeiouAEIOU']
print(vowels)

word=input("enter a word")
values=[ord(ch)for ch in word]
print(values)
