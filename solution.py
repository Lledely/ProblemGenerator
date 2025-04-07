from sympy import Matrix, Eq, S
from sympy.abc import x, y

def simplex_method(constraints, objective_function):
    variables = list(objective_function.free_symbols)
    if len(variables) != 2:
        raise ValueError("This implementation supports only two variables.")

    equations = []
    for constraint in constraints:
        if constraint.rel_op == '>=':
            equations.append(Eq(constraint.lhs - constraint.rhs, 0))
        elif constraint.rel_op == '<=':
            equations.append(Eq(constraint.rhs - constraint.lhs, 0))
        else:
            equations.append(Eq(constraint.lhs, constraint.rhs))

    num_constraints = len(equations)

    tableau = []
    for eq in equations:
        row = []
        coeffs = eq.lhs.as_coefficients_dict()
        for key, val in coeffs.items():
            if key != 1:
                row.append(val)
        row.append(eq.rhs if eq.rhs.is_number else 0)
        tableau.append(row)

    obj_row = [-objective_function.as_coefficients_dict().get(var, 0) for var in variables]
    obj_row.append(0)
    tableau.append(obj_row)

    simplex_tables = []
    while True:
        simplex_tables.append([row[:] for row in tableau])

        if all(c >= 0 for c in tableau[-1][:-1]):
            break

        pivot_col = tableau[-1].index(min(tableau[-1][:-1]))

        ratios = []
        for i in range(num_constraints):
            if tableau[i][pivot_col] > 0:
                try:
                    ratios.append(tableau[i][-1] / tableau[i][pivot_col])
                except ZeroDivisionError:
                    ratios.append(S.Infinity)
            else:
                ratios.append(S.Infinity)
        
        if all(r == S.Infinity for r in ratios):
            raise ValueError("No valid pivot row found. Problem might be unbounded.")

        pivot_row = ratios.index(min(ratios))

        pivot_value = tableau[pivot_row][pivot_col]
        tableau[pivot_row] = [x / pivot_value if pivot_value != 0 else S.NaN for x in tableau[pivot_row]]
        for i in range(len(tableau)):
            if i != pivot_row:
                row_factor = tableau[i][pivot_col]
                tableau[i] = [
                    tableau[i][j] - row_factor * tableau[pivot_row][j]
                    if not (tableau[pivot_row][j] is S.NaN or row_factor is S.NaN)
                    else S.NaN
                    for j in range(len(tableau[i]))
                ]

    optimal_solution = {var: 0 for var in variables}
    for i in range(num_constraints):
        for j, var in enumerate(variables):
            if tableau[i][j] == 1 and all(tableau[k][j] == 0 for k in range(len(tableau)) if k != i):
                optimal_solution[var] = tableau[i][-1]
                break

    return simplex_tables, optimal_solution