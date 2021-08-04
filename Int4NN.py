from PyQt5 import QtWidgets, QtCore, QtGui
from NNVSCode import neuralNetwork

#def params NN
def_inputN = 5
def_hiddenN = 5
def_outputN = 1
def_learnRate = 0.3
def_epochs = 1
def_loops = 30000

#Читай "интерфейс" для общения с НН и корректной передачи в потоки гребаные
class NNControl(QtCore.QObject):
    #Сигнал для окончания потока
    finished = QtCore.pyqtSignal()
    #Сишнал для доступности кнопок
    finished4Btn = QtCore.pyqtSignal(bool)
    #Сигнал для отмены доступности кнопок
    activate4Btn = QtCore.pyqtSignal(bool)
    #Передает в окно сигнал со значением для отображения на прогресс-баре
    PBSignal = QtCore.pyqtSignal(float)
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

        self.zipInput = []

        self.learnFromFile = False
    
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
    def getCurrentWIH(self):
        return self.NN.getCurrentWIH()
    def getCurrentWHH(self):
        return self.NN.getCurrentWHH()
    def getCurrentWHO(self):
        return self.NN.getCurrentWHO()
    def changeLearnRate(self, newLR):
        self.learnRate = newLR
        self.NN.setLearnRate(newLR)
        pass
    def getLearnRate(self):
        return self.NN.getCurrentLearnRate()
    def setLearnRate(self, val):
        self.NN.setLearnRate(val)
    def setLearnLoops(self, newLL):
        self.learnLoops = newLL
        pass
    def getLearnLoops(self):
        return self.learnLoops
    def setEpochs(self, newEpoc):
        self.epochs = newEpoc
        pass
    def getEpochs(self):
        return self.epochs
    def getLFFStatus(self):
        return self.learnFromFile
    def setLFFStatus(self, val):
        self.learnFromFile = val
        pass
    #Обучение по вводимым вручную значениям
    def handLearn(self):
        it = 0
        for epochs in range(self.epochs):
            for count in range(self.learnLoops):
                self.NN.learnProcess(self.inputVal, self.targetVal)
                self.PBSignal.emit(it / (self.learnLoops * self.epochs))
                it += 1
        print("TrainSucces")
        self.PBSignal.emit(1)
        self.finished4Btn.emit(True)
        self.finished.emit()
        pass
    #Обучение по значениям из файла
    def fileLearn(self):
        it = 0
        for epochs in range(self.epochs):
            for count in range(self.learnLoops):
                for i,t in zip(self.inputArr, self.targetArr):
                    self.NN.learnProcess(i, t)
                    self.PBSignal.emit(it / (self.learnLoops * self.epochs))
                it += 1
        print("TrainSucces")
        self.PBSignal.emit(1)
        self.finished4Btn.emit(True)
        self.finished.emit()
        pass
    #Булево нужно для корректной работы с потоком, в котором выполняется(не смог придумать иначе и привязал старт потока к этой функции)
    def startLearnProcess(self):
        self.activate4Btn.emit(False)
        if (self.learnFromFile):
            self.fileLearn()
        else:
            self.handLearn()
        pass
    #Стандартный опрос сети
    def defQuery(self, inputArr):
        return self.NN.query(inputArr)
    #Установка входных значений перед отправкой выполнения обучения в отдельный поток(от параметра зависит, будут установленны
    # значения для обучения из формы, либо из файла)
    def setInputVal(self, inputArr, targetArr = 0, param = 1):
        if param == 0:
            self.inputVal = inputArr
            self.targetVal = targetArr
        elif param == 1:
            self.inputArr = inputArr[0]
            self.targetArr = inputArr[1]
        else:
            print("Uncorrect param")
        pass