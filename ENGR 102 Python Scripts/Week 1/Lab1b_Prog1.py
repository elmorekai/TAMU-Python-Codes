# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab1b activity 1
# Date:         8/24/2020
#

# A fun statement about myself
print("Hello, I am Kai Elmore and I like playing games")
print() 

# Using Ohm's Law
# Calculate the voltage across a conductor with 
# resistance 20 ohms and a current of 5 A where A represents amperes.
# I = V/R ==> V = IR
print("The voltage across a conductor with resistance 20 ohms and a current of 5 A is", 
      5*20, "V")
print()

# The kinetic energy of an object with mass 100 kg and velocity 21 m/s.
print("The kinetic energy of an object with mass 100 kg and velocity 21 m/s is",
      0.5*100*(21**2), "J")
print()

# The Reynolds ( the ratio of inertial forces to viscous forces number for a 
# fluid with velocity 100 m/s and kinematic 
# viscosity 1.2 (m^2)/s, with characteristic linear dimension 2.5 m.
print("The Reynolds number for a fluid with velocity 100 m/s and kinematic viscosity 1.2 (m^2)/s, with characteristic linear dimension 2.5 m is",
      (100*2.5)/1.2 )
print()

# Using Arqs equation
# The production of a oil and gas well after 20 days, if it had an initial
# production rate of 100 barrels/day, an initial decline rate of 2 barrels/day,
# and a hyperbolic constant of 0.8.
print("The production of a oil and gas well after 20 days, if it had an initial production rate of 100 barrels/day, an initial decline rate of 2 barrels/day,and a hyperbolic constant of 0.8 is",
      (100/(1 + (0.8*2*20))**(1/0.8)), "barrels/day")
print()

from math import *
# Using the Mohr-Coulomb Failure Criterion
# calculating the shear stress when a normal stress of 20 lbf/in^2 is applied 
# to a material with cohesion 2 lbf/in^2 and angle of internal friction 35 degrees. 
print("The shear stress when a normal stress of 20 lbf/in^2 is applied to a material with cohesion 2 lbf/in^2 and angle of internal friction 35 degrees is",
      (20*tan((7*pi)/36)) + 2, "lbf/in^2")