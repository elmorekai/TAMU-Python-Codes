# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 10 activity 0
# Date:         10/29/2020
#

import numpy as np

'''
The basics: an example
'''
print('The basics: an example')
a = np.arange(10).reshape(2,5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.size)
print(type(a))

b = np.array([8, 10, 12])
print(b)
print(type(b))

'''
The Basics: Array creation
'''
print('The Basics: Array creation')
print('')
a = np.array([5,7,9])
print(a)
print(a.dtype)

b = np.array([2.2, 4.5, 10.7])
print(b.dtype)

# a = np.array(1,2,3,4) # wrong
a = np.array([-1,20,9,4]) # right
print(a)
b = np.array([(3.4,2,8), (4,34,6)])
print(b)
c = np.array( [ [4,3], [6,7] ], dtype=complex )
print(c)
d = np.zeros((2, 2))
print(d)
e = np.ones((2,2,6), dtype = np.int16)
print(e)
f = np.empty((3,3))
print(f)
g = np.arange(5, 20, 5)
print(g)
h = np.arange(3, 7, 1)
print(h)
from numpy import pi
i = np.linspace(0, 1, 12)
print(i)
x = np.linspace(0, 2*pi, 100)
f = np.sin(x)

'''
The basics: Printing Arrays
'''
print('The basics: Printing Arrays')
print()
a = np.arange(7) # 1d array
print(a)
b = np.arange(10).reshape(2,5) # 2d array
print(b)
c = np.arange(20).reshape(2,2,5) # 3d array
print(c)
print(np.arange(30000))
print(np.arange(30000).reshape(300,100))

'''
The basics: Basic Operations
'''
print()
a = np.array( [12,32,42,52,62] )
b = np.arange( 5 )
print(b)
c = a-b
print(c)
print(b**2)
print(10*np.sin(a))
print(a<35)

A = np.array( [[1,2], [0,6]] )
B = np.array( [[2,1], [5,4]] ) 
print(A*B) # elementwise product
print(A@B) # matrix product
print(A.dot(B)) # another matrix product

rg = np.random.default_rng(1) # creates instance of default random number generator
a = np.ones((3,4), dtype = int)
b = rg.random((3,4))
a *= 4
print(a)
b += a
print(b)
#a += b # b is not automatically converted to integer type so a type error occurs

a = np.ones(3, dtype = np.int32)
b = np.linspace(0,pi,3)
print(b.dtype.name)
c = a+b
print(c)
print(c.dtype.name)
d = np.exp(c*1j)
print(d)
print(d.dtype.name)

a = rg.random((2,3))
print(a)
print(a.sum())
print(a.min())
print(a.max())

b = np.arange(12).reshape(3,4)
print(b)
print(b.sum(axis=0)) # sum of each column
print(b.min(axis = 1)) # min of each row
print(b.cumsum(axis=1)) # cumulative sum along each row

'''
The Basics: Universal functions
'''
print()
print('The Basics: Universal functions')

B = np.arange(3)
print(B)
print(np.exp(B))
print(np.sqrt(B))
C = np.array([2., -1., 4.])
print(np.add(B, C))

x = np.array([1, 4, 9, 16, 25])
#x = np.array([1, 4, 9, 16, 25], dtype = float)
y = np.sqrt(x) # takes the square root of each element in the array
print('x =', x)
print('y =', y)
# import math
# z = math.sqrt(x) # doesn't work because array is not a 1 element array
# print(z)

'''
Shape Maniputlation - changint the shape of an array
'''
print()
print('Shape Maniputlation - changint the shape of an array')

a = np.floor(10*rg.random((3,4)))
print(a)
print(a.shape)
print(a.ravel()) # returns the array, flattened
print(a.reshape(6,2)) # returns the array with a modified shape
print(a.T) # returns the array, transposed
print(a.T.shape)
print(a.shape)

print(a)
a.resize((2,6))
print(a)
print(a.reshape(3,-1))

'''
Linear Algebra – Simple Array Operations
'''
print()
print('Linear Algebra – Simple Array Operations')

a = np.array([[1.0, 2.0], [3.0, 4.0]])
print(a)
print(a.transpose())
print(np.linalg.inv(a))
u = np.eye(2) # unit 2x2 matrix; "eye" represents "I"
print(u)
j = np.array([[0.0, -1.0], [1.0, 0.0]])
print(j @ j)        # matrix product
print(np.trace(u)) # trace
y = np.array([[5.], [7.]])
print(y)
print(np.linalg.solve(a, y))






