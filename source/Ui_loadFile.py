# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Dev\neyroNet\code\NNCopyVsCode\NNGUI\uixml\loadFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 286)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.OkBtn.setGeometry(QtCore.QRect(240, 220, 75, 23))
        self.OkBtn.setObjectName("OkBtn")
        self.CancleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CancleBtn.setGeometry(QtCore.QRect(320, 220, 75, 23))
        self.CancleBtn.setObjectName("CancleBtn")
        self.pathLine = QtWidgets.QLineEdit(self.centralwidget)
        self.pathLine.setGeometry(QtCore.QRect(30, 160, 301, 16))
        self.pathLine.setObjectName("pathLine")
        self.LoadBtn = QtWidgets.QToolButton(self.centralwidget)
        self.LoadBtn.setGeometry(QtCore.QRect(340, 160, 25, 16))
        self.LoadBtn.setObjectName("LoadBtn")
        self.TypeFileBox = QtWidgets.QGroupBox(self.centralwidget)
        self.TypeFileBox.setGeometry(QtCore.QRect(9, -1, 131, 91))
        self.TypeFileBox.setObjectName("TypeFileBox")
        self.txtRBtn = QtWidgets.QRadioButton(self.TypeFileBox)
        self.txtRBtn.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.txtRBtn.setObjectName("txtRBtn")
        self.xlsxRBtn = QtWidgets.QRadioButton(self.TypeFileBox)
        self.xlsxRBtn.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.xlsxRBtn.setChecked(True)
        self.xlsxRBtn.setObjectName("xlsxRBtn")
        self.csvRBtn = QtWidgets.QRadioButton(self.TypeFileBox)
        self.csvRBtn.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.csvRBtn.setObjectName("csvRBtn")
        self.csvBox = QtWidgets.QGroupBox(self.centralwidget)
        self.csvBox.setGeometry(QtCore.QRect(160, 0, 221, 141))
        self.csvBox.setObjectName("csvBox")
        self.label = QtWidgets.QLabel(self.csvBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 201, 121))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Загрузка файла"))
        self.OkBtn.setText(_translate("MainWindow", "ОК"))
        self.CancleBtn.setText(_translate("MainWindow", "Отмена"))
        self.LoadBtn.setText(_translate("MainWindow", "..."))
        self.TypeFileBox.setTitle(_translate("MainWindow", "Тип файла"))
        self.txtRBtn.setText(_translate("MainWindow", ".txt"))
        self.xlsxRBtn.setText(_translate("MainWindow", ".xlsx"))
        self.csvRBtn.setText(_translate("MainWindow", ".csv"))
        self.csvBox.setTitle(_translate("MainWindow", "FAQ по csv"))
        self.label.setText(_translate("MainWindow", ".csv файлы - это тестовые  файлы,\n"
"где каждая строка данных\n"
"соответствует части всей выборки.\n"
"Значения отделены друг от друга \n"
"запятыми (или др. разделителями).\n"
"В случае с данной программой целевое\n"
"значение всегда должно стоять в\n"
"в начале строки, а разделителем быть\n"
"запятая."))