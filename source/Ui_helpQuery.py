# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Dev\neyroNet\code\NNCopyVsCode\NNGUI\uixml\helpQuery.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
dirname = os.path.dirname(__file__)
filenameIcon = os.path.join(dirname, 'resources/icon.png')

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_helpWindow(object):
    def setupUi(self, helpWindow):
        helpWindow.setObjectName("helpWindow")
        helpWindow.resize(669, 207)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(filenameIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        helpWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(helpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.textGroupBox.setGeometry(QtCore.QRect(10, 10, 641, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textGroupBox.setFont(font)
        self.textGroupBox.setObjectName("textGroupBox")
        self.label = QtWidgets.QLabel(self.textGroupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 621, 501))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        helpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(helpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 21))
        self.menubar.setObjectName("menubar")
        helpWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(helpWindow)
        self.statusbar.setObjectName("statusbar")
        helpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(helpWindow)
        QtCore.QMetaObject.connectSlotsByName(helpWindow)

    def retranslateUi(self, helpWindow):
        _translate = QtCore.QCoreApplication.translate
        helpWindow.setWindowTitle(_translate("helpWindow", "Помощь"))
        self.textGroupBox.setTitle(_translate("helpWindow", "Опрос"))
        self.label.setText(_translate("helpWindow", "В разделе \"Опрос\" проводится опрос нейросети.\n"
"Введите параметры в слоты \"Входные значения\" и нажмите кнопку \"Опрос\".\n"
"В окне результат опроса появится значение.\n"
"При проведении опроса сети без тренировки (или загруженных весов) результат\n"
"опроса непредсказуем, т.к. веса для сети генерируются случайным образрм\n"
"при каждом запуске программы."))
