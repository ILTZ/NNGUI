import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import Ui_shield
import threading
import numpy as np

from NNVSCode import neuralNetwork

#def params NN
def_inputN = 5
def_hiddenN = 5
def_outputN = 1
def_learnRate = 0.3
def_epochs = 1
def_loops = 30000


class GUImm(QtWidgets.QMainWindow, Ui_shield.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ##slots
        self.learnStartBtn.clicked.connect(self.startLearn)
        self.queryBtn.clicked.connect(self.defQuery)
        self.chLinksBtn.clicked.connect(self.setNewLinks)
        self.clearBtn.clicked.connect(self.clearParams)
        self.currentParamBtn.triggered.connect(self.showCurrentParams)
        self.loadFromFile.triggered.connect(self.loadFile)
        self.epochsLoopsBtn.clicked.connect(self.setNewLearnParams)
        self.tabWidget_2.tabBarClicked.connect(self.showParams)
        ##
        self.nn = neuralNetwork(def_inputN, def_hiddenN, def_outputN, def_learnRate)
        self.learnFromFile = False
        self.performanceBox.setVisible(False)
        ##def_variables
        self.inputValues = []
        self.targetValues = []
        self.epochs = def_epochs
        self.learnLoops = def_loops
        self.hand_input_arr = []
        self.hand_target_val = 0.0
        self.percentValue = 0.0

    def showDebugDialog(self, message, type):
        msgBox = QMessageBox()
        
        msgBox.setText(message)
        
        #msgBox.setStandardButtons(QMessageBox.standardButtons)
        if type == 'error':
            msgBox.setWindowTitle("ERROR")
            msgBox.setIcon(QMessageBox.Warning)
        elif type == 'info':
            msgBox.setWindowTitle("INFO")
            msgBox.setIcon(QMessageBox.Information)

        msgBox.exec_()
        pass
    def printDebugMessage(self, message, proc):
        self.debugLabel4Learn.clear()
        self.debugLabel4Query.clear()
        self.debugLabel4Links.clear()

        if proc == 'learn':
           self.debugLabel4Learn.setText(message)
        elif proc == 'query' :
            self.debugLabel4Query.setText(message)
        elif proc == 'link':
            self.debugLabel4Links.setText(message)
        pass
    def setPercents(self, targetVal, currentVal):
        showVal = currentVal / targetVal
        self.percentValue = showVal
        pass
    def showPercents(self):
        for i in range(self.learnLoops):
            self.progressBar.setValue(self.percentValue)
        pass

    #Получение начальных значений
    def getParams(self, param):
        if param == 'learn':
            first = float(self.inputVal1.toPlainText())
            second = float(self.inputVal2.toPlainText())
            thirth = float(self.inputVal3.toPlainText())
            fourth = float(self.inputVal4.toPlainText())
            fifth = float(self.inputVal5.toPlainText())
        elif param == 'query':
            first = float(self.inputVal1_2.toPlainText())
            second = float(self.inputVal2_2.toPlainText())
            thirth = float(self.inputVal3_2.toPlainText())
            fourth = float(self.inputVal4_2.toPlainText())
            fifth = float(self.inputVal5_2.toPlainText())

        x = [first, second, thirth, fourth, fifth]
        return x

    def getTargetVal(self):
        try:
            return float(self.targetVal.toPlainText())
        except:
            self.targetVal.clear()
            return 'targetError'
    def getLearnLoops(self):
        try:
            return int(self.loopCount.toPlainText())
        except:
            self.loopCount.clear()
            return -1
    def getLearnEpochs(self):
        try:
            return int(self.epochsCount.toPlainText())
        except:
            self.epochsCount.clear()
            return -1
    def getLearnRate(self):
        try:
            return float(self.learnRateBox.toPlainText())
        except:
            self.learnRateBox.clear()
            return -1.0
    
    ######################################################
    def clearLearnBoxes(self):
        self.inputVal1.clear()
        self.inputVal2.clear()
        self.inputVal3.clear()
        self.inputVal4.clear()
        self.inputVal5.clear()
        self.targetVal.clear()
        self.loopCount.clear()
    def clearQueryBoxes(self):
        self.inputVal1_2.clear()
        self.inputVal2_2.clear()
        self.inputVal3_2.clear()
        self.inputVal4_2.clear()
        self.inputVal5_2.clear()
        self.outputLabel.clear()
    def clearTargetBoxes(self):
        self.targetVal.clear()
    def clearDebagPanels(self):
        self.debugLabel4Links.clear()
        self.debugLabel4Learn.clear()
        self.debugLabel4Query.clear()
    
    def clearAll(self):
        self.clearLearnBoxes()
        self.clearQueryBoxes()
        self.clearTargetBoxes()
        self.clearDebagPanels()
    ######################################################
    def setNewLinks(self):
        procName = 'link'
        wIH = 0
        wHO = 0

        try:
            wIH = int(self.hNodesIn.toPlainText())
            wHO = int(self.oNodesIn.toPlainText())
        except:
            self.hNodesIn.clear()
            self.oNodesIn.clear()
            self.showDebugDialog('Введите значения типа "int".', 'error')
            return


        self.nn.setWHH(wIH)
        self.nn.setWHO(wHO)
        pass
    def setNewLearnParams(self):
        
        newLL = self.getLearnLoops()
        newLE = self.getLearnEpochs()
        newLR = self.getLearnRate()
        print(newLL)

        if ((newLL) < 0 or (newLE < 0)):
            self.showDebugDialog('Введите корректные значения для количества циклов и эпох!', 'error')
            return
        if ((newLR > 1.0) or (newLR < 0.0)):
            self.showDebugDialog('Введите корректное значение коэффициента ошибки!\n(оно должно быть > 0.0 и < 1.0)', 'error')
            return

        
        self.nn.setLearnRate(newLR)
        self.epochs = int(newLE)
        self.learnLoops = int(newLL)

        self.showDebugDialog("Новые значения установлены!", 'info')
        pass
    #Для отображения уставновленных параметров сети
    def showCurrentParams(self):
        mes = (f"Количество входных значений: {self.nn.getCurrentWIH()}\n" +
        f"Количество скрытых нодов: {self.nn.getCurrentWHH()}\n" +
        f"Количество выходных значений: {self.nn.getCurrentWHO()}\n" +
        f"Количество циклов обучения: {self.learnLoops}\n" +
        f"Количество эпох: {self.epochs}\n" +
        f"Коэффициент ошибки: {self.nn.getCurrentLearnRate()}\n")

        self.showDebugDialog(mes, 'info')
        pass
    #Когда тренировка запускается со значениями из приложения
    def goToLearnHand(self):
        mutex = threading.Lock()
        mutex.acquire()

      
        self.nn.learn(self.hand_input_arr, self.hand_target_val, 0)

        self.printDebugMessage("Тренировка завершена.", 'learn')
        pass

        mutex.release()
    #Когда тренировка запускается со значениями из внешнего файла
    def goToLearnFile(self):
        mutex = threading.Lock()
        mutex.acquire()


        self.nn.learnProcess(self.inputValues, self.targetValues)

        mutex.release()
    ######################################################
    def startLearn(self):
        procName = 'learn'

        #В случае загрузки значенией из внешнего файла
        if self.learnFromFile == True:
            self.goToLearnFile()
        #В случае, если значения вводятся ручками
        else:
            try:
                self.hand_input_arr = self.getParams('learn')
                self.hand_target_val = self.getTargetVal()
            except:
                self.showDebugDialog("Введите корректные значения!", 'error')
                self.clearLearnBoxes()
                return
            self.goToLearnHand()



        self.printDebugMessage("Тренировка завершена!", procName)
        pass

    def defQuery(self):
        procName = 'query'
        try:
            inputArr = self.getParams(procName)
        except:
            print("Некоректные данные!")
            self.showDebugDialog("Некорректные данные!", 'error')
            self.clearQueryBoxes()
            return

        self.outputLabel.setText(np.array2string(self.nn.query(inputArr)))
        pass
   
    #Для загрузки файлов из <file_name>.txt
    def loadFile(self):
        #Данные читаются при записе их в виде <X.X,X.X,X.X.......'\t'Y.Y>
        #где X.X - входные значения, Y.Y - целевое, '\t' - табуляция
        name = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        try:
            n = open(name, 'r')
        except:
            self.printDebugMessage("Не удается открыть файл.", 'learn')
            return 

        stringVal = ""
        stringTarg = ""
        for line in n:
            stringVal = line.split('\t')[0]
            stringTarg = line.split('\t')[1]

            floatVal = [float(x) for x in stringVal.split(',')]

            self.inputValues.append(floatVal)
            self.targetValues.append(float(stringTarg))

        self.setVisible4Input(False)
        self.learnFromFile = True
        self.printDebugMessage('Данные успешно загружены!', 'query')
        pass
    ######################################################
    ######################################################
    #Когда данные берутся из внешнего файла, боксы для входных значений нам уже не нужны
    def setVisible4Input(self, param):
        vis = 0 
        if param == True:
            vis = True
        elif param == False:
            vis = False
        self.inputValuesBox.setVisible(vis)
        self.targetValBox.setVisible(vis)
        pass
    #Сброс к дефолтным параметрам
    def clearParams(self):
        self.nn.setDefaultParams()
        self.setVisible4Input(True)
        self.loadFile = False

        self.inputValues.clear()
        self.targetValues.clear()
        self.epochs = def_epochs
        self.learnLoops = def_loops
        self.hand_target_val = 0.0
        self.hand_input_arr = []

        self.clearAll()
        pass
    #Оценка точности
    def performanceTest(self):
        #points = 0
        #for i,t in zip(self.inputValues, self.targetValues):
        #    x = self.nn.query(i)
        #    if (i+self.)

        pass
    #При переключении на вкладку с настройками
    def showParams(self, index):
        if (index == 2):
            self.hNodesIn.setText(str(self.nn.getCurrentWHH()))   
            self.oNodesIn.setText(str(self.nn.getCurrentWHO()))
            self.loopCount.setText(str(self.learnLoops))
            self.epochsCount.setText(str(self.epochs))
            self.learnRateBox.setText(str(self.nn.getCurrentLearnRate()))
        pass
    
        