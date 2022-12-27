# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore, Jaden Reyes, Nikhita Sathish, Halimat Ettu
# Section:      545
# Team:         N/A
# Assignment:   Lab 12 Activity 2
# Date:         11/15/2020
#
import numpy as np

def interpolate(T):
    ''' this function finds the interpolated value of a given data point 
    from a line derivated from a numpy array of data points '''
    if T >= data[-1][0]:
        ind1 = -2
        ind2 = -1
        T1 = data[ind1][0]
        T2 = data[ind2][0]
        values1 = data[ind1][1:]
        values2 = data[ind2][1:]
        values = values1 + (T - T1)*(values2 - values1)/(T2 - T1)
    elif T <= data[0][0]:
        ind1 = 1
        ind2 = 2
        T1 = data[ind1][0]
        T2 = data[ind2][0]
        values1 = data[ind1][1:]
        values2 = data[ind2][1:]
        values = values1 + (T - T1)*(values2 - values1)/(T2 - T1)
    else:
        for i in range(len(data)):
            if T >= data[i][0] and T <= data[i+1][0]:
                ind1 = i
                ind2 = i+1
                T1 = data[ind1][0]
                T2 = data[ind2][0]
                values1 = data[ind1][1:]
                values2 = data[ind2][1:]
                values = values1 + (T - T1)*(values2 - values1)/(T2 - T1)
    return values[0:4]

# prints purpose of program
print('This program will deliver the interpolated values of a inputted \
measurement in vector form. The data used for the interpolation is read from a \
inputted file.')

# input for the data to be used for the interpolation
file_name = input('Please enter the name of the file to be read from here: ')
# file_name = 'Lab12-Act2-Win'

# input of the measurement to interpolate
val = float(input('Please enter the measurement to find the interpolated values for \
here: '))

# open the inputted file here
file = open(file_name + '.csv', 'r')
# read all the data inside of the file
file_data = file.readlines()
# close the file
file.close()

# set a empty list to hold the converted data from strings to lists of floats
file_copy = []

# loop to add converted data to empty list
for i in file_data[4:]:
    i = i.split(',')
    for j in range(len(i)):
        i[j] = float(i[j])
    file_copy.append(i)

# set empty list to hold sorted data
data = []

# loop to sort the nested list into the empty list set before 
for line in file_copy:
    if line == file_copy[0]:
        data.append(line)
    else:
        for z in range(len(data)):
            if line[0] < data[z][0]:
                data[z:z] = [line]
                break
            elif line[0] > data[-1][0]:
                data.append(line)
# turn the list into a numpy array
data = np.array(data)
# print the interpolated values
print(interpolate(val))
