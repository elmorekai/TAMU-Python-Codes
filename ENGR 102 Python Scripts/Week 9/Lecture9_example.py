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

###################### Writing data to a file ##################

################################################################
########################## Example 1  ##########################
print('----------- Example 1 -----------')
# Ask the user to input a name for a file to be written to
# For example, the user enters 'gradebook'
user_file_name = 'gradebook'

# Open file for writing (.txt and .csv)
# Need to add proper file exention unless we asked the user to include it in the file name
fid_text = open(user_file_name + '.txt', 'w')
fid_csv = open(user_file_name + '.csv', 'w')

# Write to text file
fid_text.write('Hello! How are you doing? 1 2 3\n')
fid_text.write('Howdy! How are you? 4 5 6\n')

# Write to csv file
fid_csv.write('Hello!,How are you doing?,1,2,3\n')
fid_csv.write('Howdy!,How are you?,4,5,6\n')

# Close file
fid_text.close()
fid_csv.close()

# Print to Console
print('Hello! How are you doing? 1 2 3')
print('Howdy! How are you? 4 5 6')
print()


################################################################
########################## Example 2  ##########################
print('----------- Example 2 -----------')
# Print a table to Console
# Ask the user to input the column labels separated by comma and space
# For example, the user enters 'Greeting, Question, Value 1, Value 2, Value 3'
header_row = 'Greeting, Question, Value 1, Value 2, Value 3'
header_row = header_row.split(', ')   # convert to a list of strings
print(header_row)                     # print the list
print()

# Let's print a table that contains five (5) columns
# May need to work on the format (that is, add format codes, etc.)
my_format = '{:10} | {:20} | {:>8} | {:>8} | {:>8}'

# Print header row
print(my_format.format(header_row[0], header_row[1], header_row[2], \
                        header_row[3], header_row[4]) )

user_line = 'Hello!, How are you doing?, 1, 2, 3'
user_line = user_line.split(', ')   # convert to a list of strings
print(my_format.format(user_line[0], user_line[1], user_line[2], \
                        user_line[3], user_line[4]) )

user_line = 'Howdy!, How are you?, 4, 5, 6'
user_line = user_line.split(', ')

# Print greeting and question in columns ##1-2
print('{:10} | {:20}'.format(user_line[0], user_line[1]), end='')

# Print values in columns ##3-5
for val in user_line[2:] : 
    print(' | {:>8}'.format(val), end='')
print()
print()

################################################################
########################## Example 3  ##########################
print('----------- Example 3 -----------')
# Now let's write the same table to a file
# Open a file for writing
fid = open('gradbook.out', 'w')

# Need to use the write() function
# Copy/paste code from Example 2, make necessary changes

header_row = 'Greeting, Question, Value 1, Value 2, Value 3'
header_row = header_row.split(', ')   # convert to a list of strings
# fid.write(header_row)                     # print the list
fid.write('\n')

# Let's print a table that contains five (5) columns
# May need to work on the format (that is, add format codes, etc.)
my_format = '{:10} | {:20} | {:>8} | {:>8} | {:>8}'

# Print header row
fid.write(my_format.format(header_row[0], header_row[1], header_row[2], \
                        header_row[3], header_row[4]) + '\n')

user_line = 'Hello!, How are you doing?, 1, 2, 3'
user_line = user_line.split(', ')   # convert to a list of strings
fid.write(my_format.format(user_line[0], user_line[1], user_line[2], \
                        user_line[3], user_line[4]) + '\n' )

user_line = 'Howdy!, How are you?, 4, 5, 6'
user_line = user_line.split(', ')

# Print greeting and question in columns ##1-2
fid.write('{:10} | {:20}'.format(user_line[0], user_line[1]))

# Print values in columns ##3-5
for val in user_line[2:] : 
    fid.write(' | {:>8}'.format(val))
# fid.write('\n')
# fid.write('\n')


fid.close()







