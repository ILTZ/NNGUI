# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Dev\neyroNet\code\NNCopyVsCode\NNGUI\uixml\MBDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_messageDBox(object):
    def setupUi(self, messageDBox):
        messageDBox.setObjectName("messageDBox")
        messageDBox.resize(375, 190)
        self.gridLayout_2 = QtWidgets.QGridLayout(messageDBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(messageDBox)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.iconLabel = QtWidgets.QLabel(self.groupBox)
        self.iconLabel.setObjectName("iconLabel")
        self.verticalLayout.addWidget(self.iconLabel)
        self.gridLayout_3.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.messageLabel = QtWidgets.QLabel(self.groupBox)
        self.messageLabel.setFont(font)
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.messageLabel.setObjectName("messageLabel")
        self.verticalLayout_2.addWidget(self.messageLabel)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.emptyLabel1 = QtWidgets.QLabel(self.groupBox)
        self.emptyLabel1.setText("")
        self.emptyLabel1.setObjectName("emptyLabel1")
        self.horizontalLayout.addWidget(self.emptyLabel1)
        self.emptyLabel2 = QtWidgets.QLabel(self.groupBox)
        self.emptyLabel2.setText("")
        self.emptyLabel2.setObjectName("emptyLabel2")
        self.horizontalLayout.addWidget(self.emptyLabel2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(messageDBox)
        QtCore.QMetaObject.connectSlotsByName(messageDBox)

    def retranslateUi(self, messageDBox):
        _translate = QtCore.QCoreApplication.translate
        messageDBox.setWindowTitle(_translate("messageDBox", "Dialog"))
        self.iconLabel.setText(_translate("messageDBox", "iLabel"))
        self.messageLabel.setText(_translate("messageDBox", "mLabel"))