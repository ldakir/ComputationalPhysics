from __future__ import division, print_function
from numpy import exp
from math import sqrt, log, fabs


"""
Glycolosis

"""

"""
Solving the equations using the binary search method

"""


#Setting the value of the constants a and b 
a=1
b=2

#Defining the binary search method that returns y, the solution of the function in terms of x
def solution_x(f,x1,x2,target_accuracy,x):
	while(fabs(x1-x2)> target_accuracy):
		mid_point= (x1+x2)/2

		if (f(mid_point,x)>0 and f(x1,x)>0) or (f(mid_point,x)<0 and f(x1,x)<0):
			x1=mid_point
		else:
			x2=mid_point
	return mid_point

#Defining the second equation in terms of x and y 
def f(y,x):
	return b-a*y-x**2*y

#defining the first equation in terms of x
def h(x):
	return -x+a*solution_x(f,-6,5,10**(-6),x)+x**2*solution_x(f,-6,5,10**(-6),x)
	
#Defining the binary search method that returns x	
def solution(f,x1,x2,target_accuracy):
	while(fabs(x1-x2)> target_accuracy):
		mid_point= (x1+x2)/2
		if (f(mid_point)>0 and f(x1)>0) or (f(mid_point)<0 and f(x1)<0):
			x1=mid_point
		else:
			x2=mid_point
	return mid_point
	
#Setting x to be the solution to h(x)		
x= solution(h,-6,5,10**(-6))

#Printing the solutions
print('x = '+str(x),'and y = '+ str(solution_x(f,-6,5,10**(-6),x)))







