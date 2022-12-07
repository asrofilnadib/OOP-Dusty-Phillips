import math


class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)


class Polygon:
    def __init__(self, points=[]):
        self.verticase = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.verticase.append(point)

    def add_point(self, point):
        self.verticase.append(point)

    def perimeter(self):
        perimeter = 0
        point = self.verticase + [self.verticase[0]]
        for i in range(len(self.verticase)):
            perimeter += point[i].distance(point[i+1])
        return perimeter


class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Input")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)


class Silly:
    def _get_silly(self):
        print("You're a silly")
        return self._silly

    def _set_silly(self, value):
        print("You're making silly {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("Whoah, you killed silly")
        del self._silly

    silly = property(_get_silly, _set_silly, _del_silly, "This is a silly property")