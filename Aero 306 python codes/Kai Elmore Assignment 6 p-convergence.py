# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Class:        Aero 306
# Section:      500
# Assignment:   HW Assignment 6/Project 
# Date:         12/13/2022
#

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
def Rich(q1,q2,q3):
    extra_val = ((q2**2) - q1 * q3)/((2*q2)-q1-q3)
    return extra_val
def Beta(e1,e2):
    beta_val = np.log(e1/e2)/np.log(2)
    return beta_val
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
    if variable == 'k':
        Leg_k = w1*F_integrand(xi1,psi_m,psi_n,dx,x_mid, i) + w2*F_integrand(xi2,psi_m,psi_n,dx,x_mid, i) + w3*F_integrand(xi3,psi_m,psi_n,dx,x_mid, i)
        return Leg_k
    elif variable == 'f':
        Leg_f = w1*G_integrand(xi1,psi_m,dx,x_mid) + w2*G_integrand(xi2,psi_m,dx,x_mid) + w3*G_integrand(xi3,psi_m,dx,x_mid)
        return Leg_f
def K_L(N,i,m,n):
    nodes = N
    seg = i
    shape1 = m
    shape2 = n
    k1 = Legrendre(nodes,seg,shape1,shape2,'k')
    stiffness = k1 
    return stiffness
def F_L(N,i,m):
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
n_list = [4, 8, 16, 32, 64, 128]


''' Find U vector '''
# Function to Find U vector by finding K matrix and F vector
def U_vector_L(N,applied = 0):
    K_mat = np.zeros((N-1,N-1))
    F_vec = np.zeros((N-1,1))
    for i in range(1,N):
        for j in range(1,N):
            if i == j:
                K_mat[i-1][j-1] = K_L(N,i,2,2) + K_L(N,i+1,1,1)
            elif ((i - j) == 1):
                K_mat[i-1][j-1] = K_L(N,i,2,1)
            elif ((i - j) == -1):
                K_mat[i-1][j-1] = K_L(N,i+1,1,2)
            else:
                K_mat[i-1][j-1] = 0
    for i in range(1,N):
        F_vec[i-1] = F_L(N,i,2) + F_L(N,i+1,1)
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
'----------------------------------------------------------------------------'
"Linear Elements"

print('LINEAR ELEMENTS SECTION')
U_vector_list = []
x_list = []
for i in range(len(n_list)):
    U_vector_list.append(U_vector_convert(U_vector_L(n_list[i],P)))
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
plt.title('Normalized Horizontal Displacement of the Bar under Distributive Load \n(Linear Elements)')
plt.legend()

''' Rate of Convergence '''
print('======================================================================')
print()
def N_0_dd_linear(U_vect,n):
    dx = (pi*L/6)/(n/2)
    N_0 = E_cs*A(0)*((U_vect[1])/dx)
    return N_0
def N_0_we(U_vect,n):
    N_0 = F_L(n,1,1) - K_L(n,1,1,2)*U_vect[1]
    return N_0

N_0_dd_list = []
N_0_we_list = []
U_mid_list = []
result_title = 'Linear element Base Normal Reaction and Midpoint Displacment Value Table'
print(result_title)
print('-'*len(result_title))
result_header = '{}|{:^27}|{:^22}|{:^22}'.format('N Value', 'Direct Differentiation N(0)', 'Weak Equilibrium N(0)', 'U(L/2) value')
print(result_header)
print('-'*len(result_header))
for t in range(len(n_list)):
    mid = int(n_list[t]/2)
    dd = N_0_dd_linear(U_vector_list[t],n_list[t])
    we = N_0_we(U_vector_list[t],n_list[t])
    N_0_dd_list.append(dd)   
    N_0_we_list.append(we)
    U_mid_list.append(U_vector_list[t][mid])
    print('n = {:^3}|{:^27}|{:^22}|{:^22}'.format(n_list[t],dd,we,U_vector_list[t][mid]))

