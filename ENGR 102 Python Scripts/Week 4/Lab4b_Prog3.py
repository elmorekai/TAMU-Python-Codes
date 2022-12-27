# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 4b program 3
# Date:         09/19/2020
#

# This predicts the amount of widgets a machine produces from a user inputed 
# amount of days between 0 days to 100 days
print('This program predicts the amount of widgets a machine produces from a \
user inputed amount of days between 0 days to 100 days')

# Variables
days = float(input('Please enter the amount of days between 0 and 100 here: '))
widgets = 0

# Conditionals
if (days >= 0) and (days <= 10): # if 0 <= days <= 10
    widgets += 10 * days # equation for total of widgets
elif (days >= 11) and (days <= 60): # if 11 <= days <= 60
    widgets += 100 + 40 * (days - 10) # equation for total of widgets
elif (days >= 61) and (days <= 100): # if 61 <= days <= 100
    widgets += 2100 + (((days - 61) + 1) * (39 + (39 - (days - 61)))) / 2 
    # equation for total of widgets
else:
    print('Error: the amount of days given is out of domain. ')
    
print('The total amount of widgets made after', days,'days is', widgets,'widgets.')

