# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 5 Activity 1
# Date:         09/21/2020
#

# This program evaluates the limit of h(x) = (1 + (1/x))^x as x approaches 
# infinity. It does this by inputing x values from 1.0 to 1e7, with each 
# successive x being 10 times greater

print('This program evaluates the limit of h(x) = (1 + (1/x))^x as x \
approaches infinity. It does this by inputing x values from 1.0 to 1e7, \
with each successive x being 10 times greater.')

# Variables
x = 1 
h_x = (1 + (1 / x)) ** x

# Loop for limit
while x <= 1e7:
    h_x = (1 + (1/x))**x
    print('for x = {:>10}   h(x) = {:<10.4f}'.format(x, h_x))
    x *= 10
    

