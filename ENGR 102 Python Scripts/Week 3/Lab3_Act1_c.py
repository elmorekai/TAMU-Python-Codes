# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 3 Activity 1c
# Date:         09/08/2020

# A program to convert a inputed Pascals to Millimeters of Mercury
print('This program converts a number of Pascals (Pa) to a number of \
      Millimeters of Mercury (mmHg)')

# Variables
Pascals = 0 # entered as string then changed to a float
Mercury = 0 # float
Conversion_factor = 0.00750062 # integer

# Input for the amount of Pascals
print('Please enter the number of Pascals to be converted to Millimeters of \
      Mercury:')
Pascals = float(input('Pascals: '))


# Converting input to Millimeters of Mercury
Mercury = Pascals * Conversion_factor

# Print statement
print(Pascals, 'Pascals is equivalent to {:.2f} Millimeters of \
Mercury'.format(Mercury))
print(Pascals, 'Pa = {:.2f} mmHg'.format(Mercury))

