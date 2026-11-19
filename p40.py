

square = lambda side: side * side

rectangle = lambda length, breadth: length * breadth

triangle = lambda base, height: 0.5 * base * height

# Area of square
side = float(input("Enter the side of square: "))
print("Area of square =", square(side))

# Area of rectangle
length = float(input("Enter the length of rectangle: "))
breadth = float(input("Enter the breadth of rectangle: "))
print("Area of rectangle =", rectangle(length, breadth))

# Area of triangle
base = float(input("Enter the base of triangle: "))
height = float(input("Enter the height of triangle: "))
print("Area of triangle =", triangle(base, height))

