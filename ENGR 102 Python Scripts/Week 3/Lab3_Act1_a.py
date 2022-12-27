# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 3 Activity 1a
# Date:         09/08/2020

# A program to convert a inputed force measured in pounds to Newtons
print('This program converts number of pounds (lbf) to number of Newtons (N)')

# Variables
Force = 0 # entered as string then changed to a float
Newtons = 0 # float
Conversion_factor = 4.44822 # integer

# Input for the amount of force
print(' Please enter the number of pounds to be converted to Newtons:')
Force = float(input('Force: '))


# Converting input to Newtons
Newtons = Force * Conversion_factor

# Print statement
print(Force, 'pounds is equivalent to {:.2f} Newtons'.format(Newtons))
print(Force, 'lbf = {:.2f} N'.format(Newtons))


