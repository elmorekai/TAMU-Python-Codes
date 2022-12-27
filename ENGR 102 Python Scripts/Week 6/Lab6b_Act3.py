# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 6b Activity 3
# Date:         10/02/2020
#

# This program will ask the user to input an integer N such that N is between 
# 2 and 100, inclusive. For all numbers from 2 to N, it will print a series of 
# lines indicating which numbers are divisors of other numbers. 
# Also, for each number it will print the number of divisors or ‘prime’. 
# Calculate the number of prime numbers between 2 and N. 

# print what the program does
print('This program will ask the user to input an integer N such that N is \
between 2 and 100, inclusive. For all numbers from 2 to N, it will print \
a series of lines indicating which numbers are divisors of other \
numbers. Also, for each number it will print the number of \
divisors or ‘prime’. Calculate the number of prime numbers \
between 2 and N. ')
print()

# Table: 
'''
----------------------------------------------------------------
Number   Divisors                         Number of Divisors
2        2                                prime
3        3                                prime
…
17       17                               prime
18       2 3 6 9 18                       5
…
99       3 9 11 33 99                     5
100      2 4 5 10 20 25 50 100            8
----------------------------------------------------------------
'''

# Variables
n = input("Please enter a 'n' between 2 and 100 here: ") # input value for n
low_lim = 2 # lower limit
up_lim = n # upper limit
header_format = '{:<6}   {:<30}   {:<20}' # header format
header = header_format.format('Number', 'Divisors', 'Number of Divisors') 
num_of_divisors = 0  # number of divisors
num_of_prime = 0 # number of prime numbers
divisor_length = 0 # string length of divisor


# Conditional check if n is a valid input
if n.isdigit() == True:
    n = int(n) 
    if 2 <= n <= 100:
        # Print the lower, upper limits, line seperator, and header
        print()
        print('The lower limit is', low_lim)
        print('The Upper limit is', up_lim)
        print('-' * len(header))
        print(header)
        # Loop from 2 to inputted n
        for i in range(2, n + 1):
            print('{:<6}   '.format(i),end = '') # print for number 'i' 
            for j in range(2,101): # loop to find the divisors
                if (i % j) == 0:   # conditional to find divisors
                    print('{} '.format(j),end = '') # print for divisors
                    num_of_divisors += 1 # divisor counter
                    divisor_length += len(str(j)) + 1
            if num_of_divisors > 1: # conditional to print amount of divisors
                print('{}{:<}'.format(' '*(33 - divisor_length), num_of_divisors))
            else: # else statement to print the amount of prime numbers
                print('{}{:<}'.format(' '*(33 - divisor_length), 'prime'))
                num_of_prime += 1 # prime number counter
            num_of_divisors = 0 # resetting counted divisors to zero
            divisor_length = 0
        print('-' * len(header)) #printing seperation line
        print('There are', num_of_prime,'prime numbers from', low_lim,'and', up_lim)
    else:
        print('Error: n value is out of range of program.')
else:
    print('Error: input for n is not an integer.')











