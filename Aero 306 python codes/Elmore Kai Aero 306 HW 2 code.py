# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Class:        Aero 306
# Section:      500
# Team:         N/A
# Assignment:   HW 2
# Date:         10/1/22
#

#Goal: Use the finite element method to find the displacement of a rotating slender
#      bar undergoing centripetal force
#

import numpy as np
import math as math
import matplotlib.pyplot as plt
def A(x):
    return A_0 * (1 - (x/L)) + A_L*(x/L)
def f(x):
    return rho*x*A(x)*Omega**2


'Variables'
rho = 1
Omega = 1
E = 1
A_0 = 1
A_L = (5/9)*A_0
L = 1
dx = [L/2, L/4, L/8, L/16]
n_list = [2, 4, 8, 16]

''' Find U vector '''
# Function to Find U vector by finding K matrix and F vector
def U_vector(n):
    dx = L/n
    x_list = np.linspace(0,L,n+1)
    x_i = L*x_list
    K_mul = E/dx
    F_mul = dx/6
    K = np.zeros((n-1,n-1))
    F_i = np.zeros((n-1,1))
    for i in range(1,n):
        for j in range(1,n):
            if i == j:
                K[i-1][j-1] = K_mul*(A(x_i[i]-0.5*dx) + A(x_i[i]+0.5*dx))
            elif ((i - j) == 1):
                K[i-1][j-1] = K_mul*(-A(x_i[i] - 0.5*dx))
            elif ((i - j) == -1):
                K[i-1][j-1] = K_mul*(-A(x_i[i] + 0.5*dx))
            else:
                K[i-1][j-1] = 0

    for i in range(1, n):
        if i == 0:
            F_i[i-1] = F_mul*(2*f(x_i[i]) + f(x_i[i+1]))
        elif i > 0 and i < n:
            F_i[i-1] = F_mul*(f(x_i[i-1]) + 4*f(x_i[i]) + f(x_i[i+1]))
        elif i == n:
            F_i[i-1] = F_mul*(f(x_i[i-1]) + 2*f(x_i[i]))
    U = np.linalg.solve(K,F_i)

    return U


# Function to convert U vector matrix to list
def U_vector_convert(U_vect):
    U_list = []
    for row in range(len(U_vect)):
        U_list.append(U_vect[row][0])
    U_list.insert(0, 0.0)
    U_list.append(0.0)
    return U_list

U_2_list = U_vector_convert(U_vector(2))
U_4_list = U_vector_convert(U_vector(4))
U_8_list = U_vector_convert(U_vector(8))
U_16_list = U_vector_convert(U_vector(16))


''' Finding N(0) values '''
N_0_exact = (1060 + 2187*np.log(5/9))/(2592*np.log(5/9))
# Weak Formulation
def N_value(U_list, n):
    dx = L/n
    x_list = np.linspace(0,L,n+1)
    x_i = L*x_list
    F = (f(x_i[1])*dx)/6
    K = (E*U_list[1]*A(x_i[0]+0.5*dx))/dx
    N = F + K
    return N
N_0_we2 = N_value(U_2_list,2)
N_0_we4 = N_value(U_4_list,4)
N_0_we8 = N_value(U_8_list,8)
N_0_we16 = N_value(U_16_list,16)
N_0_exact = (1060 + 2187*np.log(5/9))/(2592*np.log(5/9))
Q1 = N_0_we2
Q1_2 = N_0_we4
Q1_4 = N_0_we8
N_0_extra_we = (Q1_2**2 - (Q1 * Q1_4))/(2*Q1_2 - Q1 - Q1_4)

# Direct Differentiation
def N_value_d(U_list,n):
    dx = L/n
    N = (A_0*E*U_list[1])/dx
    return N
N_0_dd2 = N_value_d(U_2_list,2)
N_0_dd4 = N_value_d(U_4_list,4)
N_0_dd8 = N_value_d(U_8_list,8)
N_0_dd16 = N_value_d(U_16_list,16)
Q1 = N_0_dd2
Q1_2 = N_0_dd4
Q1_4 = N_0_dd8
N_0_extra_dd = (Q1_2**2 - (Q1 * Q1_4))/(2*Q1_2 - Q1 - Q1_4)


