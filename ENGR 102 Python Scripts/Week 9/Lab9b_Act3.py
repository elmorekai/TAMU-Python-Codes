# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 9b Activity 3
# Date:         10/19/2020
#

from math import *
print('This program will find a variety of data points from weather data in \
      Byran,Tx for 3 years.')

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

# code to find the maximum and minmum temperature values
max_val = None 
min_val = float('Infinity')
for temp in new_lines:
    if max_val == None:
        max_val = temp[1]
    if temp[1] > max_val:
        max_val = temp[1]
    if temp[3] > max_val:
        max_val = temp[3]
    if min_val == float('Infinity'):
        min_val = temp[1]
    if temp[1] < min_val:
        min_val = temp[1]
    if temp[3] < min_val:
        min_val = temp[3]
print('The maximum temperature value in the 3 year period is', max_val,'degrees \
      fahrenheit.')
print('The minimum temperature vlue in the 3 year period is', min_val,'degrees \
      fahrenheit.')

# code to find the average daily precipitation over the 3 years
average = 0
total = 0
data_counter = 0
for data in new_lines:
    total += data[13]
    data_counter += 1
average = total / data_counter
print('The average level of precipitation over the 3 year period was {:.2f} inches.'\
      .format(average))
    
# code to find the maximum and minimum temperature for December 25 over the 3 years
temp_list = []
desired_date = '12/25'
max_val = None
min_val = float('Infinity')
for data in new_lines:
    if desired_date in data[0]:
        temp_list.append(data[1])
        temp_list.append(data[3])
for temp in temp_list:
    if max_val == None:
        max_val = temp
    elif temp > max_val:
        max_val = temp
    if min_val == float('Infinity'):
        min_val = temp
    elif temp < min_val:
        min_val = temp
print('The maximum temperature value for December 25 in the 3 year period was'\
      , max_val,'degrees fahrenheit')
print('The minimum temperature value for December 25 in the 3 year period was'\
      , min_val,'degrees fahrenheit')
    
# code to find the standard deviation and mean of the dew average for July 2015 
desired_month = '7'
desired_year = '2015'
total_dew_avg = 0
mean_dew_avg = 0
deviation_dew_avg = 0
total_deviation = 0
num_dew_avg = 0
dew_avg_list = []
for data in new_lines:
    date = data[0].split('/')
    if desired_year == date[2] and desired_month == date[0]:
        dew_avg_list.append(data[5])
for dew in dew_avg_list:
    total_dew_avg += dew
    num_dew_avg += 1
mean_dew_avg = total_dew_avg / num_dew_avg
for i in range(len(dew_avg_list)):
    deviation_dew_avg = dew_avg_list[i] - mean_dew_avg
    total_deviation += deviation_dew_avg ** 2
standard_deviation = sqrt(total_deviation / (num_dew_avg - 1))
print('The average of the average dew point in July 2015 was', mean_dew_avg)
print('The standard deviation of the average dew points in July 2015 was'\
      ,standard_deviation)

# code to calculate the percentage of days the humidity was above 90%
humidity_bar = 90
above_counter = 0
humidity_counter = 0
percentage = 0
for data in new_lines:
    humidity_counter += 2
    if data[7] > 90 or data[9] > 90:
        above_counter += 1
percentage = (100 * above_counter) / humidity_counter
print('The percentage of humidity readings above 90% humidity was {:.2f}%'\
      .format(percentage))





