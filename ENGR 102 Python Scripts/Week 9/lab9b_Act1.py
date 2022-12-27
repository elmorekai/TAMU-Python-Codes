# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 9b Activity 1
# Date:         10/23/2020
#

print('This program will replace the temperature data in celsius of a file to \
      a file with all the data in fahrenheit.')
      
# Setting empty list for fahrenheit data
Faren_data = []

# Opening Celsius and Fahrenheit files to read and write respectively
Cel_file = open('Celsius.dat', 'r+')
Faren_file = open('Fahrenheit.dat', 'w')

# Reading the temperature data from the Celsius file
temp_data = Cel_file.readlines()

# Loop to convert from Celsius to Fahrenheit
for temp in temp_data:
    int_temp = int(temp)
    Faren = (int_temp * (9/5)) + 32
    str_faren = str(Faren)
    Faren_data.append(str_faren)

# Joining the list of fahrenheit data into a single string
str_Faren_data = '\n'.join(Faren_data)

# Writing the fahrenheit data into the new file
Faren_file.write(str_Faren_data)

# Closing both files
Cel_file.close()
Faren_file.close()

