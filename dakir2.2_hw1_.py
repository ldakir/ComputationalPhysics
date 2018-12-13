from __future__ import print_function, division
import math

T= input('The value of T = ')
G= 6.67*(10**(-11))
M= 5.97*(10**(24))
R= 6371*(10**(3))

h = float(((G * M * (T**2))/(4* (math.pi**2)))**(1/3) - R)

print h
