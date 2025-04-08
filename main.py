from generation import generate_problem
import solution
import os
import latex_handler
from sympy import symbols, Eq

def prompt_user() -> int:
    number_of_variants = input("Введите количество вариантов: ")
    if not number_of_variants.isdigit():
        print("Введено не число. Попробуйте снова.")
        number_of_variants = input("Введите количество вариантов: ")
    return int(number_of_variants)

if __name__ == "__main__":
    os.remove(latex_handler.default_latex_problems_file_name) if os.path.exists(latex_handler.default_latex_problems_file_name) else None
    os.remove(latex_handler.default_latex_solutions_file_name) if os.path.exists(latex_handler.default_latex_solutions_file_name) else None

    x, y = symbols('x y')
    constrains = [
        Eq(-2 * x + 10 * y, 20),
        Eq(-2 * x - 6 * y, -12),
        Eq(4 * x - 4 * y, 24)
    ]
    # constrains = [ eq <= 0 for eq in constrains ]
    obj = 40 * x + 5 * y
    stuff = solution.simplex_method(constrains, obj)
    print(stuff)

    # number_of_variants = prompt_user()

    # constraints, objectives = [], []
    # for _ in range(number_of_variants):
    #     constraints_, objective_ = generate_problem()
    #     constraints.append(constraints_)
    #     objectives.append(objective_)
    # latex_handler.write_problems_to_latex(constraints, objectives)

    # all_tables, opt_solutions = [], []
    # for i in range(len(constraints)):
    #     simplex_tables, optimal_solution = solution.simplex_method(constraints[i], objectives[i])
    #     all_tables.append(simplex_tables)
    #     opt_solutions.append(optimal_solution)
    # latex_handler.write_solutions_to_latex(all_tables, opt_solutions)
