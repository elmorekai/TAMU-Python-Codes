# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 4b Program 4
# Date:         09/19/2020
#

from math import *
# This program tsolves a quadratic (or linear) equation. The program asks a 
# user for the coefficients 𝐴, 𝐵, and 𝐶 and outputs the roots of that equation
print('This program tsolves a quadratic (or linear) equation. The program asks \
a user for the coefficients 𝐴, 𝐵, and 𝐶 and outputs the roots of that \
equation.')

# Variables
A = float(input('Please enter the coefficient A: ')) # takes user input for 
B = float(input('Please enter the coefficient B: ')) # coefficients
C = float(input('Please enter the coefficient C: '))
D = (B ** 2) - (4 * A * C)

# Conditionals
if D < 0: # What to do when D equates to a negative number
    x_real_comp = str((-1 * B) / (2 * A)) # the real component of x
    x_imag_comp = str(sqrt(abs(D)) / (2 * A)) # the imaginary compnent of x
    print('There are two complex roots: ')
    print('x1 =', x_real_comp, '+', x_imag_comp + 'i')
    print('x2 =', x_real_comp, '-', x_imag_comp + 'i')
elif D == 0: # What to do when D equates to 0
    if (A == 0) and (A == B) and not(C == 0): # if only A and B equal zero
        print('Error: this is a horizontal line and has no roots to find')
    elif C == 0: # if only C equals 0
        print('Error: no equation to solve')
    else: 
        x1 = ((-1 * B) + sqrt(D)) / (2 * A) # equation for root
        print('There is one real roots')
        print('x1 =', x1)
elif D > 0: # What to do if D equates to something greater than zero
    if A == 0: # if only A equals zero
        x1_linear = (-1 * C) / B # equation for root in linear line
        print('This is a linear equation with one real root')
        print('x1 =', x1_linear)
    else:
        x1 = ((-1 * B) + sqrt(D)) / (2 * A) # equation for root with addition
        x2 = ((-1 * B) - sqrt(D)) / (2 * A) # equation for root with subtraction
        print('There are two real roots')
        print('x1 =', x1)
        print('x2 =', x2)

    

