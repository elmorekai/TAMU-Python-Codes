# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 3b program 1b
# Date:         09/11/2020
#

# Using the kinetic energy formula
# Find kinetic energy of an object from a given mass in kg and velocity in m/s.

print("This program calculates the Kinetic Energy from a given amount of mass \
      in kilograms and velocity in meters per second using the kinetic energy \
          formula. ") # description of program

print('Please only type in numbers and not letters, for example 20 is a good \
      input.') # instructions on how to input values

mass = float(input('Please enter mass (kg) here: ')) 
# input of mass as a string turned to a float in kilograms

velocity = float(input('Please enter velocity (m/s) here: ')) 
# input of velocity as a string turned to a float in meters per second

kinetic_energy = 0.5 * mass * (velocity ** 2) 
# Kinetic engery formula used to assign the found value of kinetic engergy in 
# joules

print()
print("The Kinetic Energy =", kinetic_energy, "J")


