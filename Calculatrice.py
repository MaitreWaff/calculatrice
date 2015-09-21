# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculatrice.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Calculatrice(object):
    def setupUi(self, Calculatrice):
        Calculatrice.setObjectName(_fromUtf8("Calculatrice"))
        Calculatrice.resize(382, 533)
        self.centralwidget = QtGui.QWidget(Calculatrice)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.screen = QtGui.QListView(self.centralwidget)
        self.screen.setObjectName(_fromUtf8("screen"))
        self.gridLayout.addWidget(self.screen, 0, 0, 1, 4)
        self.pbac = QtGui.QPushButton(self.centralwidget)
        self.pbac.setObjectName(_fromUtf8("pbac"))
        self.gridLayout.addWidget(self.pbac, 1, 0, 1, 1)
        self.pbpom = QtGui.QPushButton(self.centralwidget)
        self.pbpom.setObjectName(_fromUtf8("pbpom"))
        self.gridLayout.addWidget(self.pbpom, 1, 1, 1, 1)
        self.pbprcen = QtGui.QPushButton(self.centralwidget)
        self.pbprcen.setObjectName(_fromUtf8("pbprcen"))
        self.gridLayout.addWidget(self.pbprcen, 1, 2, 1, 1)
        self.pbdiv = QtGui.QPushButton(self.centralwidget)
        self.pbdiv.setObjectName(_fromUtf8("pbdiv"))
        self.gridLayout.addWidget(self.pbdiv, 1, 3, 1, 1)
        self.pb7 = QtGui.QPushButton(self.centralwidget)
        self.pb7.setObjectName(_fromUtf8("pb7"))
        self.gridLayout.addWidget(self.pb7, 2, 0, 1, 1)
        self.pb8 = QtGui.QPushButton(self.centralwidget)
        self.pb8.setObjectName(_fromUtf8("pb8"))
        self.gridLayout.addWidget(self.pb8, 2, 1, 1, 1)
        self.pb9 = QtGui.QPushButton(self.centralwidget)
        self.pb9.setObjectName(_fromUtf8("pb9"))
        self.gridLayout.addWidget(self.pb9, 2, 2, 1, 1)
        self.pbmul = QtGui.QPushButton(self.centralwidget)
        self.pbmul.setObjectName(_fromUtf8("pbmul"))
        self.gridLayout.addWidget(self.pbmul, 2, 3, 1, 1)
        self.pb4 = QtGui.QPushButton(self.centralwidget)
        self.pb4.setObjectName(_fromUtf8("pb4"))
        self.gridLayout.addWidget(self.pb4, 3, 0, 1, 1)
        self.pb5 = QtGui.QPushButton(self.centralwidget)
        self.pb5.setObjectName(_fromUtf8("pb5"))
        self.gridLayout.addWidget(self.pb5, 3, 1, 1, 1)
        self.pb6 = QtGui.QPushButton(self.centralwidget)
        self.pb6.setObjectName(_fromUtf8("pb6"))
        self.gridLayout.addWidget(self.pb6, 3, 2, 1, 1)
        self.pbsub = QtGui.QPushButton(self.centralwidget)
        self.pbsub.setObjectName(_fromUtf8("pbsub"))
        self.gridLayout.addWidget(self.pbsub, 3, 3, 1, 1)
        self.pb1 = QtGui.QPushButton(self.centralwidget)
        self.pb1.setObjectName(_fromUtf8("pb1"))
        self.gridLayout.addWidget(self.pb1, 4, 0, 1, 1)
        self.pb2 = QtGui.QPushButton(self.centralwidget)
        self.pb2.setObjectName(_fromUtf8("pb2"))
        self.gridLayout.addWidget(self.pb2, 4, 1, 1, 1)
        self.pb3 = QtGui.QPushButton(self.centralwidget)
        self.pb3.setObjectName(_fromUtf8("pb3"))
        self.gridLayout.addWidget(self.pb3, 4, 2, 1, 1)
        self.pbadd = QtGui.QPushButton(self.centralwidget)
        self.pbadd.setObjectName(_fromUtf8("pbadd"))
        self.gridLayout.addWidget(self.pbadd, 4, 3, 1, 1)
        self.pb0 = QtGui.QPushButton(self.centralwidget)
        self.pb0.setObjectName(_fromUtf8("pb0"))
        self.gridLayout.addWidget(self.pb0, 5, 0, 1, 2)
        self.pbdec = QtGui.QPushButton(self.centralwidget)
        self.pbdec.setObjectName(_fromUtf8("pbdec"))
        self.gridLayout.addWidget(self.pbdec, 5, 2, 1, 1)
        self.pbeq = QtGui.QPushButton(self.centralwidget)
        self.pbeq.setObjectName(_fromUtf8("pbeq"))
        self.gridLayout.addWidget(self.pbeq, 5, 3, 1, 1)
        Calculatrice.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Calculatrice)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Calculatrice.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Calculatrice)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Calculatrice.setStatusBar(self.statusbar)

        self.retranslateUi(Calculatrice)
        QtCore.QMetaObject.connectSlotsByName(Calculatrice)

    def retranslateUi(self, Calculatrice):
        Calculatrice.setWindowTitle(_translate("Calculatrice", "Calculatrice", None))
        self.screen.setToolTip(_translate("Calculatrice", "Afficheur de la Calculatrice", None))
        self.pbac.setText(_translate("Calculatrice", "AC", None))
        self.pbpom.setText(_translate("Calculatrice", "+/-", None))
        self.pbprcen.setText(_translate("Calculatrice", "%", None))
        self.pbdiv.setText(_translate("Calculatrice", "/", None))
        self.pb7.setText(_translate("Calculatrice", "7", None))
        self.pb8.setText(_translate("Calculatrice", "8", None))
        self.pb9.setText(_translate("Calculatrice", "9", None))
        self.pbmul.setText(_translate("Calculatrice", "X", None))
        self.pb4.setText(_translate("Calculatrice", "4", None))
        self.pb5.setText(_translate("Calculatrice", "5", None))
        self.pb6.setText(_translate("Calculatrice", "6", None))
        self.pbsub.setText(_translate("Calculatrice", "-", None))
        self.pb1.setText(_translate("Calculatrice", "1", None))
        self.pb2.setText(_translate("Calculatrice", "2", None))
        self.pb3.setText(_translate("Calculatrice", "3", None))
        self.pbadd.setText(_translate("Calculatrice", "+", None))
        self.pb0.setText(_translate("Calculatrice", "0", None))
        self.pbdec.setText(_translate("Calculatrice", ",", None))
        self.pbeq.setText(_translate("Calculatrice", "=", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Calculatrice = QtGui.QMainWindow()
    ui = Ui_Calculatrice()
    ui.setupUi(Calculatrice)
    Calculatrice.show()
    sys.exit(app.exec_())

