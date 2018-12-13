from __future__ import division, print_function
from gaussxw import gaussxw, gaussxwab
import matplotlib.pyplot as plt
import numpy as np
from math import log

G= 6.674*(10**(-11))
sigma= 1000/(10*10)

def f(x,y,z):
	return 1/((x**2+y**2+1)**(3/2))

def F(y,z):
	return integrate1(f,y,z,-5/z,y/z)
	
#Defining the gravitational force 
def gf(z):
	return G*sigma*integrate2(F,z,-5/z,5/z)

#Defining the Gaussian quadrature rule to evaluate an integral

x,w = gaussxw(100)
def integrate1(f,y,z,a,b):
	xp = 0.5*(b-a)*x +0.5*(b+a)
	wp = 0.5*(b-a)*w
	s=0
	for k in range (100):
		s+= wp[k]*f(xp[k],y,z)
	return s
	
def integrate2(f,z,a,b):
	xp = 0.5*(b-a)*x +0.5*(b+a)
	wp = 0.5*(b-a)*w
	s=0
	for k in range (100):
		s+= wp[k]*f(xp[k],z)
	return s
	
#Computing the gravitational force for values of z from 0 to 10

#Defining the function f(x)    

zvals=[] #Array of z values 
gfvals=[] #Array of gravitational forces


for z in np.arange(0.1,10,0.05):
	zvals.append(z)
	gfvals.append(gf(z))
	
#Plotting the gravitational force as a function of z
plt.plot(zvals,gfvals,'k')
plt.title('Gravitational force as a function of z')
plt.xlabel('z values')
plt.ylabel('gravitational force')
plt.savefig('Gravitational_Force.pdf')
plt.show()
	
