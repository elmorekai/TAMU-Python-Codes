# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 5b Program 2
# Date:         09/25/2020
#

# This program asks a user for measurements and prints the number of 
# measurements, the average, the maximum, and the minimum measurement. Users
# are allowed to enter as many measurements as they want, until entering a 
# negative measurement. The negative measurement is not be processed, but is 
# just used to indicate that the user has finished entering measurements.

print('This program asks a user for measurements and prints the number of \
measurements, the average, the maximum, and the minimum measurement. Users \
are allowed to enter as many measurements as they want, until entering a \
negative measurement. The negative measurement is not be processed, but is \
just used to indicate that the user has finished entering measurements.')

# Variables 
measurement = 0
total = 0
min_val = float('Infinity')
max_val = -1
num_of_measure = 0

# Loop to take in inpute and calculate the max, min, and number of inputs, and
# the average. 
while measurement >= 0:
    measurement = float(input('Please enter measurment without units here: '))
    if measurement >= 0:
        if measurement > max_val:
            max_val = measurement
        if measurement < min_val:
            min_val = measurement
        num_of_measure += 1
        total += measurement
    else:
        average = total / num_of_measure    
        print('The number of measurements:', num_of_measure)
        print('The average: {:.3f}'.format(average))
        print('The maximum: {:.3f}'.format(max_val))
        print('The minimum: {:.3f}'.format(min_val))