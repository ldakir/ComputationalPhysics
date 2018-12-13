from __future__ import print_function, division
import matplotlib.pyplot as plt
Z= input('The value of Z = ')
a1= 15.8
a2= 18.3
a3= 0.714
a4= 23.2
Avalues = []
Bvalues = []

for A in range(Z,3*Z):
	if A%2 !=0:
		a5=0
	elif A%2 ==0 & Z%2==0:
		a5=12
	elif A%2 ==0 & Z%2 !=0:
		a5=-12
	Bn= float(a1*A- a2*(A**(2/3))- a3*((Z**2)/(A**(1/3)))- a4*(((A-2*Z)**2)/A)+ a5/(A**(1/2)))/A
	Avalues.append(A)
	Bvalues.append(Bn)
	
max= Bvalues[0]
for i in range(0, len(Bvalues)-1):
	if Bvalues[i+1]>Bvalues[i]:
		max= Bvalues[i+1]
		Avalue= Avalues[i+1]
print ('The most stable nucleus has a value A of',Avalue, 'and the value of its binding energy per nucleus is ', max)
plt.plot(Avalues, Bvalues)
plt.show()
