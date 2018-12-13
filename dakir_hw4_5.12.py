#Lamiaa Dakir Ex 5.12
from __future__ import division, print_function 
from gaussxw import gaussxw
from math import pi, tan, cos
from numpy import exp


#Defining the function I want to integrate
def f(x):
	return x**3/((1-x)**5*(exp(x/(1-x))-1))
	
#Defining the Gaussian quadrature rule to evaluate an integral
def integrate(f,a,b,N):
	x,w = gaussxw(N)
	xp = 0.5*(b-a)*x +0.5*(b+a)
	wp = 0.5*(b-a)*w
	s=0
	for k in range (N):
		s+= wp[k]*f(xp[k])
	return s
	
#Defining the constants
B= 1.38*(10**(-23))
hbar= 1.054*(10**(-34))
c= 3*(10**8)

#Finding the Stefan-Boltzmann constant
sigma= B**4*integrate(f,0,1,100)/(4*pi**2*c**2*hbar**3)

print (sigma)