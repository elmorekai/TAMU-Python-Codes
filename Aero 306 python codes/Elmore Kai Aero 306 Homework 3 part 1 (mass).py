#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Class:        Aero 306
# Section:      500
# Team:         N/A
# Assignment:   HW 3 Part 2
# Date:         10/21/22
#

#Goal: Use the finite element method to find the displacement of a rotating slender
#      bar undergoing centripetal force using a non-uniform mesh and linear elements,
#      with a concentrated mass at x = pi*L/6

import numpy as np
import math as math
import matplotlib.pyplot as plt
def A(x):
    return A_0 * (1 - (x/L)) + A_L*(x/L)
def f(x):
    return rho*x*A(x)*Omega**2
def x_listfun(n):
    x_lis = []
    mid = pi*L/6
    step = int(n/2)
    lis_1 = np.linspace(0,mid,step + 1)
    lis_2 = np.linspace(mid,L,step + 1)
    for i in range(len(lis_1)):
        x_lis.append(lis_1[i])
    for z in range(1,len(lis_2)):
        x_lis.append(lis_2[z])
    return x_lis


'Variables'
rho = 1
Omega = 1
E = 1
pi = math.pi
A_0 = 1
A_L = (5/9)*A_0
L = 1
P = (rho*A_0*L**2*pi*Omega**2)/24
dx_1 = [(pi*L/6),(pi*L/6)/2, (pi*L/6)/4, (pi*L/6)/8 ]
dx_2 = [(L - (pi*L/6)), (L - (pi*L/6))/2, (L - (pi*L/6))/4, (L - (pi*L/6))/8 ]
n_list = [2, 4, 8, 16]

''' Find U vector '''
# Function to Find U vector by finding K matrix and F vector
def U_vector(n):
    dx_1 = (pi*L/6)/(n/2)
    dx_2 = (L - (pi*L/6))/(n/2)
    nodes = x_listfun(n)
    x_i = L*nodes
    K = np.zeros((n-1,n-1))
    f_i = np.zeros((n-1,1))
    for i in range(1,n):
        if i == (n/2):
            k_mul_1 = E/dx_1
            k_mul_2 = E/dx_2
            dx1 = dx_1
            dx2 = dx_2
        elif i < (n/2):
            k_mul_1 = E/dx_1
            k_mul_2 = E/dx_1
            dx1 = dx_1
            dx2 = dx_1
        elif i > (n/2):
            k_mul_1 = E/dx_2
            k_mul_2 = E/dx_2
            dx1 = dx_2
            dx2 = dx_2
        for j in range(1,n):
            if i == j:
                K[i-1][j-1] = k_mul_1*(A(x_i[i]-0.5*dx1)) + k_mul_2*(A(x_i[i+1]-0.5*dx2))
            elif ((i - j) == 1):
                K[i-1][j-1] = k_mul_1*(-A(x_i[i] - 0.5*dx1))
            elif ((i - j) == -1):
                K[i-1][j-1] = k_mul_2*(-A(x_i[i+1] - 0.5*dx2))
            else:
                K[i-1][j-1] = 0
        
    for i in range(1, n):
        if i == (n/2):
            f_mul_1 = dx_1/6
            f_mul_2 = dx_2/6
        elif i < (n/2):
            f_mul_1 = dx_1/6
            f_mul_2 = dx_1/6
        elif i > (n/2):
            f_mul_1 = dx_2/6
            f_mul_2 = dx_2/6
        
        f_el_i_2 = f_mul_1*(f(x_i[i-1])+ 2*f(x_i[i]))
        f_el_iplus_1 = f_mul_2*(2*f(x_i[i]) + f(x_i[i+1]))
        
        if i == (n/2):
            f_i[i-1] = f_el_i_2 + f_el_iplus_1 + P
        else:
            f_i[i-1] = f_el_i_2 + f_el_iplus_1 
    U = np.linalg.solve(K,f_i)
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
t = [U_2_list, U_4_list,U_8_list,U_16_list]

for i in range(4):
    print('U vector for n =',n_list[i],' the vector is:',t[i])
    print()

''' Find rate of convergence '''
N_0_exact = (pi/24) +(108*pi*np.log(np.abs(27/(2*pi-27)))+2187*np.log(5/9)+1060)/(2592*np.log(5/9))

def N_0_cal_dd(U_list,n):
    dx = (pi*L/6)/(n/2)
    N_0 = E*A(0)*U_list[1]/dx
    error = np.abs(N_0_exact - N_0)
    return N_0, error

