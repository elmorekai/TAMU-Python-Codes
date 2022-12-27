# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 12 Activity 0
# Date:         11/13/2020
#

def poly(coef):
    '''This function creates a polynomial from a given list of coefficients'''
    poly_coef = coef.split(', ')
    poly = ''
    power = len(poly_coef) - 1
    for i in poly_coef:
        if power > 0:
            if i == poly_coef[0]:
                poly += i + 'x^{}'.format(power)
            elif '-' in i: 
                poly += ' ' + i + 'x^{}'.format(power)
            else: 
                poly += ' + ' + i + 'x^{}'.format(power)
        elif power == 0:
            if '-' in i:
                poly += ' ' + i + 'x^{}'.format(power)
            else:
                if len(poly_coef) == 1:
                    poly += str(i)
                else:
                    poly += ' + ' + i 
        power -= 1
    return (poly, poly_coef)

def derivative(coef):
    '''This function calculates the derivative and derivative coefficients of a 
        given list of polynomial coefficients'''
    deriv_coef = coef.split(', ')
    deriv = ''
    power = len(deriv_coef) - 1
    deriv_coef.pop(-1)
    new_coef = []
    for j in range(len(deriv_coef)):
        deriv_coef[j] = float(deriv_coef[j])
    for i in deriv_coef:
        if power > 1:
            if i == deriv_coef[0]:
                new_coef.append(i * power)
                co = str(i * power)
                deriv += co + 'x^{}'.format(power - 1)
            elif i < 0:
                new_coef.append(i * power)
                co = str(i * power)
                deriv += ' ' + co + 'x^{}'.format(power - 1)
            else:
                new_coef.append(i * power)
                co = str(i * power)
                deriv += ' + ' + co + 'x^{}'.format(power - 1)
        elif power == 1:
            if i < 0:
                new_coef.append(i * power)
                co = str(i * power)
                deriv += ' ' + co
            else:
                if len(deriv_coef) == 1:
                    deriv += str(i * power)
                else:
                    new_coef.append(i * power)
                    co = str(i * power)
                    deriv += ' + ' + co 
        power -= 1
    if len(deriv_coef) == 0:
        deriv += str(0)
    return (deriv, new_coef)

def calculate(x, polynomial):
    ''' this function finds the value of a polynomial at a given x '''
    f_x = 0
    new_power = len(polynomial) - 1
    for i in range(len(polynomial)):
        polynomial[i] = int(polynomial[i])
    for i in polynomial:
        f_x += i * (x ** new_power)
        new_power -= 1
    return f_x

# prints the purpose of this program for Part A
print('In part A of this program, the program takes in a polynomial as a set of \
coefficients, creates a derivative based off that polynomial, and to evaluate \
an inputted x for the polynomial and derivative.')
print()

# prints the purpose of this program for Part B
print('In part B of this program, the program will take the polynomial from part A \
and compute the limit of the polynomial at the inputted x using these equations: \
(f(x+a) - f(x)/a), (f(x) - f(x-a)/a), and (f(x+a) - f(x-a)/2a) \
as the difference, a, approaches 1*10^-6.')
print()
print('-----Part A-----')

# asks for the list of coefficients for the polynomial
coef_list = input('Please the polynomial as a list of polynomials seperated by \
commas: ')

# asks for the x value to be compute in the polynomial and derivative
x_val = float(input('Please input the x value to be computed in the polynomial and \
              derivative here: '))

# finding the polynomial and the list of coefficients 
polynomial, poly_coef = poly(coef_list)
# finding the derivative and the list of coefficients
deriv, deriv_coef = derivative(coef_list)
# print statement
print('Polynomial:', polynomial)
print('The derivative:', deriv)
print('f(x) is', calculate(x_val, poly_coef))
print("f'(x) is", calculate(x_val, deriv_coef))
print()

print('-----Part B-----')

# setting the tolerance of difference of successive calculations
TOL = 1e-6

# calculating first estimate
a = 0.1
f_x = calculate(x_val, poly_coef)
f_xa = calculate(x_val + a, poly_coef)
pre_limit = (f_xa - f_x)/a

# setting the difference of successive calculations as a random number
difference = 1

# setting the loop counter
counter = 0

# setting the loop for the (f(x+a)-f(x)/a) limit calculation
while difference >= TOL:
    a = a/2
    f_x = calculate(x_val, poly_coef)
    f_xa = calculate(x_val + a, poly_coef)
    limit = (f_xa - f_x)/a
    difference = pre_limit - limit
    pre_limit = limit
    counter += 1
print("f'(x) = (f(x+a) - f(x))/a =", limit) # very little difference from calculated f'(x)
print('This method took', counter,'evaluations') # take the most evaluations

# calculating first estimate
a = 0.1
f_x = calculate(x_val, poly_coef)
f_x_a = calculate(x_val - a, poly_coef)
pre_limit = (f_x - f_x_a)/a

# setting the difference of successive calculations as a random number
difference = 1

# setting the loop counter
counter = 0

# setting the loop for the (f(x)-f(x-a)/a) limit calculation
while difference >= TOL:
    a = a/2
    f_x = calculate(x_val, poly_coef)
    f_x_a = calculate(x_val - a, poly_coef)
    limit = (f_x - f_x_a)/a
    difference = pre_limit - limit
    pre_limit = limit
    counter += 1
print("f'(x) = (f(x) - f(x-a))/a =", limit) # off by a little from the calculated f'(x)
print('This method took', counter,'evaluations') 

# calculating first estimate
a = 0.1
f_x_a = calculate(x_val - a, poly_coef)
f_xa = calculate(x_val + a, poly_coef)
pre_limit = (f_xa - f_x_a)/(2*a)

# setting the difference of successive calculations as a random number
difference = 1

# setting the loop counter
counter = 0

# setting the loop for the (f(x+a)-f(x-a)/a) limit calculation
while difference >= TOL:
    a = a/2
    f_x_a = calculate(x_val - a, poly_coef)
    f_xa = calculate(x_val + a, poly_coef)
    limit = (f_xa - f_x_a)/(2*a)
    difference = pre_limit - limit
    pre_limit = limit
    counter += 1
print("f'(x) = (f(x+a) - f(x-a))/a =", limit) # very little  difference from calculated f'(x)
print('This method took', counter,'evaluations') # takes the least amount of evaluations