# Calculating the Extrapolated value of N(0) using n = 2,4,and 8
leng = len(N_0_dd_list)
N_extra_dd = Rich(N_0_dd_list[leng-3], N_0_dd_list[leng-2], N_0_dd_list[leng-1])
N_extra_we = Rich(N_0_we_list[leng-3], N_0_we_list[leng-2], N_0_we_list[leng-1])
U_mid_extra = Rich(U_mid_list[leng-3],U_mid_list[leng-2],U_mid_list[leng-1])
print('---------------------------------------------------------------')
print('The extrapolated value for N(0) using Direct Differentiation is N(0) = ', N_extra_dd)
print('The extrapolated value for N(0) using Weak Equilibrium is N(0) = ', N_extra_we)
print('The extrapolated value for U(L/2) using linear elements is U(L/2) = ', U_mid_extra)
print("======================================================================")
print()
# finding the difference between the calculated values and the exact/extrapolated value
extra_diff_dd_list = []
extra_diff_we_list = []
U_mid_extra_diff_list = []
error_header = '{:^7}|{:^22}|{:^22}|{:^22}'.format('N Value','dd extrapolated error','we extrapolated error','U(L/2) extrapolated error')
error_title = 'Linear Element Extrapolated N(0) and U(L/2) Error Table'
print(error_title)
print('-'*len(error_header))
print(error_header)
print('-'*len(error_header))
for u in range(len(n_list)):
    diff_dd = np.abs(N_extra_dd - N_0_dd_list[u])
    diff_we = np.abs(N_extra_we - N_0_we_list[u])
    diff_U_mid = np.abs(U_mid_extra - U_mid_list[u])
    extra_diff_dd_list.append(diff_dd)
    extra_diff_we_list.append(diff_we)
    U_mid_extra_diff_list.append(diff_U_mid)
    print('n = {:^3}|{:^22}|{:^22}|{:^22}'.format(n_list[u],diff_dd,diff_we,diff_U_mid))

print("======================================================================")
print()
beta_extra_dd_list = []
beta_extra_we_list = []
beta_extra_U_mid_list = []
for i in range(1,len(extra_diff_dd_list)):
    beta_dd = Beta(extra_diff_dd_list[i-1],extra_diff_dd_list[i])
    beta_we = Beta(extra_diff_we_list[i-1],extra_diff_we_list[i])
    beta_U_mid = Beta(U_mid_extra_diff_list[i-1],U_mid_extra_diff_list[i])
    beta_extra_dd_list.append(beta_dd)
    beta_extra_we_list.append(beta_we)
    beta_extra_U_mid_list.append(beta_U_mid)
beta_title = 'Linear element Rate of Convergence (Beta) Values for N(0) & U(L/2)'
print(beta_title)
print('-'*len(beta_title))
beta_header = "{:^18}|{:^22}|{:^22}|{:^22}".format('Beta(n -> n)','DD ROC value','WE ROC value',"U-mid ROC value")
print(beta_header)
print('-'*len(beta_header))
for i in range(1,len(n_list)):
    print('n = {:^3} -> n = {:^3}|{:^22}|{:^22}|{:^22}'.format(n_list[i-1],n_list[i],beta_extra_dd_list[i-1],beta_extra_we_list[i-1],beta_extra_U_mid_list[i-1]))

# Plotting the rate of Convergence
horizontal_list = []
vertical_dd_extra = []
vertical_we_extra = []
vertical_U_mid_extra = []
for e in range(len(n_list)):
    dx = L/(n_list[e])
    x_point = -np.log(dx)
    horizontal_list.append(x_point)
    y_point_1 = np.log(extra_diff_dd_list[e])
    vertical_dd_extra.append(y_point_1)
    y_point_2 = np.log(extra_diff_we_list[e])
    vertical_we_extra.append(y_point_2)
    y_point_3 = np.log(U_mid_extra_diff_list[e])
    vertical_U_mid_extra.append(y_point_3)

