from os import path
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import Ui_shield
import numpy as np



from Int4NN import NNControl
from fileUploader import FileUpLoader

#def params NN
def_inputN = 5
def_hiddenN = 5
def_outputN = 1
def_learnRate = 0.3
def_epochs = 1
def_loops = 30000

class GUImm(QtWidgets.QMainWindow, Ui_shield.Ui_MainWindow):
    finished = QtCore.pyqtSignal()
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

        self.learnFAQBtn.clicked.connect(self.changeVisFAQLearn)
        self.setingsFAQBtn.clicked.connect(self.changeVisFAQSet)

        #Веса
        self.LoadWeightsBtn.clicked.connect(self.loadWeights)
        self.SaveWeightsBtn.clicked.connect(self.saveWeights)
        self.RerandWeightsBtn.clicked.connect(self.rerandWeights)

        #Количество нейронов на слой
        self.chCountBtn.clicked.connect(self.setNewNeironCounts)
        ##
        self.FAQLearnBox.setVisible(False)
        #self.FAQSetingsBox.setVisible(False)
        #Переменные для отображения подсказок
        self.showFAQLearn = False
        self.showFAQSet = False

        self.learnFromFile = False

        #Количество принимаемых значений
        self.countOfNumbers = def_inputN

        self.hand_input_arr = []
        self.hand_target_val = 0.0
        self.inputValues = []
        self.targetValues = []  
        self.zipInput = []
        #Поток для процесса обучения
        self.LearnThread = QtCore.QThread()
        self.INT = NNControl()

        self.INT.PBSignal.connect(self.showPercents)
        self.INT.activate4Btn.connect(self.btnLock)
        self.INT.finished4Btn.connect(self.btnLock)

        self.INT.moveToThread(self.LearnThread)
        self.LearnThread.started.connect(self.INT.startLearnProcess)
        self.INT.finished.connect(self.LearnThread.quit)
        self.INT.finished.connect(self.showPerformance)
        self.LearnThread.finished.connect(self.correctThread)
        #Debug signal
        self.INT.DebugSignal.connect(self.showDebugDialog)
        #Поток для процесса загрузки файлов
        self.ReadThread = QtCore.QThread()
        self.UpLoader = FileUpLoader()
        
        self.UpLoader.correctSignal.connect(self.fileUpLoadMessage)
        self.UpLoader.correctSimbols.connect(self.showDebugDialog)
        
        self.UpLoader.moveToThread(self.ReadThread)
        self.ReadThread.started.connect(self.UpLoader.loadFromFile)
        self.ReadThread.finished.connect(self.correctThread)
    ##################################
    ##Проверка пользовательского ввода    
    def correctToInt(self, val):
        try:
            x = int(val)
        except:
            self.showDebugDialog("Введите значение типа <int> (целое число).", "error")
            return False
        return True
    def correctToFloat(self, val):
        try:
            x = float(val)
        except:
            self.showDebugDialog("Введите значение типа <float> (натуральная дробь).", "error")
            return False
        return True
    ##################################
    ##################################

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

        self.ReadThread.quit()
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
    def showPercents(self, value):
        self.progressBar.setValue(value * 100.0)
        pass
    def fileUpLoadMessage(self, bVal):
        if (bVal == True):
            self.showDebugDialog("Данные успешно загружены!", 'info')
            self.learnFromFile = True
            self.setParametrsAfterRead()
            self.ReadThread.quit()
            self.setVisible4Input(False)
            self.woLoadFromFileBoxFAQ.setVisible(False)
        else:
            self.showDebugDialog("Ошибка при чтении файлов!", 'error')
            self.ReadThread.quit()
        pass
    #После загрузки из файла аплоадер подает сигнал, и GUI получает у него извлеченные из файла значения
    #ток счас понял, что надо бы сразу в INT Отправлять
    def setParametrsAfterRead(self):
        self.zipInput = self.UpLoader.getValues()
        pass

    #Enable/disable слоты для входных значений после изменения количества входных значений
    def disSlots(self):
        self.inputVal1.setEnabled(False)
        self.inputVal1_2.setEnabled(False)

        self.inputVal2.setEnabled(False)
        self.inputVal2_2.setEnabled(False)

        self.inputVal3.setEnabled(False)
        self.inputVal3_2.setEnabled(False)

        self.inputVal4.setEnabled(False)
        self.inputVal4_2.setEnabled(False)

        self.inputVal5.setEnabled(False)
        self.inputVal5_2.setEnabled(False)
        pass
    def slotsEnDis(self):
        self.disSlots()
        for i in range(self.countOfNumbers):
            if (i == 0):
                self.inputVal1.setEnabled(True)
                self.inputVal1_2.setEnabled(True)
            if (i == 1):
                self.inputVal2.setEnabled(True)
                self.inputVal2_2.setEnabled(True)
            if (i == 2):
                self.inputVal3.setEnabled(True)
                self.inputVal3_2.setEnabled(True)
            if (i == 3):
                self.inputVal4.setEnabled(True)
                self.inputVal4_2.setEnabled(True)
            if (i == 4):
                self.inputVal5.setEnabled(True)
                self.inputVal5_2.setEnabled(True)
        pass

    #Отображение подсказок в форме
    def changeVisFAQLearn(self):
        self.showFAQLearn = not self.showFAQLearn
        self.FAQLearnBox.setVisible(self.showFAQLearn)
        pass
    def changeVisFAQSet(self):
        self.showFAQSet = not self.showFAQSet
        self.FAQSetingsBox.setVisible(self.showFAQSet)
    #############################
    #Получение начальных значений
    def getParams(self, param):
        #Хз как иначе брать из ячеек ровно то количество параметров, 
        #под которое в процессе работы может быть подстроена сетка
        x = []
        if param == 'learn':
            for i in range(self.countOfNumbers):
                if (i == 0):
                    first = float(self.inputVal1.toPlainText())
                    x.append(first)
                if (i == 1):
                    second = float(self.inputVal2.toPlainText())
                    x.append(second)
                if (i == 2):
                    thirth = float(self.inputVal3.toPlainText())
                    x.append(thirth)
                if (i == 3):
                    fourth = float(self.inputVal4.toPlainText())
                    x.append(fourth)
                if (i == 4):
                    fifth = float(self.inputVal5.toPlainText())
                    x.append(fifth)
        elif param == 'query':
            for i in range(self.countOfNumbers):
                if (i == 0):
                    first = float(self.inputVal1_2.toPlainText())
                    x.append(first)
                if (i == 1):
                    second = float(self.inputVal2_2.toPlainText())
                    x.append(second)
                if (i == 2):
                    thirth = float(self.inputVal3_2.toPlainText())
                    x.append(thirth)
                if (i == 3):
                    fourth = float(self.inputVal4_2.toPlainText())
                    x.append(fourth)
                if (i == 4):
                    fifth = float(self.inputVal5_2.toPlainText())
                    x.append(fifth)

        print(x)
        return x
    #############################
    #Получение значений с вкладки "Настройки"
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
    def getNeironCount(self): #количество нейронов в слоях
        H1 = int(self.hiddenLayerCount1.toPlainText())
        H2 = int(self.HiddenLayerCount2.toPlainText())
        return [H1, H2]
        pass
    ######################################################
    ######################################################
    #Очистка слотов от установленных значений
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

    
    def clearAll(self):
        self.clearLearnBoxes()
        self.clearQueryBoxes()
        self.clearTargetBoxes()

    ######################################################
    ######################################################
    #Установка новых значений
    #Смена количества входных/выходных значений
    def setNewLinks(self):
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

        self.countOfNumbers = wIH
        self.slotsEnDis()
        self.INT.changeLinks(wIH, wHO, wIH)
        self.showDebugDialog("Параметры успешно изменены!", "info")
        pass
    #После смены может потребоваться перерандомить веса
    def rerandWeights(self):
        self.INT.rerandWeights()
        self.showDebugDialog("Новые веса сгенерированы.", 'info')
        pass
    #Установка новых количество циклов, эпох и К-обучения
    def setNewLearnParams(self):
        newLL = self.getLearnLoops()
        newLE = self.getLearnEpochs()
        newLR = self.getLearnRate()

        if ((newLL) < 0 or (newLE < 0)):
            self.showDebugDialog('Введите корректные значения для количества циклов и эпох!', 'error')
            return
        if ((newLR > 1.0) or (newLR < 0.0)):
            self.showDebugDialog('Введите корректное значение коэффициента ошибки!\n(оно должно быть > 0.0 и < 1.0)', 'error')
            return

        self.INT.setLearnRate(newLR)
        self.INT.setEpochs(newLE)
        self.INT.setLearnLoops(newLL)
        self.showDebugDialog("Новые значения установлены!", 'info')
        pass
    
    def setNewNeironCounts(self):
        try:
            newCounts = self.getNeironCount()
        except:
            self.showDebugDialog("Введите корректноые значения количества нейронов!", "error")
            self.hiddenLayerCount1.clear()
            self.HiddenLayerCount2.clear()
            return
        
        self.INT.setCurrentNeironH2(newCounts)
        self.showDebugDialog("Новые значения нейронов установлены!", "info")
        pass

    #Для отображения уставновленных параметров сети
    def showCurrentParams(self):
        mes = (f"Количество входных значений: {self.INT.getCurrentWIH()}\n" +
        f"Количество скрытых нодов: {self.INT.getCurrentWHH()}\n" +
        f"Количество выходных значений: {self.INT.getCurrentWHO()}\n" +
        f"Количество циклов обучения: {self.INT.getLearnLoops()}\n" +
        f"Количество эпох: {self.INT.getEpochs()}\n" +
        f"Коэффициент ошибки: {self.INT.getLearnRate()}\n" + 
        f"Количество нейронов в 1-м скрытом слое: {self.INT.getCurrentNeironsCount()[0]}\n" + 
        f"Количество нейронов во 2-м скрытом слое: {self.INT.getCurrentNeironsCount()[1]}")

        self.showDebugDialog(mes, 'info')
        pass
    #Когда тренировка запускается со значениями из приложения
    def goToLearnHand(self):
        inputArr = self.hand_input_arr
        targetArr = self.hand_target_val
        self.INT.setLFFStatus(False)
        self.INT.setInputVal(inputArr, targetArr, 0)

        self.LearnThread.start()
        pass
    #Когда тренировка запускается со значениями из внешнего файла
    def goToLearnFile(self):
        self.INT.setInputVal(self.zipInput)
        self.INT.setLFFStatus(True)
        self.INT.setPerfError(self.errorBox.value())

        self.LearnThread.start()
        pass
    #Загрузка весов
    def loadWeights(self):
        path = QFileDialog.getOpenFileName(self, 'Open file')
        if (path[0] == ""):
            print("UnLoaded")
            return
        self.INT.loadWeights(path[0])
        pass
    def saveWeights(self):
        path = QFileDialog.getSaveFileName(self, 'Save file')
        if (path[0] == ""):
            print("UnSaved")
            return
        self.INT.saveWeights(path[0])
        pass
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
        pass
    #Дебаг в консоль про потоки
    def correctThread(self):
        print("ThreadStopped")
    #Стандартный опрос, наверное, тоже стоит в поток запихать(?)
    def defQuery(self):
        procName = 'query'
        try:
            inputArr = self.getParams(procName)
        except:
            print("Некоректные данные!")
            self.showDebugDialog("Некорректные данные!", 'error')
            self.clearQueryBoxes()
            return
        self.outputLabel.setText(np.array2string(self.INT.defQuery(inputArr)))
        pass
    #Для загрузки файлов из <file_name>.txt/.xlsx
    def setFilePath(self, path):
        self.UpLoader.setPath(path)
        pass
    def loadFile(self):
        #Делегировать открытие окна UpLoader-у низя(т.к. нужен parent, а объекты с 
        # parent-ом низя передать в отдельный поток)
        path = QFileDialog.getOpenFileName(self, 'Open file', filter=("TextFiles (*.txt *.xlsx)"))
        if (path[0] == ""):
            print("UnLoaded")
            return
        self.setFilePath(path[0])
        self.ReadThread.start()
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
        self.setVisible4Input(True)
        self.learnFromFile = False
        self.countOfNumbers = def_inputN

        self.inputValues.clear()
        self.targetValues.clear()
        self.epochs = def_epochs
        self.learnLoops = def_loops
        self.hand_target_val = 0.0
        self.hand_input_arr.clear()
        self.woLoadFromFileBoxFAQ.setVisible(True)

        self.showPercents(0)
        self.clearAll()
        self.slotsEnDis()
        self.INT.backToDefaultParams()
        pass
    #При переключении на вкладку с настройками параметры заполняются из текущих
    # параметров сети
    #Отображение производительности сети
    def showPerformance(self):
        if (self.learnFromFile):
            self.performanceLabel.setText(str(self.INT.getPerformanceRate()))
        pass
    def showParams(self, index):
        if (index == 2):
            self.hNodesIn.setText(str(self.INT.getCurrentWHH()))   
            self.oNodesIn.setText(str(self.INT.getCurrentWHO()))
            self.loopCount.setText(str(self.INT.getLearnLoops()))
            self.epochsCount.setText(str(self.INT.getEpochs()))
            self.learnRateBox.setText(str(self.INT.getLearnRate()))
        pass
    #Лок кнопока при начале обучения
    def btnLock(self, val):
        self.clearBtn.setEnabled(val)
        self.learnStartBtn.setEnabled(val)
        self.queryBtn.setEnabled(val)
        self.chLinksBtn.setEnabled(val)
        self.epochsLoopsBtn.setEnabled(val)
        self.errorBox.setEnabled(val)
        self.RerandWeightsBtn.setEnabled(val)
        self.chCountBtn.setEnabled(val)

    
    
        