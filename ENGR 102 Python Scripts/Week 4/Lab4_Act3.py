# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 4b Activity 3
# Date:         09/18/2020
#

# This program gives an output of true or false based on the give inputs
print('This program gives an output of true or false based on the give inputs')
print("Please enter 'T' for true and 'F' for false")

#### Part A ####

a = input('Please enter True or False for a: ') #code for a, b, and c as 
b = input('Please enter True or False for b: ') #boolean values
c = input('Please enter True or False for c: ')
if a == 'T':
    a = True
else:
    a = False
if b == 'T':
    b = True
else:
    b = False
if c == 'T':
    c = True
else:
    c = False

#### Part B ####
Part_B_1 = (a == True) and (b == True) and (c == True) # boolean expressions
Part_B_2 = (a == True) or (b == True) or (c == True)   # Part b

print('Part B 1', Part_B_1)
print('Part B 2', Part_B_2)

#### Part C ####
Part_C_1 = a != b # boolean expressions for part c
Part_C_2 = (a + b + c) == 1 or (a + b + c) == 3
print('Part C 1', Part_C_1)
print('Part C 2', Part_C_2)