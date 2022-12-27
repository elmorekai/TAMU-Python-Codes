# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lecture 7 activity 2
# Date:         10/8/2020
#

from math import*
# Grade Data for Lab7 Activity 2

gradeData=[79,99,73	,49,67,62,52,99,57,58	,67,88,71	,69,41,74	,53,90,63	,
           66,92,54	,61,59,48,71,83,89,99	,69,66,40,48,41,99,68	,52,78,77,
           71,40,65,77,87,96,44,54,60,89,72]
'''
Part A: Calculate the mean
'''
# Variables
total = 0 # the sum of the list 
num_grade = 0 # the number of grades
mean = 0 # the mean of the list
# Loope to caluclate the mean
for grade in gradeData:
    total += grade
    num_grade += 1
mean = total / num_grade
print('The mean of the grade data is', mean)

'''
Part B: Calculate the population standard deviation
'''
# Variables
pop_standard_deviation = 0 # standard deviation of grade data
num_grade = 0 # amount of grades in the list
deviation = 0 # deviation for each grade
total_deviation = 0 # the summantion of each deviation
# Loop to calculate the standard deviation
for grade in gradeData:
    deviation = (grade - mean) ** 2
    total_deviation += deviation
    num_grade += 1
    deviation = 0
pop_standard_deviation = sqrt(total_deviation/num_grade)
print('The population standard deviation for the grade data \
is',pop_standard_deviation)

'''
Part C: finding the maximum and minimum 
'''
# Variables
minimum = None
maximum = None
# Loop to find the minimum and maximum
for grade in gradeData:
    if maximum == None:
        maximum = gradeData[0]
    if maximum != None:
        if grade > maximum:
            maximum = grade
    if minimum == None:
        minimum = gradeData[0]
    if minimum != None:
        if grade < minimum:
            minimum = grade
print('The highest grade in the grade data is', maximum)
print('The lowest grade in the grade data is', minimum)

'''
Part D: get the average to equal 75.0
'''
# Variables 
desired_average = 75.0
deltagrade = 0
# Equation to find delta grade
deltagrade = ((desired_average * num_grade) - total)/num_grade
print('The constant to add to each grade to make the \
average =', desired_average,'is', deltagrade)




