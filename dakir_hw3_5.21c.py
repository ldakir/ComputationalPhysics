from __future__ import division
from math import pi, sqrt,sin
from pylab import imshow, show, hsv,hot, jet
from numpy import empty,meshgrid,arange, mgrid, transpose, fromfunction, vectorize
import matplotlib.pyplot as plt


q0=  100
L= 10
k=89875.52



def sigma(x,y):
	return q0*sin(2*pi*x/L)*sin(2*pi*y/L)	
sigma_v= vectorize(sigma)	
Sigmas= fromfunction(sigma_v,(100,100))
plt.pcolor(Sigmas)
plt.show()

#Defining the Gaussian quadrature rule to evaluate an integral
N=100
x,w = gaussxw(N)
def integrate1(f,y,a,b):
	xp = 0.5*(b-a)*x +0.5*(b+a)
	wp = 0.5*(b-a)*w
	s=0
	for k in range (N):
		s+= wp[k]*f(xp[k],y)
	return s
	
def integrate2(f,a,b):
	xp = 0.5*(b-a)*x +0.5*(b+a)
	wp = 0.5*(b-a)*w
	s=0
	for k in range (N):
		s+= wp[k]*f(xp[k])
	return s
	

def S(y,x0):
	return integrate1(sigma,y,x0,x0+L)

def pot(x,y,x0,y0):
	r= sqrt(x**2 + y**2)
	return integrate2(S,y0,y0+L)*k/r
	

	
	
	

	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	