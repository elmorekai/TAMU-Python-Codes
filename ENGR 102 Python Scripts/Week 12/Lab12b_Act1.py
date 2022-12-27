# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jaden Thomas Reyes, Nikhita Sathish, Halimat Ettu, Kai Elmore
# Section:      545
# Team:         25
# Assignment:   LAB 12b Activity 1
# Date:         14 November 2020


import matplotlib.pyplot as plt
import numpy as np

print('This program will graph a polynomial, and its first and second '
      'derivatives given a set of coefficients from the user')


# CREATE FUNCTIONS
def find_poly (coefficients):
    '''This function will find the f(x) equation of the given coefficients
       Input parameters: list of coefficients given from user
       Returns: equation of f(x), list of powers, and float list of coefficients'''
       
    power = len(coefficients) - 1
    equation = ''
    list_power = []
    
    # for loop to find the equation - concatenate string 
    for i in range (len(coefficients)):
        
        # keep track of the list of powers
        list_power.append(power)
        
        if (coefficients[i] == '0'):
            equation += ''
            
        elif (power == 1) and (coefficients[i] != '0'):
            equation +='({})x + '.format(coefficients[i])
            
        elif (power == 0) and (coefficients[i] != '0'):
            equation +='({})'.format(coefficients[i])
            
        elif (coefficients[i] != '0'):    
            equation += '({})x^{} + '.format(coefficients[i], power)
            
        power -= 1
        
    
    # convert the list of string coefficients into a list of floats
    float_list = []
    for i in range (len(coefficients)):
        float_list.append(float(coefficients[i]))
    
    
    # return equation
    return equation, list_power, float_list



def first_deriv (coefficients):
    '''This function will find the f'(x) equation of the given coefficients
       Input parameters: list of coefficients given from user
       Returns: float list of the coefficients of the derivative, list of powers '''
       
    # create local variables to keep track of new coeffcients and new powers
    power = len(coefficients) - 1
    deriv_power = []
    deriv_coefficients = []
    
    # add new terms and powers to their respective lists
    for i in range (len(coefficients)):
        term = coefficients[i] * power
        deriv_coefficients.append(term)
        power -= 1
        deriv_power.append(power)
    
    # remove the last numbers in the lists - deriv of constant is 0
    deriv_coefficients.pop(-1)
    deriv_power.pop(-1)
    
    return deriv_coefficients, deriv_power



def second_deriv (coefficients):
    '''This function will find the coefficients of the f"(x) equation from the given coefficients
       Input parameters: first derivative coefficients and powers
       Returns second derivative coefficients and powers'''
       
    # create local variables to keep track of new coeffcients and new powers
    power = len(coefficients) - 1
    second_deriv_coefficients = []
    second_deriv_power = []
    
    # add new terms and powers to their respective lists
    for i in range (len(coefficients)):
        term = coefficients[i] * power
        second_deriv_coefficients.append(term)
        power -= 1
        second_deriv_power.append(power)
    
    # remove the last numbers in the lists - deriv of constant is 0
    second_deriv_coefficients.pop(-1)
    second_deriv_power.pop(-1)
    
    return second_deriv_coefficients, second_deriv_power
    
    
    
    
    
# MAIN CODE

# ask user for coefficient input and convert to a list
numbers = input('Please enter the coeffcients separated by a comma: ')
coefficient = numbers.split(',')

list_coefficient = []
for num in coefficient:
    list_coefficient.append(num)
    
    
# ask user for x range and number of points to plot
x1 = int(input('Please enter the starting x value for the graph: '))
x2 = int(input('Please enter the ending x value for the graph: '))
num_points = int(input('Please enter the number of points to plot: '))

 

# call function that finds the equation of f(x), and plot the graph
f_x, power, poly_coefficients = find_poly(list_coefficient)

x = np.linspace(x1, x2, num_points)
y = 0


# calculate the y for the graph
for i in range (len(poly_coefficients)):
    if (power[i] == 0):
        y += poly_coefficients[i]
        
    else:
        y += poly_coefficients[i] * x ** power[i]
        

# plot the f(x) function
plt.title('f(x) = {}'.format(f_x))
plt.plot(x,y, '-b', label = 'f(x)')



# check how many coefficients are inputted, ouput varies based on degree of polynomial
# 1st degree polynomial
if (len(list_coefficient) == 2):
    deriv_co, deriv_power = first_deriv(poly_coefficients)

    y1 = list_coefficient[0]
    plt.axhline(y=y1, color = 'r', label = "f'(x)")       


# 2nd degree polynomial
elif (len(list_coefficient) == 3):
    
    # call function that finds the coefficients of f'(x), and plot the graph
    deriv_co, deriv_power = first_deriv(poly_coefficients)

    y1 = 0
    for i in range (len(deriv_co)):
        if (deriv_power[i] == 0):
            y1 += deriv_co[i]
        else:
            y1 += deriv_co[i] * x ** deriv_power[i]
        
    plt.plot(x, y1, '-r', label = "f'(x)")
        
    # call function that find the coefficients of f"(x), plot straight line
    second_co, second_power = second_deriv(deriv_co)

    y2 = second_co[0]
    plt.axhline(y = y2, color = 'g', label = 'f"(x)') 
    
    
else:
# call function that finds the coefficients of f'(x), and plot the graph
    deriv_co, deriv_power = first_deriv(poly_coefficients)

    y1 = 0
    for i in range (len(deriv_co)):
        if (deriv_power[i] == 0):
            y1 += deriv_co[i]
        else:
            y1 += deriv_co[i] * x ** deriv_power[i]
        
    plt.plot(x, y1, '-r', label = "f'(x)")



    # call function that finds the coefficients and power of f"(x), and plot the graph
    second_co, second_power = second_deriv(deriv_co)

    y2 = 0
    for i in range (len(second_co)):
        if (second_power[i] == 0):
            y2 += second_co[i]
        else:
            y2 += second_co[i] * x ** second_power[i]
            
    plt.plot(x, y2, '-g', label = 'f"(x)')



# plot the legend and the ylimit of the graph
plt.ylim(-50,50)
plt.legend(loc = 'lower left')