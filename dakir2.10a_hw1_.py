from __future__ import print_function, division
A= input('The value of A = ')
Z= input('The value of Z = ')
a1= 15.8
a2= 18.3
a3= 0.714
a4= 23.2
if A%2 !=0:
	a5=0
elif A%2 ==0 & Z%2==0:
	a5=12
elif A%2 ==0 & Z%2 !=0:
	a5=-12

B= float(a1*A- a2*(A**(2/3))- a3*((Z**2)/(A**(1/3)))- a4*(((A-2*Z)**2)/A)+ a5/(A**(1/2)))
print  ("The binding energy is" , B)

