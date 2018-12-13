import matplotlib.pyplot as plt
import numpy as np
import urllib2
from pylab import imshow, gray
from math import pi
from numpy import cos, sin, sqrt
#Open the on-line resources
file = urllib2.urlopen("http://www-personal.umich.edu/~mejn/cp/data/stm.txt")
#Reading the file
data= np.loadtxt(file)

#Finding dw/dx
h=2.5
new_data=np.roll(data, 1, axis=0)
der_x=(new_data-data)/h

#Finding dw/dy
new_data1=np.roll(data, 1, axis=1)
der_y=(new_data1-data)/h


Is= np.empty([663,676],float)
phi= 45*pi/180

#Finding the intensities 
for x in range(663):
	for y in range(676):
		Is[x,y]= - (cos(phi)*der_x[x,y] + sin(phi)*der_y[x,y])/ sqrt((der_x[x,y])**2+(der_y[x,y])**2+1)


# Plotting the density plot of the intensities
imshow(Is)
plt.title('Silicon Surface')
plt.savefig('silicon.pdf')
plt.show()