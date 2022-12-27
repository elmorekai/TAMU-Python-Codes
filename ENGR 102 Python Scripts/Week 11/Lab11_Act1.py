# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 11 Activity 1
# Date:         11/2/2020
#

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

# Test Cases:
    # 3x^2 + 5x - 3, a = 0, b = 10, root = 0.468
    # 3x^5 + x^2 -15, a = 1, b = 100, root = 1.345
    # -12x^4 + 5x^3 - 2x + 20, a -100, b= 0, root = -1.074
    
# print statment to explain program
print('This program uses the bisection method to find a single root of P(x) on \
      interval (a, b)')

# input for the coefficents of the polynomials
coef = input('Please enter the coefficients of the polynomial you want to find\
 the root of P(x) here seperated by commas: ')
# input for the interval bounds a and b
interval = input("Please enter the interval that contains exactly one single \
 root of P(x), where 'a' is less than 'b', here (eg: 15, 20): ")

# format of the header for the data table
header_format = '{:>4} {:^12} {:^12} {:^12} {:^12} {:^12} {:^12}'
header = header_format.format('iter', 'a', 'b', 'c', 'fa', 'fc', '|b - a|')
data_format = '{:>4} {:>12.8f} {:>12.8f} {:>12.8f} {:>12.8f} {:>12.8f} {:>12.8f}'
# splitting the interval into a and b seperately
bounds = interval.split(',')
a = int(bounds[0])
b = int(bounds[1])

# creating the polynomial to print from the given coefficents
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
            poly += ' + ' + i 
    power -= 1

# tolerance values for |b-a| and |f(c)|
TOL_1 = 1e-6 # tolerance for |b-a|
TOL_2 = 1e-8 # tolerance for |f(c)|

# main body of code to find the root of the polynomial
print('P(x) =', poly)
print('Interval (a,b) = ({}, {})'.format(a, b))
print('The loop iterates until the size of the interval decreases below 1.0e-06 \
or the absolute value of the function decreases below 1.0e-08, or both.')
print()
print(header)
print('-' * len(header))

iteration = 1

if a < b and coef != '': 
    c = (a + b)/2
    f_c = calculate(c, poly_coef)
    f_a = calculate(a, poly_coef)
    difference = abs(b - a)
    
    while abs(b - a) >= TOL_1 and abs(f_c) >= TOL_2:
        data = data_format.format(iteration, a, b, c, f_c, f_a, difference)
        print(data)
        product = f_a * f_c
        if product < 0:
            b = c
        elif product > 0:
            a = c
        else:
            print('The root is {}'.format(c))
            break
        
        c = (a + b)/2
        f_c = calculate(c, poly_coef)
        f_a = calculate(a, poly_coef)
        difference = abs(b - a)
        iteration += 1
    
    print()
    print('The root of P(x) is {:.8f}'.format(c))
    print('P(root) = {:.8f}'.format(f_c))
    print('The number of iterations was', iteration)
    
# error statements
elif a > b:
    print()
    print("Error: the value of 'a' must be less than the value of 'b'.")
elif coef == '' or interval == '':
    print()
    print('Error: there were empty input values detected, please input values')