plt.figure()
plt.plot(horizontal_list,vertical_dd_extra, label = 'direct differentiation')
plt.plot(horizontal_list,vertical_we_extra, label = 'weak equilibrium')
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
plt.title('Graph of the rate of convergence of Extrapolated N(0) \n(linear elements)')
plt.legend()
plt.figure()
plt.plot(horizontal_list,vertical_U_mid_extra)
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
plt.title('Graph of the error of the displacement at the midpoint \n linear elements')
N_0_dd_list_linear = N_0_dd_list
N_0_we_list_linear = N_0_we_list
U_mid_list_linear = U_mid_list
print('======================================================================')
print()

"Quadratic Elements"
def K_Q(N,i,m,n):
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
def F_Q(N,i,m):
    nodes = N
    seg = i
    shape = m
    f1 = Legrendre(nodes,seg,shape,3,'f')
    f2 = Legrendre(nodes,seg,3,3,'f')
    k3 = Legrendre(nodes,seg,shape,3,'k')
    k4 = Legrendre(nodes,seg,3,3,'k')
    Load = f1 - (f2*(k3/k4))
    return Load
def U_vector_Q(N,applied = 0):
    K_mat = np.zeros((N-1,N-1))
    F_vec = np.zeros((N-1,1))
    for i in range(1,N):
        for j in range(1,N):
            if i == j:
                K_mat[i-1][j-1] = K_Q(N,i,2,2) + K_Q(N,i+1,1,1)
            elif ((i - j) == 1):
                K_mat[i-1][j-1] = K_Q(N,i,2,1)
            elif ((i - j) == -1):
                K_mat[i-1][j-1] = K_Q(N,i+1,1,2)
            else:
                K_mat[i-1][j-1] = 0
    for i in range(1,N):
        F_vec[i-1] = F_Q(N,i,2) + F_Q(N,i+1,1)
        if i == (N/4) or i == (3*N/4):
            F_vec[i-1] += applied
    U = np.linalg.solve(K_mat,F_vec)
    return U


print('QUADRATIC ELEMENT SECTION')
U_vector_list = []
x_list = []
for i in range(len(n_list)):
    U_vector_list.append(U_vector_convert(U_vector_Q(n_list[i],P)))
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
plt.title('Normalized Horizontal Displacement of the Bar under Distributive Load \n(Quadratic Elements)')
plt.legend()

''' Rate of Convergence '''
print('======================================================================')
print()

def N_0_dd_Quad(U_vect,n):
    dx = (pi*L/6)/(n/2)
    alpha = (Legrendre(n,1,3,3,'f') - Legrendre(n,1,3,2,'k')*U_vect[1])/Legrendre(n,1,3,3,'k')
    N_0 = E_cs*A(0)*((U_vect[1] + alpha)/dx)
    return N_0

def N_0_we_Quad(U_vect,n):
    N_0 = F_Q(n,1,1) - K_Q(n,1,1,2)*U_vect[1]
    return N_0

N_0_dd_list = []
N_0_we_list = []
U_mid_list = []
result_title = 'Quadratic element Base Normal Reaction and Midpoint Displacment Value Table'
result_header = '{}|{:^22}|{:^22}|{:^22}'.format('N Value', 'dd N(0) value', 'we N(0) value', 'U(L/2) value')
print(result_title)
print('-'*len(result_header))
print(result_header)
print('-'*len(result_header))
for t in range(len(n_list)):
    mid = int(n_list[t]/2)
    dd = N_0_dd_Quad(U_vector_list[t],n_list[t])
    we = N_0_we_Quad(U_vector_list[t],n_list[t])
    U_mid_list.append(U_vector_list[t][mid])
    N_0_dd_list.append(dd)   
    N_0_we_list.append(we)
    print('n = {:^3}|{:^22}|{:^22}|{:^22}'.format(n_list[t],dd,we,U_vector_list[t][mid]))

