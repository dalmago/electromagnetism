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

#try:
    #_fromUtf8 = QtCore.QString.fromUtf8
#except AttributeError:
    #def _fromUtf8(s):
        #return s

#try:
    #_encoding = QtGui.QApplication.UnicodeUTF8
    #def _translate(context, text, disambig):
        #return QtGui.QApplication.translate(context, text, disambig, _encoding)
#except AttributeError:
    #def _translate(context, text, disambig):
        #return QtGui.QApplication.translate(context, text, disambig)

class ActionsPlot(object):
        def __init__(self, uiMain, mainWindow, Plot, matplotlibPlot):
                self.uiMain = uiMain
                self.mainWindow = mainWindow
                self.Plot = Plot
                self.matplotlibPlot = matplotlibPlot

                self.connectSlots()

                self.k0= 9*10**9

                #self.X = [0.4, 0, 1]
                #self.Y = [-0.3, 0.5, 1.3]
                #self.Z = [0.6, 0.24, 1]
                #self.cargas = [8, 9, 10]

                self.X = []
                self.Y = []
                self.Z = []
                self.cargas = []

        def connectSlots(self):
                QtCore.QObject.connect(self.uiMain.pushButtonOk, QtCore.SIGNAL("clicked()"), self.addCharge)
                QtCore.QObject.connect(self.uiMain.pushButtonPlot, QtCore.SIGNAL("clicked()"), self.plot)

        def addCharge(self):
                self.X.append(self.uiMain.doubleSpinBoxX.value())
                #self.uiMain.doubleSpinBoxX.cleanText()
                self.Y.append(self.uiMain.doubleSpinBoxY.value())
                #self.uiMain.doubleSpinBoxY.cleanText()
                self.Z.append(self.uiMain.doubleSpinBoxZ.value())
                #self.uiMain.doubleSpinBoxZ.cleanText()
                self.cargas.append(self.uiMain.doubleSpinBoxForce.value())
                #self.uiMain.doubleSpinBoxForce.cleanText()

        def plot(self):
                self.mainWindow.close()
                self.matplotlibPlot.plotCharge\
                        (self.X, self.Y, self.Z, self.cargas)

                self.calculateForces()
                self.matplotlibPlot.plotAxis()
                self.Plot.show()

        def calculateForces(self):
                #self.forca = []
                for i in range (len(self.X)):
                        #resultante = []
                        somatorio = np.array([0,0,0])
                        for j in range (len(self.X)):
                                if i != j:
                                        print ("\nCarga %d em %d" %(i,j))
                                        #print ("em %d" %(j))
                                        vector = np.array([self.X[j]-self.X[i], \
                                                self.Y[j]-self.Y[i], \
                                                self.Z[j]-self.Z[i]])
                                        modulo = math.sqrt((vector[0]**2)+(vector[1]**2)+\
                                                (vector[2]**2))
                                        unitario = np.array([float(vector[0]/modulo), \
                                                float(vector[1]/modulo), float(vector[2]/\
                                                modulo)])
                                        print ("unitario")
                                        print (unitario)

                                        valor = self.k0*(self.cargas[i]*10**(-6))*\
                                                (self.cargas[j]*10**(-6))/ \
                                                (modulo**3)
                                        final = unitario*valor

                                        somatorio = somatorio + final

                                        print ("final")
                                        print (final)
                                        self.matplotlibPlot.ax.plot(\
                                                [self.X[j], self.X[j]+final[0]],\
                                                [self.Y[j], self.Y[j]+final[1]],\
                                                [self.Z[j], self.Z[j]+final[2]], 'r', linewidth=2)

                        print ("resultante")
                        print (somatorio)
                        self.matplotlibPlot.ax.plot(\
                                [self.X[i], self.X[i]+somatorio[0]],\
                                [self.Y[i], self.Y[i]+somatorio[1]],\
                                [self.Z[i], self.Z[i]+somatorio[2]], 'g', linewidth=2)

                                        #print (self.X[j]+final[0])
                                        #print (self.Y[j]+final[0])
                                        #print (self.Z[j]+final[0])

                        """resultante.append((self.k0*\
                                                (self.cargas[i]*10**(-6))*\
                                                (self.cargas[j]*10**(-6)))/ \
                                                ((self.X[i]-self.X[j])**2+\
                                                (self.Y[i]-self.Y[j])**2+\
                                                (self.Z[i]-self.Z[j])**2)**(1.5))"""
                        #final = 0
                        #for k in range (len(resultante)):
                                #final = final+(resultante[k])**2
                        #self.forca.append(math.sqrt(final))

