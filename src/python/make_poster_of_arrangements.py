#Used to build 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from matplotlib.patches import Ellipse
import matplotlib.patheffects as patheffects
import sys
import math
from pylab import *

def tile(locx,locy,colors):
    mst=6
    ys = 1.5
    fade=0.4
    dy = 0.25
    dx = 0.25
    y = (locy-dy,locy-dy,locy-dy, locy, locy, locy, locy+dy, locy+dy, locy+dy)
    x = (locx-dx,locx, locx+dx,locx-dx,locx, locx+dx,locx-dx,locx, locx+dx)


    for i in range(0,9):
        if (colors[i] == 'w'):
            circ =plt.Circle((x[i],y[i]),radius=dx/2,edgecolor='k',fc=colors[i],linestyle='dashed',zorder=4)
            dashdict = [0., (1.,1.)]
            stroke = patheffects.Stroke(dashes=dashdict)
            circ.set_path_effects([stroke])

            plt.gca().add_artist(circ)
        elif (colors[i][1] == 1):
            circ =plt.Circle((x[i],y[i]),radius=dx/2,edgecolor='k',fc='#ffff00',zorder=4)
            if (colors[i][0] >= 0):
                if (colors[i][0] == 0):
                    plt.arrow(x[i]-0.0625,y[i],0.0625,0,zorder=5,color='k',head_width=0.05,width=0.005)
                if (colors[i][0] == 1):
                    plt.arrow(x[i]+0.0625,y[i],-0.0625,0,zorder=5,color='k',head_width=0.05,width=0.005)
                if (colors[i][0] == 2):
                    plt.arrow(x[i],y[i]-0.0625,0,0.0625,zorder=5,color='k',head_width=0.05,width=0.005)
                if (colors[i][0] == 3):
                    plt.arrow(x[i],y[i]+0.0625,0,-0.0625,zorder=5,color='k',head_width=0.05,width=0.005)
                if (colors[i][0] == 4):
                    plt.plot([x[i]-0.0625,x[i]+0.0625],[y[i]-0.0625,y[i]+0.0625],zorder=5,color='k')#,lw=.5)
                    plt.plot([x[i]+0.0625,x[i]-0.0625],[y[i]-0.0625,y[i]+0.0625],zorder=5,color='k')#,lw=.5)
                if (colors[i][0] == 5):
                    plt.plot(x[i],y[i],'k.',zorder=5)#,ms=1)                    
            plt.gca().add_artist(circ)
        elif (colors[i][1] == 2):
            circ =plt.Circle((x[i],y[i]),radius=dx/2,edgecolor='k',fc='g',zorder=4)
            plt.gca().add_artist(circ)
        else:
            circ =plt.Circle((x[i],y[i]),radius=dx/2,edgecolor='k',fc=colors[i],zorder=4)
            plt.gca().add_artist(circ)

# def tile(locx,locy,colors):
#     dy = 0.25
#     dx = 0.25
#     #Think about this bit, sets up the scaling for the tiles.
#     y = [i*.1 for i in range(-5+int(10*dy), 5-int(10*dy), int(10*dy))]*3
#     x = [i*.1 for i in range(-5+int(10*dx),5-int(10*dy), int(10*dx))]*3
#     x = [locx + i for i in x]
#     y = sorted([locy + i for i in y])

#     for i in range(0,len(colors)):
#         if (colors[i] == 'w'):
#             circ =plt.Circle((x[i],y[i]),radius=dx/2.5,edgecolor='k',fc=colors[i],zorder=4)
#             plt.gca().add_artist(circ)
#         elif (colors[i] == 'y'):
#             circ =plt.Circle((x[i],y[i]),radius=dx/2.5,edgecolor='k',lw = .1 ,fc='#ffff00',zorder=4)
#             plt.gca().add_artist(circ)
#         else:
#             circ =plt.Circle((x[i],y[i]),radius=dx/2.5,edgecolor='k',lw = .1 ,fc=colors[i],zorder=4)
#             plt.gca().add_artist(circ)
        


# #read in results from a file to make poster from
# value = []

# # with open("results2.txt") as f:
# #     for line in f:
# #         value.append(map(int, line.split()))

