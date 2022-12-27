# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 1b activity 2
# Date:         8/27/2020
#

from math import *
print(pow(10,-7))
print(1e-7)
print(1/10000000)
print(0.0000001)
print()

print("This shows the evaluation of f(x)=sin(x)/x close to x=0")
print("My guess is 0.4")
print("evaluating f(x) at 1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, and 10^(-7)")
print("x will take on the values 1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, and 10^(-7)")
print(sin(1.0)/1.0)
print(sin(0.1)/0.1)
print(sin(0.01)/0.01)
print(sin(0.001)/0.001)
print(sin(0.0001)/0.0001)
print(sin(0.00001)/0.00001)
print(sin(0.000001)/0.000001)
print(sin(1e-7)/1e-7)
print()

print("This shows the evaluation of g(x)=(1-cos(x))/x close to x=0")
print("My guess is 0.3")
print("evaluating g(x) at 1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, and 10^(-7)")
print("x will take on the values 1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, and 10^(-7)")
print((1-cos(1.0))/1.0)
print((1-cos(0.1))/0.1)
print((1-cos(0.01))/0.01)
print((1-cos(0.001))/0.001)
print((1-cos(0.0001))/0.0001)
print((1-cos(0.00001))/0.00001)
print((1-cos(0.000001))/0.000001)
print((1-cos(1e-7))/1e-7)
print()

print("This shows the evaluation of h(x)=(1 + (1/x))**x close to x=infinity")
print("My guess is 10^8")
print("evaluating h(x) at 1.0, 10, 100, 1000, 10000, 100000, 1000000, and 10^(7)")
print("x will take on the values 1.0, 10, 100, 1000, 10000, 100000, 1000000, and 10^(7)")
print((1 + (1/1))**1)
print((1 + (1/10))**10)
print((1 + (1/100))**100)
print((1 + (1/1000))**1000)
print((1 + (1/10000))**10000)
print((1 + (1/100000))**100000)
print((1 + (1/1000000))**1000000)
print((1 + (1/1e7))**(1e7))
print()