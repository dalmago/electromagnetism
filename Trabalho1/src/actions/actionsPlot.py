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
import math
import numpy as np

class ActionsPlot(object):
        def __init__(self, uiMain, mainWindow, Plot, matplotlibPlot):
                self.uiMain = uiMain
                self.mainWindow = mainWindow
                self.Plot = Plot
                self.matplotlibPlot = matplotlibPlot

                self.connectSlots()

                self.k0= 9*10**9

                self.X = [0.4, 0]
                self.Y = [-0.3, 0.5]
                self.Z = [0.6, 0.24]
                self.cargas = [4, 9]

                #self.X = [0.4, 0, 0.2]
                #self.Y = [-0.3, 0.5, 0.2]
                #self.Z = [0.6, 0.24, 0.1]
                #self.cargas = [4, 9, 2]

                #self.X = [0, 0.4, 0, 0.4]
                #self.Y = [0.3, 0.3, 0, 0]
                #self.Z = [0, 0, 0, 0]
                #self.cargas = [-10, 5, 12, -3]

                #self.X = []
                #self.Y = []
                #self.Z = []
                #self.cargas = []

        def connectSlots(self):
                QtCore.QObject.connect(self.uiMain.pushButtonOk, QtCore.SIGNAL("clicked()"), self.addCharge)
                QtCore.QObject.connect(self.uiMain.pushButtonPlot, QtCore.SIGNAL("clicked()"), self.plot)

        def addCharge(self):
                self.X.append(self.uiMain.doubleSpinBoxX.value())
                self.uiMain.doubleSpinBoxX.setValue(0)
                self.Y.append(self.uiMain.doubleSpinBoxY.value())
                self.uiMain.doubleSpinBoxY.setValue(0)
                self.Z.append(self.uiMain.doubleSpinBoxZ.value())
                self.uiMain.doubleSpinBoxZ.setValue(0)
                self.cargas.append(self.uiMain.doubleSpinBoxForce.value())
                self.uiMain.doubleSpinBoxForce.setValue(0)

        def plot(self):
                self.mainWindow.close()
                self.matplotlibPlot.plotCharge\
                        (self.X, self.Y, self.Z, self.cargas)

                self.calculateForces()
                self.matplotlibPlot.plotAxis()
                self.Plot.show()

        def calculateForces(self):
                for i in range (len(self.X)):
                        somatorio = np.array([0,0,0])
                        moduloFinal = 0
                        for j in range (len(self.X)):
                                if i != j:
                                        print ("\nCarga %d em %d" %(j, i))
                                        vector = np.array([self.X[i]-self.X[j], \
                                                self.Y[i]-self.Y[j], \
                                                self.Z[i]-self.Z[j]])
                                        modulo = math.sqrt((vector[0]**2)+(vector[1]**2)+\
                                                (vector[2]**2))
                                        unitario = np.array([float(vector[0]/modulo), \
                                                float(vector[1]/modulo), float(vector[2]/\
                                                modulo)])
                                        print ("unitario")
                                        print (unitario)

                                        valor = self.k0*(self.cargas[i]*10**(-6))*\
                                                (self.cargas[j]*10**(-6))/ \
                                                (modulo**2)
                                        final = unitario*valor

                                        moduloFinal += (final[0]**2+final[1]**2+final[2]**2)
                                        print ("intensidade")
                                        print (math.sqrt(final[0]**2+final[1]**2+final[2]**2))

                                        somatorio = somatorio + final

                                        #print ("final")
                                        #print (final)
                                        self.matplotlibPlot.ax.plot(\
                                                [self.X[i], self.X[i]+final[0]],\
                                                [self.Y[i], self.Y[i]+final[1]],\
                                                [self.Z[i], self.Z[i]+final[2]], 'r', linewidth=2)

                                        self.matplotlibPlot.canvas.draw()


                        print ("\nresultante carga %d" %(i))
                        print (somatorio)
                        print ("Módulo da força:")
                        print (math.sqrt(moduloFinal))
                        self.matplotlibPlot.ax.plot(\
                                [self.X[i], self.X[i]+somatorio[0]],\
                                [self.Y[i], self.Y[i]+somatorio[1]],\
                                [self.Z[i], self.Z[i]+somatorio[2]], 'g', linewidth=2)

                        self.matplotlibPlot.ax.text(\
                                (self.X[i]+somatorio[0]+self.matplotlibPlot.xDistance),\
                                (self.Y[i]+somatorio[1]+self.matplotlibPlot.yDistance),\
                                (self.Z[i]+somatorio[2]+self.matplotlibPlot.zDistance),\
                                ("%f N" %(moduloFinal)))

                self.matplotlibPlot.canvas.draw()
