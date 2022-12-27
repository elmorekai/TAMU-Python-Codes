# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lecture 5
# Date:         09/21/2020

'''
# Given a quadratic function f(x) = ax^2 + bx + c and a closed interval
# [x1, x2], evaluate f(x) for n evenly spaced values of x and print
# the results in a table:
# x      f(x)
# - set the width of each column to 10 spaces
# - show four(4) decimal places for x and f(x)
# - The values should be printed right justified
# - There should be exactly three (3) spaces between the columns


# Ask the user to input 10 values and find the smallest value.


# Approxiamte the f(x) = ln(1+x) for -1 < x <= 1 using the Maclaurin series expanison
# https://mathworld.wolfra.com/MaclurinSeries.html
'''

# a = 3.4
# b = -2.5
# c = 0.4 

# x1 = 0
# x2 = 10

# n = 5

# x_step = (x2 - x1) / (n - 1)

# # x - float, current value of x
# # f_x - float, value of f at x

# # Print the table header
# print('{:^10s}   {:^10s}'.format('x', 'f(x)'))

# x = x1
# while (x <= x2):
#     # Caluclate f(x)
#     f_x = a*x*x + b*x + c
#     # Print x and f(x)
#     print('{:>10.4f}   {:>10.4f}'.format(x, f_x))
#     # Update x
#     # x = x + x_step
#     x += x_step

# print()

# for i in range(5):
#     x = x1 + i*x_step
#     # Caluclate f(x)
#     f_x = a*x*x + b*x + c
#     # Print x and f(x)
#     print('{:>10.4f}   {:>10.4f}'.format(x, f_x))

# print()

# x = x1
# for i in range(5):
#     # Caluclate f(x)
#     f_x = a*x*x + b*x + c
#     # Print x and f(x)
#     print('{:>10.4f}   {:>10.4f}'.format(x, f_x))
#     x += x_step
    
'''    
# Ask the user to input 10 positive values and find the largest value.
'''
# max_val = -1

# for i in range(10):
#     # Ask the user to input a positive number
#     # Compare the user input to the max_val
#     # If the user input is smaller then update max_val
#     num = float(input('Please enter a positive number: '))
    
#     if (num > max_val):
#         max_val = num
        
# print(max_val)

# '''    
# # Ask the user to input 10 positive values and find the smallest value.
# '''

# max_val = float('Infinity')

# for i in range(10):
#     # Ask the user to input a positive number
#     # Compare the user input to the max_val
#     # If the user input is smaller then update max_val
#     num = float(input('Please enter a positive number: '))
    
#     if (num < max_val):
#         max_val = num
        
# print(max_val)

'''
# Approxiamte the f(x) = ln(1+x) for -1 < x <= 1 using the Maclaurin series expanison
# https://mathworld.wolfra.com/MaclurinSeries.html

The general term is 
(-1)^(n+1) / n * x^n
'''
from math import log
# number_of_terms = 10
# # -1 < x <= 1
# x = 0.24

# f_x = 0
# # term = current value of term, (-1)^(n+1) / n * x^n

# for n in range (1, number_of_terms+1):
#     term = (-1)**(n+1) / n * x**n
#     f_x = f_x + term
#     print('n=', n, 'term=', term, 'f(x)', f_x)
    
# print(log(1+x))

##################### NEW PROGRAM
# Stop summation when a term becomes less than TOL (in absolute value)    

TOL = 1e-6
x = 0.24
f_x = 0

n = 1
term = (-1)**(n+1) / n * x**n
counter = 0

while abs(term) >= TOL:
    f_x = f_x + term
    counter += 1
    print('n=', n, 'term=', term, 'f(x)', f_x)
    n += 1
    term = (-1)**(n+1) / n * x**n

print(counter)
    
    
    
    