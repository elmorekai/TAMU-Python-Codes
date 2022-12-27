# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 2b Program 1
# Date:         09/02/2020
#

# A fun statement about myself
print("Hello, I am Kai Elmore and I like researching history")
print()

# Using Ohm's Law
# Calculate the voltage across a conductor with 
# resistance of 20 ohms and a current of 5 A where A represents amperes.
# I = V/R ==> V = IR
resistance = 20 # ohms
current = 5 # amperes
volts = resistance * current # volts
print("The voltage across a conductor with resistance 20 ohms and a current of \
      5 A is", volts, "V")
print()

# Using the kinetic energy formula
# Find kinetic energy of an object with mass 100 kg and velocity 21 m/s.
mass = 100 # kilograms
velocity = 21 # meters per second
kinetic_energy = 0.5 * mass * (velocity ** 2) # joules
print("The kinetic energy of an object with mass 100 kg and velocity 21 m/s is",
      kinetic_energy, "J")
print()

# Using the Reynolds Number formula
# Find the Reynolds (the ratio of inertial forces to viscous forces) number for 
# a fluid with velocity 100 m/s and kinematic 
# viscosity 1.2 (m^2)/s, with characteristic linear dimension 2.5 m.
velocity = 100 # meters per second
kinematic_viscosity = 1.2 # meters squared per second
linear_dimension = 2.5 # meters
reynolds_number = (velocity * linear_dimension) / kinematic_viscosity
print("The Reynolds number for a fluid with velocity 100 m/s and kinematic \
      viscosity 1.2 (m^2)/s, with characteristic linear dimension 2.5 m is", 
      reynolds_number)
print()

# Using Arqs equation
# Find the production of a oil and gas well after 20 days, if it had an initial
# production rate of 100 barrels/day, an initial decline rate of 2 barrels/day,
# and a hyperbolic constant of 0.8.
time = 20 # days
intial_rate = 100 # barrels/day
declined_rate = 2 # barrels/day
hyperbolic_constant = 0.8 #barrels/day
total_production = intial_rate / (1 + hyperbolic_constant * declined_rate * time) ** (1 / hyperbolic_constant)
print("The production of a oil and gas well after 20 days, if it had an initial \
      production rate of 100 barrels/day, an initial decline rate of \
      2 barrels/day,and a hyperbolic constant of 0.8 is",
      total_production, "barrels/day")
print()

from math import *
# Using the Mohr-Coulomb Failure Criterion
# calculate the shear stress when a normal stress of 20 lbf/in^2 is applied 
# to a material with cohesion 2 lbf/in^2 and angle of internal friction 35 degrees. 
stress = 20 # pounds * f/ inches squared
cohension = 2 # pounds * f / inches squared
friction_angle = 35 # degrees
sheer_stress = stress * tan(friction_angle * (pi / 180)) + cohension # lbf/in^2
print("The shear stress when a normal stress of 20 lbf/in^2 is applied to a \
material with cohesion 2 lbf/in^2 and angle of internal friction 35 degrees is",
sheer_stress, "lbf/in^2")