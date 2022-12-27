# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Class:        Aero 306
# Section:      500
# Team:         N/A
# Assignment:   Homework 1 Code
# Date:         09/14/2022
#
#Goal: Find the coefficiencts U to plug into a summation fomula to approximate
#      the displace in a uniaxial beam undergoing centripetal force. 
#Method: Use a matrix solver to find the U and plug into a summation solver to 
#        find the displacement at the end of the bar. 

import numpy as np
import math as math
def f(x):
 return rho * A * Omega**2 * x

'Variables'
rho = 1
Omega = 1
E = 1
A = 1
L = 1
dx = [L, L/2, L/4, L/8, L/16]
n_list = [1, 2, 4, 8, 16]
K = np.zeros((3,3))
x_list = np.linspace(0,L,4)

''' Find U vector '''
# Function to Find U vector by finding K matrix and F vector
def U_vector(n):
    dx = L/n
    x_list = np.linspace(0,L,n+1)
    x_i = L*x_list
    #print('x_i = ', x_i)
    K = np.zeros((n,n))
    multiplier = (rho*Omega**2*dx**2)/6
    F_i = np.zeros((n,1))
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j and i != n: 
                K[i-1][j-1] = 2
            elif np.abs(i-j) == 1:
                K[i-1][j-1] = -1
            elif np.abs(i-j) > 1:
                K[i-1][j-1] = 0
            elif i == j and i == n:
                K[i-1][j-1] = 1
    for i in range(0, n + 1):
        if i == 0:
            F_i[i-1] = 0
        elif i < n and i != 0:
            F_i[i-1] = f(x_i[i-1]) + 4*f(x_i[i]) + f(x_i[i+1])
        elif i == n:
            F_i[i-1] = f(x_i[i-1]) + 2*f(x_i[i])
    U = np.linalg.solve(K,multiplier*F_i)
    return U

# Function to convert U vector matrix to list
def U_vector_convert(U_vect):
    U_list = []
    for row in range(len(U_vect)):
        U_list.append(U_vect[row][0])
    U_list.insert(0, 0.0)
    return U_list

U_1_list = U_vector_convert(U_vector(1))
U_2_list = U_vector_convert(U_vector(2))
U_4_list = U_vector_convert(U_vector(4))
U_8_list = U_vector_convert(U_vector(8))
U_16_list = U_vector_convert(U_vector(16))

''' Finding N values '''
def N_vector(U_list, n, delta_x):
    N_values = [0.0] * n
    for i in range(1, n+1):
        if i == 1:
            N_values[i-1] = A*E*U_list[i]/delta_x
        else:
            N_values[i-1] = A*E*(U_list[i] - U_list[i - 1])/delta_x
    return N_values

def N_plot(N_list, x_list, n):
    N_x_list = [0]
    N_plot_list = []
    for point in range(1, n + 1):
        if point == n:
            N_x_list.append(x_list[point])
        else:
            N_x_list.append(x_list[point])
            N_x_list.append(x_list[point])
        N_plot_list.append(N_list[point - 1])
        N_plot_list.append(N_list[point - 1])
    return N_x_list, N_plot_list

N_1_list = N_vector(U_1_list,1,dx[0])
N_2_list = N_vector(U_2_list,2,dx[1])
N_4_list = N_vector(U_4_list,4,dx[2])
N_8_list = N_vector(U_8_list,8,dx[3])
N_16_list = N_vector(U_16_list,16,dx[4])


''' Plotting '''
import matplotlib.pyplot as plt

def u_x(x):
    u = ((rho*Omega**2)/6*E)*(3*L**2*x - x**3)
    return u
def N_x(x):
    N = (0.5*rho*A*Omega**2)*(L**2 - x**2)
    return N

# plotting displacement U
x_list = np.linspace(0,L,100)
x_1_list = np.linspace(0,L,n_list[0] + 1)
x_2_list = np.linspace(0,L,n_list[1] + 1)
x_4_list = np.linspace(0,L,n_list[2] + 1)
x_8_list = np.linspace(0,L,n_list[3] + 1)
x_16_list = np.linspace(0,L,n_list[4] + 1)

