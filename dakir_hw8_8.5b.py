#Lamiaa Dakir Ex 8.5b
from __future__ import division, print_function
from numpy import arange,array
from math import sin,cos
import matplotlib.pyplot as plt

"""
Driven Pendulum
"""
#defining the constants
g=9.81
l=0.1
C=2

#Defining the function for the two first order differential equations 
def f(r,t,OM):
	theta= r[0]
	omega=r[1]
	ftheta= omega
	fomega= -(g/l)*sin(theta)+ C* cos(theta)*sin(OM*t)
	return array([ftheta,fomega],float)

a = 0
b =100
N =5000 
h = (b-a)/N #Defining the step size
t_points = arange(a,b,h)

#Creating arrays for constant OMEGA and and the maximum values of all thetas of a specific OMEGA
thetas = [] 
OMs=[]


##Defining the fourth-order Runge-Kutta method
for OM in arange(0,20,0.1):
	theta_points=[]
	r = array([0,0],float)
	for t in t_points:
		theta_points.append(r[0])
		k1 = h*f(r,t,OM)
		k2 = h*f(r+0.5*k1,t+0.5*h,OM)
		k3 = h*f(r+0.5*k2,t+0.5*h,OM)
		k4 = h*f(r+k3,t+h,OM)
		r += (k1+2*k2+2*k3+k4)/6	
	OMs.append(OM)
	thetas.append(max(theta_points)) #Finding the maximum of all the thetas for a certain OMEGA

#Making a graph of the max thetas as a function of OMEGA
plt.plot(OMs,thetas,'b')
plt.xlabel("OMEGA")
plt.ylabel("Maximum angles")
plt.savefig('Resonance.pdf')
plt.show()

#Finding the values of OMEGA for which the pendulum resonates
index_of_max= thetas.index(max(thetas))
OMEGA_resonance= OMs[index_of_max]
print ('The value for which the pendulum resonates with the driving force and swings widely from side to side is',OMEGA_resonance)


"""
Making a graph of theta as a function of t for OMEGA=9.5

"""

OM= OMEGA_resonance
#Creating arrays for omega and theta
new_theta_points = [] 


#Defining the fourth-order Runge-Kutta method
r = array([0,0],float)
for t in t_points:
    new_theta_points.append(r[0])
    k1 = h*f(r,t,OM)
    k2 = h*f(r+0.5*k1,t+0.5*h,OM)
    k3 = h*f(r+0.5*k2,t+0.5*h,OM)
    k4 = h*f(r+k3,t+h,OM)
    r += (k1+2*k2+2*k3+k4)/6
    
#Plotting theta as a function of t
plt.plot(t_points,new_theta_points,'b')
plt.xlabel("t")
plt.ylabel("Angle in radians")
plt.title("Angle of displacement for several periods")
plt.savefig('NewOMEGA.pdf')
plt.show()    
