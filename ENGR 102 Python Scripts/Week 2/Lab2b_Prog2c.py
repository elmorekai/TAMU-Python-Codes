# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 2b Program 2c (e.g. Lab 1b-2)
# Date:         09/03/2020
#

# Write a program that will take two observed 3D positions at two points in 
# time, and then calculate five 3D position along in between and including
# the starting and ending 3D points, which are evenly spaced. 

# The initial point will be at time t1 located: (1, 3, 7) 
# The final point will be at time t2 located: (23, -5, 10)

# Constants
t1 = 13 # seconds
x = 1 #meters
y = 3 #meters
z = 7 #meters

t2 = 84 #seconds
x2 = 23 #meters
y2 = -5 #meters
z2 = 10 #meters

# Various slopes between the two end points
x_slope = ((x2 - x) / (t2 - t1))
y_slope = ((y2 - y) / (t2 - t1))
z_slope = ((z2 - z) / (t2 - t1))

t0 = 20 #seconds
x0 = x + (t0 - t1) * x_slope
y0 = y + (t0 - t1) * y_slope
z0 = z + (t0 - t1) * z_slope

print("Calculate the 3D point at time t0 between (1,3,7) at 13 seconds and \
(23,-5,10) at time 84 seconds.")
print("time of interest ", t0, "seconds")
print("x0 = ", x0, "meters")
print("y0 = ", y0, "meters")
print("z0 = ", z0, "meters")
print("--------------------------")

t0 = 27.5 #seconds
x0 = x + (t0 - t1) * x_slope
y0 = y + (t0 - t1) * y_slope
z0 = z + (t0 - t1) * z_slope

print("Calculate the 3D point at time t0 between (1,3,7) at 13 seconds and \
(23,-5,10) at time 84 seconds.")
print("time of interest t0 = ", t0, "seconds")
print("x0 = ", x0, "meters")
print("y0 = ", y0, "meters")
print("z0 = ", z0, "meters")
print("--------------------------")

t0 = 35 #seconds
x0 = x + (t0 - t1) * x_slope
y0 = y + (t0 - t1) * y_slope
z0 = z + (t0 - t1) * z_slope

print("Calculate the 3D point at time t0 between (1,3,7) at 13 seconds and \
(23,-5,10) at time 84 seconds.")
print("time of interest t0 = ", t0, "seconds")
print("x0 = ", x0, "meters")
print("y0 = ", y0, "meters")
print("z0 = ", z0, "meters")
print("--------------------------")

t0 = 42.5 #seconds
x0 = x + (t0 - t1) * x_slope
y0 = y + (t0 - t1) * y_slope
z0 = z + (t0 - t1) * z_slope

print("Calculate the 3D point at time t0 between (1,3,7) at 13 seconds and \
(23,-5,10) at time 84 seconds.")
print("time of interest t0 = ", t0, "seconds")
print("x0 = ", x0, "meters")
print("y0 = ", y0, "meters")
print("z0 = ", z0, "meters")
print("--------------------------")

t0 = 50 #seconds
x0 = x + (t0 - t1) * x_slope
y0 = y + (t0 - t1) * y_slope
z0 = z + (t0 - t1) * z_slope

print("Calculate the 3D point at time t0 between (1,3,7) at 13 seconds and \
(23,-5,10) at time 84 seconds.")
print("time of interest t0 = ", t0, "seconds")
print("x0 = ", x0, "meters")
print("y0 = ", y0, "meters")
print("z0 = ", z0, "meters")
print("--------------------------")

