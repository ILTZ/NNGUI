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

#Читай "интерфес" для общения с НН и корректной передачи в потоки гребаные
class NNControl(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    activate = QtCore.pyqtSignal()
    def __init__(self):
        QtCore.QObject.__init__(self)

        self.inputN = def_inputN
        self.hiddenN = def_hiddenN
        self.outputN = def_outputN
        self.learnRate = def_learnRate
        self.epochs = def_epochs
        self.learnLoops = def_loops

        self.NN = neuralNetwork(self.inputN, self.hiddenN, self.outputN, self.learnRate)

        self.inputVal = []
        self.targetVal = 0.0

        self.inputArr = []
        self.targetArr = []
    
    #Восстановление стандартных параметров
    def backToDefaultParams(self):
        self.inputN = def_inputN
        self.hiddenN = def_hiddenN
        self.outputN = def_outputN
        self.epochs = def_epochs
        self.learnLoops = def_loops

        self.inputVal.clear()
        self.targetVal = 0.0
        self.inputArr.clear()
        self.targetArr.clear()

        self.changeLinks(self.hiddenN, self.outputN)
        self.changeLearnRate(def_learnRate)
        pass
    #Геттеры/сеттеры
    def changeLinks(self, hiddenL, outL):
        self.NN.setWHH(hiddenL)
        self.NN.setWHO(outL)
        self.NN.reRandWHOWeights()
        self.NN.reRandWIHWeights()
        pass
    def changeLearnRate(self, newLR):
        self.learnRate = newLR
        self.NN.setLearnRate(newLR)
        pass
    def getLearnRate(self):
        return self.NN.getCurrentLearnRate()
    def setLearnLoops(self, newLL):
        self.learnLoops = newLL
        pass
    def getLearnLoops(self):
        return self.learnLoops()
    def setEpochs(self, newEpoc):
        self.epochs = newEpoc
        pass
    def getEpochs(self):
        return self.epochs
    #Обучение по вводимым вручную значениям
    def handLearn(self):
        for epochs in range(self.epochs):
            for count in range(self.learnLoops):
                self.NN.learnProcess(self.inputVal, self.targetVal)
        print("TrainSucces")
        self.finished.emit()
        pass
    #Обучение по значениям из файла
    def fileLearn(self):
        for epochs in range(self.epochs):
            for count in range(self.learnLoops):
                for i,t in zip(self.inputArr, self.targetArr):
                    self.NN.learnProcess(i, t)
        print("TrainSucces")
        pass
    #Стандартный опрос сети
    def defQuery(self, inputArr):
        return self.NN.query(inputArr)
    #Установка входных значений перед отправкой выполнения обучения в отдельный поток
    def setInputVal(self, inputArr, targetArr, param):
        if param == 0:
            self.inputVal = inputArr
            self.targetVal = targetArr
        elif param == 1:
            self.inputArr = inputArr
            self.targetArr = targetArr
        else:
            print("Uncorrect param")
        pass
    



class GUImm(QtWidgets.QMainWindow, Ui_shield.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ##slots
        self.learnStartBtn.clicked.connect(self.learnInDefThread)
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
        
        #Threadings
        self.MainThread = QtCore.QThread()
        self.INT = NNControl()

        self.INT.moveToThread(self.MainThread)
        self.MainThread.started.connect(self.INT.handLearn)
        self.INT.finished.connect(self.MainThread.quit)
        self.MainThread.finished.connect(self.correctThread)


        

    #Потоке
        

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
    def setPercents(self, currentVal, targetVal, epochs):
        showVal = currentVal / (targetVal * epochs)
        self.percentValue = showVal
        pass
    def showPercents(self, value):
        self.progressBar.setValue(value * 100.0)
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
        for epochs in range(self.epochs):
            for count in range(self.learnLoops):
                self.nn.learnProcess(self.hand_input_arr, self.hand_target_val)
                #self.setPercents(j, self.learnLoops, self.epochs)
                self.showPercents(count / (self.learnLoops * self.epochs))
        print("TrainSucces")
        pass
    #Когда тренировка запускается со значениями из внешнего файла
    def goToLearnFile(self):
        for epochs in range(self.epochs):
            for count in range(self.learnLoops):
                for i,t in zip(self.inputValues, self.targetValues):
                    self.nn.learnProcess(i, t)
                    #self.setPercents(count, self.learnLoops, self.epochs)
                    self.showPercents(count / (self.learnLoops * self.epochs))
        print("TrainSucces")
        pass
    ######################################################
    def learnInDefThread(self):
        #self.MainThread.started.connect(self.startLearn)
        #self.MainThread.finished.connect(self.MainThread.deleteLater)
        #self.MainThread.start()

        
        self.INT.setInputVal([1.0,1.0,1.0,1.0,1.0], [1.0], 0)
        self.MainThread.start()


        pass
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
        pass
    def correctThread(self):
        print("ThreadStopped")


    def defQuery(self):
        procName = 'query'
        try:
            inputArr = self.getParams(procName)
        except:
            print("Некоректные данные!")
            self.showDebugDialog("Некорректные данные!", 'error')
            self.clearQueryBoxes()
            return

        #self.outputLabel.setText(np.array2string(self.nn.query(inputArr)))
        self.outputLabel.setText(np.array2string(self.INT.defQuery(inputArr)))
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
        self.inputValuesBox.setVisible(param)
        self.targetValBox.setVisible(param)
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
    
    
        