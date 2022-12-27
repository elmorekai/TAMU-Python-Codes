""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jaden Thomas Reyes, Nikhita Sathish, Halimat Ettu, Kai Elmore
# Section:      545
# Team:         25
# Assignment:   Lab 12b_Activity 2
# Date:         18/11/2020


##### children functions

#function to calculate f(x)
def F(f, x):
    '''This program will evaluate the function given at value of x provided '''
    return eval(f)   #calculate the function at the value of x given






#integrating the function within the intervals/range provided by the user
def area_f1(f, start, end, elements):                 #function for method 1, Shape: Rectangle
    ''' This program calculate the area under a function using the value of the function at the beginning of the interval
    (left bound of the interval)'''
    count = 0
    # elements = 10
    x = start                  #lower bound
    length = (end-start)/ elements     #subinterval lengths
    area = 0
    for i in range(elements):
        area += F(f,x) * length                #formula for area of rectangle = l*w
        x += length
        count += 1
    return area


def area_f2(f, start, end, elements):                  #function for method 2
    '''This program calculate the area under a function using the value of the function at the end of the subintervals
    (right bound of the inteval)'''
    length = (end - start)/ elements
    x = start + length
    area = 0
    for i in range(elements):
        area += F(f,x)*length
        x += length
    return area

def area_f3(f, start, end, elements):                  # functtion for method 3
    '''This program calculates the area under a function using the value of the function at the midpoint'''                  # elements is the subintervals
    length = (end - start)/ elements         #length/subinterval distance of the subintervals        
    x = start + (length / 2)                  
    area = 0
    for i in range(elements):
        area += F(f,x)* length
        x += length
    return area


def area_f4(f, start, end, elements):                    #function for method 4
    '''This program calculates the area under a function with trapezoid with one parallel edge being the value of the function
    at the beginning of the interval, and another being the value of the function at the end of the interval.'''
    length = (end - start)/ elements              
    x = start
    area = 0
    for i in range(elements):
        area += ((F(f,x)+ F(f, x+length))/2) * length    #formula for area of trapezoid = ((a+b)/2)*height
        x += length                                     #width is the height
    return area

##### main/ parent function
def area(area_f, f, start, end):                   #area_f is the children functions above
    '''This program calculates the area under a function using any method in the other functions created above 
    until the area converges'''
    elements = 10 #initially considering no of sub intervals to 10
    count = 0
    while True:
        current_area = area_f(f, start, end, elements) #area before the increment of elements(subintervals)
        elements += 1 #increasing sub intervals
        count += 1
        new_area = area_f(f, start, end, elements)    #area after the increment of elements(subintervals)
        if current_area - new_area < 10**(-6): #if difference between them is less than 10^-6 it returns the new_area
            return ('{:.4f}'.format(new_area)), count

#get user inputs
start = float(input('enter the starting value of the range: '))       #lower bound converted to float
end = float(input('enter the ending value of the range: '))            #upper bound converted to float
f = input('enter a function  f(x)'
          'for example, f(x) = x**2 -1 or np.sin(6*x): ')                                     #function as a string
filename = input('enter the name of the file without any extension: ')   

#create a file with the file name given by the user
fid = open(filename + '.out', 'w')

        
    

#print result
print('f(x) = ', f)
print(area(area_f1, f, start, end))
print(area(area_f2, f, start, end))
print(area(area_f3, f, start, end))
print(area(area_f4, f, start, end))


#write the result in file created
fid.write('f(x) = ' + str(f) + '\n')
fid.write('range: (' + str(start) + ',' + str(end) + ')' + '\n')
fid.write('(area    iteration)' + '\n')
fid.write(str(area(area_f1, f, start, end)) + '\n')
fid.write(str(area(area_f2, f, start, end)) + '\n')
fid.write(str(area(area_f3, f, start, end)) + '\n')
fid.write(str(area(area_f4, f, start, end)) + '\n')


#close file
fid.close()

    
    
    
    