''' Rate of Convergence of N(0)'''
# Variables and setting up graph axes
Q_ref_ex = N_0_exact
Q_ref_ext_dd = N_0_extra_dd
Q_ref_ext_we = N_0_extra_we
dx_list = [L/2, L/4, L/8, L/16]
hor_list = []
ver_list_dd_ex = []
ver_list_we_ex = []
ver_list_dd_ext = []
ver_list_we_ext = []
dd_list = [N_0_dd2,N_0_dd4,N_0_dd8,N_0_dd16]
we_list = [N_0_we2,N_0_we4,N_0_we8,N_0_we16]
for i in range(len(dx_list)):
    point = -np.log(dx_list[i])
    hor_list.append(point)
    dd_point_ex = np.log(np.abs(Q_ref_ex - dd_list[i]))
    we_point_ex = np.log(np.abs(Q_ref_ex - we_list[i]))
    dd_point_ext = np.log(np.abs(Q_ref_ext_dd - dd_list[i]))
    we_point_ext = np.log(np.abs(Q_ref_ext_we - we_list[i]))
    ver_list_dd_ex.append(dd_point_ex)
    ver_list_we_ex.append(we_point_ex)
    ver_list_dd_ext.append(dd_point_ext)
    ver_list_we_ext.append(we_point_ext)
    
# Plotting Rate of Convergence

plt.figure()
plt.plot(hor_list,ver_list_dd_ex, label = 'Based on the exact')
plt.plot(hor_list,ver_list_dd_ext, label = 'Based on the extrapolated')
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
plt.title('Rate of Convergence for the Root Reaction of the Bar under Centrifugal Load - Direct Differentiation')
plt.figure()
plt.plot(hor_list,ver_list_we_ex, label = 'Based on the exact')
plt.plot(hor_list,ver_list_we_ext, label = 'Based on the extrapolated')
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
plt.title('Rate of Convergence for the Root Reaction of the Bar under Centrifugal Load - Weak Formulation')

# Rate of Convergence Calculation

B_dd_ext = np.log((N_0_extra_dd - N_0_dd2)/(N_0_extra_dd - N_0_dd4))/np.log(2)
B_we_ext = np.log((N_0_extra_we - N_0_we2)/(N_0_extra_we - N_0_we4))/np.log(2)
B_dd_ex = np.log((N_0_exact - N_0_dd2)/(N_0_exact - N_0_dd4))/np.log(2)
B_we_ex = np.log((N_0_exact - N_0_we2)/(N_0_exact - N_0_we4))/np.log(2)


''' Plotting '''

def u_x(x):
    C = (1060 + 2187*np.log(5/9))/(2592*np.log(5/9))
    D = (((2592*C - 2187)*np.log(9))/1152)
    p1 = -(128*x**3-216*x**2-972*x-2187*np.log(np.abs(4*x-9)))/1152
    p2 = (2592/1152)*np.log(np.abs(4*x-9))
    u = p1 - p2*C + D
    
    return u
x_list = np.linspace(0,L,100)
x_2_list = np.linspace(0,L,n_list[0] + 1)
x_4_list = np.linspace(0,L,n_list[1] + 1)
x_8_list = np.linspace(0,L,n_list[2] + 1)
x_16_list = np.linspace(0,L,n_list[3] + 1)

u_exact_list = []
for point in range(len(x_list)):
    u_exact_list.append(u_x(x_list[point]))


plt.figure()

plt.plot(x_list,u_exact_list, label = 'exact')
plt.plot(x_2_list,U_2_list, label = 'n = 2')
plt.plot(x_4_list,U_4_list, label = 'n = 4')
plt.plot(x_8_list,U_8_list, label = 'n = 8')
plt.plot(x_16_list,U_16_list, label = 'n = 16')
plt.xlabel('x/L')
plt.ylabel('Normalized Horizontal Displacement, u(x/L)')
plt.title('Normalized Horizontal Displacement of the Bar under Centifugal Load')
plt.legend()