# # #Now change #'s to colors
# # for i in range(len(value)):
# #     for j in range(len(value[0])):
# #         if value[i][j] == 1:
# #             value[i][j] = 'y'
# #         elif value[i][j] == 2:
# #             value[i][j] = 'r'
# #         elif value[i][j] == 3:
# #             value[i][j] = 'g'
# #         elif value[i][j] == 4:
# #             value[i][j] = 'c'
# #         else:
# #             value[i][j] = 'b'

# value = [['w','w','w','w','w','w','w','w','w']]#[['r','r','y','y','y','g','g','g','g'],['r','r','y','y','g','y','g','g','g'],['r','r','y','y','g','g','y','g','g'],['r','r','y','y','g','g','g','y','g'],['r','r','y','y','g','g','g','g','y'],['r','r','y','g','g','y','g','g','y'],['r','r','g','y','y','y','g','g','g'],['r','r','g','y','y','g','y','g','g'],['r','r','g','y','y','g','g','g','y'],['r','r','g','y','g','y','y','g','g'],['r','r','g','y','g','y','g','y','g'],['r','r','g','y','g','g','g','y','y'],['r','y','y','y','r','g','g','g','g'],['r','y','y','g','r','y','g','g','g'],['r','y','y','g','r','g','y','g','g'],['r','y','y','g','r','g','g','y','g'],['r','y','y','g','r','g','g','g','y'],['r','y','g','y','r','g','g','g','y'],['r','y','g','g','r','y','y','g','g'],['r','y','g','g','r','y','g','g','y'],['r','g','y','g','r','y','y','g','g'],['r','g','y','g','r','y','g','g','y'],['r','g','y','g','r','g','y','g','y'],['r','g','y','g','r','g','g','y','y']]
value = [[[0, 1], [0, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[1, 1], [0, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[2, 1], [0, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [0, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [0, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [0, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[0, 1], [1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[2, 1], [1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[2, 1], [2, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [2, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [2, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [2, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [3, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [3, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [3, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [4, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [4, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [5, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2]],[[0, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[1, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[2, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[0, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[1, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[2, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[0, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[1, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[2, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[0, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[1, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[2, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[0, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[1, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[2, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[0, 1], [5, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[1, 1], [5, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[2, 1], [5, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [5, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [5, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [5, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[0, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[1, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[2, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[3, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[4, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[5, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[0, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[2, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[3, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[4, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[5, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[2, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[3, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[4, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[5, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[2, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[4, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[5, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[4, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[5, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[5, 1], [5, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1], [-1, 2]],[[0, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [0, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [2, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [3, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [4, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [5, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [5, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [5, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [5, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [5, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [5, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [0, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [0, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [0, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [0, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [2, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [2, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [2, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [2, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [4, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [4, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[1, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[2, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[0, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[2, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[2, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[3, 1], [3, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [3, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [3, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [4, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[5, 1], [4, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[4, 1], [5, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2]],[[0, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [3, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [3, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [3, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [3, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [3, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [3, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [4, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [4, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [4, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [4, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [4, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [4, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [5, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [5, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [5, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [5, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [5, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [5, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [0, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [2, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [3, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [3, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [3, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [4, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [4, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [5, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[1, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[2, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[3, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[4, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[5, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 1], [-1, 2], [-1, 2]],[[0, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[1, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[2, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[3, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[4, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[5, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[0, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[1, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[2, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[3, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[4, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[5, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[0, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[1, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[2, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[3, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[4, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[5, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[0, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[1, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[2, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[3, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[4, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[5, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[0, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[1, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[2, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[3, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[4, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[5, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[0, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[1, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[2, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[3, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[4, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[5, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2]],[[0, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [0, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [2, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [3, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [4, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[0, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[1, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[2, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[3, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[4, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]],[[5, 1], [5, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 1], [-1, 2], [-1, 2], [-1, 1]]]

#define image ratio in terms of horizontal over vertical for your poster size
def poster(value):
    fig = plt.gcf()
    image_ratio = float(1.0/1.0)
    x_size = math.floor(math.sqrt(image_ratio*len(value)))
    y_size = math.ceil(x_size/image_ratio)
    init_x = 0
    init_y = y_size
    # print(len(value))
    for i in range(0,len(value)):
        tile(init_x, init_y, value[i])
        init_x += 1
        if init_x > x_size:
            init_y -= 1
            init_x = 0
    

    plt.axis('off')
    plt.ylim(-1,y_size+1)
    plt.xlim(-1,x_size+1)
    fig.patch.set_alpha(0)
    filename = 'blank.pdf'
    fig.savefig('%s'%filename)
    plt.show()
