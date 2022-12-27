# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 3b program 1d
# Date:         09/11/2020
#

# Using Arqs equation
# This program finds the production of a oil and gas well after a given time 
# in days, if it had a given initial production rate in barrels/day, a given 
# initial decline rate of in barrels/day, and a given hyperbolic constant.
print('This program finds the production of a oil and gas well after a given \
time in days, if it had a given initial production rate in barrels/day, a \
given initial decline rate of in barrels/day, and a given hyperbolic constant.')
# program description 

print('Please only type in numbers and not letters, for example 20 is a good \
input.') # instructions on how to input values)

time = float(input('Please input time (days) here: '))
# input of time as a string turned into a float in days

intial_rate = float(input('Please input the intial rate (barrels/day) here: '))
# input of the intial rate as a string turned into a float in barrels/day

declined_rate = float(input('Please input the declined rate (barrels/day) here: '))
# input of the declined rate as a string turned into a float in barrels/day

hyperbolic_constant = float(input('Input the hyperbolic constant (barrels/day) \
here: ')) # input of the hyperbolic constant as a string turned into a float in 
# barrels/day

total_production = intial_rate / (1 + hyperbolic_constant * declined_rate * time) ** (1 / hyperbolic_constant)
# assigning the total production using the Arqs equation in barrels/day
print()

print("The production of the oil and gas well =", total_production, "\
barrels/day")

