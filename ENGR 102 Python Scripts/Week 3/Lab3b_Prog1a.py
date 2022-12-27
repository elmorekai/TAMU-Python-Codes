# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 3b program 1a
# Date:         09/11/2020
#

# Using Ohm's Law
# Calculate the voltage across a conductor from a given amount of 
# resistance in ohms and current in A, where A represents amperes.
# I = V/R ==> V = IR

print("This program calculates the voltage across a conductor from a given \
      amount of resistance in ohms and current in A, where A represents \
          amperes using Ohm's Law. ") # description of program

print('Please only type in numbers and not letters, for example 20 is a good \
      input.') # instructions on how to input values

resistance = float(input('Enter resistance (ohms) here: ')) 
# input of resistance in string then turned to a float in ohms

current = float(input('Enter current (A) here: ')) 
# input of current in string then turned to a float in amperes

volts = resistance * current 
# Using ohm's law to assign the value of volts in volts

print()
print("Voltage =", volts, "V") # printing of answer




