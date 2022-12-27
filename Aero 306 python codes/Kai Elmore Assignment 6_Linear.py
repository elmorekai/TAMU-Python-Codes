# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Class:        Aero 306
# Section:      500
# Team:         N/A
# Assignment:   HW 6
# Date:         12/4/2022

import numpy as np
import math as math
import matplotlib.pyplot as plt
def p(x):
    val = p_0*(x/L)
    return val 
def d(x):
    val = d_0*(1-(x/L)) + (d_0/3)*(x/L)
    return val
def A(x):
    val = (pi*((d(x))**2))/4
    return val
def x_listfun(n): # Function to find x locations across the bar in a list
    x_lis = np.linspace(0,L,n+1)
    x_i_pts = L*x_lis
    return x_i_pts
def psi_list(xi,m):
    if m == 0:
        psi_val = (1-xi)/2
    elif m == 1:
        psi_val = (1+xi)/2
    elif m == 2:
        psi_val = (1/4)*(1-xi**2)
    elif m == 3:
        psi_val = (1/4)*(xi-xi**3)
    return psi_val
def psi_prime_list(xi,m):
    if m == 0:
        psi_val = -1/2
    elif m == 1:
        psi_val = 1/2
    elif m == 2:
        psi_val = (-1/2)*xi
    elif m == 3:
        psi_val = (1/4)*(1 - 3*(xi**2))
    return psi_val
def F_integrand(xi, m, n, delta_x,mid_point, i):
    if i <= 2:
        E = E_cs
    elif i > 2:
        E = E_ss
    F_hat = E*A(x_psi(xi,delta_x,mid_point))*psi_prime_list(xi,m-1)*psi_prime_list(xi,n-1)*(2/delta_x)
    return F_hat
def G_integrand(xi, m, delta_x,mid_point):
    G_hat = p(x_psi(xi,delta_x,mid_point))*psi_list(xi,m-1)*(delta_x/2)
    return G_hat
def x_psi(psi,delta,mid):
    x_psi = (delta/2)*psi + mid
    return x_psi
def Legrendre(n,segment, psi_m, psi_n, variable):
    dx = L/n
    i = segment
    position = x_listfun(n)
    x_mid = position[i] - 0.5*dx
    w1 = (5/9)
    w2 = (8/9)
    w3 = w1
    xi1 = -math.sqrt(3/5)
    xi2 = 0.0
    xi3 = math.sqrt(3/5)
    Leg_k = w1*F_integrand(xi1,psi_m,psi_n,dx,x_mid, i) + w2*F_integrand(xi2,psi_m,psi_n,dx,x_mid, i) + w3*F_integrand(xi3,psi_m,psi_n,dx,x_mid, i)
    Leg_f = w1*G_integrand(xi1,psi_m,dx,x_mid) + w2*G_integrand(xi2,psi_m,dx,x_mid) + w3*G_integrand(xi3,psi_m,dx,x_mid)
    if variable == 'k':
        return Leg_k
    elif variable == 'f':
        return Leg_f
def K(N,i,m,n):
    nodes = N
    seg = i
    shape1 = m
    shape2 = n
    k1 = Legrendre(nodes,seg,shape1,shape2,'k')
    stiffness = k1 
    return stiffness
def F(N,i,m):
    nodes = N
    seg = i
    shape = m
    f1 = Legrendre(nodes,seg,shape,1,'f')
    Load = f1 
    return Load

'Variables'
pi = math.pi
p_0 = 1
d_0 = 1
E_cs = 200*10**9
E_ss = 190*10**9
L = 1
P = p_0*(L/4)
n_list = [4, 8, 16, 32, 64]


''' Find U vector '''
# Function to Find U vector by finding K matrix and F vector
def U_vector(N,applied = 0):
    K_mat = np.zeros((N-1,N-1))
    F_vec = np.zeros((N-1,1))
    for i in range(1,N):
        for j in range(1,N):
            if i == j:
                K_mat[i-1][j-1] = K(N,i,2,2) + K(N,i+1,1,1)
            elif ((i - j) == 1):
                K_mat[i-1][j-1] = K(N,i,2,1)
            elif ((i - j) == -1):
                K_mat[i-1][j-1] = K(N,i+1,1,2)
            else:
                K_mat[i-1][j-1] = 0
    for i in range(1,N):
        F_vec[i-1] = F(N,i,2) + F(N,i+1,1)
        if i == (N/4) or i == (3*N/4):
            F_vec[i-1] += applied
    U = np.linalg.solve(K_mat,F_vec)
    return U

# Function to convert U vector matrix to list
def U_vector_convert(U_vect):
    U_list = []
    for row in range(len(U_vect)):
        U_list.append(U_vect[row][0])
    U_list.insert(0, 0.0)
    U_list.append(0.0)
    return U_list

