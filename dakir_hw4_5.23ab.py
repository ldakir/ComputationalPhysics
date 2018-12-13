#Lamiaa Dakir Ex5.23

import matplotlib.pyplot as plt
import numpy as np
import urllib2
from pylab import imshow
#from math import cos, sin, sqrt, pi
from math import pi
from numpy import cos, sin, sqrt
#Open the on-line resources
file = urllib2.urlopen("http://www-personal.umich.edu/~mejn/cp/data/altitude.txt")
#Reading the file
data= np.loadtxt(file)


h=30000
#Finding dw/dx
new_data=np.roll(data, 1, axis=0)
der_x=(new_data-data)/h

#Finding dw/dy
new_data1=np.roll(data, 1, axis=1)
der_y=(new_data1-data)/h



Is= np.empty([512,1024],float)
phi= 45*pi/180

#Finding the intensities 
for x in range(512):
	for y in range(1024):
		Is[x,y]= - (cos(phi)*der_x[x,y] + sin(phi)*der_y[x,y])/ sqrt((der_x[x,y])**2+(der_y[x,y])**2+1)

# Plotting the density plot of the intensities
imshow(Is)
plt.title('Map of the World')
plt.xlabel('x position')
plt.ylabel('y position')
plt.savefig('altitude.pdf')
plt.show()
