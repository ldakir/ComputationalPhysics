from __future__ import division
def catalan(n):
	if n==0:
		return 1
	else:
		return ((4*n-2)/(n+1))*(catalan(n-1))
print 'Catalan of 100=',catalan(100)