# Calculating the Extrapolated value of N(0) using n = 2,4,and 8
leng = len(N_0_dd_list)
N_extra_dd = Rich(N_0_dd_list[leng-3], N_0_dd_list[leng-2], N_0_dd_list[leng-1])
N_extra_we = Rich(N_0_we_list[leng-3], N_0_we_list[leng-2], N_0_we_list[leng-1])
U_mid_extra = Rich(U_mid_list[leng-3],U_mid_list[leng-2],U_mid_list[leng-1])
print('---------------------------------------------------------------')
print('The extrapolated value for N(0) using Direct Differentiation is N(0) = ', N_extra_dd)
print('The extrapolated value for N(0) using Weak Equilibrium is N(0) = ', N_extra_we)
print('The extrapolated value for U(L/2) using quadratic elements is U(L/2) = ', U_mid_extra)
print("=======================================================================")
print()
# finding the difference between the calculated values and the exact/extrapolated value
extra_diff_dd_list = []
extra_diff_we_list = []
U_mid_extra_diff_list = []
error_title = 'Quadratic Element Extrapolated N(0) and U(L/2) Error Table'
error_header = '{:^7}|{:^22}|{:^22}|{:^22}'.format('N Value','dd extrapolated error','we extrapolated error','U(L/2) extrapolated error')
print(error_title)
print('-'*len(error_header))
print(error_header)
print('-'*len(error_header))
for u in range(len(n_list)):
    diff_dd = np.abs(N_extra_dd - N_0_dd_list[u])
    diff_we = np.abs(N_extra_we - N_0_we_list[u])
    diff_U_mid = np.abs(U_mid_extra - U_mid_list[u])
    extra_diff_dd_list.append(diff_dd)
    extra_diff_we_list.append(diff_we)
    U_mid_extra_diff_list.append(diff_U_mid)
    print('n = {:^3}|{:^22}|{:^22}|{:^22}'.format(n_list[u],diff_dd,diff_we,diff_U_mid))

print("=======================================================================")
print()
beta_extra_dd_list = []
beta_extra_we_list = []
beta_extra_U_mid_list = []
for i in range(1,len(extra_diff_dd_list)):
    beta_dd = Beta(extra_diff_dd_list[i-1],extra_diff_dd_list[i])
    beta_we = Beta(extra_diff_we_list[i-1],extra_diff_we_list[i])
    beta_U_mid = Beta(U_mid_extra_diff_list[i-1],U_mid_extra_diff_list[i])
    beta_extra_dd_list.append(beta_dd)
    beta_extra_we_list.append(beta_we)
    beta_extra_U_mid_list.append(beta_U_mid)
beta_title = 'Quadratic element Rate of Convergence (Beta) Values for N(0) & U(L/2)'
beta_header = "{:^18}|{:^22}|{:^22}|{:^22}".format('Beta(n -> n)','DD ROC value','WE ROC value','U-mid ROC value')
print(beta_title)
print('-'*len(beta_header))
print(beta_header)
print('-'*len(beta_header))
for i in range(1,len(n_list)):
    print('n = {:^3} -> n = {:^3}|{:^22}|{:^22}|{:^22}'.format(n_list[i-1],n_list[i],beta_extra_dd_list[i-1],beta_extra_we_list[i-1],beta_extra_U_mid_list[i-1]))

# Plotting the rate of Convergence
horizontal_list = []
vertical_dd_extra = []
vertical_we_extra = []
vertical_U_mid_extra = []
for e in range(len(n_list)):
    dx = L/(n_list[e])
    x_point = -np.log(dx)
    horizontal_list.append(x_point)
    y_point_2 = np.log(extra_diff_dd_list[e])
    vertical_dd_extra.append(y_point_2)
    y_point_2 = np.log(extra_diff_we_list[e])
    vertical_we_extra.append(y_point_2)
    y_point_3 = np.log(U_mid_extra_diff_list[e])
    vertical_U_mid_extra.append(y_point_3)
    
