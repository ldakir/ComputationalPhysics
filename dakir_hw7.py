from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np
from math import log,fabs, pi
import urllib2
from scipy.interpolate import interp1d
from gaussxw import gaussxw

#Open the on-line resources
file = urllib2.urlopen("https://lambda.gsfc.nasa.gov/tmp/camb/camb_04671438_scalcls.dat")
#Reading the file
data= np.loadtxt(file)

#Taking only the first two columns
l_array=data[:,0]
temp_array= data[:,1]


#Using 200 points instead of 2199
l_new_array=l_array[::11]
temp_new_array=temp_array[::11]


#Using cubic spline interpolation to approximate C_l^(TT)
f=interp1d(l_new_array,temp_new_array, kind='cubic') 

#Plotting the initial data plot
plt.plot(l_array,temp_array,'k')
plt.title('CMB temperature power spectrum') 
plt.xlabel('l') #Labeling the x-axis
plt.ylabel('Temperature variance') #Labeling the y-axis
plt.savefig('initial_plot.pdf') #Saving the figure as a pdf
plt.show()

#Plotting the initial and interpolated data plot
plt.plot(l_array,temp_array,'k',l_new_array, f(l_new_array), 'r--')
plt.title('CMB temperature power spectrum')
plt.xlabel('l')
plt.ylabel('Temperature variance')
plt.savefig('interpolation.pdf')
plt.show()
	
#Calculating the residual error
residual_error=[] #Creating an array for the residual errors
l=[] #Creating an array for the values of l
precision=[] 

for i in range(2190):
	l.append(l_array[i])
 	error= (f(l_array[i])-temp_array[i])/temp_array[i] # Calculating the error at each point
	residual_error.append(error) #Storing the values in the array
	precision.append(3/l_array[i]) #Calculating the precision that shows if a spline does well enough

#Plotting the residual error and the fractional precision as function of l
plt.plot(l, np.abs(residual_error),label='The residual fractional error')
plt.plot(l,precision, label='The fractional precision')
plt.yscale('log') #setting the scale of the residual error to be log
plt.xlabel('l')
plt.ylabel('Error')
plt.legend()
plt.savefig('residual_error.pdf')
plt.show()

 	

"""
Finding the derivative

"""
 
#Finding the derivative of l(l+1)C/(2pi)	
def derivative(f,x):
	h=0.01
	s= (f(x+h)-f(x-h))/(2*h)
	return s
	
#Finding the derivative of C
def derivative_C(f,x): 
	h=0.01
	s= pi*(f(x+h)/((x+h)*(x+h+1))-f(x-h)/((x-h)*(x-h+1)))/h 
	return s
	
#Finding the fourth derivative 
def fourth_d(f,x):
	return derivative(derivative(derivative(derivative(f,x),x),x),x)
	
#Calculating the derivative of C_l^TT
dC=[]
for i in range(3,2190):
	dC.append(derivative_C(f,i))	
print('The derivative of C_l^TT is: ', dC)


	
"""
Computing the typical fluctuation^2

"""

#Defining the Gaussian quadrature rule to evaluate the integral
def integrate(f,a,b,N):
	x,w = gaussxw(N)
	xp = 0.5*(b-a)*x +0.5*(b+a)
	wp = 0.5*(b-a)*w
	s=0
	for k in range (N):
		s+= wp[k]*f(xp[k])/(xp[k]+1) 
	return s

print('The typical fluctuation^2 is:',integrate(f,2,2190,1000))




