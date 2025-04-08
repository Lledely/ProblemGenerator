from sympy import latex, shape
from constants import default_latex_headers, default_latex_problems_file_name, default_latex_solutions_file_name

def write_problems_to_latex(constraints, objective_functions, filename=default_latex_problems_file_name):
    write_to_latex(filename, default_latex_headers)
    write_to_latex(filename, f"\\begin{{document}}\n")

    for i in range(len(constraints)):
        beginning = f"""\\section*{{Вариант {i + 1}}}
        \\subsection*{{Ограничения}}
        \\begin{{itemize}}\n"""
        write_to_latex(filename, beginning)
        for constraint in constraints[i]:
            write_to_latex(filename, f"\\item ${latex(constraint)}$\n")
        write_to_latex(filename, f"\\item $x, y \\geq 0$\n")
        write_to_latex(filename, f"\\end{{itemize}}\n")
        write_to_latex(filename, "\\subsection*{Целевая функция}\n")
        write_to_latex(filename, f"\\begin{{equation}} {latex(objective_functions[i])} \\longrightarrow \\max \\end{{equation}}\n")
        
    write_to_latex(filename, f"\\end{{document}}")

def write_solutions_to_latex(simplex_tables, optimal_solutions, filename=default_latex_solutions_file_name):
    write_to_latex(filename, default_latex_headers)
    write_to_latex(filename, f"\\begin{{document}}\n")

    for i in range(len(simplex_tables)):
        write_to_latex(filename, f"\\section*{{Вариант {i + 1}}}\n")
        write_to_latex(filename, "\\subsection*{Таблицы решения}\n")
        for j in range(len(simplex_tables[i])):
            write_to_latex(filename, f"\\subsubsection*{{Таблица {j + 1}}}\n")
            write_to_latex(filename, "\\begin{center}\n")
            write_to_latex(filename, "\\begin{tabular}{|c|" + "|".join(["c"] * (len(simplex_tables[i][0]) - 1)) + "|}\n")
            write_to_latex(filename, "\\hline\n")
            for row in range(shape(simplex_tables[i][j])[0]):
                write_to_latex(filename, " & ".join([f"${latex(cell)}$" for cell in simplex_tables[i][j].row(row)]) + "\\\\\n")
                write_to_latex(filename, "\\hline\n")
            write_to_latex(filename, "\\end{tabular}\n")
            write_to_latex(filename, "\\end{center}\n")
        
        write_to_latex(filename, "\\subsection*{Оптимальное решение}\n")
        write_to_latex(filename, "\\begin{equation}\n")
        write_to_latex(filename, f"{latex(optimal_solutions[i].T)}^{{T}}\n")
        write_to_latex(filename, "\\end{equation}\n")

    write_to_latex(filename, f"\\end{{document}}")

def write_to_latex(filename, latex_code):
    if not filename.endswith('.tex'):
        raise ValueError("Filename must end with .tex")
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(latex_code)