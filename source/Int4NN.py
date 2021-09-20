from PyQt5 import QtCore
from NNVSCode import neuralNetwork
from NNV2 import neuralNetwork2
import numpy as np


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
    #Дебаг сообщение
    DebugSignal = QtCore.pyqtSignal(str, str)
    def __init__(self):
        QtCore.QObject.__init__(self)

        self.inputN = def_inputN
        self.hiddenN = def_hiddenN
        self.outputN = def_outputN
        self.learnRate = def_learnRate
        self.epochs = def_epochs
        self.learnLoops = def_loops

        self.stopSignal = False
        #self.NN = neuralNetwork(self.inputN, self.hiddenN, self.outputN, self.learnRate)
        self.NN = neuralNetwork2(self.inputN, self.hiddenN, self.outputN, self.learnRate)

        self.inputVal = []
        self.targetVal = 0.0

        self.inputArr = []
        self.targetArr = []

        self.zipInput = []

        self.learnFromFile = False
        self.performanceError = 0.0
        self.performanceRate = 0.0
    
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

        self.learnFromFile = False
        self.NN.setDefaultParams()
        pass
    #Процесс смены количества связей и перерандома весов
    def changeLinks(self, hiddenL, outL, inputL = 5):
        self.NN.setWIH(inputL)
        self.NN.setWHH(hiddenL)
        self.NN.setWHO(outL)
        pass
    def rerandWeights(self):
        self.NN.randWeights4H1()
        self.NN.randWeights4H2()
        self.NN.randWeights4F()
        pass
    #Геттеры/сеттеры
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

    def setPerfError(self, value):
        self.performanceError = value
        pass
    def getPerformanceRate(self):
        return self.performanceRate

    def getCurrentNeironsCount(self):
        return self.NN.getCurrentNeironCount()
        pass
    def setCurrentNeironH2(self, arr):
        self.NN.setCurrentNeironCount(arr)
        pass
    #Обучение по вводимым вручную значениям
    def handLearn(self):
        print("HandLearn", self.epochs, self.learnLoops, self.learnFromFile)
        it = 0
        for epochs in range(self.epochs):
            for count in range(self.learnLoops):
                self.NN.learnProcess(self.inputVal, self.targetVal)
                self.PBSignal.emit(it / (self.learnLoops * self.epochs))
                it += 1
                if (self.stopSignal == True):
                    self.stopSignal = False
                    self.finished4Btn.emit(True)
                    self.DebugSignal.emit("Процесс тренировки остановлен.", 'info')
                    self.finished.emit()
                    return
        print("TrainSucces")
        self.PBSignal.emit(1)
        self.finished4Btn.emit(True)
        self.finished.emit()
        pass
    #Обучение по значениям из файла
    def fileLearn(self):
        print("FileLearn", self.epochs, self.learnLoops, self.learnFromFile)
        it = 0
        for epochs in range(self.epochs):
            for count in range(self.learnLoops):
                for i,t in zip(self.inputArr, self.targetArr):
                    self.NN.learnProcess(i, t)
                    self.PBSignal.emit(it / (self.learnLoops * self.epochs))
                it += 1
                if (self.stopSignal == True):
                    self.stopSignal = False
                    self.finished4Btn.emit(True)
                    self.DebugSignal.emit("Процесс тренировки остановлен.", 'info')
                    self.finished.emit()
                    return
        print("TrainSucces")
        self.performanceTest()
        self.PBSignal.emit(1)
        self.finished4Btn.emit(True)
        self.finished.emit()
        pass
    #Булево нужно для корректной работы с потоком, в котором выполняется(не смог придумать иначе и привязал старт потока к этой функции)
    def startLearnProcess(self):
        self.activate4Btn.emit(False)
        try:
            if (self.learnFromFile):
                self.fileLearn()
            else:
                self.handLearn()
            pass
        except:
            self.activate4Btn.emit(True)
            self.DebugSignal.emit("Проверьте параметры сети (после изменеия количества входных значений связи должны быть изменены)", 'error')
            self.finished.emit()
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
    def performanceTest(self):
        val = 0
        count = 0


        for i,t in zip(self.inputArr, self.targetArr):
            count += 1
            value = self.NN.query(i)

            inArrVal = 0
            for count in range(len(value)):
                minVal = t[0] - self.performanceError
                maxVal = t[0] + self.performanceError
                if ((value[count] < maxVal) and (value[count] > minVal)):
                    inArrVal += 1
            if (inArrVal == len(value)):
                val += 1

        self.performanceRate = val/count
        pass
    #Процесс схоранения/загрузки весов
    def saveWeights(self, path):
        ####################
        ##For 1-neirons net
        #HN1w = self.NN.HN.getWeights()
        #HN2w = self.NN.HN2.getWeights()
        #FNw = self.NN.FN.getWeights()
        #np.savez(path, HN1w, HN2w, FNw)
        #self.DebugSignal.emit("Веса сохранены.", 'info')

        ####################
        ##For multiNerirons net
        tempArr = []
        for i in range(self.NN.HiddenLayer1Count):
            tempArr.append(self.NN.HiddenLayer1[i].getWeights())
        tempArr2 = []
        for i in range(self.NN.HiddenLayer2Count):
            tempArr2.append(self.NN.HiddenLayer2[i].getWeights())
        tempArr3 = []
        tempArr3.append(self.NN.FN.getWeights())

        try:
            np.savez(path, tempArr, tempArr2, tempArr3)
        except:
            self.DebugSignal.emit("Невозможно сохранить!", "error")
            return

        self.DebugSignal.emit("Веса сохранены!", "info")
        pass
    def loadWeights(self, path):
        allArr = np.load(path)
        
        HN = allArr['arr_0']
        HN2 = allArr['arr_1']
        FN = allArr['arr_2']




        try:
            for i in range(len(HN)):
                self.NN.setWeights1st(HN[i],i)
            for i in range(len(HN2)):
                self.NN.setWeights2nd(HN2[i], i)
            self.NN.setFinalNeironWeights(FN[0])
        except:
            self.DebugSignal.emit("Несоответствие весов и нейронов!", "error")
            return

  

        

        self.DebugSignal.emit("Веса загружены и поставлены.", 'info')
        pass