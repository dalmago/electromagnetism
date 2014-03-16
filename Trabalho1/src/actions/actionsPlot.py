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
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

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
        def __init__(self, uiMain, uiPlot, mainWindow, Plot):
                self.uiMain = uiMain
                self.uiPlot = uiPlot
                self.mainWindow = mainWindow
                self.Plot = Plot

                self.connectSlots()
                self.setupPlotArea()

        def setupPlotArea(self):
                self.fig = plt.figure()
                self.canvas = FigureCanvas(self.fig)
                self.uiPlot.figura.addWidget(self.canvas)

                self.X = []
                self.Y = []
                self.Z = []
                self.cargas = []

        def connectSlots(self):
                QtCore.QObject.connect(self.uiMain.pushButtonOk, QtCore.SIGNAL("clicked()"), self.addCharge)
                QtCore.QObject.connect(self.uiMain.pushButtonPlot, QtCore.SIGNAL("clicked()"), self.plot)

        def addCharge(self):
                self.X.append(self.uiMain.doubleSpinBoxX.value())
                self.Y.append(self.uiMain.doubleSpinBoxY.value())
                self.Z.append(self.uiMain.doubleSpinBoxZ.value())
                self.cargas.append(self.uiMain.doubleSpinBoxForce.value())

        def plot(self):
                self.mainWindow.close()
                self.Plot.show()