plt.figure()
plt.plot(horizontal_list,vertical_dd_extra, label = 'direct differentiation')
plt.plot(horizontal_list,vertical_we_extra, label = 'weak equilibrium')
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
plt.title('Graph of the rate of convergence of Extrapolated N(0) \n(quadratic elements)')
plt.legend()
plt.figure()
plt.plot(horizontal_list,vertical_U_mid_extra)
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
plt.title('Graph of the error of the displacement at the midpoint \n quadratic elements')
N_0_dd_list_quadratic = N_0_dd_list
N_0_we_list_quadratic = N_0_we_list
U_mid_list_quadratic = U_mid_list
print('======================================================================')
print()
def K_C(N,i,m,n):
    nodes = N
    seg = i
    shape1 = m
    shape2 = n
    kmn = Legrendre(nodes,seg,shape1,shape2,'k')
    k34 = Legrendre(nodes,seg,3,4,'k')
    k43 = Legrendre(nodes,seg,4,3,'k')
    k33 = Legrendre(nodes,seg,3,3,'k')
    k44 = Legrendre(nodes,seg,4,4,'k')
    k4n = Legrendre(nodes,seg,4,shape2,'k')
    k3n = Legrendre(nodes,seg,3,shape2,'k')
    diff1 = np.abs(k34*k4n - k44*k3n)
    diff2 = np.abs(k43*k3n - k33*k4n)
    dem = np.abs(k33*k44 - k34*k43)
    km3 = Legrendre(nodes,seg,shape1,3,'k')
    km4 = Legrendre(nodes,seg,shape1,4,'k')
    stiffness = kmn + (km3*diff1 + km4*diff2)/dem
    return stiffness
def F_C(N,i,m):
    nodes = N
    seg = i
    shape = m
    fm = Legrendre(nodes,seg,shape,1,'f')
    f3 = Legrendre(nodes,seg,3,1,'f')
    f4 = Legrendre(nodes,seg,4,1,'f')
    km3 = Legrendre(nodes,seg,shape,3,'k')
    km4 = Legrendre(nodes,seg,shape,4,'k')
    k34 = Legrendre(nodes,seg,3,4,'k')
    k43 = Legrendre(nodes,seg,4,3,'k')
    k33 = Legrendre(nodes,seg,3,3,'k')
    k44 = Legrendre(nodes,seg,4,4,'k')
    diff1 = np.abs(k44*f3 - k34*f4)
    diff2 = np.abs(k33*f4 - k43*f3)
    dem = np.abs(k33*k44 - k34*k43)
    Load = fm - f3*((km3*diff1 + km4*diff2)/dem)
    return Load
def U_vector(N,applied = 0):
    K_mat = np.zeros((N-1,N-1))
    F_vec = np.zeros((N-1,1))
    for i in range(1,N):
        for j in range(1,N):
            if i == j:
                K_mat[i-1][j-1] = K_C(N,i,2,2) + K_C(N,i+1,1,1)
            elif ((i - j) == 1):
                K_mat[i-1][j-1] = K_C(N,i,2,1)
            elif ((i - j) == -1):
                K_mat[i-1][j-1] = K_C(N,i+1,1,2)
            else:
                K_mat[i-1][j-1] = 0
    for i in range(1,N):
        F_vec[i-1] = F_C(N,i,2) + F_C(N,i+1,1)
        if i == (N/4) or i == (3*N/4):
            F_vec[i-1] += applied
    U = np.linalg.solve(K_mat,F_vec)
    return U

'Cubic Elements'
print('CUBIC ELEMENTS SECTION')
U_vector_list = []
x_list = []
for i in range(len(n_list)):
    U_vector_list.append(U_vector_convert(U_vector(n_list[i],P)))
    x_list.append(x_listfun(n_list[i]))
for w in range(len(U_vector_list)):
    print('U vector list for n = {}:'.format(n_list[w]), U_vector_list[w])
    print()

'''Plotting'''
plt.figure()
for i in range(len(x_list)):
    plt.plot(x_list[i],U_vector_list[i], label = 'n = {}'.format(n_list[i]))
plt.xlabel('x/L')
plt.ylabel('Normalized Horizontal Displacement, u(x/L)')
plt.title('Normalized Horizontal Displacement of the Bar under Distributive Load \n(cubic Elements)')
plt.legend()

'''Rate of Convergence'''
print('=======================================================================')
print()

