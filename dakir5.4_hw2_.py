from __future__ import division
import math
import matplotlib.pyplot as plt
from pylab import imshow, show, hot
from numpy import empty
import numpy as np

#Defining the function that we want to integrate
def f(theta,m ,x):
	return (1/math.pi)*(math.cos(m*theta-x*math.sin(theta)))


#Defining Simpson's integrating method
def integrate(f,a,b,N,m,x):
	h= (b-a)/N
	s1=0
	s2=0
	for i in range(1, N,2):
		s1 += f(a+i*h,m,x)
	for i in range(2, N,2):
		s2 += f(a+i*h,m,x)
	I= float((1/3)*h*(f(a,m,x)+f(b,m,x)+4*s1+2*s2))
	return (I)

#Integrating the function f to find the Bessel functions
xvalues=[]	
J0values=[]
J1values=[]
J2values=[]
for x in np.arange(0,20,0.05): 
	xvalues.append(x)
	J0= integrate(f,0, math.pi,1000,0,x) #Calculating the Bessel function J0
	J1= integrate(f,0, math.pi,1000,1,x) #Calculating the Bessel function J1
	J2= integrate(f,0, math.pi,1000,2,x) #Calculating the Bessel function J2
	J0values.append(J0)
	J1values.append(J1)
	J2values.append(J2)
					
#Plotting the Bessel functions J0, J1 and J2 as a function of x
plt.xlabel('x values')
plt.ylabel('Bessel functions J0, J1 and J2')
plt.plot(xvalues, J0values,'b', label='Bessel function J0')
plt.plot(xvalues, J1values, 'k', label='Bessel function J1' )
plt.plot(xvalues, J2values,'r', label= 'Bessel function J2')
plt.legend()
plt.show()

#Defining the intensity of the light
def I(r,w):
	k= (2*math.pi)/(w)
	J1= integrate(f,0, math.pi,100,1,k*r)
	return (J1/(k*r))**2
	

side= 1.0
points=200
spacing=side/points
x0=spacing*100
y0=spacing*100

#Array that stores the intensities
Is= empty([points,points],float)

#Calculating the intensities 	
for i in range(points):
	y= spacing*i
	for j in range(points):
		x= spacing*j
		r= math.sqrt((x-x0)**2 + (y-y0)**2)
		if r==0:
			Is[i,j]= 0.5
		else:
			Is[i,j]= I(r,0.5)
						

#Plotting the density plot of the intensities
imshow(Is,vmax=0.01)
plt.title('Density plot of the intensity of the circular diffraction pattern')
hot()
show()
	
#Computing the Bessel Functions via recursion
def J(n,x):
	if n==0:
		return integrate(f,0, math.pi,1000,0,x)
	elif n==1:
		return integrate(f,0, math.pi,1000,1,x)
		
	else: 
		return ((2*n)/x)*J(n-1,x)-J(n-2,x)

#Defining the fractional error function		
def ferr(a,b):
	return math.fabs((a/b)-1)

#Computing Bessel functions J2, J3, J4 using the two methods 
xvals= []
EforJ2= []
EforJ3= []
EforJ4= []
for x in np.arange(1,20):
	xvals.append(x)
	
	#fractional error between the two methods for J2
	b2=J(2,x)
	a2= integrate(f,0, math.pi,1000,2,x)
	E2= ferr(a2,b2)
	EforJ2.append(E2)
	
	
	#fractional error between the two methods for J2	
	b3=J(3,x)
	a3= integrate(f,0, math.pi,1000,3,x)
	E3= ferr(a3,b3)
	EforJ3.append(E3)
	
	
	#fractional error between the two methods for J2	
	b4=J(4,x)
	a4= integrate(f,0, math.pi,1000,4,x)
	E4= ferr(a4,b4)
	EforJ4.append(E4)
	
#Plotting  the fractional error between the two methods as a function of x for n = 2, 3, and 4
plt.plot(xvals,EforJ2, 'r', label= 'fractional error as a function of x for n = 2' )
plt.plot(xvals,EforJ3, 'b', label= 'fractional error as a function of x for n = 3' )
plt.plot(xvals,EforJ4, 'k', label= 'fractional error as a function of x for n = 4' )
plt.legend()
plt.show()



	

	
	
	




		




	
		


