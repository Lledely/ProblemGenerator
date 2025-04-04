import math

class Point:

    def __init__(self, x_coord:float = 0, y_coord:float = 0):
        self.x = x_coord
        self.y = y_coord

    def __sub__(self, other:'Point') -> 'Vector':
        if not isinstance(other, Point):
            raise ValueError("Subtraction is only supported between Point instances.")
        return Vector(self.x - other.x, self.y - other.y)
    
    def __add__(self, other:'Vector') -> 'Point':
        if not isinstance(other, Vector):
            raise ValueError("Addition is only supported between Point and Vector instances.")
        return Point(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other:float) -> 'Point':
        if not isinstance(other, (int, float)):
            raise ValueError("Multiplication is only supported with scalar values.")
        return Point(self.x * other, self.y * other)
    
    def rotate(self, angle:float) -> None:
        angle_rad = math.radians(angle)
        x_new = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        y_new = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        self.x = x_new
        self.y = y_new

    def make_integer(self) -> None:
        self.x = round(self.x)
        self.y = round(self.y)

class Vector:
    
    def __init__(self, x:float = 0, y:float = 0):
        self.x = x
        self.y = y
    
    def normalize(self) -> None:
        length = (self.x**2 + self.y**2)**0.5
        if length == 0:
            self.x = 0
            self.y = 0
        else:
            self.x /= length
            self.y /= length

    def normal_vector(self) -> 'Vector':
        to_ret = Vector(-self.y, self.x)
        to_ret.normalize()
        return to_ret
    
    def __mul__(self, other:float) -> 'Vector':
        return Vector(self.x * other, self.y * other)
    
class Triangle:
    
    def __init__(self, point1:Point, point2:Point, point3:Point):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
    
    def rotate(self, angle:float) -> None:
        self.point1.rotate(angle)
        self.point2.rotate(angle)
        self.point3.rotate(angle)

    def scale(self, factor:float) -> None:
        self.point1 *= factor
        self.point2 *= factor
        self.point3 *= factor

    def shift(self, vector:Vector) -> None:
        self.point1 += vector
        self.point2 += vector
        self.point3 += vector

    def make_integer(self) -> None:
        self.point1.make_integer()
        self.point2.make_integer()
        self.point3.make_integer()
        