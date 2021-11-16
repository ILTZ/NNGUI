# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Dev\neyroNet\code\NNCopyVsCode\NNGUI\uixml\helpLearnDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_helpLearnDialog(object):
    def setupUi(self, helpLearnDialog):
        helpLearnDialog.setObjectName("helpLearnDialog")
        helpLearnDialog.resize(663, 521)
        self.textGroupBox = QtWidgets.QGroupBox(helpLearnDialog)
        self.textGroupBox.setGeometry(QtCore.QRect(10, 30, 641, 481))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textGroupBox.setFont(font)
        self.textGroupBox.setObjectName("textGroupBox")
        self.label = QtWidgets.QLabel(self.textGroupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 611, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        self.retranslateUi(helpLearnDialog)
        QtCore.QMetaObject.connectSlotsByName(helpLearnDialog)

    def retranslateUi(self, helpLearnDialog):
        _translate = QtCore.QCoreApplication.translate
        helpLearnDialog.setWindowTitle(_translate("helpLearnDialog", "Помощь"))
        self.textGroupBox.setTitle(_translate("helpLearnDialog", "Обучение"))
        self.label.setText(_translate("helpLearnDialog", "В разделе \"Обучение\" проходит процесс выбора параметров, на которые будет\n"
"настраиваться нейросеть.\n"
"Данные для нейросети (выборка) могут быть как заданы в ручную, так и \n"
"выбраны из файла (при помощи кнопки в \"Меню\" в левом верхнем углу).\n"
"При задании данных в ручную необходимо ввести значения в слоты \"Входные\n"
"значения\", а также целевое для этих данных значение в слот \"Целевое значение\".\n"
"Загрузить выборку из файла можно в случае, если файл имеет расширение\n"
"\".txt\" и \".xlsx\". Для корректного чтение необходимо, чтобы:\n"
"1) Если файл имеет расширение \".txt\" - значения должны быть введены в \n"
"формате \"X.X,X.X,X.X,X.X_/t_Y.Y\", где X.X - одно из входных значений, Y.Y - \n"
"выходное значение, а _/t_ - табуляция (кнопка \"Tab\");\n"
"2) Если файл имеет расширение \".xlsx\" - одно значение должно занимать одну\n"
"ячейку (число должно быть разделено точкой), а последнее значение в строке\n"
"должно быть целевым для данной строки.\n"
"Кнопки \"Старт\" и \"Стоп\" выполняют одноименные действия в процессе\n"
"тренировки.\n"
"\"Оценка точности\" отвечает за то, на сколько корректно настроилась нейросеть\n"
"на представленную выборку, и работает только в случае загрузки выборки из \n"
"файла. Перед стартом тренировки выберите нужную погрешность, и после\n"
"завершения тренировки в строке \"Значение\" появится значение от 0.0 до 1.0,\n"
"где 0.0 - оценка точности неудовлетворительна, а 1.0 - сеть настроена точно\n"
"(относительно заданной погрешности)."))