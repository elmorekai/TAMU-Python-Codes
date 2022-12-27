# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 12 Activity 1
# Date:         11/14/2020
#
import numpy as np
import matplotlib.pyplot as plt

def F(str_f, x):
    '''this function evaluates a given x in an abritary function'''
    return eval(str_f)

def deriv(x):
    '''This function approximates the derivative of an inputted x value'''
    a = 1e-10
    fun_xa = str(F(function, x + a))
    fun_x = str(F(function, x))
    approx = eval('(' + fun_xa + '-' + fun_x +')' + '/' + 'a')
    return approx

def newton_step(x_i):
    '''This function calculates an guess of a root of a polynomial using newton\
        method on an original guess'''
    new_x_i = x_i - (F(function,x_i))/(deriv(x_i))
    return new_x_i

def newton(x_0):
    '''This function calculates a list of guesses for a root of a polynomial \
        using newton method on an original guess'''
    guess_list = []
    TOL1 = 1e-6
    TOL2 = 1e-8
    difference = 1
    ab_val = 1
    while difference >= TOL1 and ab_val >= TOL2:
        new_x = newton_step(x_0)
        guess_list.append(new_x)
        difference = x_0 - new_x
        ab_val = abs(F(function,new_x))
        x_0 = new_x
    return guess_list

print('This program asks a user for a function, an initial guess of a root, \
x0 and prints the set of root approximations that Newton’s method computes from \
that initial guess.')

function = input('Please enter a polynomial function in python syntax form here: ')

x_guess = float(input('Please enter the initial guess here: '))

guesses = newton(x_guess)

print('Guess list:')
print('-' * 20)
for i in range(len(guesses)):
    print(guesses[i])


