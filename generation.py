import random
from constants import constraints_upper_bound, constraints_lower_bound, third_point_max_shift
from sympy.geometry import Point, Line
from sympy import Rational, Eq, Symbol
from math import ceil

def generate_objective_function(point: "Point"):
    x = Symbol('x')
    y = Symbol('y')
    coeff_x = Rational(random.randint(1, 10), random.randint(1, 10))
    coeff_y = Rational(random.randint(1, 10), random.randint(1, 10))
    objective_function = coeff_x* point.x * x + coeff_y * point.y * y
    return objective_function

def generate_problem(is_dual: bool = False):
    point1 = Point(0, random.randint(constraints_lower_bound, constraints_upper_bound))
    point2 = Point(random.randint(constraints_lower_bound, constraints_upper_bound), 0)

    middle_point = (point1 + point2) / 2
    point3_shift = random.uniform(1, third_point_max_shift)

    point3_float = middle_point * point3_shift
    point3 = Point(ceil(point3_float.x), ceil(point3_float.y))

    points = [point1, point3, point2]

    constraints = []
    for i in range(len(points)):
        if not is_dual and i == len(points) - 1:
            break
        line = Line(points[i], points[(i + 1) % len(points)])
        equation = line.equation()
        inequality = equation <= 0
        constraints.append(inequality)
    
    objective_function = generate_objective_function(point3)
    return constraints, objective_function