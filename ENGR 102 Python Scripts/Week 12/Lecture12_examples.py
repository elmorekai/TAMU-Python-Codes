# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Dr. O.
# Section:      ENGR 102-...
# Team:         N/A
# Assignment:   Lab ___________
# Date:         _______________

import numpy as np
import matplotlib.pyplot as plt

##################################
### Lab 12 Activity 0 Example ###  
# Part b) Evaluating a polynomial derivative numerically

# def quadratic(a, b, c, x):
#     '''This function evaluates a quadratic function f(x)=ax^2+bx+c at x.
#     Input parameters: a, b, c are the coefficients, real numbers; x is a real number.
#     Return f(x).'''
#     return a*x*x + b*x + c

# # Print info
# print('This program...')

# # Get coefficients
# coef_a, coef_b, coef_c = 1, -2, -4

# # Let's plot the curve
# x_values = np.linspace(-2, 4)
# y_values = quadratic(coef_a, coef_b, coef_c, x_values)

# plt.plot(x_values, y_values)
# plt.title("Quadratic function")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.show()

# # Get x value from the user
# x = 1

# # Evaluating derivative of quadratic function analytically
# deriv_analyt = 2*coef_a*x + coef_b
# print(deriv_analyt)

# Evaluating derivative of quadratic function numerically



##################################
### Lab 12 Activity 1 Example ###  
# Part a) Use eval() to evaluate an arbitrary function that the user enters. 

print('This program imports numpy as np.'\
      ' For example, to input f(x) = sin(6x), type np.sin(6*x)')

user_function = 'x**2 - 1'
# user_function = 'np.sin(6*x)'
print('user_function =', user_function)

# # Let's plot the curve
# x1, x2 = -5, 5   # some interval 
# x_values = np.linspace(x1, x2)
# y_values = quadratic(a, b, c, x_values)

# plt.plot(x_values, y_values)
# plt.title("user_function = '"+ user_function + "'")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.show()


#################################
### Lab 12 Activity 2 Example ###  

#      Thermodynamic Properties of Compressed Water
#    The temperature and property values for P = 5 MPa
# The columns in each sublist contain the following data:
#    Temperature in units of degree C
#    Specific volume (v) in units of m^3⁄kg
#    Specific internal energy (u) in units of kJ/kg
#    Specific enthalpy (h) in units of kJ/kg
#    Specific entropy (s) in units of kJ/(kg∙K)

# A nested list
#   0          1             2             3            4           # column index
#   T          v             u             h            s           # quantity stored
data = [
[	0	, 	0.0009977	, 	0.04	, 	5.03	, 	0.0001	],      # sublist at position 0 in data, that is data[0]
[	20	, 	0.0009996	, 	83.61	, 	88.61	, 	0.2954	],      # sublist at position 1 in data, that is data[1]
[	40	, 	0.0010057	, 	166.92	, 	171.95	, 	0.5705	],      # sublist at position 2 in data, that is data[2]
[	60	, 	0.0010149	, 	250.29	, 	255.36	, 	0.8287	],      # sublist at position 3 in data, that is data[3]
[	80	, 	0.0010267	, 	333.82	, 	338.96	, 	1.0723	],      # etc.
[	100	, 	0.0010410	, 	417.65	, 	422.85	, 	1.3034	],
[	120	, 	0.0010576	, 	501.91	, 	507.19	, 	1.5236	],
[	140	, 	0.0010769	, 	586.8	, 	592.18	, 	1.7344	],
[	160	, 	0.0010988	, 	672.55	, 	678.04	, 	1.9374	],
[	180	, 	0.0011240	, 	759.47	, 	765.09	, 	2.1338	],
[	200	, 	0.0011531	, 	847.92	, 	853.68	, 	2.3251	],
[	220	, 	0.0011868	, 	938.39	, 	944.32	, 	2.5127	],
[	240	, 	0.0012268	, 	1031.6	, 	1037.7	, 	2.6983	],
[	260	, 	0.0012755	, 	1128.5	, 	1134.9	, 	2.8841	]
]

# Linear interpolation: recall Lab 8
# v(T) = v1 + (T – T1)(v2 – v1)/(T2 – T1)

import numpy as np

data = np.array(data)
print(data)