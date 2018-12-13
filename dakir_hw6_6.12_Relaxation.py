from __future__ import division, print_function
from numpy import exp
from math import sqrt, log, fabs


"""
Glycolosis

"""

"""
Solving the equations using the relaxation method

"""

#Setting the value of the constants a and b 
a=1
b=2


def f(y,x): 
	return	b/(a+x**2) #Represents the second equation b-ay-x^2y=0

#Defining the relaxation method that returns y, the solution of the function in terms of x
def solution_x(f,x):
	guess= 1
	answer=f(guess,x)
	for i in range (30):
		answer = f(answer,x)
	return (answer)
	
	
def h(x):
	return solution_x(f,x)*(a+x**2) #Represents the first equation -x+ay+x^2y=0
	
#Defining the relaxation method that returns x
def solution(f):
	guess= 1
	answer=f(guess)
	for i in range (10):
		answer = f(answer)
	return (answer)
	
#Setting x to be the solution to h(x)		
x= solution(h)

#Printing the solutions
print('x = '+str(x),'and y = '+ str(solution_x(f,x)))































