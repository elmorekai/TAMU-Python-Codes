# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 7b Program 2
# Date:         10/10/2020
#

from math import*
print('This program lets a user enter two vectors, A and B of arbitary \
dimension, and caluclate each magnitude,the vector addition, the vector \
subtraction, and the dot product')
print()

# Variables
vect_A = input('Please enter vector A (components separated by space): ')      
vect_B = input('Please enter vector B (components separated by space): ')
com_vect_A = vect_A.split() # components of vector A
com_vect_B = vect_B.split() # components of vector B
com_mag_vect_A = 0 # component of vector A magnitude
com_mag_vect_B = 0 # component of vector B magnitude
vect_add = [] # empty list for vector addition
vect_sub_AB = [] # empty list for vector B from A subtraction
vect_sub_BA = [] # empty list for vector A from B subtraction
dot_product = 0 # dot product of vectors


for i in range(len(com_vect_A)):  # loop to convert string to float
    com_vect_A[i] = float(com_vect_A[i])
    com_vect_B[i] = float(com_vect_B[i])
for i in range(len(com_vect_A)): # loop to calculate magnitude of vectors
    com_mag_vect_A += com_vect_A[i]**2
    com_mag_vect_B += com_vect_B[i]**2
mag_vect_A = sqrt(com_mag_vect_A)
mag_vect_B = sqrt(com_mag_vect_B)
print('The magnitude of vector A is', mag_vect_A)
print('The magnitude of vector B is', mag_vect_B)
if len(com_vect_A) == len(com_vect_B): # conditional to check the lengths
    for i in range(len(com_vect_A)): # loop to check sum, difference, and product
        vect_add.append(com_vect_A[i] + com_vect_B[i])
        vect_sub_AB.append(com_vect_A[i] - com_vect_B[i])
        vect_sub_BA.append(com_vect_B[i] - com_vect_A[i])
        dot_product += (com_vect_A[i] * com_vect_B[i])
    print('The vector addition between A and B is', vect_add)
    print('The vector subtraction of B from A is', vect_sub_AB)
    print('The vector subtraction of A from B is', vect_sub_BA)
    print('The dot product between vectors A and B is', dot_product)
elif len(com_vect_A) != len(com_vect_B):
    print('Error: Cannot not calculate sum, difference, and product because \
the amount of vector components do not match.')














