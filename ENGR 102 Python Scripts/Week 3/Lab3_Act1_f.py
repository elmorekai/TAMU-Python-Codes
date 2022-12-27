# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 3 Activity 1f
# Date:         09/09/2020
#

# A program to convert a inputed Fahrenheit to Celsius
print('This program converts a measurement of Fahrenheit (\u00B0F) to a \
measurement of Celsius (\u00B0C)')

# Variables
Fahrenheit = 0 # entered as string then changed to a float
Celsius = 0 # float
Conversion_factor = ((Fahrenheit - 32) * 5) / 9 # equation

# Input for the measurement of Fahrenheit
print('Please enter the measurement of Fahrenheit to be converted to Celsius:')
Fahrenheit = float(input('Fahrenheit: '))

# Converting input to Celsius
Conversion_factor = ((Fahrenheit - 32) * 5) / 9 
Celsius = Conversion_factor

# Print statement
print(Fahrenheit, 'degrees Fahrenheit is equivalent to {:.2f} degrees Celsius '\
      .format(Celsius))
print(Fahrenheit, '\u00B0F = {:.2f} \u00B0C'.format(Celsius))

