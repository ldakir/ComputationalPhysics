#Lamiaa Dakir Ex 8.2
from __future__ import division, print_function
from numpy import arange,array
from math import sin,cos
import matplotlib.pyplot as plt

"""
Predator-prey populations

"""
#defining the constants
alpha=1
beta=0.5
gamma=0.5
delta=2

#Defining the function for the two first-order differential equations 
def f(r,t):
	x= r[0]
	y=r[1]
	fx= alpha*x-beta*x*y
	fy= gamma*x*y- delta*y
	return array([fx,fy],float)

a = 0
b =30
N =1000
h = (b-a)/N #Defining the step size
t_points = arange(a,b,h)
#Creating arrays for x and y
x_points = [] 
y_points = []

#Defining the fourth-order Runge-Kutta method
r = array([2,2],float)
for t in t_points:
    x_points.append(r[0]*1000)
    y_points.append(r[1]*1000)
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6


#Plotting the size of the populations of rabbits and foxes as a function of time 
plt.plot(t_points,x_points,'b',label='Population of rabbits')
plt.plot(t_points,y_points,'r', label='Population of foxes')
plt.xlabel("t")
plt.ylabel("Size of the populations")
plt.legend()
plt.title("Population of the foxes and the rabbit")
plt.savefig('populations.pdf')
plt.show()