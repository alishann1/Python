class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self, color):
        print(f"Color:{color}")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self, radius):
        return 3.14 * radius ** 2


c = Circle("Red", 5)
c.describe()
c.area()
