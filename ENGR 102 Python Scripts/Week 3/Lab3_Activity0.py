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

from math import pi

# Output a string with special characters: using Unicode (zyBook Ch. 3.13)
# Using the string format() method and the chr() function
# format(): using Inferred positional replacement (zyBook Ch. 3.9)
print('1) \u263A')   
print('2) 270\u00B0')  # \uZeroZeroBZero, not letter 'O'
print('3) 180{:s}'.format('\u00b0'))  
print('4) 90' + chr(176))
print('5) 45{:s}'.format(chr(176)))

# Creating a string variable before printing
my_string = '6) 2\u03c0 rad = 360\u00b0'
print(my_string)
my_string = '7) 2{:s} rad = 360{:s}'.format('\u03c0', '\u00b0')
print(my_string)

# Print a divider
print('\n', '\u263A' * 50, '\n', sep = "")

# Creating a formatted output for different data types
# See zyBook Ch. 3.11 Advanced string formatting
my_int = 5
my_float = 3.678
my_str = 'abc'
print('my_int = {}, my_float = {}, my_str = {}'.format(my_int, my_float, my_str))
print('my_int = {:<10d}, my_float = {:<10f}, my_str = {:<10s}'.format(my_int, my_float, my_str))
print('my_int = {:10d}, my_float = {:10.2f}, my_str = "{:10s}"'.format(my_int, my_float, my_str))

# Print a divider
print('\n', '*' * 50, '\n', sep = "")

print('\u03c0 = {}'.format(pi))
print('\u03c0 = {:f}'.format(pi))
print('\u03c0 = {:.6}'.format(pi))
print('\u03c0 = {:12.6}'.format(pi))

# Print a divider
print('\n', '-' * 50, '\n', sep = "")

# Output a 2D vector in a component form
ax = 2.3      # x component of vector a
ay = -1.3     # y component of vector a
print('Vector a = \u2329{}, {}\u232A'.format(ax, ay))
print('Vector a = \u2329{:f}, {:f}\u232A'.format(ax, ay))
print('Vector a = \u2329{:.1f}, {:.1f}\u232A'.format(ax, ay))

