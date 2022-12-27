# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 12b Activity 2
# Date:         11/16/2020
#

def integrate_right(a, b, f_x, n = 10):
    ''' Function calculates the area under a curve using right endpoints and \
        rectangles'''
    counter = 0
    TOL = 1e-6
    partion = (b - a)/n
    pre_total = 0
    for i in (range(n)):
        x = a + (i+1) * partion
        area = eval(f_x) * partion
        pre_total += area
    difference = 1
    while difference >= TOL:
        n *= 2
        partion = (b - a)/n
        total = 0
        for i in (range(n)):
            x = a + (i+1) * partion
            area = eval(f_x) * partion
            total += area
        counter += 1
        difference = pre_total - total
        pre_total = total
    return (total, counter)

def integrate_left(a, b, f_x, n = 10):
    ''' Function calculates the area under the curve using left endpoints and \
        rectangles'''
    counter = 0
    TOL = 1e-6
    partion = (b - a)/n
    pre_total = 0
    for i in (range(n)):
        x = a + (i * partion)
        area = eval(f_x) * partion
        pre_total += area
    difference = 1
    while difference >= TOL:
        n *= 2
        partion = (b - a)/n
        total = 0
        for i in (range(n)):
            x = a + (i * partion)
            area = eval(f_x) * partion
            total += area
        counter += 1
        difference = pre_total - total
        pre_total = total
    return (total, counter)

def integrate_mid(a, b, f_x, n = 10):
    '''Function calculates the area under a curve using midpoints and \
        rectangles'''
    counter = 0
    TOL = 1e-6
    partion = (b - a)/n
    pre_total = 0
    for i in (range(n)):
        x = a + (((2*(i+1)-1)/2) * partion)
        area = eval(f_x) * partion
        pre_total += area
    difference = 1
    while difference >= TOL:
        n *= 2
        partion = (b - a)/n
        total = 0
        for i in (range(n)):
            x = a + (((2*(i+1)-1)/2) * partion)
            area = eval(f_x) * partion
            total += area
        counter += 1
        difference = pre_total - total
        pre_total = total
    return (total, counter)

def integrate_trap(a, b, f_x, n = 10):
    '''Function calculates the area under a curve using trapezoids'''
    counter = 0
    TOL = 1e-6
    partion = (b - a)/(n)
    x = a
    f_a = eval(f_x)
    x = b
    f_b = eval(f_x)
    pre_total = 0
    for i in (range(1,n)):
        x = a + i * partion
        area = (2*eval(f_x))
        pre_total += area
    pre_total += f_a + f_b
    pre_total *= partion * 0.5
    difference = 1
    while difference >= TOL:
        n *= 2
        partion = (b - a)/n
        total = 0
        for i in (range(1,n)):
            x = a + i * partion
            area = 2*eval(f_x)
            total += area
        total += f_a + f_b
        total *= partion * 0.5
        counter += 1
        difference = pre_total - total
        pre_total = total
    return (total, counter)

# print statement stating what the program does
print('This program computes the area under a function from one value to another.')

# get input for the function to find the area under
function = input('Please enter the function to intergrate here in python syntax: ')

# get input for the interval of the area under the curve
a = float(input('Please enter the starting value of the interval here: '))
b = float(input('Please enter the ending value of the interval here: '))

# open a file that will contain the areas of each shape under the curve and the total iterations
# file_name = input('Please enter the name of the file to write to here: ')
file_name = 'Lab12b_Act2_fil'
file = open(file_name + '.out', 'w')

# write function to file in a formated way
file.write(('Function: {}' + '\n').format(function))

# write interval to file
file.write(('Interval: a = {} to b = {} \n').format(a, b))

# set up the shape to fill up the space under the curve
# calculate the area under the curve
total_area_right, iterations_right = integrate_right(a, b, function)
total_area_left, iteration_left = integrate_left(a, b, function)
total_area_mid, iterations_mid = integrate_mid(a, b, function)
total_area_trap, iterations_trap = integrate_mid(a, b, function)

# print to the console along with writing to the file the areas

print('The area under the curve with right endpoints is', total_area_right)
print('It took', iterations_right,'iterations')
file.write(('The area under the curve with right endpoints is {}.\n').format(total_area_right))
file.write(('It took a total of {} iterations.\n').format(iterations_right))

print('The area under the curve with left endpoints is', total_area_left)
print('It took', iteration_left,'iterations')
file.write(('The area under the curve with left endpoints is {}.\n').format(total_area_left))
file.write(('It took a total of {} iterations.\n').format(iteration_left))

print('The area under the curve with midpoints is', total_area_mid)
print('It took', iterations_mid,'iterations')
file.write(('The area under the curve with midpoints is {}.\n').format(total_area_mid))
file.write(('It took a total of {} iterations.\n').format(iterations_mid))

print('The area under the curve using trapezoidal rule is', total_area_trap)
print('It took', iterations_trap,'iterations')
file.write(('The area under the curve using trapezoidal rule is {}.\n').format(total_area_trap))
file.write(('It took a total of {} iterations.\n').format(iterations_trap))

# close file
file.close

# code for testing functions
# n= 10
# counter = 0
# TOL = 1e-6
# partion = (b - a)/n
# pre_total = 0
# for i in (range(n)):
#     x = a + (i+1) * partion
#     area = eval(function) * partion
#     pre_total += area
# difference = 1
# while difference >= TOL:
#     n *= 2
#     partion = (b - a)/n
#     total = 0
#     for i in (range(n)):
#         x = a + (i+1) * partion
#         area = eval(function) * partion
#         total += area
#     counter += 1
#     difference = pre_total - total
#     pre_total = total
# print(total)