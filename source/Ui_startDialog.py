# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Dev\neyroNet\code\NNCopyVsCode\NNGUI\uixml\startDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 540)
        Dialog.setWhatsThis("")
        Dialog.setModal(False)
        self.MainTextLabel = QtWidgets.QLabel(Dialog)
        self.MainTextLabel.setGeometry(QtCore.QRect(250, 180, 381, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.MainTextLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MainTextLabel.setFont(font)
        self.MainTextLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MainTextLabel.setLineWidth(0)
        self.MainTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MainTextLabel.setObjectName("MainTextLabel")
        self.DevLabel = QtWidgets.QLabel(Dialog)
        self.DevLabel.setGeometry(QtCore.QRect(50, 370, 661, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DevLabel.setFont(font)
        self.DevLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DevLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.DevLabel.setObjectName("DevLabel")
        self.FAQBtn = QtWidgets.QPushButton(Dialog)
        self.FAQBtn.setGeometry(QtCore.QRect(160, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.FAQBtn.setFont(font)
        self.FAQBtn.setAutoDefault(False)
        self.FAQBtn.setDefault(False)
        self.FAQBtn.setFlat(False)
        self.FAQBtn.setObjectName("FAQBtn")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 110, 851, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("f:\\Dev\\neyroNet\\code\\NNCopyVsCode\\NNGUI\\uixml\\../source/resources/startWindowPict.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(360, 480, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(370, 20, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.StartWorkBtn = QtWidgets.QPushButton(Dialog)
        self.StartWorkBtn.setGeometry(QtCore.QRect(10, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.StartWorkBtn.setFont(font)
        self.StartWorkBtn.setStyleSheet("")
        self.StartWorkBtn.setAutoDefault(False)
        self.StartWorkBtn.setDefault(False)
        self.StartWorkBtn.setFlat(False)
        self.StartWorkBtn.setObjectName("StartWorkBtn")
        self.LogoLabel = QtWidgets.QLabel(Dialog)
        self.LogoLabel.setGeometry(QtCore.QRect(640, 10, 201, 61))
        self.LogoLabel.setText("")
        self.LogoLabel.setTextFormat(QtCore.Qt.RichText)
        self.LogoLabel.setPixmap(QtGui.QPixmap("f:\\Dev\\neyroNet\\code\\NNCopyVsCode\\NNGUI\\uixml\\../source/resources/logo.png"))
        self.LogoLabel.setScaledContents(True)
        self.LogoLabel.setWordWrap(False)
        self.LogoLabel.setObjectName("LogoLabel")
        self.MainTextLabel_2 = QtWidgets.QLabel(Dialog)
        self.MainTextLabel_2.setGeometry(QtCore.QRect(260, 200, 381, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.MainTextLabel_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MainTextLabel_2.setFont(font)
        self.MainTextLabel_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MainTextLabel_2.setLineWidth(0)
        self.MainTextLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.MainTextLabel_2.setObjectName("MainTextLabel_2")
        self.exitBtn = QtWidgets.QPushButton(Dialog)
        self.exitBtn.setGeometry(QtCore.QRect(710, 470, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.exitBtn.setFont(font)
        self.exitBtn.setStyleSheet("")
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setDefault(False)
        self.exitBtn.setFlat(False)
        self.exitBtn.setObjectName("exitBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "УГЛТУ"))
        self.MainTextLabel.setText(_translate("Dialog", "НЕЙРОННАЯ СЕТЬ С ОБРАТНЫМ\n"
"РАСПРОСТРАНЕНИЕМ ОШИБКИ"))
        self.DevLabel.setText(_translate("Dialog", "Разработал:           Писарев Илья Дмитриевич\n"
"\n"
"Руководитель:       проф., д.т.н. Побединский В. В."))
        self.FAQBtn.setText(_translate("Dialog", "О программе"))
        self.label_3.setText(_translate("Dialog", "Екатеринбург\n"
"2021"))
        self.label.setText(_translate("Dialog", "Уральский государственный\n"
"лесотехнический университет"))
        self.StartWorkBtn.setText(_translate("Dialog", "Начать работу"))
        self.MainTextLabel_2.setText(_translate("Dialog", "НЕЙРОННАЯ СЕТЬ С ОБРАТНЫМ\n"
"РАСПРОСТРАНЕНИЕМ ОШИБКИ"))
        self.exitBtn.setText(_translate("Dialog", "Выход"))
