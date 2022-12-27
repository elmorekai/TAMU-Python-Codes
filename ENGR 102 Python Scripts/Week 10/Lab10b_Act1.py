# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 10b Activity 1
# Date:         11/1/2020
#

import numpy as np
import matplotlib.pyplot as plt
product = np.array([[1], [0]])
M = np.array([(1.00583, -0.087156), (0.087156, 1.00583)])
counter = 0
for i in range(0, 200):
    
    v = product
    plt.plot(v[0],v[1], '.r')
    product = M @ v
    print(product)
    counter += 1
print('The number of iterations was', counter)
plt.xlabel('x-component')
plt.ylabel('y-component')
plt.title('swirl outline')