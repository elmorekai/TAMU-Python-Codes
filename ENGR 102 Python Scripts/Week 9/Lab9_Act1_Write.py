# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 9 Activity 1
# Date:         10/19/2020
#

# This program will read in data from the keyboard and store it in a file
print('This program will read in data from the keyboard and store it in a file')
print()
#file_name = input('Please enter the name of the file to store the data: ')
file_name = 'user_file_name'

# file_txt = open(file_name + '.txt', 'w')
# file_csv = open(file_name + '.csv', 'w')

print('Please make a header line for table that sets each column to an \
assignment seperated by a comma and space like: Name, hw1, hw2, midterm, final')

# header = int('Please enter header here: ')
header = 'Name, hw1, hw2, midterm, final'
header_row = header.split(', ')
print(header_row)
print()

my_format = '{:<10} {:>10} {:>10} {:>10} {:>10}'
print(my_format.format(header_row[0], header_row[1], header_row[2], \
                        header_row[3], header_row[4]))