def N_0_dd_Cubic(U_vect,n):
    dx = (pi*L/6)/(n/2)
    k34 = Legrendre(n,1,3,4,'k')
    k43 = Legrendre(n,1,4,3,'k')
    k33 = Legrendre(n,1,3,3,'k')
    k44 = Legrendre(n,1,4,4,'k')
    k42 = Legrendre(n,1,4,2,'k')
    k32 = Legrendre(n,1,3,2,'k')
    f3 = Legrendre(n,1,3,1,'f')
    f4 = Legrendre(n,1,4,1,'f')
    diff1 = k34*k42 - k44*k32
    diff2 = k43*k32 - k33*k42
    dem = np.abs(k33*k44 - k34*k43)
    a = np.abs((U_vect[1]*diff1 + k44*f3 - k34*f4)/dem)
    b = np.abs((U_vect[1]*diff2 + k33*f4 - k43*f3)/dem)
    N_0 = E_cs*A(0)*((U_vect[1] + a + b)/dx)
    return N_0

def N_0_we_Cubic(U_vect,n):
    N_0 = F_C(n,1,1) - K_C(n,1,1,2)*U_vect[1]
    return N_0

N_0_dd_list = []
N_0_we_list = []
U_mid_list = []
result_title = 'Cubic element Base Normal Reaction and Midpoint Displacment Value Table'
print(result_title)
result_header = '{}|{:^27}|{:^21}|{:^22}'.format('N Value', 'Direct Differentiation N(0)', 'Weak Equilibrium N(0)', 'U(L/2) value')
print('-'*len(result_header))
print(result_header)
print('-'*len(result_header))
for t in range(len(n_list)):
    mid = int(n_list[t]/2)
    dd = N_0_dd_Cubic(U_vector_list[t],n_list[t])
    we = N_0_we_Cubic(U_vector_list[t],n_list[t])
    N_0_dd_list.append(dd)   
    N_0_we_list.append(we)
    U_mid_list.append(U_vector_list[t][mid])
    print('n = {:^3}|{:^27}|{:^21}|{:^22}'.format(n_list[t],dd,we,U_vector_list[t][mid]))


# Calculating the Extrapolated value of N(0) using n = 2,4,and 8
leng = len(N_0_dd_list)
N_extra_dd = Rich(N_0_dd_list[leng-3], N_0_dd_list[leng-2], N_0_dd_list[leng-1])
N_extra_we = Rich(N_0_we_list[leng-3], N_0_we_list[leng-2], N_0_we_list[leng-1])
U_mid_extra = Rich(U_mid_list[leng-3],U_mid_list[leng-2],U_mid_list[leng-1])
print('---------------------------------------------------------------')
print('The extrapolated value for N(0) using Direct Differentiation is N(0) = ', N_extra_dd)
print('The extrapolated value for N(0) using Weak Equilibrium is N(0) = ', N_extra_we)
print('The extrapolated value for U(L/2) using cubic elements is U(L/2) = ', U_mid_extra)
print("======================================================================")
print()
# finding the difference between the calculated values and the exact/extrapolated value
extra_diff_dd_list = []
extra_diff_we_list = []
U_mid_extra_diff_list = []
error_title = 'Cubic Element Extrapolated N(0) and U(L/2) Error Table'
error_header = '{:^7}|{:^22}|{:^22}|{:^22}'.format('N Value','dd extrapolated error','we extrapolated error','U(L/2) extrapolated error')
print(error_title)
print('-'*len(error_header))
print(error_header)
print('-'*len(error_header))
for u in range(len(n_list)):
    diff_dd = np.abs(N_extra_dd - N_0_dd_list[u])
    diff_we = np.abs(N_extra_we - N_0_we_list[u])
    diff_U_mid = np.abs(U_mid_extra - U_mid_list[u])
    extra_diff_dd_list.append(diff_dd)
    extra_diff_we_list.append(diff_we)
    U_mid_extra_diff_list.append(diff_U_mid)
    print('n = {:^3}|{:^22}|{:^22}|{:^22}'.format(n_list[u],diff_dd,diff_we,diff_U_mid))