u_exact_list = []
N_exact_list = []
for point in range(len(x_list)):
    u_exact_list.append(u_x(x_list[point]))
    N_exact_list.append(N_x(x_list[point]))

plt.figure()

plt.plot(x_list,u_exact_list, label = 'exact')
plt.plot(x_1_list,U_1_list, label = 'n = 1')
plt.plot(x_2_list,U_2_list, label = 'n = 2')
plt.plot(x_4_list,U_4_list, label = 'n = 4')
plt.plot(x_8_list,U_8_list, label = 'n = 8')
plt.plot(x_16_list,U_16_list, label = 'n = 16')
plt.xlabel('Position along bar (x/L)')
plt.ylabel('Normalized Horizontal Displacement, u(x)')
plt.title('Normalized Horizontal Displacement along bar')
plt.legend()

# plotting reaction N
N_x_1_list, N_1_plot_list = N_plot(N_1_list, x_1_list, n_list[0])
N_x_2_list, N_2_plot_list = N_plot(N_2_list, x_2_list, n_list[1])
N_x_4_list, N_4_plot_list = N_plot(N_4_list, x_4_list, n_list[2])
N_x_8_list, N_8_plot_list = N_plot(N_8_list, x_8_list, n_list[3])
N_x_16_list, N_16_plot_list = N_plot(N_16_list, x_16_list, n_list[4])

plt.figure()
plt.plot(x_list,N_exact_list, label = 'exact')
plt.plot(N_x_1_list, N_1_plot_list, label = 'n = 1')
plt.plot(N_x_2_list, N_2_plot_list, label = 'n = 2')
plt.plot(N_x_4_list, N_4_plot_list, label = 'n = 4')
plt.plot(N_x_8_list, N_8_plot_list, label = 'n = 8')
plt.plot(N_x_16_list, N_16_plot_list, label = 'n = 16')
plt.xlabel('Position along bar (x/L)')
plt.ylabel('Normalized Normal Force Reaction, N(x)')
plt.title('Normalized Normal Force Reaction along bar')
plt.legend()

''' Rate of Convergence Calculation '''

'''    first method'''
N_0_exact = (rho*A*Omega**2)/2*(L**2)
error_1 = np.abs(N_0_exact - N_1_list[0])
error_2 = np.abs(N_0_exact - N_2_list[0])
fraction = error_1/error_2
Rate = math.log(fraction,2)

'''    second method'''
N_0_estimate = [0.0] * len(dx)
def N_estimate(U_list,dx):
    estimate = A*E*(U_list[1]/dx) + ((rho*A*Omega**2)*(dx**2))/6
    return estimate

N_0_estimate[0] = N_estimate(U_1_list, dx[0])
N_0_estimate[1] = N_estimate(U_2_list, dx[1])
N_0_estimate[2] = N_estimate(U_4_list, dx[2])
N_0_estimate[3] = N_estimate(U_8_list, dx[3])
N_0_estimate[4] = N_estimate(U_16_list, dx[4])

###############################################################################
''' Part 2 '''

'Variables'
rho = 1
Omega = 1
E = 1
A = 1
L = 1
dx = [L, L/2, L/4, L/8, L/16]
n_list = [1, 2, 4, 8, 16]
M = rho*L*A*0.5
P = M*Omega**2*L
M_x = L

''' Find U vector '''
# Function to Find U vector by finding K matrix and F vector
def U_vector_2(n):
    dx = L/n
    x_list = np.linspace(0,L,n+1)
    x_i = L*x_list
    #print('x_i = ', x_i)
    K = np.zeros((n,n))
    multiplier = (rho*Omega**2*dx**2)/(6*E)
    F_i = np.zeros((n,1))
    # Finding K matrix
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j and i != n: 
                K[i-1][j-1] = 2
            elif np.abs(i-j) == 1:
                K[i-1][j-1] = -1
            elif np.abs(i-j) > 1:
                K[i-1][j-1] = 0
            elif i == j and i == n:
                K[i-1][j-1] = 1
    # Finding F vector
    for i in range(0, n + 1):
        if i == 0:
            F_i[i-1] = 0
        elif i < n and i != 0:
            F_i[i-1] = f(x_i[i-1]) + 4*f(x_i[i]) + f(x_i[i+1])
        elif i == n:
            F_i[i-1] = f(x_i[i-1]) + 2*f(x_i[i])

    # Correction Vector for F
    vP = np.zeros((n,1))
    delta = (M_x % dx)
    index = int((M_x - delta)/dx)
    if index == 1:
        vP[0][0] = ((delta + 1) / dx) * P
    else:
        vP[index - 1][0] = (1 - (delta/dx)) * P
        vP[index - 2][0] = (delta/dx) * P
    F_i = F_i *multiplier
    F_i = F_i + vP
    U = np.linalg.solve(K,F_i)
    print('U = ', U)
    return U
    


