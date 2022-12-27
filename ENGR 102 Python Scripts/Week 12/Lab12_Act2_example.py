# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 12 Activity 2 Example
# Date:         11/9/2020
#

##################################
### Lab 12 Activity 2 Example ###  

#      Thermodynamic Properties of Compressed Water
#    The temperature and property values for P = 5 MPa
# The columns in each sublist contain the following data:
#    Temperature in units of degree C
#    Specific volume (v) in units of m^3⁄kg
#    Specific internal energy (u) in units of kJ/kg
#    Specific enthalpy (h) in units of kJ/kg
#    Specific entropy (s) in units of kJ/(kg∙K)

# A nested list
#   0          1             2             3            4           # column index
#   T          v             u             h            s           # quantity stored
data = [
[	0	, 	0.0009977	, 	0.04	, 	5.03	, 	0.0001	],      # sublist at position 0 in data, that is data[0]
[	20	, 	0.0009996	, 	83.61	, 	88.61	, 	0.2954	],      # sublist at position 1 in data, that is data[1]
[	40	, 	0.0010057	, 	166.92	, 	171.95	, 	0.5705	],      # sublist at position 2 in data, that is data[2]
[	60	, 	0.0010149	, 	250.29	, 	255.36	, 	0.8287	],      # sublist at position 3 in data, that is data[3]
[	80	, 	0.0010267	, 	333.82	, 	338.96	, 	1.0723	],      # etc.
[	100	, 	0.0010410	, 	417.65	, 	422.85	, 	1.3034	],
[	120	, 	0.0010576	, 	501.91	, 	507.19	, 	1.5236	],
[	140	, 	0.0010769	, 	586.8	, 	592.18	, 	1.7344	],
[	160	, 	0.0010988	, 	672.55	, 	678.04	, 	1.9374	],
[	180	, 	0.0011240	, 	759.47	, 	765.09	, 	2.1338	],
[	200	, 	0.0011531	, 	847.92	, 	853.68	, 	2.3251	],
[	220	, 	0.0011868	, 	938.39	, 	944.32	, 	2.5127	],
[	240	, 	0.0012268	, 	1031.6	, 	1037.7	, 	2.6983	],
[	260	, 	0.0012755	, 	1128.5	, 	1134.9	, 	2.8841	]
]

# Linear interpolation: recall Lab 8
# v(T) = v1 + (T – T1)(v2 – v1)/(T2 – T1)
# values(T) = values1 + (T – T1)(values2 – values1)/(T2 – T1)

import numpy as np

data = np.array(data)
print(data[0][0])
print(data[0][1:])
print(data[1][0])
print(data[1][1:])
T = 15 # user input for temp

# write code to find the bounding temp. values T1, T2
# actually, need indices for the rows
ind1 = 0
ind2 = 1

T1 = data[ind1][0]
T2 = data[ind2][0]

values1 = data[ind1][1:]
values2 = data[ind2][1:]

values = values1 + (T - T1)*(values2 - values1)/(T2 - T1)
print(values)



