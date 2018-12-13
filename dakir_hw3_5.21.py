from __future__ import division, print_function
from math import pi, sqrt,sin
from pylab import imshow, show, hsv,hot, jet
from numpy import empty,meshgrid,arange, mgrid, transpose, fromfunction
import matplotlib.pyplot as plt
from gaussxw import gaussxw

#Defining the electric potential Phi
k=89875.52

def Phi(x,y):
	r1= sqrt((x-0.5)**2.0 + y**2.0)+0.001
	r2= sqrt((x+0.5)**2.0 + y**2.0)+0.001
	return k*(1/r1-1/r2)	
points=100

#Array that stores the values of the potential
Phis= empty([points,points],float)

#Calculating the values of the potential  	
for i in range(points):
	y=i
	for j in range(points):
		x=j
		Phis[i,j]= Phi(x-50,y-50)

# Plotting the density plot of the potential 
plt.figure(1)
plt.pcolor(Phis)
plt.title('Density plot of the potential')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.savefig('potential.pdf')
plt.show()


#Calculating the electric field
h=0.01
def pdx(f,x,h):
	s= (f(x+h/2,y)-f(x-h/2,y))/h
	return s
	
def pdy(f,y,h):
	s= (f(x,y+h/2)-f(x,y-h/2))/h
	return s
	
	
def Ex(x,y):
	return -pdx(Phi,x,h)
	
def Ey(x,y):
	return -pdy(Phi,y,h)
	
#Array that stores the values of the electric field
Exs= empty([points,points],float)
Eys= empty([points,points],float)
Es= empty([points,points],float)

#Calculating the values of the magnitude electric field  	
for i in range(points):
	y= i
	for j in range(points):
		x= j
		Exs[i,j]= Ex(x-50,y-50)
		Eys[i,j]= Ey(x-50,y-50)
		Es[i,j]= sqrt(Ex(x-50,y-50)**2+Ey(x-50,y-50)**2)		

# Plotting the density plot of the direction of the electric field 
plt.figure(2)
plt.pcolor(Exs)  
plt.show()  
plt.pcolor(Eys)
plt.show()
plt.quiver(Exs,transpose(Eys))
plt.title('The direction of the electric field')
plt.show()

#Plotting the density plot of the magnitude of the electric field 
plt.figure(3)
plt.pcolor(Es)
plt.title('The magnitude of the electric field')
plt.show()



	



	                                                                         