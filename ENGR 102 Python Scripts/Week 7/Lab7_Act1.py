# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 7 Activity 1
# Date:         10/5/2020
#

'''
# Part 1: Iterating through a list
'''
# # This program finds and prints the minimum odd number in a given list. 
# print('This program finds and prints the minimum odd number in a given list.')

# # User inputs string w/ numbers: '203 12 5 800 -10'
# user_input = input('Enter numbers: ')
# tokens = user_input.split() # Split into separate strings
# print(tokens) # Print the list of strings returned by the split() method

# # Convert strings to integers
# nums = [] # Create an empty list named nums to store the integers
# for token in tokens:
#  nums.append(int(token)) # Assuming that the user enters only integers

# # Print each position and number
# print() # Print a single newline
# for index in range(len(nums)):
#  value = nums[index]
#  print('{}: {}'.format(index, value))

# # Determine maximum even number
# min_num = None
# for num in nums:
#  if (min_num == None) and (num % 2 == 1):
#      # First even number found
#      min_num = num
#  elif (min_num != None) and (num < min_num ) and (num % 2 == 1):
#      # Larger even number found
#      min_num = num
# print('Min even #:', min_num)

'''
# Part 2: Printing a list
'''
# This program takes in a string of numbers and turns them into a list with a
# $ in front of each entry. 

print('This program takes in a string of numbers and turns them into a list \
with a $ in front of each entry. ')

user_input_stock = input('Enter numbers here: ')
stock_prices = user_input_stock.split()

for i in range(len(stock_prices)):
    stock_prices[i] = float(stock_prices[i])

for price in stock_prices:
    print('$ {:8.2f}'.format(price))

'''
# Part 3
'''
# # This program will print a list of temperatures seperated by an inputted from the keyboard.
# print('This program will print a list of temperatures seperated by an inputted from the keyboard.')
# print('Examples of two-character separtors: ->, <>, =>, etc.  ')
# my_temp_list = [75, 76]

# input_seperator = input('Enter a two-character sting to use as a seprator during printing: ')
# print()
# for temp in my_temp_list:
#     if temp is not my_temp_list[-1]:
#         print('{} {}'.format(temp, input_seperator),end= ' ')
#     else:
#         print('{} '.format(temp))
# print()





