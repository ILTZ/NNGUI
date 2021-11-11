import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QBoxLayout, QDialog, QFileDialog, QGroupBox, QHBoxLayout, QLabel, QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QScrollBar

dirname = os.path.dirname(__file__)
filenameCloseIcon = os.path.join(dirname, 'resources/close.png')

def getMask(object, x = 10, y = 10):
    PP = QtGui.QPainterPath() 
    PP.addRoundedRect(QtCore.QRectF(object.rect()), x, y)
    mask = QtGui.QRegion(PP.toFillPolygon().toPolygon())
    return mask

##Parent for QDialog {
class GUIDialogOrigin(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.closeBtn = QPushButton(self)
        self.closeBtn.hide()
        self.closeBtn.setFixedSize(40,20)
        self.closeBtn.clicked.connect(self.closeWindow)
               

    def setCustomMask(self):
        PP = QtGui.QPainterPath() 
        PP.addRoundedRect(QtCore.QRectF(self.rect()), 10.0, 10.0)
        mask = QtGui.QRegion(PP.toFillPolygon().toPolygon())
        self.setMask(mask)
        pass 

    def setButtons(self, x = 20, y = 0):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(filenameCloseIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.closeBtn.setGeometry(QtCore.QRect(self.width() - x, y, 31, 19))
        self.closeBtn.setObjectName("dialogCloseBtn")
        self.closeBtn.setIcon(icon)
        self.closeBtn.show()
        pass

    def deleteButton(self):
        self.closeBtn.deleteLater()
        pass

    def closeWindow(self):
        self.close()
        self.deleteLater()
        pass
    pass
##Parent for QDialog }

class HelpDialog(GUIDialogOrigin):
    def __init__(self, param):
        super().__init__()
        if (param == "def"):
            return
        self.setupUi(param)

        self.setFixedSize(self.size())
        GUIDialogOrigin.setCustomMask(self)
        GUIDialogOrigin.setButtons(self, 50, 10)

    def setupUi(self, param):
        
        ##FAQ_Dialog {
        if (param == "faq"):
            self.setObjectName("FAQDialog")
            self.setWindowModality(QtCore.Qt.NonModal)
            self.resize(640, 360)
            self.gridLayout = QtWidgets.QGridLayout(self)
            self.gridLayout.setObjectName("gridLayout")
            self.scrollArea = QtWidgets.QScrollArea(self)
            self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
            self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setObjectName("scrollArea")
            self.scrollAreaWidgetContents = QtWidgets.QWidget()
            self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 598, 1076))
            self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
            self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
            self.gridLayout_2.setObjectName("gridLayout_2")
            self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            self.frame.setMinimumSize(QtCore.QSize(0, 900))
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
            self.gridLayout_4.setObjectName("gridLayout_4")
            self.label_7 = QtWidgets.QLabel(self.frame)
            self.label_7.setMinimumSize(QtCore.QSize(0, 200))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(12)
            self.label_7.setFont(font)
            self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.label_7.setWordWrap(True)
            self.label_7.setObjectName("label_7")
            self.gridLayout_4.addWidget(self.label_7, 5, 0, 1, 1)
            self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            self.groupBox_3.setFont(font)
            self.groupBox_3.setObjectName("groupBox_3")
            self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
            self.gridLayout_6.setObjectName("gridLayout_6")
            self.label_4 = QtWidgets.QLabel(self.groupBox_3)
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(False)
            font.setWeight(50)
            self.label_4.setFont(font)
            self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.label_4.setWordWrap(True)
            self.label_4.setObjectName("label_4")
            self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
            self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 1)
            self.groupBox = QtWidgets.QGroupBox(self.frame)
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            self.groupBox.setFont(font)
            self.groupBox.setObjectName("groupBox")
            self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
            self.gridLayout_3.setObjectName("gridLayout_3")
            self.label = QtWidgets.QLabel(self.groupBox)
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(False)
            font.setWeight(50)
            self.label.setFont(font)
            self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.label.setWordWrap(True)
            self.label.setObjectName("label")
            self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
            self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
            self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            self.groupBox_4.setFont(font)
            self.groupBox_4.setObjectName("groupBox_4")
            self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
            self.gridLayout_7.setObjectName("gridLayout_7")
            self.label_5 = QtWidgets.QLabel(self.groupBox_4)
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(False)
            font.setWeight(50)
            self.label_5.setFont(font)
            self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.label_5.setWordWrap(True)
            self.label_5.setObjectName("label_5")
            self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)
            self.gridLayout_4.addWidget(self.groupBox_4, 3, 0, 1, 1)
            self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            self.groupBox_5.setFont(font)
            self.groupBox_5.setObjectName("groupBox_5")
            self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_5)
            self.gridLayout_8.setObjectName("gridLayout_8")
            self.label_6 = QtWidgets.QLabel(self.groupBox_5)
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(False)
            font.setWeight(50)
            self.label_6.setFont(font)
            self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.label_6.setWordWrap(True)
            self.label_6.setObjectName("label_6")
            self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 1)
            self.gridLayout_4.addWidget(self.groupBox_5, 4, 0, 1, 1)
            self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            self.groupBox_2.setFont(font)
            self.groupBox_2.setObjectName("groupBox_2")
            self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
            self.gridLayout_5.setObjectName("gridLayout_5")
            self.label_3 = QtWidgets.QLabel(self.groupBox_2)
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(False)
            font.setWeight(50)
            self.label_3.setFont(font)
            self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.label_3.setWordWrap(True)
            self.label_3.setObjectName("label_3")
            self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
            self.gridLayout_4.addWidget(self.groupBox_2, 2, 0, 1, 1)
            self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.gridLayout.addWidget(self.scrollArea, 1, 1, 1, 1)
            self.label_2 = QtWidgets.QLabel(self)
            self.label_2.setMaximumSize(QtCore.QSize(300, 300))
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.label_2.setFont(font)
            self.label_2.setWordWrap(True)
            self.label_2.setObjectName("label_2")
            self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
            self.retranslateUi(param)
            QtCore.QMetaObject.connectSlotsByName(self)
            return
            ##FAQ_Dialog }
            

        ##Learn_/Query_/Prop_ Dialog {
        oName = ""
        wRect = QtCore.QRect()
        wSize = []
        lRect = QtCore.QRect()

        if (param == "learn"):
            oName = "helpLearnDialog"
            wRect = QtCore.QRect(10,30,640,480)
            wSize = [660,520]
            lRect = QtCore.QRect(20,30,610,450)
            pass
        elif(param == "query"):
            oName = "helpQueryDialog"
            wRect = QtCore.QRect(10,30,640,160)
            wSize = [660,200]
            lRect = QtCore.QRect(20,30,620,500)
            pass
        elif(param == "prop"):
            oName = "htlpPropDialog"
            wRect = QtCore.QRect(10,30,640,440)
            wSize = [660,480]
            lRect = QtCore.QRect(20,30,620,410)
            pass
        
        self.setObjectName(oName)
        self.resize(wSize[0], wSize[1])
        self.textGroupBox = QtWidgets.QGroupBox(self)
        self.textGroupBox.setGeometry(wRect)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textGroupBox.setFont(font)
        self.textGroupBox.setObjectName("textGroupBox")
        self.label = QtWidgets.QLabel(self.textGroupBox)
        self.label.setGeometry(lRect)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.retranslateUi(param)
        QtCore.QMetaObject.connectSlotsByName(self)
        ##Learn_/Query_/Prop_ Dialog }

        pass

    def retranslateUi(self, param):
        _translate = QtCore.QCoreApplication.translate
        if (param == "learn"):
            self.setWindowTitle(_translate("helpLearnDialog", "Помощь"))
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
            pass
        elif(param == "query"):
            self.setWindowTitle(_translate("helpQueryDialog", "Помощь"))
            self.textGroupBox.setTitle(_translate("helpQueryDialog", "Опрос"))
            self.label.setText(_translate("helpQueryDialog", "В разделе \"Опрос\" проводится опрос нейросети.\n"
"Введите параметры в слоты \"Входные значения\" и нажмите кнопку \"Опрос\".\n"
"В окне результат опроса появится значение.\n"
"При проведении опроса сети без тренировки (или загруженных весов) результат\n"
"опроса непредсказуем, т.к. веса для сети генерируются случайным образрм\n"
"при каждом запуске программы."))
            pass
        elif(param == "prop"):
            self.setWindowTitle(_translate("htlpPropDialog", "Помощь"))
            self.textGroupBox.setTitle(_translate("htlpPropDialog", "Настройки"))
            self.label.setText(_translate("htlpPropDialog", "В разделе \"Настройки\" отображены текущие параметры нейронной сети, \n"
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
"Кнопки \"Сохранить/Загрузить веса\" отвечают за одноименные действия."))
        elif (param == "faq"):
            self.setWindowTitle(_translate("FAQDialog", "О программе"))
            self.label_7.setText(_translate("FAQDialog", "Более подробно про каждый раздел нейросети можно узнать, кликнув по кнопке \"Помощь\", а также кнопке \"Подсказка\" в соответствующих разделах."))
            self.groupBox_3.setTitle(_translate("FAQDialog", "\"Меню\""))
            self.label_4.setText(_translate("FAQDialog", "Во вкладке \"Меню\" (левый верхний угол), кликнув по соответствующей кнопке, пользователь может увидеть текущие параметры нейросети. Также, по нажатию на кнопку \"Загрузить из внешнего файла\" можно выбрать файл с выборкой данных. Сама выборка должна быть подготовлена (все переменные нормированы) и представлена в формате \"X.X,X.X,X.X......Y.Y\", где \"X.X\" - входной параметр, \"Y.Y\" - целевое значение. Последнее значение в строке выборки всегда будет целевым значением элемента выборки этой строки."))
            self.groupBox.setTitle(_translate("FAQDialog", "Назначение"))
            self.label.setText(_translate("FAQDialog", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Программа предназначена для численного решения широкого класса задач. Исходные данные вводятся в нормированном, т.е. в безразмерном виде от 0 до 1 виде, что делает ее универсальной.</span></p></body></html>"))
            self.groupBox_4.setTitle(_translate("FAQDialog", "Раздел \"Прогон\""))
            self.label_5.setText(_translate("FAQDialog", "В данном разделе происходит стандартный опрос сети (пользователь вводит значения, ожидая\n"
"получить требуемый результат). Производить стандартный опрос имеет смысл лишь после обучения сети на какой-либо выборке данных."))
            self.groupBox_5.setTitle(_translate("FAQDialog", "Раздел \"Настройки\""))
            self.label_6.setText(_translate("FAQDialog", "<html><head/><body><p>Данный раздел отвечает за внутренние параметры сети. В левой части экрана пользователь может изменять количество входных/выходных значений, количество нейронов в 1-м и 2-м скрытых слоях (после данных изменений веса должны быть сгенерированы заново, за что отвечает одноименная кнопка). Параметры &quot;Количество циклов&quot; и &quot;Количество эпох&quot; будут определять, на сколько точно нейросеть будет обучена на представляемой выборке. Параметр &quot;Коэффициент обучения&quot; отвечает за то, на сколько &quot;быстро&quot; нейросеть будет обучаться (как сильно её веса будут меняться за 1 цикл). Если текущие веса нейросети удовлетворяют целям пользователя, он может их сохранить, нажав на кнопку &quot;Сохранить веса&quot;. &quot;Загрузить веса&quot; отвечает за одноименное действие.</p></body></html>"))
            self.groupBox_2.setTitle(_translate("FAQDialog", "Раздел \"Обучение\""))
            self.label_3.setText(_translate("FAQDialog", "<html><head/><body><p>В разделе обучения происходит старт и остановка обучения. Пользователь имеет возможность как вводить значения вручную(в соответствующие слоты для входных значений), так и использовать выборки из внешних файлов. Перед началом обучения убедитесь, что параметры нейронной сети (количество входных/выходных значений соответствуют вашим требованиям).</p></body></html>"))
            self.label_2.setText(_translate("FAQDialog", "NEIRONET V_1.0"))
            pass
        pass