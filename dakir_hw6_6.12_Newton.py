from __future__ import division, print_function
from numpy import exp
from math import sqrt, log, fabs


"""
Glycolosis

"""

"""
Solving the equations using Newton's method

"""


#Setting the value of the constants a and b and the accuracy
a=1
b=2
accuracy= 10**(-6)

#Defining the second equation in terms of x and y and its derivative
def f(y,x):
	return b-a*y-x**2*y

def f_prime(x):
	return -a-x**2
	
#Defining Newton's method that returns y, the solution of the function in terms of x
def solution_x(f,x):
	y=0 #initial guess
	delta= 1
	while fabs(delta)> accuracy:
		delta= f(y,x)/f_prime(x)
		y-= delta
	return y

#defining the first equation in terms of x
def g(x):
	return -x+a*solution_x(f,x)+x**2*solution_x(f,x)
	
def g_prime(x):
	h=0.01
	return (g(x+h)-g(x-h))/(2*h)
	
#Defining Newton's method that returns x	
def solution(f):
	x=0 #initial guess
	delta= 1
	while fabs(delta)> accuracy:
		delta= f(x)/g_prime(x)
		x-= delta
	return x
	
#Setting x to be the solution to h(x)		
x= solution(g)

#Printing the solutions
print('x = '+str(x),'and y = '+ str(solution_x(f,x)))
	

	

	
	

