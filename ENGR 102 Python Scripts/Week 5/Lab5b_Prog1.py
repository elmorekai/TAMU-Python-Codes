# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 5b program 1
# Date:         09/25/2020

# This program takes in a positive integerfrom a user, and computes the Collatz 
# sequence, printing out all the numbers in the sequence, followed by a line 
# stating how many iterations it took to reach the value 1.

print('This program takes in a positive integer from a user, and computes the \
Collatz sequence, printing out all the numbers in the sequence, followed \
by a line stating how many iterations it took to reach the value 1.')

# Variable
integer = int(input('Please enter a positie integer here: '))
iterations = 0

# loop for Collatz sequence
if integer > 0:      # conditional to start sequence, only if positive integer
    print('Sequence: ', end = '')
    while integer > 1:           # loop for when the integer is greater than 1
        print('{}, '.format(integer), end = '')
        iterations += 1
        if ((integer % 2) == 0):
            integer = int(integer/2)
        elif ((integer % 2) != 0):
            integer = int((3 * integer) + 1)        
    print(1)                                  # to add the last one 
    print('Number of iterations:', iterations)
else:
    print('Error: invalid input')