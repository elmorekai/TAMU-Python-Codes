# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 3 Activity 1e
# Date:         09/09/2020
#

# A program to convert a inputed miles per hour to meters per second
print('This program converts a number of mile per hour (mi/h) to a number of \
     meters per second (m/s)')

# Variables
Miles_hour = 0 # entered as string then changed to a float
Meters_second = 0 # float
Conversion_factor = 0.4470388889 # integer

# Input for the amount of Miles per hour
print('Please enter the number of miles per hour to be converted to meters per \
      seconds:')
Miles_hour = float(input('Miles per hour: '))


# Converting input to Meters per hour
Meters_second = Miles_hour * Conversion_factor

# Print statement
print(Miles_hour, 'Miles per hour is equivalent to {:.2f} meters per second '\
      .format(Meters_second))
print(Miles_hour, 'mi/h = {:.2f} m/s'.format(Meters_second))

