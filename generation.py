import random
from constants import constraints_upper_bound, constraints_lower_bound, third_point_max_shift
from sympy.geometry import Point, Line
from sympy import Rational, Eq, Symbol
from math import ceil

def generate_objective_function(point: "Point"):
    coefficient_x = Rational(1, point.x) if point.x != 0 else 0
    coefficient_y = Rational(1, point.y) if point.y != 0 else 0
    
    objective_function = coefficient_x * Symbol("x") + coefficient_y * Symbol("y")
    return objective_function

def generate_problem(is_dual: bool = False):
    point1 = Point(0, random.randint(constraints_lower_bound, constraints_upper_bound))
    point2 = Point(random.randint(constraints_lower_bound, constraints_upper_bound), 0)

    middle_point = (point1 + point2) / 2
    point3_shift = random.uniform(1, third_point_max_shift)

    point3_float = middle_point * point3_shift
    point3 = Point(ceil(point3_float.x), ceil(point3_float.y))

    points = [point1, point3, point2]

    if is_dual:
        points.append(Point(0, 0))

    constraints = []
    for i in range(len(points)):
        line = Line(points[i], points[(i + 1) % len(points)])
        equation = line.equation()
        inequality = equation <= 0
        constraints.append(inequality)
    
    objective_function = generate_objective_function(point3)
    return constraints, objective_function