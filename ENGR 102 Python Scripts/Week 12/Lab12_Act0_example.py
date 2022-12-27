# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 12 Activity 0 example
# Date:         11/9/2020
#

import numpy as np
import matplotlib.pyplot as plt

##################################
### Lab 12 Activity 0 Example ###  
# Part b) Evaluating a polynomial derivative numerically

def quadratic(a, b, c, x):
    '''This function evaluates a quadratic function f(x)=ax^2+bx+c at x.
    Input parameters: a, b, c are the coefficients, real numbers; x is a real number.
    Return f(x).'''
    return a*x*x + b*x + c

# Print info
print('This program...')

# Get coefficients
coef_a, coef_b, coef_c = 1, -2, -4

# Let's plot the curve
x_values = np.linspace(-2, 4)
y_values = quadratic(coef_a, coef_b, coef_c, x_values)

plt.plot(x_values, y_values)
plt.title("Quadratic function")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# Get x value from the user
x = 2

# Evaluating derivative of quadratic function analytically
deriv_analyt = 2*coef_a*x + coef_b
print('deriv_anlyt =', deriv_analyt)
print()

# Evaluating derivative of quadratic function numerically
TOL = 1e-6

# Calculate the first evaluation of f'(x) using formward differene formula
a = 0.1 # step
dfx = quadratic(coef_a, coef_b, coef_c, x+a) - quadratic(coef_a, coef_b, coef_c, x)
dfx = dfx/a

# Calculate the second evaluation of f'(x) using formward differene formula
a = a/2 # step
dfx_new = quadratic(coef_a, coef_b, coef_c, x+a) - quadratic(coef_a, coef_b, coef_c, x)
dfx_new = dfx_new/a

print('dfx  dfx_new   |dfx_new - dfx|')
print('{:20.16f} {:20.16f} {:20.16f}'.format(dfx, dfx_new, abs(dfx_new - dfx)))

while abs(dfx_new - dfx) >= TOL:
    a = a/2 # step
    dfx = dfx_new
    dfx_new = quadratic(coef_a, coef_b, coef_c, x+a) - quadratic(coef_a, coef_b, coef_c, x)
    dfx_new = dfx_new/a
    print('{:20.16f} {:20.16f} {:20.16f}'.format(dfx, dfx_new, abs(dfx_new - dfx)))