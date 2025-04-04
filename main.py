from constants import default_latex_headers, default_latex_file_name
from generation import generate_problem
import latex_handler

if __name__ == "__main__":
    constraints, objective, solution = generate_problem()
    latex_code = latex_handler.transform_to_latex(constraints, objective, solution, headers=default_latex_headers)
    latex_handler.write_to_latex(default_latex_file_name, latex_code)
