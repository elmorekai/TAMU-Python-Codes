# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Dr. O.
# Section:      ENGR 102 - 212, 214, 220, 242, 250, 420, 427, 520, 545
# Team:         N/A
# Assignment:   Lab #3 Activity 0
# Date:         September 7, 2020
#

'''
------------------------------------
 Course         | CR  | Study Hours
------------------------------------
 ENGR 102-515   | 2   | 6
 MATH 151-505   | 4   | 7
 CHEM 107-225   | 3   | 5
------------------------------------ 
'''

# This program asks the user to input information for three (3) courses. 
# The program outputs the user information in a tabular form.

'''
Create/print a header
Print divider line
Print column labels
Print divide line
Get input for course #1:
    Input course "ENGR 102"
    Input section "520"
    Input credits "2"
    Input study hours "5"
Print info for course #1
Get input for course #2
    Input course "ENGR 102"
    Input section "520"
    Input credits "2"
    Input study hours "5"
Get input for course #2
...
'''

#Variables
course = '' # string
section = '' # string
credit = '' # string
hours = 0 # integer
course1 = '' # row for course 1
course2 = '' # row for course 2
course3 = '' # row for course 3
my_format = '{:^15s} || {:^3s} || {:^15s}'

# Get input for course #1:
print('Please enter information for course #1: for example '\
      'course name is ENGR 102 '\
          'section 520 '\
              'credit')
course = input('Course name: ')
section = input('Section: ')
credit = input('Credit: ')
course1 = my_format.format(course + '-' + section, credit, str(5))

# course = 'ENGR 102'
# section = '520'
# credit = '2'

# Get input for course #2
print('Please enter information for course #2: ')
course = input('Course name: ')
section = input('Section: ')
credit = input('Credit: ')
course2 = my_format.format(course + '-' + section, credit, str(5))

# course = 'Math 151'
# section = '210'
# credit = '4'

# Print table header
header_line = my_format.format('Course', 'CR', 'Study Hours')
print('-' * len(header_line))
print(my_format.format('Course', 'CR', 'Study Hours'))
print('-' * len(header_line))

# print infor for the courses
print(course1)
print(course2)
