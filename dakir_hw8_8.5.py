#Lamiaa Dakir Ex 8.5a
from __future__ import division, print_function
from numpy import arange,array
from math import sin,cos, pi
import matplotlib.pyplot as plt

"""
Driven Pendulum
"""
#defining the constants
g=9.81
l=0.1
C= 2
OM= 5


#Defining the function for the two first order differential equations 
def f(r,t):
	theta= r[0]
	omega=r[1]
	ftheta= omega
	fomega= -(g/l)*sin(theta)+ C* cos(theta)*sin(OM*t)
	return array([ftheta,fomega],float)

a = 0
b =100
N =3000
h = (b-a)/N #Defining the step size
t_points = arange(a,b,h)

#Creating arrays for omega and theta
theta_points = [] 
omega_points = []

#Defining the fourth-order Runge-Kutta method
r = array([0,0],float)
for t in t_points:
    theta_points.append(r[0])
    omega_points.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6


#Making a graph of theta as a function of t
plt.plot(t_points,theta_points,'b')
plt.xlabel("t")
plt.ylabel("Angle in radians")
plt.title("Angle of displacement for several periods")
plt.savefig('driven_pendulum.pdf')
plt.show()

    	
    	
    	