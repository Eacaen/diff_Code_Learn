# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pilao
import eccel_solution
import os
import pandas as pd

MAC = "qt_mac_set_native_menubar" in dir()


class FindAndReplaceDlg(QDialog , QMainWindow,pilao.Ui_Dialog):
    def __init__(self, parent=None):
        super(FindAndReplaceDlg, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)


        if not MAC:
            self.Solu_pushButton.setFocusPolicy(Qt.NoFocus)
            self.Close_pushButton.setFocusPolicy(Qt.NoFocus)

        self.__frame = pd.DataFrame()

        self.Solu_pushButton.clicked.connect(self.Start)

        self.connect(self.File_choose_Button, SIGNAL("clicked()"),self.fileOpen)

        self.connect(self.Save_Button, SIGNAL("clicked()"), self.fileSave)

        self.Save_Button.setEnabled(0)

        self.updateUi()
        self.setWindowTitle("Plot_Will")

    def Start(self):
        self.clear_result()
        path_in = self.In_lineEdit.text()
        if path_in == "":
            path_in = '/home/eacaen/PY_deal/GUI/611-paji/T06_10.xlsx'

        path_out = self.Out_lineEdit.text()
        if path_out == "":
            path_out = 'Result'

        Show_Fig = self.Fig_show_checkBox.isChecked()
        Save_Fig = self.Fig_save_checkBox.isChecked()

        if os.path.exists(path_in):
            try:
                self.Solu_pushButton.setEnabled(0)
                self.File_choose_Button.setEnabled(0)
                self.Save_Button.setEnabled(0)

                frame = eccel_solution.Soluton(path_in, path_out,Show_Fig,Save_Fig)
                self.__frame = frame

            except :
                QMessageBox.warning(self, "File Error", unicode('The format of the file is error'))

                self.Solu_pushButton.setEnabled(1)
                self.File_choose_Button.setEnabled(1)
                self.Save_Button.setEnabled(1)

            else:
                self.tableWidget.setHorizontalHeaderLabels(frame.columns)

                self.tableWidget.setRowCount( len(frame) )

                for i in range(self.tableWidget.rowCount()):
                    for j in range(self.tableWidget.columnCount()):
                        cnt = frame.iloc[i,j]
                        newItem = QTableWidgetItem( QString("%1").arg(cnt,0,'r',4) )
                        self.tableWidget.setItem(i, j, newItem)

                self.Solu_pushButton.setEnabled(1)
                self.File_choose_Button.setEnabled(1)
                self.Save_Button.setEnabled(1)
        else:
            QMessageBox.warning(self, "Path Error",unicode('The path error'))
            self.In_lineEdit.selectAll()
            self.In_lineEdit.setFocus()

    def updateUi(self):
        enable = self.In_lineEdit.text().isEmpty()
        self.File_choose_Button.setEnabled(enable)

    def fileOpen(self):
        s = QFileDialog.getOpenFileName(self, "Open file", " ", "Excel files(*.xlsx *.xls *.csv);;all files(*.*)")
        self.In_lineEdit.setText(QString(s))

    def fileSave(self):
        s = QFileDialog.getSaveFileName(self, "Save file", "./Result.xlsx", "Excel files(*.xlsx *.xls *.csv)")
        s = unicode(s)
        if s:
            if "." not in s:
                s += ".xlsx"
            self.Out_lineEdit.setText(QString(s))
            self.__frame.to_excel(s)

    @pyqtSignature("QString")
    def on_In_lineEdit_textEdited(self):
        self.updateUi()

    def clear_result(self):
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['1','2','3'])
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                newItem = QTableWidgetItem(QString(" "))
                self.tableWidget.setItem(i, j, newItem)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = FindAndReplaceDlg()
    form.updateUi()
    form.show()
    app.exec_()

