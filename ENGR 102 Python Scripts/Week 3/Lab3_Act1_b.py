# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 3 Activity 1b
# Date:         09/08/2020

# A program to convert a inputed BTUs to Joules
print('This program converts number of BTUs (BTU) to number of Joules (J)')

# Variables
BTUs = 0 # entered as string then changed to a float
Joules = 0 # float
Conversion_factor = 1055.06 # integer

# Input for the amount of BTUs
print(' Please enter the number of BTUs to be converted to Joules:')
BTUs = float(input('BTUs: '))


# Converting input to Joules
Joules = BTUs * Conversion_factor

# Print statement
print(BTUs, 'BTU is equivalent to {:.2f} Joules'.format(Joules))
print(BTUs, 'BTU = {:.2f} J'.format(Joules))


