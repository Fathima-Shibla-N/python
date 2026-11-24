class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()

r1 = Rectangle(int(input("Enter length 1: ")),
               int(input("Enter width 1: ")))

r2 = Rectangle(int(input("Enter length 2: ")),
               int(input("Enter width 2: ")))

if r1 < r2:
    print("Rectangle 1 is smaller")
else:
    print("Rectangle 2 is smaller or equal")
