#Lamiaa Dakir Ex6.9
from __future__ import division, print_function
from gaussxw import gaussxw
from math import sin, pi, fabs,sqrt
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigh, eigvalsh

"""
Asymmetric quantum well

"""

"""
H_mn for arbitrary m and n when the particle in the well is an electron

"""
	
#The constants
h_bar= 1.055*10**(-34) #m^(2) kg/s
M= 9.1094*10**(-31) #kg
a= 10*1.6*10**(-19) #J
L= 5*10**(-10) #m	

#Defining the function for the Hamiltonian matrix H

def H(m,n):
    #Evaluation of the integral of xsin(pimx/L)sin(pinx/L) and sin(pimx/L)sin(pinx/L) depending on m and n 
	if m==n:
		A= L**2/4
		B= L/2
	elif (m%2==0 and n%2==0) or (m%2!=0 and n%2!=0):
		A= 0
		B= 0
	else:
		A= -(2*L/pi)**2*(m*n/(m**2-n**2)**2)
		B= 0	
	#Returning the value of H as a function of n and m 	
	return ((h_bar*n*pi)**2)/(L**3*M)*B + (2*a/L**2)*A


H_matrix= np.ndarray([10,10], float) #Creating a 10x10 matrix 
for m in range(10):
	for n in range(10):
		H_matrix[m,n]= H(m+1,n+1) #Adding elements to the matrix
"""
Eigenvalues of the Hamiltonian matrix

"""

print ('Eigenvalues of the 10X10 Hamiltonian matrix in eV')

Eigenvalues,Eigenvectors=eigh(H_matrix) #Finding the eigenvalues and eigenvectors of the Hamiltonian matrix
print(Eigenvalues*6.242*10**(18))  # Printing the eigenvalues 


               
"""
First ten energy eigenvalues for a 100X100 matrix

"""

H_bigger_matrix= np.ndarray((100,100)) #Creating a 100x100 matrix 
for m in range(100):
	for n in range(100):
		H_bigger_matrix[n,m]= H(m+1,n+1) #Adding elements to the matrix
		
print('Eigenvalues of the 100X100 Hamiltonian matrix in eV')
Eigvals,Eigvecs= eigh(H_bigger_matrix)
for i in range(10):
	print (Eigvals[i]*6.242*10**(18))  # First ten energy eigenvalues
	
"""
Wavefunction for the ground state and the first two excited states of the well

"""

#Defining the wavefunction

def wavefunction(x,n): #n is the level state energy
	s=0
	for i in range(10):
		s+=Eigvecs[i,n]*sin(pi*(i+1)*x/L)*6.242*10**(18)
		
	return s
	
"""
Graph with three curves showing the probability density as a function of x in each of the ground state and the first two excited states of the well

"""

#Calculating the probability density for a range of values for x

x_values=[]
probability_density_0= [] #Array of probability densities in the ground state
probability_density_1= [] #Array of probability densities in the first excited state
probability_density_2= [] #Array of probability densities in the second excited state

for x in np.arange(0,6,0.01):
	x_values.append(x)
	probability_density_0.append(fabs(wavefunction(x*10**(-10),0)*6.38098129782e-16)**2)
	probability_density_1.append(fabs(wavefunction(x*10**(-10),1)*6.10174919657e-16)**2)
	probability_density_2.append(fabs(wavefunction(x*10**(-10),2)*5.78626616347e-16)**2)
	

#Plotting the probability densities as a function of x	
plt.plot(x_values,probability_density_0,'r', label= 'Probability density in the ground state')
plt.plot(x_values, probability_density_1,'b', label= 'Probability density in the first excited state')
plt.plot(x_values, probability_density_2,'k', label= 'Probability density in the second excited state')
	
plt.xlabel('x values in Angstrom') #Labeling the x-axis
plt.ylabel('Probability density') #Labeling the y-axis
plt.title('Probability density as a function of x') #Labeling the graph
plt.legend()
plt.savefig('Probability_density.pdf') #Saving the graph as a pdf
plt.show()	








