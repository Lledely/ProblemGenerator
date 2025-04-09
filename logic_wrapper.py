from generation import generate_problem
import solution
import os
import latex_handler

def prompt_user() -> int:
    number_of_variants = input("Введите количество вариантов: ")
    if not number_of_variants.isdigit():
        print("Введено не число. Попробуйте снова.")
        number_of_variants = input("Введите количество вариантов: ")
    return int(number_of_variants)

def generate(
        number_of_variants: int, 
        do_dual: bool = False,
        problem_file_name: str = latex_handler.default_latex_problems_file_name, 
        solution_file_name: str = latex_handler.default_latex_solutions_file_name
    ) -> None:
    constraints, objectives = [], []
    for _ in range(number_of_variants):
        constraints_, objective_ = generate_problem(is_dual=do_dual)
        constraints.append(constraints_)
        objectives.append(objective_)
    os.remove(problem_file_name) if os.path.exists(problem_file_name) else None
    latex_handler.write_problems_to_latex(constraints, objectives, problem_file_name)

    all_tables, opt_solutions, first_rows, first_columns = [], [], [], []
    for i in range(len(constraints)):
        stuff = solution.simplex_method(constraints[i], objectives[i])
        all_tables.append(stuff[0])
        opt_solutions.append(stuff[1])
        first_rows.append(stuff[2])
        first_columns.append(stuff[3])
    os.remove(solution_file_name) if os.path.exists(solution_file_name) else None
    latex_handler.write_solutions_to_latex(all_tables, opt_solutions, first_rows, first_columns, solution_file_name)
