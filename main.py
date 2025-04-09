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

    # x, y = symbols('x y')
    # constrains = [
    #     Eq(0 * x + 1 * y - 2, 0),
    #     Eq(1 * x - 0 * y - 1, 0),
    #     Eq(-2 * x - 1 * y + 2, 0)
    # ]
    # obj = 10 * x + 4 * y
    # stuff = solution.simplex_method(constrains, obj)
    # os.remove(latex_handler.default_latex_solutions_file_name) if os.path.exists(latex_handler.default_latex_solutions_file_name) else None
    # latex_handler.write_solutions_to_latex([stuff[0]], [stuff[1]])

    number_of_variants = prompt_user()

    constraints, objectives = [], []
    for _ in range(number_of_variants):
        constraints_, objective_ = generate_problem(is_dual=True)
        constraints.append(constraints_)
        objectives.append(objective_)
    os.remove(latex_handler.default_latex_problems_file_name) if os.path.exists(latex_handler.default_latex_problems_file_name) else None
    latex_handler.write_problems_to_latex(constraints, objectives)

    all_tables, opt_solutions, first_rows, first_columns = [], [], [], []
    for i in range(len(constraints)):
        stuff = solution.simplex_method(constraints[i], objectives[i])
        # simplex_tables, optimal_solution = solution.simplex_method(constraints[i], objectives[i])
        all_tables.append(stuff[0])
        opt_solutions.append(stuff[1])
        first_rows.append(stuff[2])
        first_columns.append(stuff[3])
    os.remove(latex_handler.default_latex_solutions_file_name) if os.path.exists(latex_handler.default_latex_solutions_file_name) else None
    latex_handler.write_solutions_to_latex(all_tables, opt_solutions, first_rows, first_columns)
