# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lecture 4 example
# Date:         09/14/2020
#


# This program prints a quadratic equation in the format
# Ax^2 + Bx + C = 0

# Get coefficient A, B, and C
# A = float(input('Enter coefficient A: '))
# B = float(input('Enter coefficient B: '))
# C = float(input('Enter coefficient C: '))

coef_A = 0.00000001
coef_B = 0
coef_C = 0


print('{:s}x^2 + {:f}x + {:f} = 0'.format(str(coef_A), coef_B, coef_C))

if coef_A == 0:
    print('This is not a quadratic equation, The coefficient A cannot be zero.')
else:
    if coef_A == 1:
        print('x^2', end = '')
    else:
        print('{}x^2'.format(coef_A), end = '')
    
    if coef_B < 0:
        print(' - {}x'.format(abs(coef_B)), end = '')
    elif coef_B > 0:
        print(' + {}x'.format(coef_B), end = '')
    
    if coef_C < 0:
        print(' - {}'.format(abs(coef_C)), end = '')
    elif coef_C > 0:
        print(' + {}'.format(coef_C), end = '')
    
    print(' = 0')


# x = Re + i*Im
Re = 3.4
Im = 1.2

print('x = {} + i*{}'.format(Re, Im))
print('x = {} + {}*i'.format(Re, Im))





