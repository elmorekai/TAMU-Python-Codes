# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 11b Functions
# Date:         11/8/2020
#

from math import *

''' Part A '''
def function_a1(length, width, height, radius):
    ''' Function to find the left over volume of a box with a small hole'''
    volume_box = length * width * height
    Area_hole = pi * (radius**2)
    volume_hole = Area_hole * height
    volume_left = volume_box - volume_hole
    return volume_left

def function_a2(length, width, height, radius):
    ''' Function to find the left over volume of a box with a big hole'''
    volume_box = length * width * height
    Area_hole = pi * (radius**2)
    hyp = sqrt((length/2)**2 + (width/2)**2)
    volume_hole = Area_hole * height
    if radius >= hyp:
        volume_left = 0
    else:
        volume_left = volume_box - volume_hole
    return volume_left

''' Part B '''
def function_b(name, cost, value):
    '''Function finds the company with the lowest profitability from a list'''
    minimum = None
    company = 0
    profit = []
    for i in range(len(name)):
        profit.append(value[i]-cost[i])
    for i in range(len(profit)):
        if minimum == None:
            minimum = profit[i]
        elif profit[i] <= minimum:
            minimum = profit[i]
            company = name[i]
    return (company, minimum)

''' Part C '''
def function_c(name, state, city, zip_code, address_1, address_2 = ''):
    '''Function prints the mailing label of a given address'''
    print(name)
    print(address_1, address_2)
    print(city, state, zip_code)
    
''' Part D '''
def function_d(file_name):
    ''' This file creates a .tsv file from a .csv file'''
    fid = open(file_name + '.csv', 'r')
    fid_2 = open(file_name + '.tsv', 'w')
    
    # read in the lines, and close csv file
    lines = fid.readlines()
    fid.close()
    
    # iterate through lines, split each line, assign to sublist
    for i in range(len(lines)):
        sublist = lines[i].split(',')
        
        # iterate through each sublist and add it to tsv file - if last value in list, don't tab
        for j in range(len(sublist)):
            if (j == len(sublist) - 1):
                fid_2.write(sublist[j])
            else:
                fid_2.write(sublist[j] + '\t')
    # close tsv file after writing
    fid_2.close()
    
    # return new .tsv file
    return fid_2

''' Part E '''
def function_e(list_name):
    '''finds the maximum, minimum, and mean of a given'''
    max_val = None
    min_val = None
    total = 0
    number = 0
    for i in list_name:
        if max_val == None and min_val == None:
            max_val = i
            min_val = i
        elif i > max_val:
            max_val = i
        elif i < min_val:
            min_val = i
        total += i
        number += 1
    average = total / number
    return (max_val, average, min_val)

''' Part F '''
def function_f(time, distance):
    '''finds the average velocity between consecutive time segment of two list'''
    velocity_list = []
    for i in range(len(time)):
        velocity = (distance[i+1] - distance[i])/(time[i+1] - time[i])
        velocity_list.append(velocity)
    return velocity_list