# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'defaultpasswd.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(482, 523)
        self.pushButton = QtWidgets.QPushButton(GroupBox)
        self.pushButton.setGeometry(QtCore.QRect(180, 30, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(GroupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 30, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(GroupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 161, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(GroupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 110, 211, 31))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(GroupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 30, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(GroupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 170, 291, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(GroupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 230, 291, 31))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(GroupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(60, 290, 291, 31))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label = QtWidgets.QLabel(GroupBox)
        self.label.setGeometry(QtCore.QRect(10, 370, 461, 131))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("border-width: 1px;border-style: solid;background-color: rgb(152, 128, 129);")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(GroupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 41, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(GroupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 41, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(GroupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 41, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(GroupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 290, 41, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(GroupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 330, 81, 31))
        self.label_6.setObjectName("label_6")
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_3.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_6.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label.raise_()

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)



    def retranslateUi(self, GroupBox):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("GroupBox", "查询"))
        self.pushButton_2.setText(_translate("GroupBox", "更改"))
        self.pushButton_3.setText(_translate("GroupBox", "还原"))
        self.label_2.setText(_translate("GroupBox", "姓名"))
        self.label_3.setText(_translate("GroupBox", "密码"))
        self.label_4.setText(_translate("GroupBox", "电话"))
        self.label_5.setText(_translate("GroupBox", "id"))
        self.label_6.setText(_translate("GroupBox", "存储日志"))

