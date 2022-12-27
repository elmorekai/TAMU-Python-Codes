# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 2b Program 3 (e.g. Lab 1b-2)
# Date:         09/03/2020
#

# You are to create a program consisting of only the following lines of code. 
# You may put these lines of code in any order, and can re-use the lines as
# frequently as you wish to. There will be more than one way to achieve the 
# result – try to see if you can obtain the output using fewer lines of code.
# Note: you can only print z to the screen, so you have to
# build the value of z that you want using the other statements, then print z.

# Write code consisting of only these lines to print z as 1, 3, 11, 28
# 123, 10^32, and 4321

# Usable lines of code
x = 1
y = 10
z = 0
x = y
x += 1
y += x
y *= x
z += x
z += y

# Code usded to print z as 1
x = 1
z = 0
z += x
print(z)

# Code usded to print z as 3
x = 1
z = 0
x += 1
x += 1
z += x
print(z)

# Code usded to print z as 11
x = 1
y = 10
z = 0
y += x
z += y
print(z)

# Code usded to print z as 28
x = 1
y = 10
z = 0
x += 1
y += x
y *= x
x += 1
x += 1
z += x
z += y
print(z)

# Code usded to print z as 123
x = 1
y = 10 
z = 0
x += 1
x += 1
z += x
x = y 
y *= x
y += x
z += x
z += y
print(z)

# Code usded to print z as 10^32
x = 1
y = 10
z = 0
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
z += y
print(z)

# Code usded to print z as 4321
x = 1
y = 10
z = 0
z += x
x = y
y += x
z += y
y = 10
y *= x
x = 1
x += 1
x += 1
y *= x
z += y
y = 10
x = y
y *= x
y *= x
x = 1
x += 1
x += 1
x += 1
y *= x
z += y
print(z)

