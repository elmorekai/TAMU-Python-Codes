# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore, Nikhita Sathish, Jaden Reyes, Halimat Ettu
# Section:      545
# Team:         N/A
# Assignment:   Lab 11 Activity 2
# Date:         11/2/2020
#

def interpolate(search, x_vals, y_vals):
    ''' this function finds the interpolated value of a given data point 
    from a line derivated from a list of data points '''
    if search >= x_vals[-1]:
            slope = (y_vals[-2] - y_vals[-1])/(x_vals[-2] - x_vals[-1])
            found_val = slope*(search - x_vals[-1]) + y_vals[-1]
    elif search <= x_vals[0]:
            slope = (y_vals[1] - y_vals[0])/(x_vals[1] - x_vals[0])
            found_val = slope*(search - x_vals[0]) + y_vals[0]
    else:
        for i in range(len(x_vals)):
            if search >= x_vals[i] and search <= x_vals[i+1]:
                slope = (y_vals[i+1] - y_vals[i])/(x_vals[i+1] - x_vals[i])
                found_val = slope*(search - x_vals[i]) + y_vals[i]
    return(found_val)


# print statement stating the purpose of the program
print('This program will find the interpolated or extrapolated value of a given \
      query value from a line constructed from a given list of data. ')

# input for the file to read the data from 
file_name = input('Please enter the file name which wil build the line for the \
                  interpolation and extrapolation here: ')

# set file for development and testing
# file_name = 'Lab11-data-Act2'

# open the file to be read
file_data = open(file_name + '.txt', 'r')

# input for data point value your looking for
query = float(input('Please enter the number you which to find the value for here: '))

# reads all the lines of the file and closes the file
lines = file_data.readlines()
file_data.close()

# sets to empty list for data points and data values
data_pt = []
data_val = []

# converts list data from strings to floats
for line in lines[4:]:
    line = line.split(' ')
    if '' in line:
        data_pt.append(float(line[0]))
        data_val.append(float(line[-1]))
    else:
        data_pt.append(float(line[0]))
        data_val.append(float(line[1]))

# sorts all data to be used for interpolation later
# set two more empty list sorted data points and sorted data values
sort_data_pt = []
sort_data_val = []
for i in range(len(data_pt)):
    if i == 0: 
        sort_data_pt.append(data_pt[i])
        sort_data_val.append(data_val[i])
    else:
        for z in range(len(sort_data_pt)):
            if data_pt[i] < sort_data_pt[z]:
                sort_data_pt[z:z] = [data_pt[i]]
                sort_data_val[z:z] = [data_val[i]]
                break
            if data_pt[i] > sort_data_pt[-1]:
                sort_data_pt.append(data_pt[i])
                sort_data_val.append(data_val[i])

# print the interpolated  or extrapolated value 
print(interpolate(query, sort_data_pt, sort_data_val))



