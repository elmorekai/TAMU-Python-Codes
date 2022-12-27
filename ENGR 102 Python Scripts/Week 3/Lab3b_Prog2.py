# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 3b Program 2
# Date:         09/11/2020
#

from math import * 
# This programs will take the angle between two line vectors formed from a 
# 3D point of an observer to two other 3D points

'''
input positions of each point
create two vectors from the observer to each of the points
caculate the cosine of the angle between the vectors
output the angle in degrees
create and print output format
'''

print('This programs will take the angle between two line vectors formed from \
a 3D point of an observer to two other 3D points')
print()

# Variables
# inputs for all the positions of x, y, and z for the observer and the two 
# points as strings turned to integers
x0 = int(input('Enter observer x position: '))
y0 = int(input('Enter observer y position: '))   
z0 = int(input('Enter observer z position: '))
x1 = int(input('Enter point 1 x position: '))
y1 = int(input('Enter point 1 y position: '))
z1 = int(input('Enter point 1 z position: '))
x2 = int(input('Enter point 2 x position: '))
y2 = int(input('Enter point 2 y position: '))
z2 = int(input('Enter point 2 z position: '))

# x0 = 1
# y0 = 2
# z0 = 3
# x1 = 4
# y1 = 5
# z1 = 6
# x2 = 9
# y2 = 8
# z2 = 7

# Forumula Variables
# All the variables of the used formulas for ease of coding
vect01x = x1 - x0
vect01y = y1 - y0
vect01z = z1 - z0
vect02x = x2 - x0
vect02y = y2 - y0
vect02z = z2 - z0
magvect01 = sqrt(vect01x ** 2 + vect01y ** 2 + vect01z ** 2)
magvect02 = sqrt(vect02x ** 2 + vect02y ** 2 + vect02z ** 2)
mult12 = (vect01x * vect02x) + (vect01y * vect02y) + (vect01z * vect02z)
angcos = mult12 / (magvect01 * magvect02)
ang = ((acos(angcos)) * (180 / pi))

print(angcos)
# print(magvect01)
# print(magvect02)
# print(mult12)
# print(angcos)

# Output Format
# final print statements
print()
print('Observer location is x =', x0, ',y =', y0, ',z =', z0)
print(' Point 1 location is x =', x1, ',y =', y0, ',z =', z0)
print(' Point 2 location is x =', x2, ',y =', y2, ',z =', z2)
print('The angle between the points is {:.3f} degrees.'.format(ang))




