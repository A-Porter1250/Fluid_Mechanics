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

dUdx = sp.diff(U, x)
# [...]

# Generating Colour Diagrams
# data = np.random.random((10, 10))
# plt.imshow(data, cmap='viridis', interpolation='nearest')
# plt.colorbar()
# plt.show()

# Streamline equations
integration_Vdx = sp.simplify(sp.integrate(V, x))
integration_Udy = sp.simplify(sp.integrate(U, y))
streamline_equation = sp.simplify(integration_Vdx - integration_Udy + c)

'''
Pathline: The actual path traversed by a fluid parcel.
Streamline: A line that is everywhere tangenet to the local velocity vector.
Streakline: The loci of all parcels that have passed through a prescribed point in space.
If steady state flow, all equal.
'''

# Unsteady State
t = sp.symbols('t')
Velocity_vector_unsteady = sp.Matrix([x, y, z, t])

'''
Eularian perspective: we watch a fixed region in space and monitor the fluid parcels coming in an out of this region. (control volume)
Lagrangian perspect: we follow ther follow the fluid parcels themselves.
'''

F = sp.Function('F')
m, a = sp.symbols('m a')
A = sp.symbols('A')

def pressure_on_surface(force, area):
    return force / area

def force_due_to_pressure(pressure, area):
    return pressure*area

def gradiant(function: sp.Matrix):
    dFdx = sp.diff(function[0], x)
    dFdy = sp.diff(function[1], y)
    dFdz = sp.diff(function[2], z)
    return sp.Matrix([dFdx, dFdy, dFdz])

def force_due_to_pressure_on_a_fluid_parcel(change_in_pressure: sp.Matrix):
    return sp.integrate(0 - gradiant(change_in_pressure), x, y, z)

def density(mass, volume):
    return mass / volume

def specific(density):
    # density of water = 1000 kg/m**3
    return density/1000

def force_sue_to_gravity_on_a_fluid_element(density):
    answer = sp.integral(density, x, y, z) * - 9.81 * N.j
    
# Hydrostatics
# Sum of forces = 0

def hydrostatic_pressure(atmospheric_pressure, density, height):
    return atmospheric_pressure + density * 9.81 * height

def variable_hydrostatic_pressure(atmospheric_pressure, density: sp.Function, height):
    return atmospheric_pressure + sp.integral(density, y) * height

def angled_manometer_pressure(density, length, angle):
    return density * 9.81 * length * sp.sin(angle)

class hydrostatic_fluid_parcel:
    def __init__(self, density):
        self.density = density
        
    def hydrostatic_pressure(self, surface_pressure, height):
        return surface_pressure + self.density * 9.81 * height
        
        
'''
How to we compute the force on something due to pressure
Recall: pressure for is  always normal to a surface
'''

# Unit_normal_vector = sp.Matrix([])
# dA = sp.symbols("dA")
# n = sp.Matrix([U * N.i, V * N.j, W * N.k]) # normal vector
# lecture_dict = {dF: "infinitessimal surface force wih magnitude"}
# dF_Magnitude = P*dA
# dF_direction = -n
# P = sp.symbols('P')
# # To compute the net force, we add up all the dFs 
# dF = P * n
# F = sp.integral(dF, A, A) # area integral, more of a concept

# Methods to compute:
#   Analytically (special cases)
#   Computer (more general)

'''
Steps for analytical
    1. Free oody diagram
    2. Define surface coordinate system (ŝ, n̂)
    Define global coordinate system (N.i, N.j)
    Calculate the differential force/moment due to pressure on a surface element
    sum(forces) = 0, sum(moments) = 0 while integrating
'''

'''
Compute the force P required to keep the gate closed.
Assume unit depth into the page. density = 1000 kg/m**3, g = 9.81 N/kg

________________________                                                           
                        <----P      
                            __/     
                         __/                
                      __/       air              
_____________________/|___1m___|
'''
s, l = sp.symbols('s l')

depth = (l - s) * np.sin(np.radians(45))
density_value = 1000

# step 1: free body diagram

''' See notes example
                                                                                           
                        <----P      
                            __/     
                         __/                
                      __/       air              
                 F ->/   angle = 45deg
                     ^Fy               
'''

# step 2: Define surface coordinates (ŝ, n̂)

ŝ = sp.symbols('ŝ') # where s is parralel to the surface
n̂ = sp.symbols('n̂') # where n is perpendicular to the surface 

l = np.sqrt(2)

# Step 4: Differential moment
'''
For some distance S from the hinde
'''
ds = sp.symbols('ds')
M = sp.symbols('M')

P = density_value * 9.81 * depth
A = ds * depth

Force = P * A

Moment = density_value * 9.81 * (l - s) * sp.sin(np.radians(45)) * ds * s

P = sp.integrate(Moment, s) * s

print(P)


'''
Comment: Resultant of the pressure distribution acts at a point
called the centre of pressure

Magnitude = Pcp * A
where Pcg is the hydrostatic pressure at the area centroid
Resultant acts through hcp
delta_cp = cg - cp = Ixx * sin(theta) / ycg * A (gauge units)
where Ixx = (1/12)*b*l**3 (b = depth into page)
'''

# 2. Numerical integration

F = - sp.integrate(P * n̂, A)
for i in 5:
    F_sum += -P[i] * n[i] * A[i]

