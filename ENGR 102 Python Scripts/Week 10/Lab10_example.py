# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 10 Activity 0
# Date:         10/26/2020
#

import numpy as np
import matplotlib
print('numpy, matplotlib')

a = np.arange(15).reshape(3,5)
print(a)

b = np.array([6, 7, 8])
print(b)

c = [6, 7, 8]
b = np.array(c)
print(b)

c = [6, 7, 8]
b = np.array(c, dtype = float)
print(b)

b = np.array([1.2, 3, 5.1])
print(b)

b = np.array ([(1.5,2,3), (4,5)])
print(b)

b = np.array ([(1.5,2,3), (4,5,6)])
print(b)

a = np.array ([20,30,40,50])
b = a*2
print(b)

x = np.array([1,2,3,4,5])
y = np.cos(x)

# cosine function from math module doesn't work 
# with arrays. Would need to use a list.
# Use numpy stuff for numpy arrays. 
# import math 
# y = math.cos(x)

a = np.arange(15).reshape(3,5)
print(a)

import matplotlib.pyplot as plt
# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()

x = np.linspace(1,10)
print(x)
y = x**2
print(y)
plt.plot(x, y, 'b-')
plt.title('my parabola')
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x, x**3, 'r*')

plt.show()