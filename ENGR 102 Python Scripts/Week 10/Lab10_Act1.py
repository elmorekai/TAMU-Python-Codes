# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 10 Activity 1
# Date:         09/11/2020
#

import numpy as np
#### PART E ####
# A. As a team, we have gone through all required sections of the tutorial,
# and each team member understands the material.
# B.
# creates random numbers
rg = np.random.default_rng(1)
# create matrices and print
A = np.floor(10*rg.random((3,4)))
B = np.floor(10*rg.random((4,2)))
C = np.floor(10*rg.random((2,3)))
D = np.floor(10*rg.random((3,1)))
print('A:\n', A)
print('B:\n', B)
print('C:\n', C)
print('D:\n', D)
print()
# C. Compute and product of E = ABC
E = A @ B @ C
# matrix multiplication
print('E:\n',E)
print()
# When you try to compute the Product EE = BAC, it will not work. There is an error.
# D. Print the transpose of E
print('Transpose of E:\n', E.transpose())
print()
# E. Solve linear algebraic equations
# set up system
a = np.array([[50, 75, 10], [5, 10, 3], [90, 100, 50]])
b = np.array([500, 75, 1150])
# solve for x y and z and print
vals = np.linalg.solve(a, b)
print('x =', int(np.ceil(vals[0])))
print('y =', int((vals[1])))
print('z =', int((vals[2])))
print()
# F. Solve another system
a = np.array([[1, -2, -4], [2, -3, -6], [-3, 6, 15]])
b = np.array([7, 5, 0])
# solve for x y and z and print
vals = np.linalg.solve(a, b)
print('x =', int(np.ceil(vals[0])))
print('y =', int(np.ceil(vals[1])))
print('z =', int(np.ceil(vals[2])))
# after plugging in values for x, y, and z, all equations are correct


