class Time:
    def __init__(self, h, m, s):
        self.__hour = h
        self.__minute = m
        self.__second = s

    def __add__(self, other):
        total = self.__hour * 3600 + self.__minute * 60 + self.__second
        total += other.__hour * 3600 + other.__minute * 60 + other.__second

        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60

        return Time(h, m, s)

    def display(self):
        print(self.__hour, ":", self.__minute, ":", self.__second)

t1 = Time(int(input("Enter hours: ")),
           int(input("Enter minutes: ")),
           int(input("Enter seconds: ")))

t2 = Time(int(input("Enter hours: ")),
           int(input("Enter minutes: ")),
           int(input("Enter seconds: ")))

t3 = t1 + t2

print("Sum of two times:")
t3.display()
