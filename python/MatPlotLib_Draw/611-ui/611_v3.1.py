# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import sys
from PyQt4 import QtCore, QtGui, uic
import eccel_solution
qtCreatorFile = "611.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.Start)

    def Start(self):
        path_in = self.path_in.toPlainText()
        if path_in == "":
            path_in = '/home/eacaen/PY_deal/GUI/611-paji/T06_10.xlsx'

        path_out = self.path_out.toPlainText()
        if path_out == "":
            path_out = 'result'

        frame = eccel_solution.Soluton(path_in, path_out)
        self.result_win.setText(str(frame))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())