import numpy as np
import sympy as sp
from sympy.vector import CoordSys3D

x, y, z = sp.symbols('x y z')
N = CoordSys3D('N')
gravity_vector = N.j * -9.81

def gradiant_of_expression(expression, variables: sp.Matrix):
    gradient = [sp.diff(expression, var) for var in variables]
    return gradient

def gradiant_of_matrix(function: sp.Matrix):
    dFdx = sp.diff(function[0], x)
    dFdy = sp.diff(function[1], y)
    dFdz = sp.diff(function[2], z)
    return sp.Matrix([dFdx, dFdy, dFdz])

def pressure_on_surface(force, area):
    return force / area

def force_due_to_pressure(pressure, area):
    return pressure*area

def differential_force_due_to_pressure_on_a_fluid_parcel(pressure_matrix: sp.Matrix):
    print(pressure_matrix)
    print(gradiant_of_matrix(pressure_matrix))
    print(sp.Matrix([0,0,0]) - gradiant_of_matrix(pressure_matrix))
    return -1 * gradiant_of_matrix(pressure_matrix)

def density(mass, volume):
    return mass / volume

def specific_density(density):
    # density of water = 1000 kg/m**3
    return density/1000

def force_due_to_gravity_on_a_fluid_element(pressure):
    return sp.integral(density, x, y, z) * gravity_vector
    
# Hydrostatics
# Sum of forces = 0

def hydrostatic_pressure(atmospheric_pressure, density: float, height: float):
    return atmospheric_pressure + density * 9.81 * height

def variable_hydrostatic_pressure(atmospheric_pressure, density: sp.Function, height):
    return atmospheric_pressure + sp.integral(density, y) * height

def angled_manometer_pressure(density, length, angle):
    return density * 9.81 * length * sp.sin(np.radians(angle))

class hydrostatic_fluid_parcel:
    def __init__(self, density):
        self.density = density
        
    def hydrostatic_pressure(self, surface_pressure, height):
        return surface_pressure + self.density * 9.81 * height
    
    
