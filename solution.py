from sympy import Matrix, Eq, Ge, Le
import numpy as np
import math

def to_tableau(c, A, b):
    xb = [eq + [x] for eq, x in zip(A, b)]
    z = c + [0]
    return xb + [z]

def can_be_improved(tableau):
    z = tableau[-1]
    return any(x > 0 for x in z[:-1])

def get_pivot_position(tableau):
    z = tableau[-1]
    tmp_val = 0
    tmp_inx = -1
    for i, x in enumerate(z):
        if x > 0:
            if x > abs(tmp_val):
                tmp_val = -x
                tmp_inx = i
    column = tmp_inx
    # column = next(i for i, x in enumerate(z[:-1]) if x > 0)
    
    restrictions = []
    for eq in tableau[:-1]:
        el = eq[column]
        restrictions.append(math.inf if el <= 0 else eq[-1] / el)

    row = restrictions.index(min(restrictions))
    return row, column

def pivot_step(tableau, pivot_position):
    new_tableau = [[] for eq in tableau]
    
    i, j = pivot_position
    pivot_value = tableau[i][j]
    new_tableau[i] = np.array(tableau[i]) / pivot_value
    
    for eq_i, eq in enumerate(tableau):
        if eq_i != i:
            multiplier = np.array(new_tableau[i]) * tableau[eq_i][j]
            new_tableau[eq_i] = np.array(tableau[eq_i]) - multiplier
   
    return new_tableau

def is_basic(column):
    return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1

def get_solution(tableau):
    columns = np.array(tableau).T
    solutions = []
    for column in columns:
        solution = 0
        if is_basic(column):
            one_index = column.tolist().index(1)
            solution = columns[-1][one_index]
        solutions.append(solution)
        
    return solutions

def simplex_method(constraints, objective_function):
    variables = ['x', 'y']
    
    equations = []
    for constraint in constraints:
        if constraint.rel_op == '>=':
            equations.append(Eq(constraint.lhs - constraint.rhs, 0))
        elif constraint.rel_op == '<=':
            equations.append(Eq(constraint.lhs - constraint.rhs, 0))
        else:
            equations.append(Eq(constraint.lhs, constraint.rhs))
    A, b = [], []
    for constraint in equations:
        lhs = constraint.lhs
        coeffs_as_symbols = lhs.as_coefficients_dict()
        coeffs_as_strings = {}
        for key, value in coeffs_as_symbols.items():
            coeffs_as_strings[str(key)] = value
        A.append([coeffs_as_strings.get(var, 0) for var in variables])
        b.append(-coeffs_as_strings["1"])
        
    for i in range(len(A)):
        tmp = [0] * len(A)
        tmp[i] = 1
        A[i].extend(tmp)
    
    coeffs_as_symbols = objective_function.as_coefficients_dict()
    coeffs_as_strings = {}
    for key, value in coeffs_as_symbols.items():
        coeffs_as_strings[str(key)] = value
    c = [coeffs_as_strings.get(var, 0) for var in variables] + [0] * len(A)

    tableau = to_tableau(c, A, b)
    tmp = tableau[:]
    tmp[-1] = list(map(lambda x: -x, tmp[-1]))
    simplex_tables = [Matrix(tmp)]
    table_first_row = variables + [f'$s_{i + 1}$' for i in range(len(A))] + ['rhs']
    table_first_column = [[f's_{i + 1}' for i in range(len(A))] + ['z']]

    while can_be_improved(tableau):
        pivot_position = get_pivot_position(tableau)

        tmp = table_first_column[-1][:]
        tmp[pivot_position[0]] = table_first_row[pivot_position[1]]
        table_first_column.append(tmp)

        tableau = pivot_step(tableau, pivot_position)
        tmp = tableau[:]
        tmp[-1] = list(map(lambda x: -x, tmp[-1]))
        simplex_tables.append(Matrix(tmp))

    return simplex_tables, get_solution(tableau)[:len(variables)] + [abs(tableau[-1][-1])], table_first_row, table_first_column
    