def N_0_cal_wd(U_list,n):
    nodes = x_listfun(n)
    x_i = L*nodes
    dx = (pi*L/6)/(n/2)
    f_1 = (dx/6)*(2*f(x_i[0])+ f(x_i[1]))
    k_1 = (E*A(x_i[1]-0.5*dx)*U_list[1])/dx
    N_0 = f_1 + k_1
    error = np.abs(N_0_exact - N_0)
    return N_0, error

# Direct differentiation
N_0_dd_2, error_dd_2 = N_0_cal_dd(U_2_list,2)
N_0_dd_4, error_dd_4 = N_0_cal_dd(U_4_list,4)
N_0_dd_8, error_dd_8 = N_0_cal_dd(U_8_list,8)
N_0_dd_16, error_dd_16 = N_0_cal_dd(U_16_list,16)

e = [N_0_dd_2, N_0_dd_4, N_0_dd_8, N_0_dd_16]
# Weak differentiation
N_0_wd_2, error_wd_2 = N_0_cal_wd(U_2_list,2)
N_0_wd_4, error_wd_4 = N_0_cal_wd(U_4_list,4)
N_0_wd_8, error_wd_8 = N_0_cal_wd(U_8_list,8)
N_0_wd_16, error_wd_16 = N_0_cal_wd(U_16_list,16)

w = [N_0_wd_2, N_0_wd_4, N_0_wd_8, N_0_wd_16]
# rate of convergence calculation 
def B(e1, e2):
    rate = np.log(e1/e2)/np.log(2)
    return rate
B_dd_2_4 = B(error_dd_2, error_dd_4)
B_dd_4_8 = B(error_dd_4, error_dd_8)
B_dd_8_16 = B(error_dd_8, error_dd_16)
B_wd_2_4 = B(error_wd_2, error_wd_4)
B_wd_4_8 = B(error_wd_4, error_wd_8)
B_wd_8_16 = B(error_wd_8, error_wd_16)

b = [B_dd_2_4, B_dd_4_8, B_dd_8_16, B_wd_2_4, B_wd_4_8, B_wd_8_16]

print('The exact value (strong formulation) for N(0) =',N_0_exact)
print()

for i in range(4):
    print('The Calculated Normal force at the root with direct differentiation \
for n = ',n_list[i],' is N(0) =', e[i] )
    print()
for i in range(4):
    print('The Calculated Normal force at the root with weak equilibrium \
for n = ',n_list[i],' is N(0) =', w[i] )
    print()
for i in range(3):
    print('The rate of convergence from n =', n_list[i],'to n =',n_list[i+1],'for direct differentiaiton is B =',b[i])
    print('The rate of convergence from n =', n_list[i],'to n =',n_list[i+1],'for weak equilibrium is B =',b[i+3])
''' Plotting '''

def u_x(x):
    if x <= pi/6:
        C = (pi/24) +(108*pi*np.log(np.abs(27/(2*pi-27)))+2187*np.log(5/9)+1060)/(2592*np.log(5/9))
        D = (np.log(9)*(2592*C-2187))/1152
    else:
        C = (108*pi*np.log(np.abs(27/(2*pi-27)))+2187*np.log(5/9)+1060)/(2592*np.log(5/9))
        D = -(1060+np.log(5)*(2187-2592*C))/1152
    p1 = -(128*x**3-216*x**2-972*x-2187*np.log(np.abs(4*x-9)))/1152
    p2 = (2592/1152)*np.log(np.abs(4*x-9))
    u = p1 - p2*C + D
    
    return u

x_list = np.linspace(0,L,100)
x_2_list = x_listfun(n_list[0])
x_4_list = x_listfun(n_list[1])
x_8_list = x_listfun(n_list[2])
x_16_list = x_listfun(n_list[3])

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

print('----------------------------------------------------------------')

''' Middle Nodal Displacement Error '''
U_mid_exact = u_x((pi/6))
print('The exact value of the displacement at the middle node is U = ', U_mid_exact)
print()
U_mid_list = []
U_mid_error_list = []
for w in range(len(n_list)):
    node = n_list[w]/2
    exprox_node = t[w][int(node)]
    error = U_mid_exact - exprox_node
    U_mid_list.append(exprox_node)
    U_mid_error_list.append(error)
for y in range(len(U_mid_error_list)):
    print('The error of the calculated displacement at the middle node when n = {} is U = {}'.format(n_list[y],U_mid_error_list[y]))
print()
for j in range(len(U_mid_list)):
    print('The calculated displacement at the middle node when n = {} is U = {}'.format(n_list[j],U_mid_list[j]))












