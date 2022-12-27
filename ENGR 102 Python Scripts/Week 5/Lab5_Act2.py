# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 5 Activity 2
# Date:         09/21/2020
#

# Write a program that will take two inputted 3D positions at two points in 
# time, and then calculate five 3D position in between them, including
# the starting and ending 3D points, which are evenly spaced. 

# The initial point will be at time t1 = 13 located: (1, 3, 7) 
# The final point will be at time t2 = 84 located: (23, -5, 10)


print('This program that will take two inputted 3D positions at two points in \
time, and then calculate five 3D position in between them, including \
the starting and ending 3D points, which are evenly spaced.')
print()
print('The initial point will be at time t1 = 13 located: (1, 3, 7)')
print('The final point will be at time t2 = 84 located: (23, -5, 10)')

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

# Variables
start_time = float(input('Please enter the start time between 13 and 84 seconds: '))
end_time = float(input('Please enter the end time between 13 and 84 seconds: '))
factor = (end_time - start_time) / 4 # what time will be changing by

# Loop for linear interpolation
while start_time <= end_time:
    if (start_time > 84) or (start_time < 13):
        print('Error: invalind input for starting time')
        break
    if (end_time > 84) or (end_time < 13) or (end_time < start_time):
        print('Error: invalid input for ending time')
        break
    x0 = x + (start_time - t1) * x_slope
    y0 = y + (start_time - t1) * y_slope
    z0 = z + (start_time - t1) * z_slope
    print('time = {:>10.2f} sec  position = ({:.4f}, {:.4f}, {:.4f})'.format(start_time, x0, y0, z0))
    start_time += factor














