# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Dr. O.
# Section:      ENGR 102-...

#########################################################
###   Simultaneous Assignment in Python
#########################################################

# Example 1

a = 3
b = 5.6
c = -1.2
print(a, b, c)
print()

# The code above is equivalent to the code below:
    
a, b, c = 3, 5.6, -1.2
print(a, b, c)
print()

#########################################################
print('-'*20)
#########################################################

# Example 2: swapping values

x = 5
y = 7
print(x, y)

temp = x    # temporary variable to store the value of x
x = y
y = temp
print(x, y)
print()

# The code above is equivalent to the code below:
x, y = 5, 7
print(x, y)

x, y = y, x    # swapping values
print(x, y)   
print()
    
#########################################################
print('-'*20)
#########################################################    

# Example 3: swapping values    

z, s = 25, 'hello'    # different data type
print(z, s)
z, s = s, z
print(z, s)

#########################################################
print('-'*20)
#########################################################    

# Example 4: swapping elements in a list
# We have to pay attention to the indices

my_list = [10, 20, 30, 40, 50]
print(my_list)
print('The list contains {} elements.'.format(len(my_list)))
# Printing one element at a time
for i in range(len(my_list)):   
    print('Index =', i, ', element =', my_list[i])
print()

for i in range(len(my_list) - 1):   # NOT range(len(my_list))
# Using range(len(my_list)) will give "IndexError: list index out of range"
    print('Current index:', i)
    print('Swapping the element at', i, 'with the element at', i+1)
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    print('Current list:', my_list)
    
    
    









    
    