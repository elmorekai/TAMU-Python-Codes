# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 3b program 1c
# Date:         09/11/2020
#

from math import *
# Using the Mohr-Coulomb Failure Criterion
# This programs calculates the shear stress when a given normal stress in 
# lbf/in^2 is applied to a material with a given cohesion in lbf/in^2 at a 
# given angle of internal friction in degrees. 

print('This programs calculates the shear stress when a given normal stress in \
lbf/in^2 is applied to a material with a given cohesion in lbf/in^2 at a \
given angle of internal friction in degrees.') # description of program

print('Please only type in numbers and not letters, for example 20 is a good \
input.') # instructions on how to input values

stress = float(input('Please enter stress (lbf/in^2) here: '))
# input of stess as a string turned into a float in pounds * f/ inches squared

cohension = float(input('Please enter cohension (lbf/in^2) here: '))
# input of cohension as a string turned into a float in 
# pounds * f / inches squared

friction_angle = float(input('Please enter the angle of internal friction \
(degrees) here: ')) 
# input of friction as a string turned into a float in degrees

sheer_stress = stress * tan(friction_angle * (pi / 180)) + cohension 
# Assigning the found sheer stress using the Mohr-Coulomb Failure Criterion 
# in lbf/in^2

print("The shear stress =", sheer_stress, "lbf/in^2")

