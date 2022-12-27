# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 2 Activity 2
# Date:         08/31/2020
#

# Calculate the position of a car on a race track given the initial measurements
# in time and distance from a starting line in seconds and meters. The measurments
# started from 30 seconds and 50 meters away from the starting line and ended 
# at 45 seconds and 615 meters away from the starting line. 

# I am solving this problem using linear interpolation, which needs the slope
# derived from the starting and ending points of the mearsurment and a given time
# to find the resulting position. 
# Constants for the car  
initial_position = 50 #meters
initial_time = 30 #seconds
final_position = 615 #meters
final_time = 45 #seconds


# the slope derived from constants
slope = ((final_position - initial_position) / (final_time - initial_time))

# Variables
t = 37 #seconds
y = initial_position + (t - initial_time) * (slope)
given_time = t
resulting_position = y

print("Calculate the position of a car on a race track given the initial measurements \
in time and distance from a starting line in seconds and meters. The measurments \
started from 30 seconds and 50 meters away from the starting line and ended \
at 45 seconds and 615 meters away from the starting line.")
print()
print("The position of the car at time t =", given_time,"seconds was y =", resulting_position,"meters.")



