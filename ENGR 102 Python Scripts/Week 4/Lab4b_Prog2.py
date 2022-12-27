# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 4b program 2
# Date:         09/19/2020


# This program calculates the Reynolds number for a pipe flow and report 
# whether the flow is laminar, in transition, or turbulent. 
# laminar pipe flow is 𝑅𝑒𝑑 < 2300 and fully turbulent for 𝑅𝑒𝑑 > 2900
# and in transition between those limits. 

print('This program calculates the Reynolds number for a pipe flow and report \
whether the flow is laminar, in transition, or turbulent.')
print('To find the Reynolds number, please enter the following values:')


# Variables for Reynolds number equation
velocity = float(input('Please enter velocity in m/s: '))
diameter = float(input('Please enter pipe diameter in meters: '))
viscosity = float(input('Please enter fluid kinematic viscosity in m^2/s: '))
Re = (velocity * diameter) / viscosity

# Conditionals for sorting type of Reynolds number
print('The Reynolds number is', Re)
if (Re < 2300):
    print('The flow is laminar')
elif (Re > 2900): 
    print('The flow is turbulent')
elif (Re >= 2300) and (Re <= 2900):
    print('The flow is transition')
    