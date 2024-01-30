import numpy as np
import sympy as sp

x, y, z = sp.symbols('x y z')

# Input: expression, sympy variables in a matrix eg. sp.Matrix([x, y, z]) - Outputs: Gradiant Expression
def gradiant_of_expression(expression, variables: sp.Matrix):
    gradient = [sp.diff(expression, var) for var in variables]
    return gradient

# Input: 3D Matrix of functions sp.Matrix([..., ..., ...])
def gradiant_of_matrix(function: sp.Matrix):
    dFdx = sp.diff(function[0], x)
    dFdy = sp.diff(function[1], y)
    dFdz = sp.diff(function[2], z)
    return sp.Matrix([dFdx, dFdy, dFdz])