U_vector_list = []
x_list = []
for i in range(len(n_list)):
    U_vector_list.append(U_vector_convert(U_vector(n_list[i],P)))
    x_list.append(x_listfun(n_list[i]))

for w in range(len(U_vector_list)):
    print('U vector list for n = {}:'.format(n_list[w]), U_vector_list[w])
    print()

''' Plotting '''

plt.figure()
for i in range(len(x_list)):
    plt.plot(x_list[i],U_vector_list[i], label = 'n = {}'.format(n_list[i]))

plt.xlabel('x/L')
plt.ylabel('Normalized Horizontal Displacement, u(x/L)')
plt.title('Normalized Horizontal Displacement of the Bar under Centifugal Load \n(Linear Elements)')
plt.legend()

''' Rate of Convergence '''
print('---------------------------------------------------------------')

def N_0_dd(U_vect,n):
    dx = (pi*L/6)/(n/2)
    #alpha = (Legrendre(n,1,3,3,'f') - Legrendre(n,1,3,2,'k')*U_vect[1])/Legrendre(n,1,3,3,'k')
    N_0 = E_cs*A(0)*((U_vect[1])/dx)
    return N_0

def N_0_we(U_vect,n):
    print('n = ', n,'u1 = ', U_vect[1])
    print('F = ', F(n,1,1))
    print('K = ', K(n,1,1,2))
    N_0 = F(n,1,1) - K(n,1,1,2)*U_vect[1]
    return N_0

N_0_dd_list = []
N_0_we_list = []
for t in range(len(n_list)):
    dd = N_0_dd(U_vector_list[t],n_list[t])
    we = N_0_we(U_vector_list[t],n_list[t])
    print('The Value of N(0) using Direct Differentiation when n = {} is N(0) = {}'.format(n_list[t],dd))
    N_0_dd_list.append(dd)
    print()
    print('The Value of N(0) using Weak Equilibrium when n = {} is N(0) = {}'.format(n_list[t],we))
    N_0_we_list.append(we)
    print()

# Calculating the Extrapolated value of N(0) using n = 2,4,and 8
leng = len(N_0_dd_list)
N_extra_dd = ((N_0_dd_list[leng-3]*N_0_dd_list[leng-1]) - N_0_dd_list[leng-2]**2)/(N_0_dd_list[leng-3] + N_0_dd_list[leng-1] - 2*N_0_dd_list[leng-2])
N_extra_we = ((N_0_we_list[leng-3]*N_0_we_list[leng-1]) - N_0_we_list[leng-2]**2)/(N_0_we_list[leng-3] + N_0_we_list[leng-1] - 2*N_0_we_list[leng-2])
print('---------------------------------------------------------------')
print('The extrapolated value for N(0) using Direct Differentiation is N(0) = ', N_extra_dd)
print('The extrapolated value for N(0) using Weak Equilibrium is N(0) = ', N_extra_we)
print("---------------------------------------------------------------")
# finding the difference between the calculated values and the exact/extrapolated value
extra_diff_dd_list = []
extra_diff_we_list = []
for u in range(len(n_list)):
    diff_dd = np.abs(N_extra_dd - N_0_dd_list[u])
    diff_we = np.abs(N_extra_we - N_0_we_list[u])
    extra_diff_dd_list.append(diff_dd)
    extra_diff_we_list.append(diff_we)
    print('Direct Differentiation: The difference between the extrapolated N(0) and\
    the calculated N(0) when n = {} is {}.'.format(n_list[u],diff_dd))
    print()
    print('Weak Equilibrium: The difference between the extrapolated N(0) and\
    the calculated N(0) when n = {} is {}.'.format(n_list[u],diff_we))
    print()
print("---------------------------------------------------------------")
Beta_extra_dd = np.log(extra_diff_dd_list[0]/extra_diff_dd_list[1])/np.log(2)
Beta_extra_we = np.log(extra_diff_we_list[0]/extra_diff_we_list[1])/np.log(2)
print('The rate of convergence using direct differentiation to the extrapolated value is B = ', Beta_extra_dd)
print('The rate of convergence using weak equilibrium to the extrapolated value is B = ', Beta_extra_we)

# Plotting the rate of Convergence
horizontal_list = []
vertical_dd_extra = []
vertical_we_extra = []
for e in range(len(n_list)):
    dx = L/(n_list[e])
    x_point = -np.log(dx)
    horizontal_list.append(x_point)
    y_point_1 = np.log(extra_diff_dd_list[e])
    vertical_dd_extra.append(y_point_1)
    y_point_2 = np.log(extra_diff_we_list[e])
    vertical_we_extra.append(y_point_2)

plt.figure()
plt.plot(horizontal_list,vertical_dd_extra, label = 'direct differentiation')
plt.plot(horizontal_list,vertical_we_extra, label = 'weak equilibrium')
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
plt.title('Graph of the rate of convergence of Extrapolated N(0) \n(linear elements)')
plt.legend()

print('----------------------------------------------------------------')

