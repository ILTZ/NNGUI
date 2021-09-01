from os import path
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import Ui_shield
import Ui_startWindow
import Ui_FAQwindow
import Ui_helpLearn
import Ui_helpQuery
import Ui_helpProp


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

        self.oNodesIn.setEnabled(False)

        ##SubWindows
        self.startTitle = GUIstartWindow()
        self.startTitle.finished.connect(self.show)
        self.startTitle.FAQsig.connect(self.showAboutWindow)
        self.FAQTitle = GUIFaqWin()

        self.helpLearnTitle = GUIhelpLearn()
        self.helpQueryWindow = GUIhelpQuery()
        self.helpPropWindow = GUIhelpProp()
        ################################################################
        #____________________________________________________start slots
        #Вкладка "Обучение"
        self.learnStartBtn.clicked.connect(self.startTrain_Act)
        self.StopBtn.clicked.connect(self.stopTrain_Act)
        self.learnHelpBtn.clicked.connect(self.showHelpLearnWindow_Act)
        self.learnFAQBtn.clicked.connect(self.changeVisFAQLearn_Act)
        self.showFAQLearn = False
        self.FAQLearnBox.setVisible(False)
        ########################################################
        #Вкладка "Прогон"
        self.queryBtn.clicked.connect(self.defQuery_Act)
        self.queryHelpBtn.clicked.connect(self.showHelpQueryHelpWindow_Act)
        ########################################################
        #Вкладка "Настройки"
        self.LoadWeightsBtn.clicked.connect(self.loadWeights_Act)
        self.SaveWeightsBtn.clicked.connect(self.saveWeights_Act)
        self.RerandWeightsBtn.clicked.connect(self.randWeights_Act)
        self.chCountBtn.clicked.connect(self.neironsCount_Act)

        self.chLinksBtn.clicked.connect(self.setNewLincks_Act)
        self.clearBtn.clicked.connect(self.clearParams_Act)
        self.epochsLoopsBtn.clicked.connect(self.setNewLearnParams_Act)

        self.setingsFAQBtn.clicked.connect(self.changeVisFAQSet_Act)
        self.showFAQSet = False 
        self.FAQSettingsBox.setVisible(False)
        self.settingsHelpBtn.clicked.connect(self.showHelpPropWindow_Act)

        self.tabWidget_2.tabBarClicked.connect(self.showParams) #Чтобы во владке всегда стояли текущие параметры сети
        #########################################################
        #Кнопки "Меню"
        self.currentParamBtn.triggered.connect(self.currentParams_Act)
        self.loadFromFile.triggered.connect(self.loadFromFile_Act)
        self.FAQbtn.triggered.connect(self.showAboutWindow_Act)
        #_______________________________________________________end slots
        #################################################################
        

        #Количество принимаемых значений
        self.countOfNumbers = def_inputN

        self.hand_input_arr = []
        self.hand_target_val = 0.0
        self.inputValues = []
        self.targetValues = []  
        self.zipInput = []
        ####################################################################
        #_______________________________________________________start threads
        #############################
        #Поток для процесса обучения#
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
        ####################################
        #Поток для процесса загрузки файлов#
        self.ReadThread = QtCore.QThread()
        self.UpLoader = FileUpLoader()
        
        self.UpLoader.correctSignal.connect(self.fileUpLoadMessage)
        self.UpLoader.correctSimbols.connect(self.showDebugDialog)
        
        self.UpLoader.moveToThread(self.ReadThread)
        self.ReadThread.started.connect(self.UpLoader.loadFromFile)
        self.ReadThread.finished.connect(self.correctThread)
        #_______________________________________________________stop threads
        ####################################################################

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
    ###############################################################################################################################
    #_____________________________________________________________________________________visibilyty/debug (and enables) work start
    #
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
    
    def changeVisFAQLearn(self):
        self.showFAQLearn = not self.showFAQLearn
        self.FAQLearnBox.setVisible(self.showFAQLearn)
        pass
    def changeVisFAQSet(self):
        self.showFAQSet = not self.showFAQSet
        self.FAQSettingsBox.setVisible(self.showFAQSet)
        pass
    def setVisible4Input(self, param):  #Когда данные берутся из внешнего файла, боксы для входных значений нам уже не нужны
        self.inputValuesBox.setVisible(param)
        self.targetValBox.setVisible(param)
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
    #Очистка боксов от вводимых пользователем значений
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
    #
    #_____________________________________________________________________________________visibilyty/debug (and enables) work end
    #############################################################################################################################
    
    #####################################################################################
    #_________________________________________________________Get parrams from form start
    #
    #Получение начальных значений со вккладки "Обучение"
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
    def getTargetVal(self):
        try:
            return float(self.targetVal.toPlainText())
        except:
            self.targetVal.clear()
            return 'targetError'
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
    #
    #_________________________________________________________Get parrams from form end
    ###################################################################################
    
    ###################################################################################
    #_________________________________________________________Set parrams for net start
    #Установка новых значений во вкладке "Настройка"
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
        self.slotsEnDis()
        self.INT.changeLinks(wIH, wHO, wIH)
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
    #
    #_________________________________________________________Set parrams for net end
    ###################################################################################
    
    ######################################################################
    #_________________________________________________Load from file start
    #
    #Для загрузки файлов из <file_name>.txt/.xlsx
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
            self.woLoadFromFileBoxFAQ.setVisible(False)
        else:
            self.showDebugDialog("Ошибка при чтении файлов!", 'error')
            self.ReadThread.quit()
        pass
    #
    #__________________________________________________Load from file end
    #####################################################################

    #######################################################
    ##____________________________________Работа с сеткой
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
        self.woLoadFromFileBoxFAQ.setVisible(True)

        self.showPercents(0)
        self.clearAll()
        self.slotsEnDis()
        self.INT.backToDefaultParams()
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
        inputArr = self.hand_input_arr
        targetArr = self.hand_target_val
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
    #######################################################
    ##_____________________________________Функции кнопочек
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

#########################################
##Стартовое окно с лого/авторами и прочим
class GUIstartWindow(QtWidgets.QMainWindow, Ui_startWindow.Ui_MainWindow):

    finished = QtCore.pyqtSignal()
    FAQsig = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.StartWorkBtn.clicked.connect(self.goToProgram)
        self.FAQBtn.clicked.connect(self.showFAQ)

        self.show()



    def goToProgram(self):
        self.finished.emit()
        self.close()
        pass
    def showFAQ(self):
        self.FAQsig.emit()
        pass
    pass

####################
##Окно "О программе"
class GUIFaqWin(QtWidgets.QMainWindow, Ui_FAQwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
###################
##Окно помощи "Обучение"
class GUIhelpLearn(QtWidgets.QMainWindow, Ui_helpLearn.Ui_helpWindow)  :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

###################
##Окно помощи "Опрос"
class GUIhelpQuery(QtWidgets.QMainWindow, Ui_helpQuery.Ui_helpWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

###################
##Окно помощи "Настройки"
class GUIhelpProp(QtWidgets.QMainWindow, Ui_helpProp.Ui_helpWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)     