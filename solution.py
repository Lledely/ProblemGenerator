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
    column = next(i for i, x in enumerate(z[:-1]) if x > 0)
    
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
    # Extract variables from the objective function
    variables = list(objective_function.free_symbols)
    
    # Convert constraints into matrix form
    A, b = [], []
    for constraint in constraints:
        lhs, rhs = constraint.lhs, constraint.rhs
        if isinstance(constraint, (Ge, Le, Eq)):
            A.append([lhs.coeff(var) for var in variables])
            b.append(rhs)
        else:
            raise ValueError("Unsupported constraint type")
        
    for i in range(len(A)):
        A[i].extend([0] * len(A))
        A[i][len(A) + i - 1] = 1
    
    c = [objective_function.coeff(var) for var in variables]
    c.extend([0] * len(A))

    tableau = to_tableau(c, A, b)

    while can_be_improved(tableau):
        pivot_position = get_pivot_position(tableau)
        tableau = pivot_step(tableau, pivot_position)

    return get_solution(tableau)
    