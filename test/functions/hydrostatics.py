import numpy as np
import sympy as sp
from sympy.vector import CoordSys3D
import gradiants
from gradiants import gradiant_of_expression, gradiant_of_matrix

x, y, z = sp.symbols('x y z')
row = sp.symbols('row')
N = CoordSys3D('N')
gravity_vector = N.j * -9.81

def density(mass, volume):
    return mass / volume

def specific_density(density):
    # density of water = 1000 kg/m**3
    return density/1000
 
# symbolic expression, not used since diff element leads to zero
def force_due_to_gravity_on_a_fluid_element(pressure):
    return sp.integral(row, x, y, z) * gravity_vector

# Simple Hydrostatic Pressure (function of height)
def hydrostatic_pressure(atmospheric_pressure, density: float, height: float):
    return atmospheric_pressure + density * 9.81 * height

# Hydrostatic pressure where the density varies
def variable_hydrostatic_pressure(atmospheric_pressure, density: sp.Function, height):
    return atmospheric_pressure + sp.integral(density, y) * height

def angled_manometer_pressure(density, length, angle):
    return density * 9.81 * length * sp.sin(np.radians(angle))

class hydrostatic_fluid:
    def __init__(self, density):
        self.density = density
        
    def hydrostatic_pressure(self, surface_pressure, height):
        return surface_pressure + self.density * 9.81 * height
    
class set_of_hydrostatic_fluids:
    # Input matrix of fluids as the class hydrostatic_fluid
    def __init__(self, matrix_of_fluids: sp.Matrix):
        self.matrix_of_fluids = matrix_of_fluids
        for item in matrix_of_fluids:
            self.matrix_of_fluids[item] = matrix_of_fluids[item]
           
theta = sp.symbols('theta')     
s, L = sp.symbols('s L')
n = sp.Matrix([N.i * sp.cos(theta), N.j * sp.sin(theta)])
    
def solve_net_force_on_submerged_angled_surface_due_to_hydrostatic_load_equation(density, angle, length_of_surface):
    L = length_of_surface
    variables = [density, angle, L]
    symbol_items = [item for item in variables if isinstance(item, sp.Symbol)]
    print(symbol_items)
    # sum of the moments
    # equation = sp.Eq(density * 9.81 * sp.sin(theta) * sp.integrate(s * (L - s), (s, 0, L))
    # expression = equation.lhs - equation.rhs
    # sp.solve(expression, unknown)
    
print(solve_net_force_on_submerged_angled_surface_due_to_hydrostatic_load_equation(1,2,s))