# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Dev\neyroNet\code\NNCopyVsCode\NNGUI\uixml\FUIfu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UploaderGUI(object):
    def setupUi(self, UploaderGUI):
        UploaderGUI.setObjectName("UploaderGUI")
        UploaderGUI.resize(411, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(UploaderGUI)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(UploaderGUI)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fileTypeGB = QtWidgets.QGroupBox(self.groupBox)
        self.fileTypeGB.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.fileTypeGB.setFont(font)
        self.fileTypeGB.setObjectName("fileTypeGB")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.fileTypeGB)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.rbCSV = QtWidgets.QRadioButton(self.fileTypeGB)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.rbCSV.setFont(font)
        self.rbCSV.setObjectName("rbCSV")
        self.verticalLayout_7.addWidget(self.rbCSV)
        self.rbXLSX = QtWidgets.QRadioButton(self.fileTypeGB)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.rbXLSX.setFont(font)
        self.rbXLSX.setChecked(True)
        self.rbXLSX.setObjectName("rbXLSX")
        self.verticalLayout_7.addWidget(self.rbXLSX)
        self.rbTXT = QtWidgets.QRadioButton(self.fileTypeGB)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.rbTXT.setFont(font)
        self.rbTXT.setObjectName("rbTXT")
        self.verticalLayout_7.addWidget(self.rbTXT)
        self.horizontalLayout_4.addWidget(self.fileTypeGB)
        self.numberGB = QtWidgets.QGroupBox(self.groupBox)
        self.numberGB.setMaximumSize(QtCore.QSize(250, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.numberGB.setFont(font)
        self.numberGB.setObjectName("numberGB")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.numberGB)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.spinBox = QtWidgets.QSpinBox(self.numberGB)
        self.spinBox.setMinimumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_4.addWidget(self.spinBox, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.numberGB)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pathTE = QtWidgets.QTextEdit(self.groupBox)
        self.pathTE.setMaximumSize(QtCore.QSize(10000, 20))
        self.pathTE.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pathTE.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pathTE.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.pathTE.setObjectName("pathTE")
        self.horizontalLayout_2.addWidget(self.pathTE)
        self.pathBtn = QtWidgets.QPushButton(self.groupBox)
        self.pathBtn.setMinimumSize(QtCore.QSize(75, 40))
        self.pathBtn.setObjectName("pathBtn")
        self.horizontalLayout_2.addWidget(self.pathBtn)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.aceptBtn = QtWidgets.QPushButton(self.groupBox)
        self.aceptBtn.setMinimumSize(QtCore.QSize(180, 30))
        self.aceptBtn.setObjectName("aceptBtn")
        self.horizontalLayout_3.addWidget(self.aceptBtn)
        self.cancleBtn = QtWidgets.QPushButton(self.groupBox)
        self.cancleBtn.setMinimumSize(QtCore.QSize(180, 30))
        self.cancleBtn.setObjectName("cancleBtn")
        self.horizontalLayout_3.addWidget(self.cancleBtn)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(UploaderGUI)
        QtCore.QMetaObject.connectSlotsByName(UploaderGUI)

    def retranslateUi(self, UploaderGUI):
        _translate = QtCore.QCoreApplication.translate
        UploaderGUI.setWindowTitle(_translate("UploaderGUI", "Dialog"))
        self.fileTypeGB.setTitle(_translate("UploaderGUI", "Тип файла"))
        self.rbCSV.setText(_translate("UploaderGUI", ".csv"))
        self.rbXLSX.setText(_translate("UploaderGUI", ".xlsx"))
        self.rbTXT.setText(_translate("UploaderGUI", ".txt"))
        self.numberGB.setTitle(_translate("UploaderGUI", "Количество целевых значений"))
        self.pathBtn.setText(_translate("UploaderGUI", "Выбрать"))
        self.aceptBtn.setText(_translate("UploaderGUI", "Принять"))
        self.cancleBtn.setText(_translate("UploaderGUI", "Отмена"))
