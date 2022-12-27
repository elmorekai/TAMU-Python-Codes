# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 6b Activity 2
# Date:         10/02/2020
#

# This program gives the corresponding stress from an inputted strain between 
# 0 and 0.26
# Print what the program does.
print('This program gives the corresponding stress from an inputted strain \
between 0 and 0.26')

# Set Variables
# Set up the input and float value of strain
# Set stress to 0
strain = float(input('Please enter a strain between 0 and 0.26 here: '))
stress = 0

# If the inputted strain falls between 0 and 0.01 (inclusive):
    # Multiply the strain by (44/0.01)
    # Set the stress to the outputted value
if 0 <= strain <= 0.01:
    stress = (44 / 0.01) * strain

# Else if the inputted strain falls between 0.01 and 0.06 (inclusive):
    # Set the stress to 44
elif 0.01 <= strain <= 0.06:
    stress = 44
    
# Else if the inputted strain falls between 0.06 and 0.18 (inclusive):
    # Subtract 0.06 from the strain
    # Multiply the difference by (16/0.12)
    # Add 44 to the product
    # Set stress to the final sum
elif 0.06 <= strain <= 0.18:
    stress = ((16 / 0.12) * (strain - 0.06)) + 44
    
# Else if the inputted strain falls between 0.18 and 0.26 (inclusive):
    # Subtract 0.18 from the strain
    # Multiply the difference by (-10/0.08)
    # Add 60 to the product
    # Set stress to the final sum
elif 0.18 <= strain <= 0.26:
    stress = ((-10 / 0.08) * (strain - 0.18)) + 60 

# If the inputted strain is outside 0 and 0.26:
    # Output an error message stating the inputted stress is out of the domain 
    # of the program
else:
    print('Error: the inputted strain is out of the range of the program.')

# Print final stress in units of ksi
print('The stress corresponding to the given strain is ', stress,'ksi.')


