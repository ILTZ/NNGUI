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
        ##
        self.FAQLearnBox.setVisible(False)
        self.FAQSetingsBox.setVisible(False)
        self.showFAQLearn = False
        self.showFAQSet = False

        self.learnFromFile = False
        self.performanceBox.setVisible(False)  
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
        self.LearnThread.finished.connect(self.correctThread)
        #Поток для процесса занрузки фалов
        self.ReadThread = QtCore.QThread()
        self.UpLoader = FileUpLoader()
        #self.UpLoader.setParent(self)

        self.UpLoader.correctSignal.connect(self.fileUpLoadMessage)
        self.UpLoader.correctSimbols.connect(self.showDebugDialog)
        

        self.UpLoader.moveToThread(self.ReadThread)
        self.ReadThread.started.connect(self.UpLoader.loadFromFile)
        self.ReadThread.finished.connect(self.correctThread)
        
        
        

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
        else:
            self.showDebugDialog("Ошибка при чтении файлов!", 'error')
            self.ReadThread.quit()
        pass
    
    def setParametrsAfterRead(self):
        self.zipInput = self.UpLoader.getValues()
        pass

        
    #Отображение подсказок в форме
    def changeVisFAQLearn(self):
        self.showFAQLearn = not self.showFAQLearn
        self.FAQLearnBox.setVisible(self.showFAQLearn)
        pass
    def changeVisFAQSet(self):
        self.showFAQSet = not self.showFAQSet
        self.FAQSetingsBox.setVisible(self.showFAQSet)
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
    ######################################################
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

        self.INT.changeLinks(wIH, wHO)
        pass
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
    #Для отображения уставновленных параметров сети
    def showCurrentParams(self):
        mes = (f"Количество входных значений: {self.INT.getCurrentWIH()}\n" +
        f"Количество скрытых нодов: {self.INT.getCurrentWHH()}\n" +
        f"Количество выходных значений: {self.INT.getCurrentWHO()}\n" +
        f"Количество циклов обучения: {self.INT.getLearnLoops()}\n" +
        f"Количество эпох: {self.INT.getEpochs()}\n" +
        f"Коэффициент ошибки: {self.INT.getLearnRate()}\n")

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
        #self.INT.setInputVal(self.inputValues, self.targetValues, 1)
        self.INT.setInputVal(self.zipInput)
        self.INT.setLFFStatus(True)

        self.LearnThread.start()
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
    #Дебаг в консоль
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
        #self.outputLabel.setText(np.array2string(self.nn.query(inputArr)))
        self.outputLabel.setText(np.array2string(self.INT.defQuery(inputArr)))
        pass
    #Для загрузки файлов из <file_name>.txt
    def setFilePath(self, path):
        self.UpLoader.setPath(path)
        pass
    def loadFile(self):
        #Делегировать открытие окна UpLoader-у низя(т.к. нужен parent, а объекты с 
        # parent-ом низя передать в отдельный поток)
        name = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        self.setFilePath(name)
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
        #self.nn.setDefaultParams()
        self.setVisible4Input(True)
        self.learnFromFile = False


        self.inputValues.clear()
        self.targetValues.clear()
        self.epochs = def_epochs
        self.learnLoops = def_loops
        self.hand_target_val = 0.0
        self.hand_input_arr.clear()

        self.showPercents(0)
        self.clearAll()
        self.INT.backToDefaultParams()
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
    
        