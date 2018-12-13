#Lamiaa Dakir Ex6.4
from __future__ import division, print_function
from numpy import array
from numpy.linalg import inv,solve

"""
Resistor Network

"""

#Defining the matrix to solve the resistor network 

A = array([[ 4,  -1,  -1,  -1 ],
           [ -1,  0, 3, -1 ],
           [ -1, -1,  -1,  4 ],
           [ -1, 3,  0,  -1 ]], float)
v = array([ 5, 5, 0, 0 ],float) 

#Finding  and printing the values of V1, V2, V3 and V4
Vn=solve(A,v)

for n in range(4):
	print( 'V'+ str(n),'=', Vn[n])
	



