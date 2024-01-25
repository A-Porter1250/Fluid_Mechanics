# Lecture 7: Manometry in Hydrostatics
import numpy as np
import scipy
import sympy as sp

'''
Pascal's Law: within the same connected fluid, two points at equal height will have equal pressure.
'''
GRAVITY = 9.81 # m / s**2

def Pressure(Pressure_not, density, height_difference):
    answer = Pressure_not + density*GRAVITY*height_difference
    return answer

# from B to 1
h = 6 * 10**(-2)
row = 997
P_not = 87*(10**3)

answer_1 = Pressure(h, row, P_not)
# print(answer_1)

# EX: A mercury manometer is used to measure air pressure inside a tank. What is the gauge pressure in the tank

SG_mercury = 13.6 # Specific Gravity as compared to water (ie, SG * water_density)
density_water = 1000 # kg / m**3
print(Pressure(Pressure_not=0, density=density_water*SG_mercury, height_difference=300*10**-3))

# EX: Manometers are often inclined to reduce error in measurement.
# Determine the "Pa/m measure" as a function of theta.
'''
| |
| |
| |
| |           _/
| |        __/  _/
\ \      __/ __/ \
 \ \____/ __/     \
  \______/         |<-angle theta
'''

def angled_gauge_pressure(density, height, angle_deg):
    return density*GRAVITY*height*np.sin(angle_deg*2*np.pi/360)

# Where theta is equal to : 90, l=1cm, %error=5% | 60, l=1.2cm, %error=4.2% | 30, l=2cm, %error=2.5% | 10, l=5.8cm, %error=0.85%