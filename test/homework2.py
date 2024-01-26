from functions import hydrostatics as hs

import numpy as np
import sympy as sp

water_density = 1000 # kg / m**3
SG_mercury = 13.6
SG_SAE_30 = 0.78
P_atm = 101.325 * 10 ** 3 # Pa

mercury_density = 13.6 * water_density
SAE_30_density = 0.78 * water_density

bottom_pressure = 242 * 10 ** 3
x = sp.symbols('x')

SAE_bottom_pressure = hs.hydrostatic_pressure(P_atm, SAE_30_density, 1)
print(SAE_bottom_pressure)
water_bottom_pressure = hs.hydrostatic_pressure(SAE_bottom_pressure, water_density,2)
print(water_bottom_pressure)
fluid_x_pressure = hs.hydrostatic_pressure(water_bottom_pressure, x, 3)
print(fluid_x_pressure)
mercury_density_expression = hs.hydrostatic_pressure(fluid_x_pressure, mercury_density, 0.5)
print(mercury_density_expression)
equation = sp.Eq(bottom_pressure, mercury_density_expression)
print(equation)
answer = sp.solve(equation, x)
print(answer[0] / 1000)
