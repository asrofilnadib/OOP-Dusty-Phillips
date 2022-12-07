class Point1:
    pass


p1 = Point1()
p2 = Point1()

# <object>.<attribute> = <value>
p1.x = 5
p1.y = 6

p2.x = 8
p2.y = 7

print(p1.x, p1.y)
print(p2.x, p2.y)

print(40 * "-")


class Point2:
    def reset(self):
        self.x = 0
        self.y = 0


p = Point2()
Point2.reset(p)
print(p.x, p.y)

print(40 * "-")

import math


class Point3:
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x) ** 2 +
            (self.y - other_point.y) ** 2
        )


point1 = Point3()
point2 = Point3()

point1.reset()
point2.move(8, 0)
print(point2.calculate_distance(point1))
assert (point2.calculate_distance(point1)
        == point1.calculate_distance(point2))
point1.move(2, 9)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))

print(40 * "-")


class Point4:
    '''Merepresentasikan titik ke dalam dua dimensi
    geometri koordinat'''

    def __init__(self, x, y):
        """Mengisi posisi dengan new point, x dan y
        bisa memiliki nilai yang sepisifik, kalau gada
        ya balik ke asalnya"""
        self.move(x, y)

    def move(self, x, y):
        """move the point to new location in two dimensional space"""
        self.x = x
        self.y = y

    def reset(self):
        """reset point back to the origins (0, 0)"""
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """menghitung jarak antara dua titik dengan menggunakan
        teorema pythagoras"""
        return math.sqrt(
            (self.x - other_point.x) ** 2 +
            (self.y - other_point.y) ** 2
        )


point3 = Point4(3, 4)
print(point3.x, point3.y)

print(40*"-")

def format_string(string, formatter=None):
    class DefaultFormatter:
        def format(self, string):
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)


hello_string = "HelLo wOrLD, hoW aRE YoU TodAy?"
print("input\t: %s" % hello_string)
print("output\t: %s" % format_string(hello_string))
