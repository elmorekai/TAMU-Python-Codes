# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lecture 7 code
# Date:         10/5/2020
#

special_characters = '123ABC -!'
DIGITS = '0123456789'

user_string = 'Welcome to ENGR-102!' # change to user input
my_string = '' # a modified copy of the user_string: remove all digits
counter = 0 # count how many times the special characters occur in the user_string

digit_counter = 0 # how many times a digit is found in user_string

for character in user_string:
    if character in DIGITS:
        digit_counter += 1
    else:
        my_string += character
    if character.upper() in special_characters:
        counter += 1

print(digit_counter)
print(counter)
print(my_string)

first_digit_index = None
# Find indices for digits
for i in range(len(user_string)):
    if user_string[i] in DIGITS:
        print(i)
        first_digit_index = i
        break

print(first_digit_index)
