'''
prints linear interlolated 3d plot of tracking data (format csv: time,x,y,z)
ignores timestamp

copyright 2010 by Bastian Migge <miggeb@ethz.ch> , IWF/inspire AG 
'''

import time, sys
from string import split
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# read data file (given by first command line argument
xData, yData, zData = [],[],[]
f = open(sys.argv[1], 'r')

for line in f:
    line = line.strip()
    b = line.split(",")
    xData.append(float(b[1]))
    yData.append(float(b[2]))
    zData.append(float(b[3]))

assert len(xData) == len(yData) and len(yData) == len(zData)

fig = plt.figure()
ax = Axes3D(fig)

#display
displayWidth = 1500.0
displayHeight = 700.0

xDisplay = np.array([0.,displayWidth,displayWidth,0.,0.])
yDisplay = np.zeros(5)
zDisplay = np.array([0.,0.,-displayHeight,-displayHeight,0.])
ax.plot(xDisplay,yDisplay,zDisplay,c="r")

# start and end point
ax.scatter(np.array([xData[0],xData[-1]]), -1.0*np.array(([zData[0],zData[-1]])), -1.0*np.array(([yData[0],yData[-1]])),c="r",marker='d')
ax.plot( np.array(xData), -1.0*np.array(zData), -1.0*np.array(yData),markersize=1200,label='view point')
ax.legend()


plt.show()

