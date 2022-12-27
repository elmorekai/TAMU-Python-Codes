# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 7b Program 3
# Date:         10/10/2020
#

'''
Part A: finding the median in a list
'''
print('This program will find the median of a given list.')

# Variables
input_str = input('Please enter the list of numbers here (seperated by commas): ')
median = 0

# Loops to turn strings into float
my_list = input_str.split(', ')
for i in range(len(my_list)):  # loop to convert string to float
    my_list[i] = float(my_list[i])
my_list.sort()

# Conditional to find when length is even
if len(my_list) % 2 == 0:
    for i in range(len(my_list)): # loop to find median
        if i == len(my_list) // 2:
            median1 = my_list[i]
        if i == ((len(my_list) // 2) - 1):
            median2 = my_list[i]
    median = (median1 + median2)/2
    print('The median of the list is', median)
else: # conditional for when length is odd
    for i in range(len(my_list)): # loop to find median
        if i == len(my_list) // 2:
            median = my_list[i]
            print('The median of the list is', median)

'''
Part B: making a 'fake sort'
'''
print('This program prints a fake sort of a inputted list.')

# Variables
input_str2 = input('Please enter the list of numbers here (seperated by commas): ')
minimum = None
new_list = []

# Loops to turn strings into float
my_list2 = input_str2.split(', ')
for i in range(len(my_list2)):  # loop to convert string to float
    my_list2[i] = float(my_list2[i])
copy_my_list = my_list2[:]
# Loop to create a new sorted list while deleting the old one
for i in range(len(copy_my_list)):
    for num in my_list2: # loop to set the minimum
        if minimum == None:
            minimum = num
        elif (minimum != None) and (num < minimum):
            minimum = num
    new_list.append(minimum) # add the minimum to the new list
    my_list2.remove(minimum) # remove the minimum from the old list
    minimum = None # reset the minimum for next loop
new_list.reverse() # reversed sorted the new list
print('The fake sort of the given data is', new_list)

# Conditional to find when length is even
if len(new_list) % 2 == 0:
    for i in range(len(new_list)): # loop to find median
        if i == len(new_list) // 2:
            median1 = new_list[i]
        if i == ((len(new_list) // 2) - 1):
            median2 = new_list[i]
    median = (median1 + median2)/2
    print('The median of the list is', median)
else: # conditional for when length is odd
    for i in range(len(new_list)): # loop to find median
        if i == len(new_list) // 2:
            median = new_list[i]
            print('The median of the list is', median)
