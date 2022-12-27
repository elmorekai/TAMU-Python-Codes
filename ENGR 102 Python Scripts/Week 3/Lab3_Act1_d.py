# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 3 Activity 1d
# Date:         09/09/2020
#

# A program to convert a inputed seconds per revolution to Hertz
print('This program converts a number of seconds per revolution (s/rev) to a \
      number of Hertz (Hz)')

# Variables
Seconds = 1 # entered as string then changed to a float, 1 is placeholder 
Hertz = 0 # float
Conversion_factor = Seconds ** -1 # equation

# Input for the amount of seconds per revolution
print('Please enter the number of Seconds per revolution to be converted to Hertz:')
Seconds = float(input('Seconds: '))       
       
# Converting input to Hertz
Conversion_factor = Seconds ** -1
Hertz = Conversion_factor

# Print statement
print(Seconds, 'seconds per revolution is equivalent to {:.2f} \
Hertz'.format(Hertz))
print(Seconds, 's/rev = {:.2f} Hz'.format(Hertz))

