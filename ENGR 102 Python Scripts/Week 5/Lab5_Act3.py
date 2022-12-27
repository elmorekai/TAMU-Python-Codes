# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 5 Activity 3
# Date:         09/25/2020
#

# This program prints a tabular map of the seating in a theatre based on an 
# inputted amount of rows and columns. 

print('This program prints a tabular map of the seating in a theatre based on \
an inputted amount of rows and columns. ')

# Variables
Rows = int(input('Please enter an amount of rows between 5 and 15: '))
Columns = int(input('Please enter an amount of columns between 10 and 20: '))
number = 1
letter = 'A'

print()

# Loops
print('Seating Map: ')
while number <= Rows:
    if (Rows > 15) or (Rows < 5): # Invalid input conditionals
        print('Error: invalid input for the amount of Rows')
        break
    if (Columns > 20) or (Columns < 10): # Invalid input conditionals
        print('Error: invalid input for the amount of Columns')
        break
    letter = 'A'
    print('Row {:>2}:'.format(number), end = '') # Formating for rows
    for i in range(Columns + 1):
        print('{:>4}{}'.format(number, letter), end = '')
        letter = chr(ord(letter) + 1)
    print()
    number += 1
