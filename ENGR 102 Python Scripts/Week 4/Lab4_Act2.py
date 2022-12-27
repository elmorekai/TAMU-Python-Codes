# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 4 Activity 2
# Date:         09/14/2020
#

# This a program that computes parking fees for a garage. The program takes
# user input of the number of hours parked in garage, and output the total fee 
# for parking.

from math import *
print('This a program that computes parking fees for a garage. The program \
takes user input of the number of hours parked in garage, and output \
the total fee for parking.')
print()
print('Enter the hours parked as a decimal number. Include a negative sign if \
the ticket is lost.')
hours = ceil(float(input('Please enter the hours parked: ')))
charge = 0 
if (hours > 0):
    if (hours >= 0) and (hours <= 2): # if 0 <= hours < 2
        charge += 4                     # add $4
    elif (hours > 2) and (hours <= 4): # if 2 <= hours <= 4
        charge += 4 + 3                 # add $7
    elif (hours > 4) and (hours < 24): # if  4 < hours < 24
        charge += 4 + 3 + (hours - 4) # add $7 + $1 per extra hour
    elif (hours >= 24):                # if 24 < hours
        charge += 24 * (hours // 24) # add $24 per day, with remaining treated the 
        if ((hours % 24) >= 0) and ((hours % 24) <= 2): # same as above
            charge += 4
        elif ((hours % 24) > 2) and ((hours % 24) <= 4): 
            charge += 4 + 3
        elif ((hours % 24) > 4) and ((hours % 24) < 24):
            charge += 4 + 3 + (hours - 4)
    print('Parking for', hours, 'hours please pay $' + str(charge))
if (hours < 0):                     # if user lost ticket, use previous rules
    hours = abs(hours)              # and add $36
    charge += 36
    if (hours >= 0) and (hours <= 2):
        charge += 4
    elif (hours > 2) and (hours <= 4): 
        charge += 4 + 3
    elif (hours > 4) and (hours < 24):
        charge += 4 + 3 + (hours - 4)
    elif (hours >= 24):
        charge += 24 * (hours // 24)
        if ((hours % 24) >= 0) and ((hours % 24) <= 2):
            charge += 4
        elif ((hours % 24) > 2) and ((hours % 24) <= 4): 
            charge += 4 + 3
        elif ((hours % 24) > 4) and ((hours % 24) < 24):
            charge += 4 + 3 + (hours - 4)
    print('Parking for', hours, 'hours and lost ticket please pay $' + str(charge))