print("=====================================================================")
print()
beta_extra_dd_list = []
beta_extra_we_list = []
beta_extra_U_mid_list = []
for i in range(1,len(extra_diff_dd_list)):
    beta_dd = Beta(extra_diff_dd_list[i-1],extra_diff_dd_list[i])
    beta_we = Beta(extra_diff_we_list[i-1],extra_diff_we_list[i])
    beta_U_mid = Beta(U_mid_extra_diff_list[i-1],U_mid_extra_diff_list[i])
    beta_extra_dd_list.append(beta_dd)
    beta_extra_we_list.append(beta_we)
    beta_extra_U_mid_list.append(beta_U_mid)
beta_title = 'Cubic element Rate of Convergence (Beta) Values for N(0) & U(L/2)'
beta_header = "{:^18}|{:^22}|{:^22}|{:^22}".format('Beta(n -> n)','DD ROC value','WE ROC value','U-mid ROC value')
print(beta_title)
print('-'*len(error_header))
print(beta_header)
print('-'*len(error_header))
for i in range(1,len(n_list)):
    print('n = {:^3} -> n = {:^3}|{:^22}|{:^22}|{:^22}'.format(n_list[i-1],n_list[i],beta_extra_dd_list[i-1],beta_extra_we_list[i-1],beta_extra_U_mid_list[i-1]))

# Plotting the rate of Convergence
horizontal_list = []
vertical_dd_extra = []
vertical_we_extra = []
vertical_U_mid_extra = []
for e in range(len(n_list)):
    dx = L/(n_list[e])
    x_point = -np.log(dx)
    horizontal_list.append(x_point)
    y_point_1 = np.log(extra_diff_dd_list[e])
    vertical_dd_extra.append(y_point_1)
    y_point_2 = np.log(extra_diff_we_list[e])
    vertical_we_extra.append(y_point_2)
    y_point_3 = np.log(U_mid_extra_diff_list[e])
    vertical_U_mid_extra.append(y_point_3)

plt.figure()
plt.plot(horizontal_list,vertical_dd_extra, label = 'direct differentiation')
plt.plot(horizontal_list,vertical_we_extra, label = 'weak equilibrium')
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
plt.title('Graph of the rate of convergence of Extrapolated N(0) \n(cubic elements)')
plt.legend()
plt.figure()
plt.plot(horizontal_list,vertical_U_mid_extra)
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
plt.title('Graph of the error of the displacement at the midpoint \n cubic elements')
N_0_dd_list_cubic = N_0_dd_list
N_0_we_list_cubic = N_0_we_list
U_mid_list_cubic = U_mid_list
p_conv_N_0_dd = N_extra_dd
p_conv_N_0_we = N_extra_we
p_conv_U_mid = U_mid_extra
print('======================================================================')
print()

print('P-series convergence, using the extrpolated value with cubic elements as exact')
print('P-series exact direct differentiation N(0) will be N(0) = ', N_extra_dd)
print('P-series exact weak equilibrium N(0) will be N(0) = ', N_extra_we)
print('P-series exact U(L/2) will be U(L/2) = ', U_mid_extra)
print("---------------------------------------------------------------------")
'P series convergence'
extra_diff_dd_list_linear = []
extra_diff_we_list_linear = []
extra_diff_dd_list_quadratic = []
extra_diff_we_list_quadratic = []
extra_diff_dd_list_cubic = []
extra_diff_we_list_cubic = []
element_list = ['Linear', 'Quadratic','Cubic']
extra_diff_dd_list = [extra_diff_dd_list_linear,extra_diff_dd_list_quadratic,extra_diff_dd_list_cubic]
extra_diff_we_list = [extra_diff_we_list_linear,extra_diff_we_list_quadratic,extra_diff_we_list_cubic]
U_mid_extra_diff_list = [[],[],[]]
element_N_dd_list = [N_0_dd_list_linear,N_0_dd_list_quadratic, N_0_dd_list_cubic]
element_N_we_list = [N_0_we_list_linear,N_0_we_list_quadratic, N_0_we_list_cubic]
element_U_mid_list = [U_mid_list_linear,U_mid_list_quadratic,U_mid_list_cubic]
error_header = '{} | {:^22} | {:^22} | {:^22} |'.format('N value','DD extrapolated error','WE extrapolated error','U-mid extrapolated error')
for i in range(3):
    print()
    print('{} elements extrapolated error table'.format(element_list[i]))
    print('-'*len(error_header))
    print(error_header)
    print('-'*len(error_header))
    for u in range(len(n_list)):
        diff_dd = np.abs(p_conv_N_0_dd - element_N_dd_list[i][u])
        diff_we = np.abs(p_conv_N_0_we - element_N_we_list[i][u])
        diff_U_mid = np.abs(p_conv_U_mid - element_U_mid_list[i][u])
        extra_diff_dd_list[i].append(diff_dd)
        extra_diff_we_list[i].append(diff_we)
        U_mid_extra_diff_list[i].append(diff_U_mid)
        print('n = {:^3} | {:^22} | {:^22} | {:^22} |'.format(n_list[u],diff_dd,diff_we,diff_U_mid))

