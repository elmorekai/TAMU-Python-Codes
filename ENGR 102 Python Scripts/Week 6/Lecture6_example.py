# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Dr. O.
# Section:      ENGR 102-...
# Team:         N/A
# Assignment:   Lab ___________
# Date:         _______________
#
'''
# ##########################################################################
# # Review zyBook Chapter 3.3 and 3.8.

# # Ask the user to input a string that represents a four-bit binary number.
# # Check if the string represents a binary number. If valid, convert to 
# # decimal (base 10). Print results (error or decimal number).
# # Descriptive input/output and comments are required. 
# ##########################################################################
'''

'''
# --------------------------------------------------------------------------
# Examples: '1001', '1110', '0001', '0101', etc.
# --------------------------------------------------------------------------
# Variables
#  - a string to store a binary number (user input)
#  - an integer to store the number in base 10
#  - may need a Boolean to check if input is valid
# -------------------------------------------------------------------------- 
# Algorithm

# Get user input:
#     Give instructions
#     Input a binary number as a string
# Check input
#     Check the length of the string
#     Check every character of the string: should be '0' or '1'
# If invalid input, print an error message and end the program
# Otherwise, convert the string to a decimal number
#     Go through the string (from left to right) one character at a time
#     Convert character to integer (0 or 1)
#     Multiply the first (from left) integer value by  2^3
#     Multiply the second integer value by 2^2
#     Multiply the third integer value by  2^1
#     Multiply the fourth integer value by 2^0
#     The decimal representation of the number is the sum of these four values
#     Print the results
# --------------------------------------------------------------------------
# Variables names:
#  - num2 - string, represents binary number
#  - num10 - integer, binary number converted to base 10
#  - is_binary - Boolean, True is valid input (may or may not use)
# --------------------------------------------------------------------------
# Tests
# Examples: '100001', '1110', '0d001', '101', etc.
#  - '100001' - error: a four-bit binary number is expected
#  - '1110' is 14
#  - Etc.
# --------------------------------------------------------------------------
'''

# # Get user input:
# print('This program...')
# #num2 = input('Please enter a four-bit binary number')
# num2 = '10d1'

# # Check input
# #     Check the length of the string
# #     Check every character of the string: should be '0' or '1'
# if (len(num2) == 4) and \
#     (num2[0] == '0' or num2[0] == '1') and \
#     (num2[1] == '0' or num2[1] == '1') and \
#     (num2[2] == '0' or num2[2] == '1') and \
#     (num2[3] == '0' or num2[3] == '1'):
#         # Valid input; convert the string to a decimal number
#         num10 = 0
#         num10 += int(num2[0]) * 2**3
#         num10 += int(num2[1]) * 2**3
#         num10 += int(num2[2]) * 2**3
#         num10 += int(num2[3]) * 2**3
        
#         print('The binary number {} is {} in base 10'.format(num2, num10))
# else:
#     print('Error: a four-bit binary number is expected.')

#################################################################################33
# Binary to base 10 with loops

print('This program...')
#num2 = input('Please enter a four-bit binary number')
num2 = '1011'
num10 = 0
is_valid_input = True

# Check input: length should be 4
if (len(num2) == 4):
    print('length correct')
    # Check the characters: '0' or '1'
    for character in num2:
        print('character', character)
        if not(character == '0' or character == '1'):
            is_valid_input = False
            print('Error: wrong character found')
            break
    print(is_valid_input)
    
    # Calculate number in base 10
    if is_valid_input:
        exponent = len(num2) - 1
        print(exponent)
        
        for character in num2:
            num10 += int(character) * 2**exponent
            print(num10)
            exponent -= 1
            
        print('The binary number {} is {} in base 10'.format(num2, num10))
else:
    print('Error: wrong length of the inputted string. A four-bit binary number is expected')



















