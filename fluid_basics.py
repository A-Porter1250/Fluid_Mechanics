import numpy as np
import sympy as sp
from sympy.vector import CoordSys3D
import matplotlib.pyplot as plt

# Fluid definition: Substance that deforms continuously under an applied shear stress.

# Steady State
x, y, z = sp.symbols('x y z')
c = sp.symbols('c') # Integration Constant

Pressure = sp.Function('Pressure')(x, y)

N = CoordSys3D('N')
U = sp.Function('U')(x, y, z)
V = sp.Function('V')(x, y, z)
W = sp.Function('W')(x, y, z)

Velocity_vector_2D = U * N.i + V * N.j
Velocity_vector_3D = U * N.i + V * N.j + W * N.k

def Magnitude_of_3D_vector(vector: sp.vector.vector.VectorMul):
    return sp.sqrt(U ** 2 + V ** 2 + W ** 2)