# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiPlot.ui'
#
# Created: Sat Mar 15 22:56:10 2014
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

class Ui_Plot(object):
    def setupUi(self, Plot):
        Plot.setObjectName(_fromUtf8("Plot"))
        Plot.resize(722, 475)
        self.gridLayout = QtGui.QGridLayout(Plot)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.figura = QtGui.QVBoxLayout()
        self.figura.setObjectName(_fromUtf8("figura"))
        self.gridLayout.addLayout(self.figura, 0, 0, 1, 1)

        self.retranslateUi(Plot)
        QtCore.QMetaObject.connectSlotsByName(Plot)

    def retranslateUi(self, Plot):
        Plot.setWindowTitle(_translate("Plot", "Form", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Plot = QtGui.QWidget()
    ui = Ui_Plot()
    ui.setupUi(Plot)
    Plot.show()
    sys.exit(app.exec_())

