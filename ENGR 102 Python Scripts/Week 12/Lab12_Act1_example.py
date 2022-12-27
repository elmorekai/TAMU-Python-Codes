# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 12 Activity 1 Example
# Date:         11/9/2020
#

##################################
### Lab 12 Activity 1 Example ###  
# Part a) Use eval() to evaluate an arbitrary function that the user enters. 
import numpy as np
import matplotlib.pyplot as plt

def F(f_str, x):
    '''This function...
    '''
    return(eval(f_str))

print('This program imports numpy as np.'\
      ' For example, to input f(x) = sin(6x), type np.sin(6*x)')

# user_function = 'x**2 - 1'
user_function = 'np.sin(6*x)'
print('user_function =', user_function)

# Let's plot the curve
x1, x2 = -5, 5   # some interval 
x_values = np.linspace(x1, x2, 200)
y_values = F(user_function, x_values)

plt.plot(x_values, y_values)
plt.title("user_function = '"+ user_function + "'")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()



