# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 4 Activity 1
# Date:         09/14/2020
#

# We first want to illustrate some examples where floating-point roundoff can 
# cause trouble and see other cases where it turns out not to.

##### Example 1 #####
a = 1/7
print('a = 1/7 =', a)
b = 7 * a
# The value of b, if we have no roundoff, should be 1. Is it?
print('b = 7*a =', b)
# The value of b is 1.0
c = 2*a
d = 5*a
e = c + d
# In this case, the value of e, if we have no roundoff, should be 1. Is it?
print('e = 2*a + 5*a =', e)
# The value of e is not 1 it is 0.99999999999999999
print('b == e evaluates to', b == e)
# The value of e is not equal to the value of b

# Now using tolerance to fix errors of floating-point runoff numbers
# define tolerance
TOL = 1e-10
# check if b and e are equal within specified tolerance
if abs(b-e) < TOL:
    print('b and e are equal within tolerance of {:.0e}'.format(TOL))
else:
    print('b and e are NOT equal within tolerance of {:.0e}'.format(TOL))
print()

##### Example 2 #####
from math import *
dif = 1/sqrt(2) - sin(radians(45))
# In this case, the value of dif, if we have no roundoff, should be 0. Is it?
print('1/sqrt(2) - sin(radians(45)) =', dif)
# dif is not zero it is -1.110e-16
print()

##### Example 3 #####
#from math import *
x = sqrt(1/3)
print(x)
y = x*x*3
# The value of (sqrt(1/3) * sqrt(1/3) * 3) should be 1. Is it?
print('y = x*x*3 =', y) # it does come out as 1
z = x*3*x
# The value of (sqrt(1/3) * 3 * sqrt(1/3)) should be 1. Is it?
print('z = x*3*x =', z) # it does not come out as 1
# This line should output True. Does it?
print('y == z evaluates to', y == z) # it evaluates as false

# Now using tolerance to fix errors of floating-point runoff numbers
# define tolerance
TOL = 1e-10
if abs(y-z) < TOL:
    print('y and z are equal within tolerance of {:.0e}'.format(TOL))
else:
    print('y and z are NOT equal within tolerance of {:.0e}'.format(TOL))
print()
