from __future__ import division
import matplotlib.pyplot as plt
from gaussxw import gaussxw
import math
from numpy import ones,copy,cos,tan,pi,linspace
    
#Defining the function f(x)    
def f(x):
	return (x**4*math.exp(x))/((math.exp(x)-1)**2)
#Defining the Gaussian quadrature rule to evaluate an integral
def integrateG(f,a,b,N):
	x,w = gaussxw(N)
	xp = 0.5*(b-a)*x +0.5*(b+a)
	wp = 0.5*(b-a)*w
	s=0
	for k in range (N):
		s+= wp[k]*f(xp[k])
	return s
#Defining the heat capacity of a solid at temperature T function	
def Cv(T):
	V= 1*(10**(-3))
	k= 1.38*(10**(-23))
	p= 6.022*(10**28)
	theta= 428
	Cv= 9*V*p*k*((T/theta)**3)*integrateG(f,0,theta/T,50)
	return Cv

#Plotting the heat capacity as a function of temperature from T=5k to T=500K
Hvalues= []
Tvalues= []

for T in range(5,500):
	H= Cv(T)
	Tvalues.append(T)
	Hvalues.append(H)	
plt.plot(Tvalues, Hvalues)
plt.xlabel('Temperatures in K')
plt.ylabel('Heat capacities')
plt.title(' Heat capacity as a function of temperature')
plt.show()

	

	