# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Dev\neyroNet\code\NNCopyVsCode\NNGUI\uixml\FAQDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FAQDialog(object):
    def setupUi(self, FAQDialog):
        FAQDialog.setObjectName("FAQDialog")
        FAQDialog.resize(652, 811)
        self.groupBox_2 = QtWidgets.QGroupBox(FAQDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 340, 631, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 611, 81))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(FAQDialog)
        self.label_7.setGeometry(QtCore.QRect(20, 760, 611, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.groupBox_5 = QtWidgets.QGroupBox(FAQDialog)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 540, 631, 211))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 611, 181))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.groupBox_4 = QtWidgets.QGroupBox(FAQDialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 450, 631, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 611, 71))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.groupBox_3 = QtWidgets.QGroupBox(FAQDialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 220, 631, 121))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 611, 101))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(FAQDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(FAQDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 631, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 611, 141))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        self.retranslateUi(FAQDialog)
        QtCore.QMetaObject.connectSlotsByName(FAQDialog)

    def retranslateUi(self, FAQDialog):
        _translate = QtCore.QCoreApplication.translate
        FAQDialog.setWindowTitle(_translate("FAQDialog", "О программе"))
        self.groupBox_2.setTitle(_translate("FAQDialog", "Раздел \"Обучение\""))
        self.label_3.setText(_translate("FAQDialog", "В разделе обучения происходит старт и остановка обучения.\n"
"Пользователь имеет возможность как вводить значения вручную(в соответствующие слоты для\n"
"входных значений), так и использовать выборки из внешних файлов.\n"
"Перед началом обучения убедитесь, что параметры нейронной сети (количество входных/выходных\n"
"значений соответствуют вашим требованиям)."))
        self.label_7.setText(_translate("FAQDialog", "Более подробно про каждый раздел нейросети можно узнать, кликнув по кнопке \"Помощь\", а также \n"
"кнопке \"Подсказка\" в соответствующих разделах."))
        self.groupBox_5.setTitle(_translate("FAQDialog", "Раздел \"Настройки\""))
        self.label_6.setText(_translate("FAQDialog", "Данный раздел отвечает за внутренние параметры сети.\n"
"В левой части экрана пользователь может изменять количество входных/выходных значений,\n"
"количество нейронов в 1-м и 2-м скрытых слоях (после данных изменений веса должны быть сгене-\n"
"рированы заново, за что отвечает одноименная кнопка).\n"
"Параметры \"Количество циклов\" и \"Количество эпох\" будут определять, на сколько точно нейросеть\n"
"будет обучена на представляемой выборке. Параметр \"Коэффициент обучения\" отвечает за то,\n"
"на сколько \"быстро\" нейросеть будет обучаться (как сильно её веса будут меняться за 1 цикл).\n"
"Если текущие веса нейросети удовлетворяют целям пользователя, он может их сохранить, нажав\n"
"на кнопку \"Сохранить веса\". \n"
"\"Загрузить веса\" отвечает за одноименное действие (перед загрузкой весов необходимо привести\n"
"нейросеть в то состояние, в котором загружаемые веса сохранялись)."))
        self.groupBox_4.setTitle(_translate("FAQDialog", "Раздел \"Прогон\""))
        self.label_5.setText(_translate("FAQDialog", "В данном разделе происходит стандартный опрос сети (пользователь вводит значения, ожидая\n"
"получить требуемый результат).\n"
"Производить стандартный опрос имеет смысл лишь после обучения сети на какой-либо выборке\n"
"данных."))
        self.groupBox_3.setTitle(_translate("FAQDialog", "\"Меню\""))
        self.label_4.setText(_translate("FAQDialog", "Во вкладке \"Меню\" (левый верхний угол), кликнув по соответствующей кнопке, пользователь может\n"
"увидеть текущие параметры нейросети.\n"
"Также, по нажатию на кнопку \"Загрузить из внешнего файла\" можно выбрать файл с выборкой\n"
"данных. Сама выборка должна быть подготовлена (все переменные нормированы) и представлена\n"
" в формате \"X.X,X.X,X.X......Y.Y\", где \"X.X\" - входной параметр, \"Y.Y\" - целевое значение. Последнее\n"
"значение в строке выборки всегда будет целевым значением элемента выборки этой строки.\n"
""))
        self.label_2.setText(_translate("FAQDialog", "NEIRONET V_1.0"))
        self.groupBox.setTitle(_translate("FAQDialog", "Назначение"))
        self.label.setText(_translate("FAQDialog", "Программа предназначена для "))