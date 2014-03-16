#! /usr/bin/python
# -*- coding: utf-8 -*-

#"THE BEER-WARE LICENSE" (Revision 42):
#
#<matheusdalmago10@hotmail.com> wrote this file. As long as you retain this
#notice you can do whatever you want with this stuff. If we meet some day,
#and you think this stuff is worth it, you can buy me a beer in return.
#
#Created: Mar 11 2014
#       by: Matheus Dal Mago
#

from PyQt4 import QtGui
import sys, os

from ui.uiMain import Ui_MainWindow
from ui.uiPlot import Ui_Plot

from actions.actionsPlot import ActionsPlot

class Runner(object):
        def __init__(self):
                self.setup()

        def setup(self):
                self.uiMain = Ui_MainWindow()
                self.uiMain.setupUi(MainWindow)

                self.uiPlot = Ui_Plot()
                self.uiPlot.setupUi(Plot)

                self.actionsPlot = ActionsPlot(self.uiMain, self.uiPlot, MainWindow, Plot)
                #self.fig = plt.figure()
                #self.ax = self.fig.add_subplot(111, projection='3d')

                #self.ax.set_xlabel('X')
                #self.ax.set_ylabel('Y')
                #self.ax.set_zlabel('Z')

        def run(self):
                MainWindow.show()
                app.exec_()
                #self.readData()
                #self.plot()
                #plt.show()

        #def plot(self):
                #for i in range (self.amount):
                        #self.ax.scatter(self.X[i], self.Y[i], self.Z[i])#, \
                                #c='b', marker='o')

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        Plot = QtGui.QWidget()
        runner = Runner()
        runner.run()
