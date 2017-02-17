# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '611-v3.35.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(421, 340)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Path_in = QtGui.QLabel(Dialog)
        self.Path_in.setObjectName(_fromUtf8("Path_in"))
        self.gridLayout.addWidget(self.Path_in, 0, 0, 1, 1)
        self.In_lineEdit = QtGui.QLineEdit(Dialog)
        self.In_lineEdit.setObjectName(_fromUtf8("In_lineEdit"))
        self.gridLayout.addWidget(self.In_lineEdit, 0, 1, 1, 1)
        self.File_choose_Button = QtGui.QPushButton(Dialog)
        self.File_choose_Button.setObjectName(_fromUtf8("File_choose_Button"))
        self.gridLayout.addWidget(self.File_choose_Button, 0, 2, 1, 1)
        self.Path_out = QtGui.QLabel(Dialog)
        self.Path_out.setObjectName(_fromUtf8("Path_out"))
        self.gridLayout.addWidget(self.Path_out, 1, 0, 1, 1)
        self.Out_lineEdit = QtGui.QLineEdit(Dialog)
        self.Out_lineEdit.setObjectName(_fromUtf8("Out_lineEdit"))
        self.gridLayout.addWidget(self.Out_lineEdit, 1, 1, 1, 1)
        self.Save_Button = QtGui.QPushButton(Dialog)
        self.Save_Button.setObjectName(_fromUtf8("Save_Button"))
        self.gridLayout.addWidget(self.Save_Button, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Result = QtGui.QLabel(Dialog)
        self.Result.setObjectName(_fromUtf8("Result"))
        self.horizontalLayout_2.addWidget(self.Result)
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.Solu_pushButton = QtGui.QPushButton(Dialog)
        self.Solu_pushButton.setObjectName(_fromUtf8("Solu_pushButton"))
        self.gridLayout_2.addWidget(self.Solu_pushButton, 0, 0, 1, 1)
        self.Fig_show_checkBox = QtGui.QCheckBox(Dialog)
        self.Fig_show_checkBox.setEnabled(True)
        self.Fig_show_checkBox.setMouseTracking(True)
        self.Fig_show_checkBox.setChecked(True)
        self.Fig_show_checkBox.setAutoRepeat(False)
        self.Fig_show_checkBox.setTristate(False)
        self.Fig_show_checkBox.setObjectName(_fromUtf8("Fig_show_checkBox"))
        self.gridLayout_2.addWidget(self.Fig_show_checkBox, 1, 0, 1, 1)
        self.Fig_save_checkBox = QtGui.QCheckBox(Dialog)
        self.Fig_save_checkBox.setObjectName(_fromUtf8("Fig_save_checkBox"))
        self.gridLayout_2.addWidget(self.Fig_save_checkBox, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.Close_pushButton = QtGui.QPushButton(Dialog)
        self.Close_pushButton.setObjectName(_fromUtf8("Close_pushButton"))
        self.gridLayout_2.addWidget(self.Close_pushButton, 4, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.Path_in.setBuddy(self.In_lineEdit)
        self.Path_out.setBuddy(self.Out_lineEdit)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Close_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Plot_Will", None))
        self.Path_in.setText(_translate("Dialog", "Path_&in", None))
        self.File_choose_Button.setText(_translate("Dialog", "&File", None))
        self.Path_out.setText(_translate("Dialog", "Path_&out", None))
        self.Save_Button.setText(_translate("Dialog", "&Save", None))
        self.Result.setText(_translate("Dialog", "Result", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "1", None))
        self.Solu_pushButton.setText(_translate("Dialog", "So&lution", None))
        self.Fig_show_checkBox.setText(_translate("Dialog", "Show_fig", None))
        self.Fig_save_checkBox.setText(_translate("Dialog", "Save_fig", None))
        self.Close_pushButton.setText(_translate("Dialog", "&Close", None))
