# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 10 Activity 2
# Date:         10/30/2020
#

import matplotlib.pyplot as plt
import numpy as np
import math
# Plot 1:
# create x values to use for graphing
x = np.linspace(-2.0,2.0)
# plot euqation when focal length = 2
y1 = (1/8) * (x**2)
plt.plot(x, y1, '-r', linewidth = 2.0, label = 'f = 2')
# plot equation when focal length = 6
y2 = (1/24) * (x**2)
plt.plot(x, y2, '-b', linewidth = 4.0, label = 'f = 6')
# add x and y axis labels, title of graph, and a legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parabola Plots with Varying Focal Length')
plt.legend(loc = 'lower left')
# Plot 2:
# create variables for values to plug into polynomial
A = 2
B = 3
C = -11
D = -6
# plot equation based on given domain values
x = np.linspace(-4.0, 4.0, 25)
y = A*(x**3) + B*(x**2) + C*x + D
plt.plot(x, y, '*')
# plot x and y axis labels, and the title of the graph
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Plot of Cubic Polynomial')
# Plot 3
# Plot equation based on given domain values
x = np.linspace(-2*math.pi, 2*math.pi)
# plot cos(x)
y1 = np.cos(x)
plt.plot(x, y1, 'r', label = 'cos(x)')
# plot sin (x)
y2 = np.sin(x)
plt.plot(x, y2, 'b', label = 'sin(x)')
# plot graph labels
plt.ylabel('y values')
plt.xlabel('x values')
plt.title('Plot of cos(x) and sin(x)')
plt.legend(loc = 'lower left')


