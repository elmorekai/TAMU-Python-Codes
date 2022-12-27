# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab ________ (e.g. Lab 1b-2)
# Date:         _____________
#

#
# YOUR CODE HERE
#

fid = open('ThermoData_P_5_10_15_MPa_win.csv', 'r')
# code to read all data in file
lines = fid.readlines()
# code to close the file
fid.close()
# code to split the each day's data into a list of floating numbers
new_lines = []
num_lines = 4
while num_lines != len(lines):
    line = lines[num_lines].split(',')
    for i in range(0, len(line)):
        if line[i] == '-':
            line[i] = 0.0
        else:
            line[i] = float(line[i])
    num_lines += 1
    new_lines.append(line)
print(new_lines)