# Function to convert U vector matrix to list
def U_vector_convert(U_vect):
    U_list = []
    for row in range(len(U_vect)):
        U_list.append(U_vect[row][0])
    U_list.insert(0, 0.0)
    return U_list

U_1_list = U_vector_convert(U_vector_2(1))
U_2_list = U_vector_convert(U_vector_2(2))
U_4_list = U_vector_convert(U_vector_2(4))
U_8_list = U_vector_convert(U_vector_2(8))
U_16_list = U_vector_convert(U_vector_2(16))

# finding N vector 
N_1_list = N_vector(U_1_list,1,dx[0])
N_2_list = N_vector(U_2_list,2,dx[1])
N_4_list = N_vector(U_4_list,4,dx[2])
N_8_list = N_vector(U_8_list,8,dx[3])
N_16_list = N_vector(U_16_list,16,dx[4])

# plotting reaction N
N_x_1_list, N_1_plot_list = N_plot(N_1_list, x_1_list, n_list[0])
N_x_2_list, N_2_plot_list = N_plot(N_2_list, x_2_list, n_list[1])
N_x_4_list, N_4_plot_list = N_plot(N_4_list, x_4_list, n_list[2])
N_x_8_list, N_8_plot_list = N_plot(N_8_list, x_8_list, n_list[3])
N_x_16_list, N_16_plot_list = N_plot(N_16_list, x_16_list, n_list[4])

''' Plotting '''

def u_x(x):
    u = ((rho*Omega**2)/E)*(L**2*x - (x**3)/6)
    return u
def N_x(x):
    N = (rho*A*Omega**2)*(L**2 - (x**2)/2)
    return N

# plotting displacement U
x_list = np.linspace(0,L,100)
x_1_list = np.linspace(0,L,n_list[0] + 1)
x_2_list = np.linspace(0,L,n_list[1] + 1)
x_4_list = np.linspace(0,L,n_list[2] + 1)
x_8_list = np.linspace(0,L,n_list[3] + 1)
x_16_list = np.linspace(0,L,n_list[4] + 1)

u_exact_list = []
N_exact_list = []
for point in range(len(x_list)):
    u_exact_list.append(u_x(x_list[point]))
    N_exact_list.append(N_x(x_list[point]))

plt.figure()
plt.plot(x_list,u_exact_list, label = 'exact')
plt.plot(x_1_list,U_1_list, label = 'n = 1')
plt.plot(x_2_list,U_2_list, label = 'n = 2')
plt.plot(x_4_list,U_4_list, label = 'n = 4')
plt.plot(x_8_list,U_8_list, label = 'n = 8')
plt.plot(x_16_list,U_16_list, label = 'n = 16')
plt.xlabel('Position along bar (x/L)')
plt.ylabel('Normalized Horizontal Displacement, u(x)')
plt.title('Normalized Horizontal Displacement along bar with Mass')
plt.legend()

plt.figure()
plt.plot(x_list,N_exact_list, label = 'exact')
plt.plot(N_x_1_list, N_1_plot_list, label = 'n = 1')
plt.plot(N_x_2_list, N_2_plot_list, label = 'n = 2')
plt.plot(N_x_4_list, N_4_plot_list, label = 'n = 4')
plt.plot(N_x_8_list, N_8_plot_list, label = 'n = 8')
plt.plot(N_x_16_list, N_16_plot_list, label = 'n = 16')
plt.xlabel('Position along bar (x/L)')
plt.ylabel('Normalized Normal Force Reaction, N(x)')
plt.title('Normalized Normal Force Reaction along bar with Mass')
plt.legend()


