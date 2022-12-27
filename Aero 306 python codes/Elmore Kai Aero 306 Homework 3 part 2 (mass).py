#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Class:        Aero 306
# Section:      500
# Team:         N/A
# Assignment:   HW 3 Part 2 massless
# Date:         10/21/22
#

#Goal: Use the finite element method to find the displacement of a rotating slender
#      bar undergoing centripetal force using a non-uniform mesh and quadratic elements
#


import numpy as np
import math as math
import matplotlib.pyplot as plt

def A(x): #Function for Area equation
    return A_0 * (1 - (x/L)) + A_L*(x/L)
def f(x): # Function for Force equation
    return rho*x*A(x)*Omega**2
def x_listfun(n): # Function to find x locations across the bar in a list
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
def F_integrand(xi, m, n, delta_x,mid_point):
    psi_prime_list = [-1/2, 1/2, (-1/2)*xi]
    F_hat = E*A(x_psi(xi,delta_x,mid_point))*psi_prime_list[m-1]*psi_prime_list[n-1]*(2/delta_x)
    return F_hat
def G_integrand(xi, m, delta_x,mid_point):
    psi_list = [(1-xi)/2, (1+xi)/2, (1/4)*(1-xi**2)]
    G_hat = f(x_psi(xi,delta_x,mid_point))*psi_list[m-1]*(delta_x/2)
    return G_hat
def x_psi(psi,delta,mid):
    x_psi = (delta/2)*psi + mid
    return x_psi
def Legrendre(n,segment, psi_m, psi_n, variable):
    i = segment
    position = x_listfun(n)
    dx_1 = (pi*L/6)/(n/2)
    dx_2 = (L - (pi*L/6))/(n/2)
    if i <= (n/2):
        dx = dx_1
    else: 
        dx = dx_2
    x_mid = position[i] - 0.5*dx
    w1 = (5/9)
    w2 = (8/9)
    w3 = w1
    xi1 = -math.sqrt(3/5)
    xi2 = 0.0
    xi3 = math.sqrt(3/5)
    Leg_k = w1*F_integrand(xi1,psi_m,psi_n,dx,x_mid) + w2*F_integrand(xi2,psi_m,psi_n,dx,x_mid) + w3*F_integrand(xi3,psi_m,psi_n,dx,x_mid)
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
    k2 = Legrendre(nodes,seg,3,shape2,'k')
    k3 = Legrendre(nodes,seg,shape1,3,'k')
    k4 = Legrendre(nodes,seg,3,3,'k')
    stiffness = k1 - (k2*(k3/k4))
    return stiffness
def F(N,i,m):
    nodes = N
    seg = i
    shape = m
    f1 = Legrendre(nodes,seg,shape,3,'f')
    f2 = Legrendre(nodes,seg,3,3,'f')
    k3 = Legrendre(nodes,seg,shape,3,'k')
    k4 = Legrendre(nodes,seg,3,3,'k')
    Load = f1 - (f2*(k3/k4))
    return Load
    
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
        if i == (N/2):
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

U_2_list = U_vector_convert(U_vector(2,P))
U_4_list = U_vector_convert(U_vector(4,P))
U_8_list = U_vector_convert(U_vector(8,P))
U_16_list = U_vector_convert(U_vector(16,P))
U_vector_list = [U_2_list, U_4_list, U_8_list, U_16_list]
for w in range(len(U_vector_list)):
    print('U vector list for n = {}:'.format(n_list[w]), U_vector_list[w])
    print()

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

''' Rate of Convergence '''
print('---------------------------------------------------------------')
N_0_exact = (pi/24) +(108*pi*np.log(np.abs(27/(2*pi-27)))+2187*np.log(5/9)+1060)/(2592*np.log(5/9))
print('The exact value of N(0) = ',N_0_exact)
print()

def N_0_dd(U_vect,n):
    dx = (pi*L/6)/(n/2)
    alpha = (Legrendre(n,1,3,3,'f') - Legrendre(n,1,3,2,'k')*U_vect[1])/Legrendre(n,1,3,3,'k')
    N_0 = E*A(0)*((U_vect[1] + alpha)/dx)
    return N_0

def N_0_we(U_vect,n):
    N_0 = F(n,1,2) - K(n,1,1,2)*U_vect[1]
    return N_0

N_0_dd_list = []
N_0_we_list = []
for t in range(len(n_list)):
    print('The Value of N(0) using Direct Differentiation when n = {} is N(0) = {}'.format(n_list[t],N_0_dd(U_vector_list[t],n_list[t])))
    N_0_dd_list.append(N_0_dd(U_vector_list[t],n_list[t]))
    print()
    print('The Value of N(0) using Weak Equilibrium when n = {} is N(0) = {}'.format(n_list[t],N_0_we(U_vector_list[t],n_list[t])))
    N_0_we_list.append(N_0_we(U_vector_list[t],n_list[t]))
    print()

