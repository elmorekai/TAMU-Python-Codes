# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 3 Activity 2
# Date:         09/09/2020
#

# This program asks the user to input their last name, first name and birth 
# city. 
# The program outputs the user information in a tabular form.

# Table:
'''
-----------------------------------------
 Last name | first name | Birth city
-----------------------------------------
 Elmore    | Kai        | New Orleans
 Jefferson | Jack       | New York
 Johnson   | Jeff       | Washington DC
 Tyrell    | Micheal    | Houston
-----------------------------------------
'''

# Algorithm 
'''
Create variables
Get input for user #1
	Input Last_name “Elmore”
	Input First_name “Kai”
	Input Birth_city “New Orleans”
Print information for person #1
Get input for user #2
	Input Last_name “Jefferson”
	Input First_name “Thomas”
	Input Birth_city “Philadelphia”  
Print information for person #2
Get input for user #3
Input Last_name “Jackson”
	Input First_name “Jack”
	Input Birth_city “New York” 
Print information for person #3
Get input for user #4
Input Last_name “Thompson”
	Input First_name “Philip”
	Input Birth_city “Washington D.C.” 
Print information for person #4
Create/print the header
Print divider line
Print column labels
Print divide line
'''

# Variables
last_name = '' # string, The first name of the person inputting
first_name = '' # string, the last name of the person inputting
birth_city = '' # string, the birth city of the person inputting
my_format = '{:<16} || {:<16} || {:<16}' # table spacing
header_line = my_format.format('Last name', 'First name', 'Birth city') # header format
user1 = '' # row for user 1
user2 = '' # row for user 2
user3 = '' # row for user 3
user4 = '' # row for user 4

# Get input for user #1
print('Please enter the first name, last name, and birth city for user #1:'\
      'for example last name is Elmore,'\
          'first name is Kai,' \
              'and birth city is New Orleans')
last_name = input('Last name: ')
first_name = input('First name: ')
birth_city = input('Birth city: ')
user1 = my_format.format(last_name, first_name, birth_city)

# Get input for user #2
print('Please enter the first name, last name, and birth city of user #2')
last_name = input('Last name: ')
first_name = input('First name: ')
birth_city = input('Birth city: ')
user2 = my_format.format(last_name, first_name, birth_city)

# Get input for user #3
print('Please enter the first name, last name, and birth city of user #3')
last_name = input('Last name: ')
first_name = input('First name: ')
birth_city = input('Birth city: ')
user3 = my_format.format(last_name, first_name, birth_city)

# Get input for user #4
print('Please enter the first name, last name, and birth city of user #4')
last_name = input('Last name: ')
first_name = input('First name: ')
birth_city = input('Birth city: ')
user4 = my_format.format(last_name, first_name, birth_city)

# Print output table
print('-' * len(header_line))
print(my_format.format('Last name', 'First name', 'Birth city'))
print('-' * len(header_line))

# Print information for the users
print(user1)
print(user2)
print(user3)
print(user4)









