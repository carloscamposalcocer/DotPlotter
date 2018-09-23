
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.plot([1,2,3],[4,3,5])
plt.show()

fig = plt.figure()
ax = plt.axes(projection='3d')

zline = [0,1,2,4]
xline = [0,1,2,3]
yline = [0,1,2,3]
ax.plot3D(xline, yline, zline, 'gray')
zline = [4,4,4,4]
xline = [0,1,2,3]
yline = [0,1,2,3]
ax.plot3D(xline, yline, zline, 'gray')
plt.show()
