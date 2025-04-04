import random
from constants import constraints_upper_bound, constraints_lower_bound
from scipy.optimize import linprog
import simple_geometry

def generate_problem() -> tuple[list[str], str, tuple[float, float]]:
    while True:
        point1 = simple_geometry.Point(random.randint(constraints_lower_bound, constraints_upper_bound), 0)
        vector1 = simple_geometry.Vector(random.randint(constraints_lower_bound, constraints_upper_bound), 
                                         random.randint(constraints_lower_bound, constraints_upper_bound))
        point2 = point1 + vector1

        vector_shift = random.uniform(0, 1)
        shift_vector = vector1 * vector_shift
        normal_vector = vector1.normal_vector()
        vector_length = random.randint(constraints_lower_bound, constraints_upper_bound)
        point3 = (point1 + shift_vector) + normal_vector * vector_length

        problem_triangle = simple_geometry.Triangle(point1, point2, point3)

        scale_factor = min(constraints_upper_bound / max(problem_triangle.point1.x, problem_triangle.point2.x, problem_triangle.point3.x, 1),
                           constraints_upper_bound / max(problem_triangle.point1.y, problem_triangle.point2.y, problem_triangle.point3.y, 1))
        problem_triangle.scale(scale_factor)

        shift_vector = simple_geometry.Vector(constraints_lower_bound - min(problem_triangle.point1.x, problem_triangle.point2.x, problem_triangle.point3.x),
                                              constraints_lower_bound - min(problem_triangle.point1.y, problem_triangle.point2.y, problem_triangle.point3.y))
        problem_triangle.shift(shift_vector)
        problem_triangle.make_integer()

        x1, y1, x2, y2, x3, y3 = problem_triangle.point1.x, problem_triangle.point1.y, problem_triangle.point2.x, problem_triangle.point2.y, problem_triangle.point3.x, problem_triangle.point3.y

        constraints = [
            f"{y2 - y1}x_1 - {x2 - x1}x_2 \\geq {round(y2*x1 - x2*y1, 2)}",
            f"{round(y3 - y1, 2)}x_1 - {round(x3 - x1, 2)}x_2 \\geq {round(y3*x1 - x3*y1, 2)}",
            f"{round(y3 - y2, 2)}x_1 - {round(x3 - x2, 2)}x_2 \\geq {round(y3*x2 - x3*y2, 2)}",
            "x_1, x_2 \\geq 0",
            "x_1, x_2 \\in \\mathbb{Z}"
        ]

        a = random.randint(1, 10)
        b = random.randint(1, 10)
        objective = f"F = {a}x_1 + {b}x_2 \\rightarrow \\text{{max}}"

        # Check if the problem is solvable using linear programming
        c = [-a, -b]  # Coefficients for the objective function (negated for maximization)
        A = [
            [y2 - y1, -(x2 - x1)],
            [y3 - y1, -(x3 - x1)],
            [y3 - y2, -(x3 - x2)]
        ]
        b_values = [
            round(y2 * x1 - x2 * y1, 2),
            round(y3 * x1 - x3 * y1, 2),
            round(y3 * x2 - x3 * y2, 2)
        ]
        bounds = [(0, None), (0, None)]

        res = linprog(c, A_ub=A, b_ub=b_values, bounds=bounds, method='highs')

        if res.success:
            print("Problem Statement:")
            for constraint in constraints:
                print(constraint)
            print(objective)

            # Optimal solution
            print(f"Optimal solution ({round(x3, 2)},{round(y3, 2)})")

            return constraints, objective, (x3, y3)
        else:
            print("The generated problem is not solvable. Generating a new problem...")