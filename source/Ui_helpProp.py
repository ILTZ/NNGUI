# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Dev\neyroNet\code\NNCopyVsCode\NNGUI\uixml\helpProp.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_helpWindow(object):
    def setupUi(self, helpWindow):
        helpWindow.setObjectName("helpWindow")
        helpWindow.resize(670, 487)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f:\\Dev\\neyroNet\\code\\NNCopyVsCode\\NNGUI\\uixml\\../source/resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        helpWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(helpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.textGroupBox.setGeometry(QtCore.QRect(10, 10, 641, 431))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 21))
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
        self.textGroupBox.setTitle(_translate("helpWindow", "Настройки"))
        self.label.setText(_translate("helpWindow", "В разделе \"Настройки\" отображены текущие параметры нейронной сети, \n"
"которые могут быть изменены пользователем.\n"
"Окна \"Количество входных/выходных значений\" отвечают за то, сколько\n"
"значений будет приниматься нейросетью на вход, и сколько значений она при\n"
"этом будет выводить (последняя функция ограничена).\n"
"Окна \"Количество нейронов\" отвечают за количество нейронов с 1-м и 2-м\n"
"скрытых слоях нейронной сети. \n"
"После изменения любых вышеприведенных параметров веса сети должны быть\n"
"сгенерированы занаво (отвечает кнопка \"Сгенерировать новые веса\").\n"
"Окна \"Количество эпох\" и \"Количество циклов\" определяют то, на сколько долго\n"
"сеть будет обучаться на представленной выборке (при выборке сыше 100\n"
"позиций имеет смысл сократить количество циклов и увеличить количество эпох).\n"
"\"Коэффициент обучения\" отвечает за то, на сколько сколько сильно сеть будет\n"
"изменять свои веса в процессе обучения (где 0.0 - вообще не изменяет, 1.0 - \n"
"изменяет максимально возможно).\n"
"После изменения любых параметров необходимо нажать на кнопку \"Изменить\",\n"
"чтобы новые настройки были приняты.\n"
"Кнопки \"Сохранить/Загрузить веса\" отвечают за одноименные действия. Перед\n"
"тем, как загрузить веса, необходимо привести параметры сети к тем, в которых\n"
"эти веса были сохранены (сеть не будет подстраивать под веса автоматически)."))
