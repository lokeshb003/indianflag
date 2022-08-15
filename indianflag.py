"""indian flag using python done by Lokesh """
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pt
# plotting the tri-colours
green = pt.Rectangle((0,1),width=12,height=2,facecolor='green',edgecolor='grey')
white = pt.Rectangle((0,3),width=12,height=2,facecolor='white',edgecolor='grey')
orange = pt.Rectangle((0,5),width=12,height=2,facecolor='#FF6103',edgecolor='grey')
a,b = plt.subplots()
b.add_patch(green)
b.add_patch(white)
b.add_patch(orange)
# Plotting the Chakra Circle
radius = 0.8
plt.plot(6,4,marker='o',markerfacecolor = '000088ff', markersize = 9.5)
chakra = plt.Circle((6,4),radius,color='#000088ff', fill=False, linewidth=7)
b.add_artist(chakra)
for i in range(0,24):
	p = 6 + radius/2 * np.cos(np.pi*i/12 + np.pi/48)
	q = 6 + radius/2 * np.cos(np.pi*i/12 - np.pi/48)
	r = 4 + radius/2 * np.sin(np.pi*i/12 + np.pi/48)
	s = 4 + radius/2 * np.sin(np.pi*i/12 - np.pi/48)
	t = 6 + radius * np.cos(np.pi*i/12)
	u = 4 + radius * np.sin(np.pi*i/12)
	b.add_patch(pt.Polygon([[6,4], [p,r], [t,u], [q,s]], fill=True, closed=True, color='#000088ff'))
plt.axis('equal')
plt.show()
