from __future__ import division
import math
def altitude(T):
	G= 6.67*(10**(-11))
	M= 5.97*(10**(24))
	R= 6371*(10**(3))
	h = float(((G * M * (T**2))/(4* (math.pi**2)))**(1/3) - R)
	return h
print 'Altitude of satellites that orbit once a day', altitude( 24*3600 )
print 'Altitude of satellites that orbit once every 90 minutes', altitude( 90*60 )
print 'Altitude of satellites that orbit once every 45 minutes', altitude( 45*60 )