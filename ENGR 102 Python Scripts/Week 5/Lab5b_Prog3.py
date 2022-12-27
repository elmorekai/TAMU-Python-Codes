# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 5b Program 3
# Date:         09/25/2020
#

# This program estimates the value of f(x) = (1/1-x) from an inputted x using 
# Maclaurin series expansion. The x must -1<x<1. 

print('This program estimates the value of f(x)=(1/1-x) from an inputted x using \
Maclaurin series expansion. The x must be -1<x<1. ')

# Variables
TOL = 1e-6
x = float(input('Please enter the an x between -1 and 1 here: '))
f_x = 0 
n = 0
term = x ** n
counter = 0 
calculate_val = 1 / (1 - x)
difference_of_val = 0

# Conditional
if x < -1 or x > 1:
    print('Error: invalid input')
else:
    # Loop for Maclaurin series expansion
    while abs(term) >= TOL:
        f_x += term
        counter += 1
        n += 1
        term = x ** n
    difference_of_val = calculate_val - f_x
    print('The estimated value of f(x) at', x,'was {:.4f}'.format(f_x))
    print('The number of terms added was', counter)
    print('The calculated value of f(x) at', x,'was {:.4f}'.format(calculate_val))
    print('The difference of the estimated value and the calculated value is', end =" ")
    print('{:.4f}'.format(difference_of_val))



















