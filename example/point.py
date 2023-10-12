from math import sqrt
class Point:
    """ Точка на плоскости XY """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    c = 0

    def distanse(self):
        return sqrt(self.x**2+self.y**2)

    def __repr__(self):
        s = f"({self.x}, {self.y})"
        return s

# (3, 4)
a = Point(3, 4)
print(a.x, a.y, a.distanse())
# (-1, 4)
a.x = -1
print(a.x, a.y)