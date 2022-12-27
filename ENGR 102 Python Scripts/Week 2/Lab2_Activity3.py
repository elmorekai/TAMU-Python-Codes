# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 2 Activity 3
# Date:         09/01/2020
#

from math import *
# Calculate the position, relative to a starting line, of a car on a circular
# track with a radius of 0.5 kilometers given the initial 
# measurements in time and distance from a starting line in 
# seconds and meters. The measurments started from 30 seconds and 50 meters 
# away from the starting line and ended at 45 seconds and 615 meters away from 
# the starting line.

# Constants for the car  
initial_position = 50 #meters
initial_time = 30 #seconds
final_position = 615 #meters
final_time = 45 #seconds
track_radius = 500 #meters
track_circumference = 2 * (pi * track_radius)

# the slope derived from constants
slope = ((final_position - initial_position) / (final_time - initial_time))

# Variables
t = 37 #seconds
y = initial_position + (t - initial_time) * (slope)
yr = y - ((y // track_circumference) * track_circumference)
given_time = t
total_travel = y
real_position = yr

print("Calculate the position, relative to a starting line, of a car on a circular \
track with a radius of 0.5 kilometers given the initial \
measurements in time and distance from a starting line in \
seconds and meters. The measurments started from 30 seconds and 50 meters \
away from the starting line and ended at 45 seconds and 615 meters away from \
the starting line.")
print()
print("The position of the car at time t =", given_time,"seconds, relative to a \
starting line, was y =", real_position,"meters.")

