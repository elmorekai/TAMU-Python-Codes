# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 4b Program 1
# Date:         09/18/2020

# this program will produced the largest value out of 3 numbers from user input
print('This program will produce the largest value out of 3 numbers from user \
input')

# Variables
Val_1 = float(input('Enter the first value here: '))
Val_2 = float(input('Enter the second value here: '))
Val_3 = float(input('Enter the third value here: '))

# Finding largest value
if (Val_1 > Val_2) and (Val_1 > Val_3): # uses conditionals to compare values
    print('The largest value is', Val_1)
elif (Val_2 > Val_1) and (Val_2 > Val_3):
    print('The largest value is', Val_2)
elif (Val_3 > Val_1) and (Val_3 > Val_2):
    print('The largest value is', Val_3)


