#! /usr/bin/python
# -*- coding: utf-8 -*-

#"THE BEER-WARE LICENSE" (Revision 42):
#
#<matheusdalmago10@hotmail.com> wrote this file. As long as you reta#
#notice you can do whatever you want with this stuff. If we meet som#
#and you think this stuff is worth it, you can buy me a beer in retu#
#
#Created: Mar 11 2014
#       by: Matheus Dal Mago
#

from PyQt4 import QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg\
         as FigureCanvas
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg \
        #as NavigationToolbar
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

class MatplotlibPlot(object):
        def __init__(self, layout):
                self.layout = layout

                self.setupPlotArea()

        def setupPlotArea(self):
                self.fig = plt.figure()
                self.canvas = FigureCanvas(self.fig)
                #self.toolbar = NavigationToolbar(self.canvas, self)
                #self.layout.addWidget(self.toolbar)
                self.layout.addWidget(self.canvas)

                self.ax = self.fig.add_subplot(111, projection='3d')

                self.ax.set_xlabel('X')
                self.ax.set_ylabel('Y')
                self.ax.set_zlabel('Z')

        def plotCharge(self, x, y, z, charge=False, forca=False):
                # Plot the charges
                for i in range (len(x)):
                        self.ax.scatter(x[i], y[i], z[i], c='b',\
                                marker='o', s=50)

                # Plot the text
                for i in range (len(x)):
                        if charge:
                                self.xDistance = (self.ax.get_xlim3d()[1]\
                                        - self.ax.get_xlim3d()[0])/30
                                self.yDistance = (self.ax.get_ylim3d()[1]\
                                        - self.ax.get_ylim3d()[0])/30
                                self.zDistance = (self.ax.get_zlim3d()[1]\
                                        - self.ax.get_zlim3d()[0])/30
                                self.ax.text(x[i]+self.xDistance,\
                                        y[i]+self.yDistance, \
                                        z[i]+self.zDistance, \
                                        str(charge[i])+'uC')
                        if forca:
                                self.ax.text(x[i]-2*self.xDistance,\
                                        y[i]-2*self.yDistance, \
                                        z[i]-2*self.zDistance, \
                                        "%f N" %(forca[i]))
                self.canvas.draw()

        def plotAxis(self):
                # Plot the axis
                self.ax.plot([self.ax.get_xlim3d()[0],self.\
                        ax.get_xlim3d()[1]], [0,0], 'k')
                self.ax.plot([0,0], [self.ax.get_ylim3d()[0],\
                        self.ax.get_ylim3d()[1]], 'k')
                self.ax.plot([0,0],[0,0], 'k', zs=[self.ax.get_zlim3d()[0],\
                        self.ax.get_zlim3d()[1]])
                self.canvas.draw()
