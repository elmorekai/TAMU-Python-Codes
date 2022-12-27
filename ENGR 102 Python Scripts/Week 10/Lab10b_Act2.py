# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 10b Activity 2
# Date:         11/1/2020
#

import numpy as np
import matplotlib.pyplot as plt

# code to open file
fid = open('WeatherDataWindows.csv', 'r')
# code to read all data in file
lines = fid.readlines()
# code to close the file
fid.close()
# code to split the each day's data into a list of floating numbers
new_lines = []
num_lines = 1
while num_lines != len(lines):
    line = lines[num_lines].split(',')
    for i in range(1, len(line)):
        line[i] = float(line[i])
    num_lines += 1
    new_lines.append(line)

'''
part A
'''
# create x values/domain
x = np.linspace(0, 1095, 1095)

pressure = []
avg_temp = []

for i in new_lines:
    pressure.append(i[11])
for i in new_lines:
    avg_temp.append(i[2])

# setting up figure
figure = plt.figure()
ax1 = figure.add_subplot(1,1,1)
ax2 = ax1.twinx()

# plot temperatures and pressures
ax1.plot(x, avg_temp, 'b', label = 'average temperature')
ax2.plot(x, pressure, 'r', label = 'average pressure')

# plot x and y axis labels, and the title of the graph
ax2.axis([0, 1095, 29, 31])
ax1.set_xlabel('Days')
ax1.set_ylabel('temperature in celsius')
ax1.legend(loc="upper left")
ax2.set_ylabel('pressure in atm')
ax2.legend(loc="upper right")






