from __future__ import division, print_function
from math import sqrt,factorial,pi, exp, fabs ,tan , cos
import matplotlib.pyplot as plt
import numpy as np
from gaussxw import gaussxwab

#Defining Hermite polynomials  
def H(n,x):
	if n==0:
		return 1
	elif n==1:
		return 2*x
	else:
		return 2*x*H(n-1,x)-2*n*H(n-2,x)
#Defining the wavefunction		
def S(n,x):
	return (1/(sqrt(2**n*factorial(n)*sqrt(pi))))* exp(-x**2/2)*H(n,x)


#Computing the wavefunctions for n=0,1,2 and 3 for x from -4 to 4	
xvals=[] 
S0vals=[]
S1vals=[]
S2vals=[]
S3vals=[]

for x in np.arange(-4,4,0.05):
	xvals.append(x) #Storing the values of x in the xvals array

	S0= S(0,x) #Calculating S0
	S0vals.append(S0) # Storing the values in the array
	
	S1= S(1,x)
	S1vals.append(S1)
	
	S2= S(2,x)
	S2vals.append(S2)
	
	S3= S(3,x)
	S3vals.append(S3)
	
#Plotting the wavefunctions
plt.plot(xvals, S0vals,'r', label= 'Wavefunction for n=0')
plt.plot(xvals, S1vals,'b', label= 'Wavefunction for n=1')
plt.plot(xvals, S2vals,'k', label= 'Wavefunction for n=2')
plt.plot(xvals, S3vals,'g', label= 'Wavefunction for n=3')
plt.xlabel('x values')
plt.ylabel('wavefunctions')
plt.title('Wavefunctions for n=0,1,2 and 3 as a function of x')
plt.legend()
plt.savefig('wavefunctions.pdf')
plt.show()

#Computing the wavefunction for n= 30 for x from -10 to 10

S30vals=[]
xvalues=[]
for x in np.arange(-10,10, 0.05):
	xvalues.append(x)
	S30= S(30,x)
	S30vals.append(S30)
	
#Plotting the wavefunction for n=30
plt.plot(xvalues, S30vals,'k')
plt.title('Wavefunction for n=30 as a function of x')	
plt.xlabel('x values')
plt.ylabel('wavefunction for n=30')
plt.savefig('wavefunctions_for_n=30.pdf')
plt.show()

#Defining the function f(x)    
def f(x,n):
	return (tan(x)**2*(fabs(S(n,tan(x))))**2)/cos(x)**2
	
#Defining the Gaussian quadrature rule to evaluate an integral
def integrateG(f,n,a,b,N):
	x,w = gaussxwab(N,a,b)
	xp = 0.5*(b-a)*x +0.5*(b+a)
	wp = 0.5*(b-a)*w
	s=0
	for k in range (N):
		s+= wp[k]*f(xp[k],n)
	return s

#Defining the quantum uncertainty for n=5
def qun(n):
	return sqrt(integrateG(f,n,-pi/2,pi/2,100))

	
print ('The uncertainty for n=5 is', qun(5))

	
	




















	
	