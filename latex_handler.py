def transform_to_latex(constraints, objective, solution, headers=None):
    if headers is None:
        headers = "\\documentclass{article}\n\\usepackage{amsmath}\n"
    latex_code = f"""{headers}
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