beta_extra_dd_list = [[],[],[]]
beta_extra_we_list = [[],[],[]]
beta_extra_U_mid_list = [[],[],[]]
beta_header = "{:^18} | {:^22} | {:^22} | {:^22} |".format('Beta(n -> n)','DD ROC value','WE ROC value','U-mid ROC value')
for j in range(3):
    print()
    print('{} elements rate of convergence (beta) table'.format(element_list[j]))
    print('-'*len(beta_header))
    print(beta_header)
    print('-'*len(beta_header))
    for i in range(1,len(n_list)):
        beta_dd = Beta(extra_diff_dd_list[j][i-1],extra_diff_dd_list[j][i])
        beta_we = Beta(extra_diff_we_list[j][i-1],extra_diff_we_list[j][i])
        beta_U_mid = Beta(U_mid_extra_diff_list[j][i-1],U_mid_extra_diff_list[j][i])
        beta_extra_dd_list[j].append(beta_dd)
        beta_extra_we_list[j].append(beta_we)
        beta_extra_U_mid_list[j].append(beta_U_mid)
        print('n = {:^3} -> n = {:^3} | {:^22} | {:^22} | {:^22} |'.format(n_list[i-1],n_list[i],beta_extra_dd_list[j][i-1],beta_extra_we_list[j][i-1],beta_extra_U_mid_list[j][i-1]))

vertical_dd_extra = [[],[],[]]
vertical_we_extra = [[],[],[]]
vertical_U_mid_extra = [[],[],[]]
for i in range(3):
    for e in range(len(n_list)):
        y_point_dd = np.log(extra_diff_dd_list[i][e])
        vertical_dd_extra[i].append(y_point_dd)  
        y_point_we = np.log(extra_diff_we_list[i][e])
        vertical_we_extra[i].append(y_point_we)
        y_point_U_mid = np.log(U_mid_extra_diff_list[i][e])
        vertical_U_mid_extra[i].append(y_point_U_mid)
plt.figure()
for i in range(3):
    plt.plot(horizontal_list,vertical_dd_extra[i], label = 'direct differentiation {}'.format(element_list[i]))
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
plt.title('Graph of the rate of convergence of Extrapolated N(0) \n of varius values of p')
plt.legend()

plt.figure()
for i in range(3):
    plt.plot(horizontal_list,vertical_we_extra[i], label = 'weak equilibrium {}'.format(element_list[i]))
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
plt.title('Graph of the rate of convergence of Extrapolated N(0) \n of varius values of p')
plt.legend()

plt.figure()
for i in range(3):
   plt.plot(horizontal_list,vertical_U_mid_extra[i], label = 'weak equilibrium {}'.format(element_list[i]))
plt.xlabel('-log(dx)')
plt.ylabel('log(|error|)')
plt.title('Graph of the rate of convergence of Extrapolated U(L/2) \n of varius values of p')
plt.legend() 
