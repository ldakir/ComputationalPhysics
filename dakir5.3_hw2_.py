from __future__ import division, print_function
import math
import matplotlib.pyplot as plt


#Defining the function that we want to integrate
def f(t):
	return math.exp(-t**2)

#Defining the second derivative of f(t)
def ddf(t): 
	return (4*(t**2)-2)*math.exp(-t**2)

#Defining Simpson's integrating method
def integrate(f,a,b,N):
	h= (b-a)/N
	s1=0
	s2=0
	for i in range(1, N,2):
		s1 += f(a+i*h)
	for i in range(2, N,2):
		s2 += f(a+i*h)
	I= float((1/3)*h*(f(a)+f(b)+4*s1+2*s2))
	return (I)

#Determining the suitable number of slices N 
def e(a,b,N): #approximation error for simpson's rule
	h= (b-a)/N
	return math.log(math.fabs((1/90)*(h**4)*(ddf(a)-ddf(b))), 12)

Nvalues=[]
evalues=[]
yvalues =[]
for N in range(10,1000):
	y=0
	yvalues.append(y)
	Nvalues.append(N)
	evalues.append(e(0,3,N))	
	
plt.plot(Nvalues, evalues) #Plot of the error approximation as a function of N slices
plt.xlabel('Number of slices N')
plt.ylabel('Error approximation')
plt.title('Graph of the error approximation as a function of N slices')
plt.show()

#Calculating E(x) for values of x from 0 to 3 in steps of 0.1
x=0
xvalues=[] 
Evalues=[]
while x<3.1: 
	Ex= integrate(f,0,x,600) #Calling the integrate function
	print ('for x=',x,'E(x)=', Ex)
	x+= 0.1 #Iterating x in steps of 0.1
	xvalues.append(x) #Storing x values in an array 
	Evalues.append(Ex) #Storing E(x) values in an array
	
#Plotting E(x) as a function of x
plt.plot(xvalues, Evalues, 'b') 
plt.xlabel('x values', fontsize=15) #Labeling the x-axis
plt.ylabel('E(x)', fontsize=15) #Labeling the y-axis
plt.title('Graph of E(x) as a function of x') #Adding a title to the graph
plt.show() 

#Defining E(x) in terms of the Erf function
def E(x):
	return math.sqrt(math.pi)* math.erf(x)*(1/2)
	
#Plotting E(x) using the definition in Ex 5.3 and using the Erf function
Exvalues=[]
for i in xvalues:
	Exvalues.append(E(i))
plt.plot(xvalues,Exvalues,'r', label =' Graph of E(x) in terms of the erf function') 
plt.plot(xvalues,Evalues, 'b', label='Graph of E(x) using the function f(t)')
plt.legend()
plt.xlabel('x values', fontsize=15) #Labeling the x-axis
plt.ylabel('E(x)', fontsize=15) #Labeling the y-axis
plt.show()


	

	


	
	