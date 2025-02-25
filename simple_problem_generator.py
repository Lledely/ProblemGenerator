import random
from scipy.optimize import linprog

def generate_problem():
    while True:
        x1_int = random.randint(1, 10)
        y1_int = 0

        x2_int = 0
        y2_int = random.randint(1, 10)

        x3_float = round(random.uniform(1, 10), 2)
        y3_float = round(random.uniform(1, 10), 2)

        # Ensure the points form a triangle
        while (y2_int - y1_int) * (x3_float - x1_int) == (y3_float - y1_int) * (x2_int - x1_int):
            x3_float = round(random.uniform(1, 10), 2)
            y3_float = round(random.uniform(1, 10), 2)

        constraints = [
            f"{y2_int - y1_int}x_1 - {x2_int - x1_int}x_2 \\geq {round(y2_int*x1_int - x2_int*y1_int, 2)}",
            f"{round(y3_float - y1_int, 2)}x_1 - {round(x3_float - x1_int, 2)}x_2 \\geq {round(y3_float*x1_int - x3_float*y1_int, 2)}",
            f"{round(y3_float - y2_int, 2)}x_1 - {round(x3_float - x2_int, 2)}x_2 \\geq {round(y3_float*x2_int - x3_float*y2_int, 2)}",
            "x_1, x_2 \\geq 0",
            "x_1, x_2 \\in \\mathbb{Z}"
        ]

        a = random.randint(1, 10)
        b = random.randint(1, 10)
        objective = f"F = {a}x_1 + {b}x_2 \\rightarrow \\text{{max}}"

        # Check if the problem is solvable using linear programming
        c = [-a, -b]  # Coefficients for the objective function (negated for maximization)
        A = [
            [y2_int - y1_int, -(x2_int - x1_int)],
            [y3_float - y1_int, -(x3_float - x1_int)],
            [y3_float - y2_int, -(x3_float - x2_int)]
        ]
        b_values = [
            round(y2_int * x1_int - x2_int * y1_int, 2),
            round(y3_float * x1_int - x3_float * y1_int, 2),
            round(y3_float * x2_int - x3_float * y2_int, 2)
        ]
        bounds = [(0, None), (0, None)]  # x_1, x_2 >= 0

        res = linprog(c, A_ub=A, b_ub=b_values, bounds=bounds, method='highs')

        if res.success:
            print("Problem Statement:")
            for constraint in constraints:
                print(constraint)
            print(objective)

            # Optimal solution
            print(f"Optimal non-integer solution ({round(x3_float, 2)},{round(y3_float, 2)})")

            return constraints, objective, (x3_float, y3_float)
        else:
            print("The generated problem is not solvable. Generating a new problem...")

def transform_to_latex(constraints, objective, solution, headers=None):
    if headers is None:
        headers = "\\documentclass{article}\n\\usepackage{amsmath}\n"
    latex_code += f"""{headers}
    \\begin{{document}}
    \\section*{{Problem Statement}}
    \\[
    \\begin{{cases}}
        {'\n'.join(constraint + '\\\\' for constraint in constraints)}
    \\end{{cases}}
    \\]
    \\textbf{{Objective: }} $\\displaystyle {objective}$
    \\section*{{Optimal non-integer solution}}
    $({round(solution[0], 2)}, {round(solution[1], 2)})$
    \\end{{document}}
    """
    return latex_code

def write_to_latex(filename, latex_code):
    if not filename.endswith('.tex'):
        raise ValueError("Filename must end with .tex")
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(latex_code)

if __name__ == "__main__":

    my_headers = r"""\documentclass[12pt]{article}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{mathabx}
\usepackage[utf8]{inputenc}
\usepackage[T1,T2A]{fontenc}
\usepackage[russian]{babel}
\usepackage{amsfonts}
\usepackage{gensymb}
\usepackage{listings}
\usepackage{titlesec}
\usepackage{color}
\usepackage[dvipsnames]{xcolor}
\usepackage{soul}
\usepackage{xfrac}
\usepackage{hyperref}
\usepackage[margin=0.5in]{geometry}
\usepackage{tikz}
\usetikzlibrary{decorations.pathreplacing,calligraphy,patterns}
\usepackage{stackengine} 
\usepackage{enumitem}
\usepackage{blindtext}
"""

    constraints, objective, solution = generate_problem()
    latex_code = transform_to_latex(constraints, objective, solution, headers=my_headers)
    write_to_latex("problem.tex", latex_code)
