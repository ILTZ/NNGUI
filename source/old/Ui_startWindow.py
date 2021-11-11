# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Dev\neyroNet\code\NNCopyVsCode\NNGUI\uixml\startWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(850, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f:\\Dev\\neyroNet\\code\\NNCopyVsCode\\NNGUI\\uixml\\resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LogoLabel = QtWidgets.QLabel(self.centralwidget)
        self.LogoLabel.setGeometry(QtCore.QRect(640, 10, 201, 61))
        self.LogoLabel.setText("")
        self.LogoLabel.setTextFormat(QtCore.Qt.RichText)
        self.LogoLabel.setPixmap(QtGui.QPixmap("f:\\Dev\\neyroNet\\code\\NNCopyVsCode\\NNGUI\\uixml\\../source/resources/logo.png"))
        self.LogoLabel.setScaledContents(True)
        self.LogoLabel.setWordWrap(False)
        self.LogoLabel.setObjectName("LogoLabel")
        self.StartWorkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.StartWorkBtn.setGeometry(QtCore.QRect(10, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.StartWorkBtn.setFont(font)
        self.StartWorkBtn.setStyleSheet("")
        self.StartWorkBtn.setAutoDefault(False)
        self.StartWorkBtn.setDefault(False)
        self.StartWorkBtn.setFlat(False)
        self.StartWorkBtn.setObjectName("StartWorkBtn")
        self.MainTextLabel = QtWidgets.QLabel(self.centralwidget)
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
        self.DevLabel = QtWidgets.QLabel(self.centralwidget)
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
        self.FAQBtn = QtWidgets.QPushButton(self.centralwidget)
        self.FAQBtn.setGeometry(QtCore.QRect(140, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.FAQBtn.setFont(font)
        self.FAQBtn.setAutoDefault(False)
        self.FAQBtn.setDefault(False)
        self.FAQBtn.setFlat(False)
        self.FAQBtn.setObjectName("FAQBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 20, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1, 110, 849, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("f:\\Dev\\neyroNet\\code\\NNCopyVsCode\\NNGUI\\uixml\\../source/resources/startWindowPict.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 480, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.LogoLabel.raise_()
        self.StartWorkBtn.raise_()
        self.DevLabel.raise_()
        self.FAQBtn.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.MainTextLabel.raise_()
        self.label_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "УГЛТУ"))
        self.StartWorkBtn.setText(_translate("MainWindow", "Начать работу"))
        self.MainTextLabel.setText(_translate("MainWindow", "НЕЙРОННАЯ СЕТЬ С ОБРАТНЫМ\n"
"РАСПРОСТРАНЕНИЕМ ОШИБКИ"))
        self.DevLabel.setText(_translate("MainWindow", "Разработал:           Писарев Илья Дмитриевич\n"
"\n"
"Руководитель:       проф., д.т.н. Побединский В. В."))
        self.FAQBtn.setText(_translate("MainWindow", "О программе"))
        self.label.setText(_translate("MainWindow", "Уральский государственный\n"
"лесотехнический университет"))
        self.label_3.setText(_translate("MainWindow", "Екатеринбург\n"
"2021"))
import style_rc
