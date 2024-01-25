'''
streamline equations

dx/U = dy/V, where U is the x component of the stream and V is the y component

'''
import numpy as np
import sympy as sp
import scipy
import math as mt
import matplotlib.pyplot as plt

K = sp.symbols('K')
x = sp.symbols('x')
y = sp.Function('y')

U = K*x
V = -K*y
function_of_x = sp.simplify(V/U)
ode = sp.Derivative(y(x), x) - function_of_x
solution = sp.dsolve(ode)
print(solution)

expression = sp.lambdify((x, y, K), function_of_x, 'math')
#print(expression)


def dydx(y, x, K):
    return expression(y, x, K)

print(dydx(y, x, K))

# K_value = 2

# def dydx(x, y):
#     return 2*y + 1

# x_values = np.linspace(0, 1, 100)
# y0 = 1
# solution = scipy.integrate.odeint(dydx, y0, x_values)

# plt.plot(x, y)
# plt.xlabel('Time')
# plt.ylabel('y(t)')
# plt.title('Solution of the Differential Equation')
# plt.show()


