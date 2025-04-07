from generation import generate_problem
import solution
import os
import latex_handler

if __name__ == "__main__":
    os.remove(latex_handler.default_latex_problems_file_name) if os.path.exists(latex_handler.default_latex_problems_file_name) else None
    constraints, objectives = [], []
    for _ in range(3):
        constraints_, objective_ = generate_problem()
        constraints.append(constraints_)
        objectives.append(objective_)
    latex_handler.write_problems_to_latex(constraints, objectives)

    for i in range(len(constraints)):
        simplex_tables, optimal_solution = solution.simplex_method(constraints[i], objectives[i])
        latex_handler.write_solutions_to_latex(simplex_tables, optimal_solution)
