# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiMain.ui'
#
# Created: Sat Mar 15 22:46:50 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(305, 193)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.doubleSpinBoxX = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxX.setObjectName(_fromUtf8("doubleSpinBoxX"))
        self.horizontalLayout_3.addWidget(self.doubleSpinBoxX)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.doubleSpinBoxY = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxY.setObjectName(_fromUtf8("doubleSpinBoxY"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxY)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.doubleSpinBoxZ = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxZ.setObjectName(_fromUtf8("doubleSpinBoxZ"))
        self.horizontalLayout.addWidget(self.doubleSpinBoxZ)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.doubleSpinBoxForce = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxForce.setObjectName(_fromUtf8("doubleSpinBoxForce"))
        self.verticalLayout_2.addWidget(self.doubleSpinBoxForce)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButtonOk = QtGui.QPushButton(self.centralwidget)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.verticalLayout_3.addWidget(self.pushButtonOk)
        self.pushButtonPlot = QtGui.QPushButton(self.centralwidget)
        self.pushButtonPlot.setObjectName(_fromUtf8("pushButtonPlot"))
        self.verticalLayout_3.addWidget(self.pushButtonPlot)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 305, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.actionSair = QtGui.QAction(MainWindow)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.menuMenu.addAction(self.actionSair)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionSair, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Coordenadas (m):", None))
        self.label_2.setText(_translate("MainWindow", "X:", None))
        self.label_3.setText(_translate("MainWindow", "Y:", None))
        self.label_4.setText(_translate("MainWindow", "Z:", None))
        self.label_5.setText(_translate("MainWindow", "Força (C):", None))
        self.pushButtonOk.setText(_translate("MainWindow", "Ok", None))
        self.pushButtonPlot.setText(_translate("MainWindow", "Plotar", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.actionSair.setText(_translate("MainWindow", "Sair", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

