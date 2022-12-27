# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lecture 11
# Date:         11/2/2020
#

'''
# Approxiamte the f(x) = ln(1+x) for -1 < x <= 1 using the Maclaurin series expanison
# https://mathworld.wolfra.com/MaclurinSeries.html

The general term is 
(-1)^(n+1) / n * x^n
'''


def ln_1_plus_x(x,tol=1e-6):
    '''This funcition will approximate the f(x) = ln(1+x) for -1 < x <= 1 using the Maclaurin series expanison
    Input parameters: x -....,tol -...
    Teturns: ln(1+x)'''
    # print(tol)
    f_x = 0

    n = 1
    term = (-1)**(n+1) / n * x**n
    counter = 0
    
    # Stop summation when a term becomes less than TOL (in absolute value)
    while abs(term) >= tol:
        f_x = f_x + term
        counter += 1
        # print('n=', n, 'term=', term, 'f(x)', f_x)
        n += 1
        term = (-1)**(n+1) / n * x**n

    # print(counter)
    
    return f_x, counter

# Main code
# Get input from user
TOLERANCE = 1e-10
x_value = 0.24

# Calculate ln(1+x)
ln1x, num_of_terms = ln_1_plus_x(x_value, TOLERANCE)
print(ln1x, num_of_terms)
    
ln1x, num_of_terms = ln_1_plus_x(x_value)
print(ln1x, num_of_terms)

print('ln(1+{}) = {}'.format(x_value, ln1x))





