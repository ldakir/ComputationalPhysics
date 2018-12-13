from __future__ import division, print_function
from numpy import exp
from math import sqrt, log, fabs
import matplotlib.pyplot as plt

"""
Lagrange Points

"""

#Setting the values of the parameters

G= 6.674* 10**(-11) #m^3 kg^(-1) s^(-2)
M= 5.974* 10**(24) #kg
m= 7.348 * 10**(22) #kg
R= 3.844* (10**8) #m
w= 2.662*10**(-6) #s^(-1)

#Defining the quintic equation
def f(r):
	return G*M/(r**2)- G*m/((R-r)**2)-(w**2)*r
	
#Defining the derivative of the quintic equation
def f_prime(r):
	h=0.01
	return (f(r+h)-f(r-h))/(2*h)

#Defining Newton's method to solve the nonlinear equation	
accuracy= 10**(-7)
def solution(f):
	r=10**8 #initial guess
	delta= 1
	while fabs(delta)> accuracy:
		delta= f(r)/f_prime(r)
		r-= delta
	return r

	
print('The distance r from Earth to the L1 point is ' + str(solution(f)*10**(-3)) +' km' )