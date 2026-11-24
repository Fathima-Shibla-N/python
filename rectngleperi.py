class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# Input for Rectangle 1
l1 = int(input("Enter length of Rectangle 1: "))
b1 = int(input("Enter breadth of Rectangle 1: "))
r1 = Rectangle(l1, b1)

# Input for Rectangle 2
l2 = int(input("Enter length of Rectangle 2: "))
b2 = int(input("Enter breadth of Rectangle 2: "))
r2 = Rectangle(l2, b2)

print("Area of Rectangle 1:", r1.area())
print("Perimeter of Rectangle 1:", r1.perimeter())
print("Area of Rectangle 2:", r2.area())

if r1.area() > r2.area():
    print("Rectangle 1 is larger")
elif r1.area() < r2.area():
    print("Rectangle 2 is larger")
else:
    print("Both rectangles have equal area")
