# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

# version ~GUI
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QDirModel, QStringListModel
from PyQt4.QtCore import SIGNAL

import Calculatrice


class Main(QtGui.QMainWindow, Calculatrice.Ui_Calculatrice):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.initUI()

    def initUI(self):
        self.setupUi(self)

        self.listelts = []

        self.connect(self.pb0, SIGNAL("clicked()"), lambda who="Zero": self.clickBtn(who))
        self.connect(self.pb1, SIGNAL("clicked()"), lambda who="One": self.clickBtn(who))
        self.connect(self.pb2, SIGNAL("clicked()"), lambda who="Two": self.clickBtn(who))
        self.connect(self.pb3, SIGNAL("clicked()"), lambda who="Tree": self.clickBtn(who))
        self.connect(self.pb4, SIGNAL("clicked()"), lambda who="Four": self.clickBtn(who))
        self.connect(self.pb5, SIGNAL("clicked()"), lambda who="Five": self.clickBtn(who))
        self.connect(self.pb6, SIGNAL("clicked()"), lambda who="Six": self.clickBtn(who))
        self.connect(self.pb7, SIGNAL("clicked()"), lambda who="Seven": self.clickBtn(who))
        self.connect(self.pb8, SIGNAL("clicked()"), lambda who="Eight": self.clickBtn(who))
        self.connect(self.pb9, SIGNAL("clicked()"), lambda who="Nine": self.clickBtn(who))
        self.connect(self.pbac, SIGNAL("clicked()"), lambda who="AC": self.clickBtn(who))
        self.connect(self.pbpom, SIGNAL("clicked()"), lambda who="POM": self.clickBtn(who))
        self.connect(self.pbprcen, SIGNAL("clicked()"), lambda who="PrCen": self.clickBtn(who))
        self.connect(self.pbdiv, SIGNAL("clicked()"), lambda who="Div": self.clickBtn(who))
        self.connect(self.pbmul, SIGNAL("clicked()"), lambda who="Mul": self.clickBtn(who))
        self.connect(self.pbsub, SIGNAL("clicked()"), lambda who="Sub": self.clickBtn(who))
        self.connect(self.pbadd, SIGNAL("clicked()"), lambda who="Add": self.clickBtn(who))
        self.connect(self.pbeq, SIGNAL("clicked()"), lambda who="Equal": self.clickBtn(who))
        self.connect(self.pbdec, SIGNAL("clicked()"), lambda who="Dec": self.clickBtn(who))

    def clickBtn(self, who):
        print "%s Clicked!" % str(who)
        self.listelts.append(str(who))
        self.model = QStringListModel(self.listelts)
        self.screen.setModel(self.model)


def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


