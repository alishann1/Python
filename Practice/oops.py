class Shape:
    def area(self):
        return


class Circle(Shape):
    def area(self, radius):
        self.radius = radius
        return 3.24 * radius ** 2


class Square(Shape):
    def area(self, side):
        self.side = side
        return side ** 2