# Calculating the Extrapolated value of N(0) using n = 2,4,and 8
N_extra_dd = ((N_0_dd_list[0]*N_0_dd_list[2]) - N_0_dd_list[1]**2)/(N_0_dd_list[0] + N_0_dd_list[2] - 2*N_0_dd_list[1])
N_extra_we = ((N_0_we_list[0]*N_0_we_list[2]) - N_0_we_list[1]**2)/(N_0_we_list[0] + N_0_we_list[2] - 2*N_0_we_list[1])
print('---------------------------------------------------------------')
print('The extrapolated value for N(0) using Direct Differentiation is N(0) = ', N_extra_dd)
print('The extrapolated value for N(0) using Weak Equilibrium is N(0) = ', N_extra_we)
print("---------------------------------------------------------------")

exact_diff_dd_list = []
exact_diff_we_list = []
extra_diff_dd_list = []
extra_diff_we_list = []
for u in range(len(n_list)):
    diff_dd = np.abs(N_0_exact - N_0_dd_list[u])
    diff_we = np.abs(N_0_exact - N_0_we_list[u])
    exact_diff_dd_list.append(diff_dd)
    exact_diff_we_list.append(diff_we)
    print('Direct Differentiation: The difference between the exact N(0) and\
    the calculated N(0) when n = {} is {}.'.format(n_list[u],diff_dd))
    print()
    print('Weak Equilibrium: The difference between the exact N(0) and\
    the calculated N(0) when n = {} is {}.'.format(n_list[u],diff_we))
    print()
    
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

#Finding Rate of Convergence using n = 2 and n = 4
Beta_exact_dd = np.log(exact_diff_dd_list[0]/exact_diff_dd_list[1])/np.log(2)
Beta_extra_dd = np.log(extra_diff_dd_list[0]/extra_diff_dd_list[1])/np.log(2)
Beta_exact_we = np.log(exact_diff_we_list[0]/exact_diff_we_list[1])/np.log(2)
Beta_extra_we = np.log(extra_diff_we_list[0]/extra_diff_we_list[1])/np.log(2)
print('The rate of convergence using direct differentiation to the exact value is B = ', Beta_exact_dd)
print('The rate of convergence using direct differentiation to the extrapolated value is B = ', Beta_extra_dd)
print('The rate of convergence using weak equilibrium to the exact value is B = ', Beta_exact_we)
print('The rate of convergence using weak equilibrium to the extrapolated value is B = ', Beta_extra_we)

# Plotting the rate of Convergence
horizontal_list = []
vertical_dd_exact = []
vertical_dd_extra = []
vertical_we_exact = []
vertical_we_extra = []
for e in range(len(n_list)):
    dx = (pi*L/6)/(n_list[e]/2)
    x_point = -np.log(dx)
    horizontal_list.append(x_point)
    
    y_point_1 = np.log(exact_diff_dd_list[e])
    y_point_2 = np.log(extra_diff_dd_list[e])
    vertical_dd_exact.append(y_point_1)
    vertical_dd_extra.append(y_point_2)
    
    y_point_1 = np.log(exact_diff_we_list[e])
    y_point_2 = np.log(extra_diff_we_list[e])
    vertical_we_exact.append(y_point_1)
    vertical_we_extra.append(y_point_2)

plt.figure()
plt.plot(horizontal_list,vertical_dd_exact,label = 'exact')
plt.plot(horizontal_list,vertical_dd_extra, label = 'extrapolated')
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
plt.title('Graph of the rate of convergence of N(0) using Direct Differentiation')
plt.legend()

plt.figure()
plt.plot(horizontal_list,vertical_we_exact, label = 'exact')
plt.plot(horizontal_list,vertical_we_extra, label = 'extrapolated')
plt.title('Graph of the rate of convergence of N(0) using Weak Equilibrium')
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
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
    exprox_node = U_vector_list[w][int(node)]
    error = U_mid_exact - exprox_node
    U_mid_list.append(exprox_node)
    U_mid_error_list.append(error)
for y in range(len(U_mid_error_list)):
    print('The error of the calculated displacement at the middle node when n = {} is U = {}'.format(n_list[y],U_mid_error_list[y]))
print()
for j in range(len(U_mid_list)):
    print('The calculated displacement at the middle node when n = {} is U = {}'.format(n_list[j],U_mid_list[j]))
