import os
dirname = os.path.dirname(__file__)
filepathStartSkin = os.path.join(dirname, 'resources/startWindowPict.png')
filenameLogo = os.path.join(dirname, 'resources/logo.png')
filenameIcon = os.path.join(dirname, 'resources/icon.png')
filenameErrorIcon = os.path.join(dirname, 'resources/errorIcon.png')
filenameInfoIcon = os.path.join(dirname, 'resources/infoIcon.png')

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QBoxLayout, QFileDialog, QMessageBox, QTextEdit, QVBoxLayout

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


##MainWindowClass {
class GUImm(QtWidgets.QMainWindow, Ui_shield.Ui_MainWindow):
    finished = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

##Icons and other cosmetic {
        self.setFixedSize(self.size())

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(filenameIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
        self.setWindowIcon(self.icon)

        self.errorIcon = QtGui.QIcon()
        self.errorIcon.addPixmap(QtGui.QPixmap(filenameErrorIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off) 

        self.infoIcon = QtGui.QIcon()
        self.infoIcon.addPixmap(QtGui.QPixmap(filenameInfoIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off) 

        #self.oNodesIn.setEnabled(False) ##Not work yet
        self.goToClose = False
        ##SubWindows
        self.startTitle = GUIstartWindow()
        self.startTitle.finished.connect(self.show)
        self.startTitle.FAQsig.connect(self.showAboutWindow)

        self.FAQTitle = GUIFaqWin()
        self.FAQTitle.setWindowIcon(self.icon)

        self.startTitle.setWindowIcon(self.icon)
        self.startTitle.setLogo(filenameLogo)

        self.helpLearnTitle = GUIhelpLearn()
        self.helpLearnTitle.setWindowIcon(self.icon)

        self.helpQueryWindow = GUIhelpQuery()
        self.helpQueryWindow.setWindowIcon(self.icon)
        
        self.helpPropWindow = GUIhelpProp()
        self.helpPropWindow.setWindowIcon(self.icon)

        ###Maski
        PP = QtGui.QPainterPath() 
        PP.addRoundedRect(QtCore.QRectF(self.rect()), 3, 3)
        mask = QtGui.QRegion(PP.toFillPolygon().toPolygon())
        self.setMask(mask)
        
        ##Startwindow
        PP2 = QtGui.QPainterPath()
        PP2.addRoundedRect(QtCore.QRectF(self.startTitle.rect()), 3, 3)
        mask2 = QtGui.QRegion(PP2.toFillPolygon().toPolygon())
        self.startTitle.setMask(mask2)
##Icons and other cosmetic }


#TextBoxes for take values from user {
        self.learnValuesBox = QVBoxLayout()
        self.learnValuesTracker = []
        self.inputValuesBox.setLayout(self.learnValuesBox)

        self.queryValuesBox = QVBoxLayout()
        self.queryValuesTracker = []
        self.inputValuesBox_2.setLayout(self.queryValuesBox)

        self.targetLearnValuesBox = QVBoxLayout()
        self.targetLearnValuesTracker = []
        self.targetValBox.setLayout(self.targetLearnValuesBox)
#TextBoxes for take values from user }


##Slots for buttons {
        ##LearnPage {
        self.learnStartBtn.clicked.connect(self.startTrain_Act)  
        self.StopBtn.clicked.connect(self.stopTrain_Act)
        self.learnHelpBtn.clicked.connect(self.showHelpLearnWindow_Act)
        ##LearnPage }
        
        ##QueryPage {
        self.queryBtn.clicked.connect(self.defQuery_Act)
        self.queryHelpBtn.clicked.connect(self.showHelpQueryHelpWindow_Act)
        ##QueryPage {

        ##SettingsPage {    
        self.LoadWeightsBtn.clicked.connect(self.loadWeights_Act)
        self.SaveWeightsBtn.clicked.connect(self.saveWeights_Act)   
        self.RerandWeightsBtn.clicked.connect(self.randWeights_Act) 
        self.chCountBtn.clicked.connect(self.neironsCount_Act)  
        self.chLinksBtn.clicked.connect(self.setNewLincks_Act)
        self.clearBtn.clicked.connect(self.clearParams_Act) 
        self.epochsLoopsBtn.clicked.connect(self.setNewLearnParams_Act) 
        self.settingsHelpBtn.clicked.connect(self.showHelpPropWindow_Act) 
        self.tabWidget_2.tabBarClicked.connect(self.showParams) #Show current params NN in textBoxes after go to the page
        ##SettingsPage }

        ##SideMenuButtons {
        self.currentParamBtn.triggered.connect(self.currentParams_Act) 
        self.loadFromFile.triggered.connect(self.loadFromFile_Act) 
        self.FAQbtn.triggered.connect(self.showAboutWindow_Act)
        self.exitAction_2.triggered.connect(self.close)
        ##SideMenuButtons {
##Slots for buttons }
        
##InitVariables {
        self.countOfNumbers = def_inputN
        self.hand_input_arr = []
        self.hand_target_val = 0.0
        self.inputValues = []
        self.targetValues = []  
        self.zipInput = []
##InitVariables }

##Threads {
        ##LearnProcessThread {
        self.learnFromFile = False   
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
        self.INT.DebugSignal.connect(self.showDebugDialog)  #Debug signal
        ##LearnProcessThread }

        ##ReadFromFileThread {
        self.ReadThread = QtCore.QThread()     
        self.UpLoader = FileUpLoader()    
        self.UpLoader.correctSignal.connect(self.fileUpLoadMessage)     
        self.UpLoader.correctSimbols.connect(self.showDebugDialog)    
        self.UpLoader.moveToThread(self.ReadThread)     
        self.ReadThread.started.connect(self.UpLoader.loadFromFile)    
        self.ReadThread.finished.connect(self.correctThread)
        ##ReadFromFileThread }
##Threads }

##FillGroupBoxes {
        self.refillValuesBoxes()
        self.refillTargetValueBoxes()
##FillGroupBoxes }

##CheckUserInput {  
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
##CheckUserInput }

##TextBoxes, debugMessageBoxes, helpBoxes {
    ##Fill groupBoxes learn/query/target {
    def clearValuesBoxes(self):
        self.learnValuesTracker.clear()
        self.queryValuesTracker.clear()
        for i in range(self.learnValuesBox.count()):
            item = self.learnValuesBox.takeAt(i)
            item2 = self.queryValuesBox.takeAt(i)
            del item
            del item2
            pass  
        for text,text1 in zip(self.inputValuesBox.findChildren(QtWidgets.QTextEdit), self.inputValuesBox_2.findChildren(QtWidgets.QTextEdit)):
            text.deleteLater()
            text1.deleteLater()
        pass
    
    def refillValuesBoxes(self):
        self.clearValuesBoxes()
        for i in range(self.INT.getCurrentWIH()):
            inputVal = QtWidgets.QTextEdit(self.inputValuesBox)
            inputVal.setFixedSize(51,31)
            inputVal.setObjectName(f"inputVal{i}")

            inputVal2 = QtWidgets.QTextEdit(self.inputValuesBox_2)
            inputVal2.setFixedSize(51,31)
            inputVal2.setObjectName(f"inputVal{i}")

            self.learnValuesBox.addWidget(inputVal)
            self.learnValuesTracker.append(inputVal)

            self.queryValuesBox.addWidget(inputVal2)
            self.queryValuesTracker.append(inputVal2)
            pass  
        pass
    
    def clearTargetValueBoxes(self):
        self.targetLearnValuesTracker.clear()
        for i in range(self.targetLearnValuesBox.count()):
            item = self.targetLearnValuesBox.takeAt(i)
            del item
        for text in self.targetValBox.findChildren(QtWidgets.QTextEdit):
            text.deleteLater()

        pass
    
    def refillTargetValueBoxes(self):
        self.clearTargetValueBoxes()
        for i in range(self.INT.getCurrentWHO()):
            targetVal = inputVal = QtWidgets.QTextEdit(self.targetValBox)
            targetVal.setFixedSize(51,31)
            targetVal.setObjectName(f"targettVal{i}")

            self.targetLearnValuesBox.addWidget(targetVal)
            self.targetLearnValuesTracker.append(targetVal)
        pass
    ##Fill groupBoxes learn/query/target }
    
    def setVisible4Input(self, param):  #Когда данные берутся из внешнего файла, боксы для входных значений нам уже не нужны
        #self.inputValuesBox.setVisible(param)
        #self.targetValBox.setVisible(param)

        self.inputValuesBox.setEnabled(param)
        self.targetValBox.setEnabled(param)

        pass
    
    def showHelpLearnTitle(self):
        self.helpLearnTitle.close()
        self.helpPropWindow.close()

        self.helpLearnTitle.show()
        pass
    
    def showHelpQueryTitle(self):
        self.helpLearnTitle.close()
        self.helpPropWindow.close()

        self.helpQueryWindow.show()
        pass
    
    def showHelpPropTitle(self):
        self.helpLearnTitle.close()
        self.helpQueryWindow.close()

        self.helpPropWindow.show()
        pass
       
    def clearLearnBoxes(self):
        for learnTB in self.learnValuesTracker:
                learnTB.setText("")
        pass
    
    def clearQueryBoxes(self):
        for queryTB in self.queryValuesTracker:
                queryTB.setText("")
        pass
    
    def clearTargetBoxes(self):
        for targetTB in self.targetLearnValuesTracker:
            targetTB.setText("")
            pass
    
    def clearAll(self):
        self.clearLearnBoxes()
        self.clearQueryBoxes()
        self.clearTargetBoxes()
    
    ##ShowSomethitg {
    def showCurrentParams(self):                    #Для отображения уставновленных параметров сети
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
    
    def showDebugDialog(self, message, type):       #Окно для отправки в него дебаг сообщений  
        if self.goToClose:
            return

        msgBox = QMessageBox()
        msgBox.setText(message)
        
        #msgBox.setStandardButtons(QMessageBox.standardButtons)
        if type == 'error':
            msgBox.setWindowTitle("ERROR")
            msgBox.setWindowIcon(self.errorIcon)
            #msgBox.setIcon(QMessageBox.Warning)
        elif type == 'info':
            msgBox.setWindowIcon(self.infoIcon)
            msgBox.setWindowTitle("INFO")
            #msgBox.setIcon(QMessageBox.Information)

        self.ReadThread.quit()
        msgBox.exec_()
        pass  
    
    def showPerformance(self):                      #Отображение точности сети
        if (self.learnFromFile):
            self.performanceLabel.setText(str(self.INT.getPerformanceRate()))
        pass
    
    def showPercents(self, value):                  #Значения для прогресс бара приходят сигналом из INT
        self.progressBar.setValue(value * 100.0)
        pass
    
    def correctThread(self):                        #Дебаг в консоль про потоки
        print("ThreadStopped")
    
    def showParams(self, index):    #При переключении на вкладку с настройками параметры заполняются из текущих параметров сети
        if (index == 2): #Через сигнал принимает индекс текущей вкладки
            self.hNodesIn.setText(str(self.INT.getCurrentWHH()))   
            self.oNodesIn.setText(str(self.INT.getCurrentWHO()))
            self.loopCount.setText(str(self.INT.getLearnLoops()))
            self.epochsCount.setText(str(self.INT.getEpochs()))
            self.learnRateBox.setText(str(self.INT.getLearnRate()))
            self.hiddenLayerCount1.setText(str(self.INT.getCurrentNeironsCount()[0]))
            self.HiddenLayerCount2.setText(str(self.INT.getCurrentNeironsCount()[1]))
        pass
    ##ShowSomethitg {
##TextBoxes, debugMessageBoxes, helpBoxes }


##Get parametrs from user {
    def getParams(self, param):
        x = []
        if param == 'learn':
            for learnTB in self.learnValuesTracker:
                x.append(float(learnTB.toPlainText()))

        elif param == 'query':
            for queryTB in self.queryValuesTracker:
                x.append(float(queryTB.toPlainText()))

        print(x)
        return x

    def getTargetVal(self):
        x = []
        for targetTB in self.targetLearnValuesTracker:
            x.append(float(targetTB.toPlainText()))
        return x
    #Получение значений с вкладки "Настройки"
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
##Get parametrs from user }
    

##Set parameters fo NN {  
    def setNewLinks(self):          #Смена количества входных/выходных значений
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
        self.INT.changeLinks(wIH, wHO, wIH)
        self.refillValuesBoxes()
        self.refillTargetValueBoxes()
        self.showDebugDialog("Параметры успешно изменены!", "info")
        pass  
    
    def rerandWeights(self):        #После смены может потребоваться перерандомить веса
        self.INT.rerandWeights()
        self.showDebugDialog("Новые веса сгенерированы.", 'info')
        pass
    
    def setNewLearnParams(self):    #Установка новых количество циклов, эпох и К-обучения, и количества нейронов в слоях
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
    
    def setNewNeironCounts(self):   #Установка нового количества нейронов в 1/2 слоях
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
##Set parameters fo NN }
    
##LoadFromFile { (<file_name>.txt/.xlsx)
    def setFilePath(self, path):
        self.UpLoader.setPath(path)
        pass
    
    def loadFile(self):
        #self.UpLoader.showPathWindow()

        path = QFileDialog.getOpenFileName(self, 'Open file', filter=("TextFiles (*.txt *.xlsx)"))
        if (path[0] == ""):
            print("UnLoaded")
            return
        self.setFilePath(path[0])
        self.UpLoader.setCountOfTargets(self.INT.getCurrentWHO())
        self.ReadThread.start()
        pass
    
    def setParametrsAfterRead(self):                #После загрузки из файла аплоадер подает сигнал, и GUI получает у него извлеченные из файла значения                                           
        self.zipInput = self.UpLoader.getValues()   #ток счас понял, что надо бы сразу в INT Отправлять
        pass
    
    def fileUpLoadMessage(self, bVal):      #После загрузки выборки аплодер отправит в ГУИ сигнал, чтобы сказать, что всё прошло успешно
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
##LoadFromFile }
    
    def closeEvent(self, event):
        result = QMessageBox.question(self, "Выход",
                                      "Закрыть программу?",
                                      QMessageBox.Yes | QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            self.goToClose = True

            self.INT.stopSignal = True
            self.helpLearnTitle.close()
            self.helpQueryWindow.close()
            self.helpPropWindow.close()
            self.FAQTitle.close()
            
            
            if (self.ReadThread.isRunning()):
                self.ReadThread.terminate()
                #self.ReadThread.wait()

            event.accept()

            

        pass


##MainProcessesNN { 
    def showAboutWindow(self):  #Отображение окна "О программе"
        self.FAQTitle.show()
        pass
    
    def clearParams(self):      #Сброс к дефолтным параметрам
        self.setVisible4Input(True)
        self.learnFromFile = False
        self.countOfNumbers = def_inputN

        self.inputValues.clear()
        self.targetValues.clear()
        self.epochs = def_epochs
        self.learnLoops = def_loops
        self.hand_target_val = 0.0
        self.hand_input_arr.clear()


        self.showPercents(0)
        self.clearAll()
        self.INT.backToDefaultParams()
        self.refillValuesBoxes()
        self.showDebugDialog("Параметры сброшены.", 'info')
        self.showParams(2)
        pass
    
    def startLearn(self):       #"Старт" обучения сетки
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
    
    def goToLearnHand(self):    #По факту - просто запускает поток обучения(та, что ниже - тоже самое)
        inputArr = []
        targetArr = []
        inputArr.append(self.hand_input_arr)
        targetArr.append(self.hand_target_val)
        # inputArr = self.hand_input_arr
        # targetArr = self.hand_target_val
        self.INT.setLFFStatus(False)
        self.INT.setInputVal(inputArr, targetArr, 0)
        self.LearnThread.start()
        pass
    
    def goToLearnFile(self):
        self.INT.setInputVal(self.zipInput)
        self.INT.setLFFStatus(True)
        self.INT.setPerfError(self.errorBox.value())

        self.LearnThread.start()
        pass
    
    def stopLearn(self):        #"Стоп" обучения сети
        self.INT.stopSignal = True
        pass
    
    def loadWeights(self):      #Загрузка весов
        path = QFileDialog.getOpenFileName(self, 'Open file')
        if (path[0] == ""):
            print("UnLoaded")
            return
        self.INT.loadWeights(path[0])
        pass
    
    def saveWeights(self):      #Сохранение весов
        path = QFileDialog.getSaveFileName(self, 'Save file')
        if (path[0] == ""):
            print("UnSaved")
            return
        self.INT.saveWeights(path[0])
        pass
    
    def defQuery(self):         #Стандартный опрос, наверное, тоже стоит в поток запихать(?)
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
##MainProcessesNN }

##ButtonsHandlers {
    def btnLock(self, val):        #Лок кнопок при начале обучения
        self.clearBtn.setEnabled(val)
        self.learnStartBtn.setEnabled(val)
        self.queryBtn.setEnabled(val)
        self.chLinksBtn.setEnabled(val)
        self.epochsLoopsBtn.setEnabled(val)
        self.errorBox.setEnabled(val)
        self.RerandWeightsBtn.setEnabled(val)
        self.chCountBtn.setEnabled(val)
        self.loadFromFile.setEnabled(val)
        self.SaveWeightsBtn.setEnabled(val)
        self.LoadWeightsBtn.setEnabled(val)
    
    def startTrain_Act(self):
        self.startLearn()
        pass
    
    def stopTrain_Act(self):
        self.stopLearn()
        pass
    
    def defaultParams_Act(self):
        self.clearParams()
        pass
    
    def loadWeights_Act(self):
        self.loadWeights()
        pass
    
    def saveWeights_Act(self):
        self.saveWeights()
        pass
    
    def defQuery_Act(self):
        self.defQuery()
        pass
    
    def randWeights_Act(self):
        self.rerandWeights()
        pass
    
    def neironsCount_Act(self):
        self.setNewNeironCounts()
        pass
    
    def setNewLincks_Act(self):
        self.setNewLinks()
        pass
    
    def clearParams_Act(self):
        self.clearParams()
        pass
    
    def setNewLearnParams_Act(self):
        self.setNewLearnParams()
        pass
    
    def currentParams_Act(self):
        self.showCurrentParams()
        pass
    
    def loadFromFile_Act(self):
        self.loadFile()
        pass
    
    def showAboutWindow_Act(self):
        self.showAboutWindow()
        pass
    
    def changeVisFAQLearn_Act(self):
        self.changeVisFAQLearn()
        pass
    
    def changeVisFAQSet_Act(self):
        self.changeVisFAQSet()
        pass
    
    def changeVisFAQQuery_Act(self):

        pass
    
    def showHelpLearnWindow_Act(self):
        self.showHelpLearnTitle()
        pass
    
    def showHelpQueryHelpWindow_Act(self):
        self.showHelpQueryTitle()
        pass
    
    def showHelpPropWindow_Act(self):
        self.showHelpPropTitle()
        pass
##ButtonsHandler }
##MainWindowClass }

##SubWindows {

##StartWindow{
import Ui_startDialog as SD
class GUIstartWindow(QtWidgets.QDialog, SD.Ui_Dialog):

    finished = QtCore.pyqtSignal()
    FAQsig = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.StartWorkBtn.clicked.connect(self.goToProgram)
        self.FAQBtn.clicked.connect(self.showFAQ)
        self.setFixedSize(self.size())
        self.exitBtn.clicked.connect(self.close)

        self.show()
        self.fastClose = True

        self.label_2.setPixmap(QtGui.QPixmap(filepathStartSkin))
        
    def setLogo(self, path):
        self.LogoLabel.setPixmap(QtGui.QPixmap(path))
        pass


    def goToProgram(self):
        self.fastClose = False
        self.finished.emit()
        self.close()
        pass
    def showFAQ(self):
        self.FAQsig.emit()
        pass
    

    def closeEvent(self, event):
        if (self.fastClose):
            result = QMessageBox.question(self, "Выход",
                                          "Закрыть программу?",
                                          QMessageBox.Yes | QMessageBox.No)
            event.ignore()

            if result == QMessageBox.Yes:
                event.accept()

            

        pass
    pass
##StartWindow{


##AboutProgrammWindow {
import Ui_FAQDialog as FD
class GUIFaqWin(QtWidgets.QDialog, FD.Ui_FAQDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
##AboutProgrammWindow }


##HelpLearnModeWeindow {
import Ui_helpLearnDialog as HD
class GUIhelpLearn(QtWidgets.QDialog, HD.Ui_helpLearnDialog)  :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
##HelpLearnModeWeindow }


##HelpQueryModeWindow {
import Ui_helpQueryDialog as QD
class GUIhelpQuery(QtWidgets.QDialog, QD.Ui_helpQueryDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
##HelpQueryModeWindow }


##HelpPropertiesModeWindow {
import Ui_helpPropDialog as PD
class GUIhelpProp(QtWidgets.QDialog, PD.Ui_htlpPropDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.setFixedSize(self.size())   
##HelpPropertiesModeWindow {

##SubWindows }