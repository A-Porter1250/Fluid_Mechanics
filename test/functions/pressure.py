import numpy as np
import sympy as sp
from sympy.vector import CoordSys3D
import gradiants
from gradiants import gradiant_of_expression, gradiant_of_matrix

x, y, z = sp.symbols('x y z')
N = CoordSys3D('N')
gravity_vector = N.j * -9.81

# Input: Numbers, Output: Numbers
def pressure_on_surface(force, area):
    return force / area

def force_due_to_pressure(pressure, area):
    return pressure*area

# Input: pressure sympy matrix (sp.Matrix([x_pressure, y_pressure, z_pressure]))
def differential_force_due_to_pressure_on_a_fluid_parcel(pressure_matrix: sp.Matrix):
    negative_pressure_gradiant = -1 * gradiant_of_matrix(pressure_matrix)
    return negative_pressure_gradiant