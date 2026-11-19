def add(*args):
    return sum(args)

n = int(input("Enter number of integers: "))
nums = []

for i in range(n):
    nums.append(int(input("Enter number: ")))

print("Sum =", add(*nums))
