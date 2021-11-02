## Required import {
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QBoxLayout, QDialog, QFileDialog, QGroupBox, QHBoxLayout, QLabel, QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QScrollBar

import Ui_shield
import Ui_shield2
import Ui_shieldV3

from Int4NN import NNControl
from fileUploader import FileUpLoader
## Required import }


## PathToResources {
dirname = os.path.dirname(__file__)
filepathStartSkin = os.path.join(dirname, 'resources/startWindowPict.png')
filenameLogo = os.path.join(dirname, 'resources/logo.png')
filenameIcon = os.path.join(dirname, 'resources/icon.png')
filenameErrorIcon = os.path.join(dirname, 'resources/errorIcon.png')
filenameInfoIcon = os.path.join(dirname, 'resources/infoIcon.png')
filenameCloseIcon = os.path.join(dirname, 'resources/close.png')
## PathToResources }

def getMask(object, x = 10, y = 10):
    PP = QtGui.QPainterPath() 
    PP.addRoundedRect(QtCore.QRectF(object.rect()), x, y)
    mask = QtGui.QRegion(PP.toFillPolygon().toPolygon())
    return mask


## DefParams NN {
def_inputN = 5
def_hiddenN = 5
def_outputN = 1
def_learnRate = 0.3
def_epochs = 1
def_loops = 30000
## DefParams NN }

##Can move window without shape {
def setMoveWindow(widget):

    win = widget.window()
    cursorShape = widget.cursor().shape()
    moveSource = getattr(widget, "mouseMoveEvent")
    pressSource = getattr(widget, "mousePressEvent")
    releaseSource = getattr(widget, "mouseReleaseEvent")
    
    def move(event):
        if move.b_move:
            x = event.globalX() + move.x_korr - move.lastPoint.x()
            y = event.globalY() + move.y_korr - move.lastPoint.y()
            win.move(x, y)
            widget.setCursor(QtCore.Qt.SizeAllCursor)
        return moveSource(event)
    
    def press(event):
        if event.button() == QtCore.Qt.LeftButton:
            # Корекция геометрии окна: учитываем размеры рамки и заголовока
            x_korr = win.frameGeometry().x() - win.geometry().x()
            y_korr = win.frameGeometry().y() - win.geometry().y()
            # Корекция геометрии виджита: учитываем смещение относительно окна
            parent = widget
            while not parent == win:
                x_korr -= parent.x()
                y_korr -= parent.y()
                parent = parent.parent()
            move.__dict__.update({"lastPoint":event.pos(), "b_move":True, "x_korr":x_korr, "y_korr":y_korr})
        else:
            move.__dict__.update({"b_move":False})
            widget.setCursor(cursorShape)
        return pressSource(event)
    
    def release(event):
        move.__dict__.update({"b_move":False})
        widget.setCursor(cursorShape)
        return releaseSource(event)
    
    setattr(widget, "mouseMoveEvent", move)
    setattr(widget, "mousePressEvent", press)
    setattr(widget, "mouseReleaseEvent", release)
    move.__dict__.update({"b_move":False})
    return widget
##Source: https://www.cyberforum.ru/python-graphics/thread1692328.html
##Can move window without shape }

##Parent for QDialog {
class GUIDialogOrigin(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.closeBtn = QPushButton(self)
        self.closeBtn.setFixedSize(40,20)
        self.closeBtn.clicked.connect(self.closeWindow)
               

    def setCustomMask(self):
        PP = QtGui.QPainterPath() 
        PP.addRoundedRect(QtCore.QRectF(self.rect()), 3, 3)
        mask = QtGui.QRegion(PP.toFillPolygon().toPolygon())
        self.setMask(mask)
        pass 

    def setButtons(self, x = 20, y = 0):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(filenameCloseIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.closeBtn.setGeometry(QtCore.QRect(self.width() - x, y, 31, 19))
        self.closeBtn.setObjectName("dialogCloseBtn")
        self.closeBtn.setIcon(icon)
        pass

    def deleteButton(self):
        self.closeBtn.deleteLater()
        pass

    def closeWindow(self):
        self.close()
        pass
    pass
##Parent for QDialog }

##MainWindowClass {
class GUImm(QtWidgets.QMainWindow, Ui_shield2.Ui_MainWindow):
    finished = QtCore.pyqtSignal()
#Constructor {
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

##Icons and other cosmetic {
        self.setFixedSize(self.size())
        #self.setAcceptDrops(True)

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(filenameIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
        self.setWindowIcon(self.icon)

        self.errorIcon = QtGui.QIcon()
        self.errorIcon.addPixmap(QtGui.QPixmap(filenameErrorIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off) 

        self.infoIcon = QtGui.QIcon()
        self.infoIcon.addPixmap(QtGui.QPixmap(filenameInfoIcon), QtGui.QIcon.Normal, QtGui.QIcon.Off) 

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
        # PP = QtGui.QPainterPath() 
        # PP.addRoundedRect(QtCore.QRectF(self.rect()), 3, 3)
        # mask = QtGui.QRegion(PP.toFillPolygon().toPolygon())
        # self.setMask(mask)

        self.setMask(getMask(self, 3, 3))
        

        ##MovebleWindow
        setMoveWindow(self)
        setMoveWindow(self.startTitle)
        setMoveWindow(self.FAQTitle)
        setMoveWindow(self.helpLearnTitle)
        setMoveWindow(self.helpQueryWindow)
        setMoveWindow(self.helpPropWindow)    
##Icons and other cosmetic }


#TextBoxes for take values from user {
        self.learnValuesBox = QVBoxLayout()
        self.learnValuesHLayoutsArray = []
        self.learnValuesTracker = []
        self.inputValuesBox.setLayout(self.learnValuesBox)

        self.queryValuesBox = QVBoxLayout()
        self.queryValuesHLayoutsArray = []
        self.queryValuesTracker = []
        self.queryInputValuesBox.setLayout(self.queryValuesBox)

        self.targetLearnValuesBox = QVBoxLayout()
        self.targetLearnHLayoutsArray = []
        self.targetLearnValuesTracker = []
        self.targetValBox.setLayout(self.targetLearnValuesBox)

        self.currentCountVibroki = 0
        self.currentCountVibrokiQ = 0
#TextBoxes for take values from user }


##Slots for buttons {
        ##LearnPage {
        self.learnStartBtn.clicked.connect(self.startTrain_Act)  
        self.StopBtn.clicked.connect(self.stopTrain_Act)
        self.learnHelpBtn.clicked.connect(self.showHelpLearnWindow_Act)
        self.addViborkaBtn.clicked.connect(self.addViborka_Act)
        self.deleteViborkaBtn.clicked.connect(self.deleteViborka_Act)
        ##LearnPage }
        
        ##QueryPage {
        self.queryBtn.clicked.connect(self.defQuery_Act)
        self.queryHelpBtn.clicked.connect(self.showHelpQueryHelpWindow_Act)
        self.addQueryViborkaBtn.clicked.connect(self.addViborkaQ_Act)
        self.deleteQueryViborkaBtn.clicked.connect(self.deleteViborkaQ_Act)
        ##QueryPage {

        ##SettingsPage {    
        self.LoadWeightsBtn.clicked.connect(self.loadWeights_Act)
        self.SaveWeightsBtn.clicked.connect(self.saveWeights_Act)   
        self.RerandWeightsBtn.clicked.connect(self.randWeights_Act) 
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

        self.learnStartBtn.setEnabled(False)
        self.queryBtn.setEnabled(False)
##Threads }

##FillGroupBoxes {
        #self.refillValuesBoxes()
        #self.refillTargetValueBoxes()
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

#Constructor }

##TextBoxes, debugMessageBoxes, helpBoxes {
     
    ##Fill groupBoxes learn/query/target {

    def addViborkaQuery(self):
        if (self.currentCountVibrokiQ >= 14):
            return



        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        LabelText = ""
        self.currentCountVibrokiQ += 1
        if (self.currentCountVibrokiQ >= 10):
            LabelText = ""
        elif (self.currentCountVibrokiQ < 10):
            LabelText = "0"

        hLayoutQ = QHBoxLayout()
        hLayoutQ.addStretch(1)
        inputValQ = QTextEdit()
        inputValQ = QtWidgets.QTextEdit()#self.frame_2)
        inputValQ.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        inputValQ.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        inputValQ.setFixedSize(self.queryInputValuesBox.width() - 35 ,25)
        inputValQ.setObjectName(f"inputVal")
        inputValQ.setFont(font)
        qTextQ = QLabel()
        qTextQ.setText(f"{LabelText}{self.currentCountVibrokiQ}")
        qTextQ.setFont(font)
        hLayoutQ.addWidget(qTextQ)
        hLayoutQ.addWidget(inputValQ)
        self.queryValuesTracker.append(inputValQ)
        self.queryValuesBox.addLayout(hLayoutQ)
        self.queryValuesHLayoutsArray.append(hLayoutQ)
        
        pass

    def delViborkaQuery(self):
        if (self.currentCountVibrokiQ <= 0):
            return


        self.currentCountVibrokiQ -= 1
        itemQ = self.queryValuesBox.takeAt(self.queryValuesBox.count() - 1)
        del itemQ

        textBoxQ = self.queryInputValuesBox.findChildren(QtWidgets.QTextEdit)
        tbQ = textBoxQ[len(textBoxQ) - 1]
        tbQ.setParent(None)
        tbQ.deleteLater()

        labelQ = self.queryInputValuesBox.findChildren(QLabel)
        lbQ = labelQ[len(labelQ) - 1]
        lbQ.deleteLater()

        self.queryValuesTracker.pop()
        self.queryValuesHLayoutsArray.pop()
        pass

    def addViborkaLearn(self):
        if (self.currentCountVibroki >= 14):
            return


        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        LabelText = ""
        self.currentCountVibroki += 1
        if (self.currentCountVibroki >= 10):
            LabelText = ""
        elif (self.currentCountVibroki < 10):
            LabelText = "0"

        hLayout = QHBoxLayout()
        hLayout.addStretch(1)
        inputVal = QtWidgets.QTextEdit(self.inputValuesBox)
        inputVal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        inputVal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        inputVal.setFixedSize(self.inputValuesBox.width() - 35 ,25)
        inputVal.setObjectName(f"inputVal")
        inputVal.setFont(font)
        qText = QLabel(self.inputValuesBox)
        qText.setText(f"{LabelText}{self.currentCountVibroki}")
        qText.setFont(font)
        hLayout.addWidget(qText)
        hLayout.addWidget(inputVal)
        self.learnValuesTracker.append(inputVal)
        self.learnValuesBox.addLayout(hLayout)
        self.learnValuesHLayoutsArray.append(hLayout)

        ##TargetValues
        hTargetLayout = QHBoxLayout()
        hTargetLayout.addStretch(1)
        targetVal = QTextEdit(self.targetValBox)
        targetVal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        targetVal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        targetVal.setFixedSize(self.targetValBox.width() - 35, 25)
        targetVal.setObjectName(f"targetVal")
        targetVal.setFont(font)
        qTarText = QLabel(self.targetValBox)
        qTarText.setText(f"{LabelText}{self.currentCountVibroki}")
        qTarText.setFont(font)
        hTargetLayout.addWidget(qTarText)
        hTargetLayout.addWidget(targetVal)
        self.targetLearnValuesTracker.append(targetVal)
        self.targetLearnValuesBox.addLayout(hTargetLayout)
        self.targetLearnHLayoutsArray.append(hTargetLayout)
        pass

    def delViborkaLearn(self):
        if (self.currentCountVibroki <= 0):
            return


        ##InputValues
        self.currentCountVibroki -= 1
        item = self.learnValuesBox.takeAt(self.learnValuesBox.count() - 1)
        del item

        textBox = self.inputValuesBox.findChildren(QtWidgets.QTextEdit)
        tb = textBox[len(textBox) - 1]
        tb.deleteLater()

        label = self.inputValuesBox.findChildren(QLabel)
        lb = label[len(label) - 1]
        lb.deleteLater()

        self.learnValuesTracker.pop()
        self.learnValuesHLayoutsArray.pop()

        ##TargetValues 
        tItem = self.targetLearnValuesBox.takeAt(self.targetLearnValuesBox.count() - 1)
        del tItem

        tTextBox = self.targetValBox.findChildren(QTextEdit)
        tTb = tTextBox[len(tTextBox) - 1]
        tTb.deleteLater()

        tLabel = self.targetValBox.findChildren(QLabel)
        tLb = tLabel[len(tLabel) - 1]
        tLb.deleteLater()

        self.targetLearnValuesTracker.pop()
        self.targetLearnHLayoutsArray.pop()
        pass

    ##Fill groupBoxes learn/query/target }
    
    def setFocusSubWindow(self, dialog):
        dialog.setFocus(True)
        dialog.activateWindow()
        dialog.raise_()
        dialog.show()
        pass

    def setVisible4Input(self, param):  #Когда данные берутся из внешнего файла, боксы для входных значений нам уже не нужны
        #self.inputValuesBox.setVisible(param)
        #self.targetValBox.setVisible(param)

        self.inputValuesBox.setEnabled(param)
        self.targetValBox.setEnabled(param)

        pass
    
    def showHelpLearnTitle(self):
        self.helpLearnTitle.close()
        self.helpPropWindow.close()

        if (not self.helpLearnTitle.isActiveWindow()):
            self.setFocusSubWindow(self.helpLearnTitle)
            return

        self.helpLearnTitle.show()
        pass
    
    def showHelpQueryTitle(self):
        self.helpLearnTitle.close()
        self.helpPropWindow.close()
        
        if ( not self.helpQueryWindow.isActiveWindow()):
            self.setFocusSubWindow(self.helpQueryWindow)
            return

        self.helpQueryWindow.show()
        pass
    
    def showHelpPropTitle(self):
        self.helpLearnTitle.close()
        self.helpQueryWindow.close()

        if (not self.helpPropWindow.isActiveWindow()):
            self.setFocusSubWindow(self.helpPropWindow)
            return

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
    
    def showDebugDialog(self, message, type): 
        """
        Show debug message. Use "signal_name".emit() in\n
        <Int4NN> or <fileUploader>.\n
        Parametrs:\n
        "message" is message whic user will see,\n
        "type" may be 'error' or 'info' - set the icon of\n
        window.
        """
        
              
        if self.goToClose:
            return
        
        msgBox = QMessageBox()
        msgBox.setText(message)
        msgBox.setMask(getMask(msgBox))
        

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
    
    def showPerformance(self):                      
        if (self.learnFromFile):
            self.performanceLabel.setText(str(self.INT.getPerformanceRate()))
        pass
    
    def showPercents(self, value): 

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
    
    def disableButtons(self, inMode):
        """
        If boxes for values in GB is absent\n
        StartBtn for learn or query process\n
        is disabled.
        """
        vTracker = len(self.learnValuesTracker)
        curBtn = self.learnStartBtn
        if (inMode == 'query'):
            vTracker = len(self.queryValuesTracker)
            curBtn = self.queryBtn

        if (vTracker < 1):
            curBtn.setEnabled(False)
        elif (vTracker > 0):
            curBtn.setEnabled(True)

        
        pass
    ##ShowSomethitg {

##TextBoxes, debugMessageBoxes, helpBoxes }


##Get parametrs from user {

    
    def getParams(self, param):
        """
        Get params for learn from selected groupBox.
        Parameters:\n
        "param" defines, which groupBox will 
        be used.\n
        It may be\n
        'query' - GB from query table,\n
        'target' - GB with target values from learn table,\n
        Default is 'learn' - GB with learn values from learn table.
        """

        x = []
        requaresLen = 0

        valuesTracker = self.learnValuesTracker
        requaresLen = self.INT.getCurrentWIH()
        if (param == 'query'):
            valuesTracker = self.queryValuesTracker
            requaresLen = self.INT.getCurrentWIH()
        elif (param == 'target'):
            valuesTracker = self.targetLearnValuesTracker
            requaresLen = self.INT.getCurrentWHO()

        for TB in valuesTracker:
            unParsed = TB.toPlainText()
            parsed = [float(y) for y in unParsed.split(',')]
            if (len(parsed) != requaresLen):
                TB.setText("")
                raise

            x.append(parsed)
            

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
    def setNewParamas(self):
        self.setNewLinks()
        self.setNewLearnParams()
        self.setNewNeironCounts()
        pass

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
    
    def clearParams(self):      
        """
        Back all app to default parameters.
        """
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
        self.showDebugDialog("Параметры сброшены.", 'info')
        self.showParams(2)
        pass
    
    def startLearn(self):       

        if self.learnFromFile == True:
            self.goToLearnFile()
        else:
            try:
                self.hand_input_arr = self.getParams('learn')
                self.hand_target_val = self.getParams('target')
            except:
                self.showDebugDialog("Введите корректные значения!", 'error')
                return
            self.goToLearnHand()
        pass
    
    def goToLearnHand(self):
        """
        Run learn in other thread with values from GB from learnTable.
        """    
        inputArr = []
        targetArr = []
        inputArr.append(self.hand_input_arr)
        targetArr.append(self.hand_target_val)
        self.INT.setPerfError(self.errorBox.value())
        self.INT.setLFFStatus(False)
        self.INT.setInputVal(inputArr, targetArr, 0)
        self.LearnThread.start()
        pass
    
    def goToLearnFile(self):
        """
        Run learn in other thread with values from file.
        """  
        self.INT.setInputVal(self.zipInput)
        self.INT.setLFFStatus(True)
        self.INT.setPerfError(self.errorBox.value())

        self.LearnThread.start()
        pass
    
    def stopLearn(self):        
        self.INT.stopSignal = True
        pass
    
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
    
    def defQuery(self):        
        try:
            inputArr = self.getParams('query')
        except:
            print("Некоректные данные!")
            self.showDebugDialog("Некорректные данные!", 'error')
            return
        self.outputLabel.setText('\n'.join(str(x) for x in self.INT.defQuery(inputArr)))
        pass
##MainProcessesNN }

##ButtonsHandlers {
    def btnLock(self, val):        #Лок кнопок при начале обучения
        self.clearBtn.setEnabled(val)
        self.learnStartBtn.setEnabled(val)
        self.queryBtn.setEnabled(val)
        self.epochsLoopsBtn.setEnabled(val)
        self.errorBox.setEnabled(val)
        self.RerandWeightsBtn.setEnabled(val)
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
        #self.setNewLearnParams()
        self.setNewParamas()
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

    def addViborka_Act(self):
        self.addViborkaLearn()
        self.disableButtons('learn')
        pass

    def deleteViborka_Act(self):
        self.delViborkaLearn()
        self.disableButtons('learn')
        pass

    def deleteViborkaQ_Act(self):
        self.delViborkaQuery()
        self.disableButtons('query')
        pass

    def addViborkaQ_Act(self):
        self.addViborkaQuery()
        self.disableButtons('query')
        pass
##ButtonsHandler }
##MainWindowClass }

##SubWindows {

##StartWindow{
import Ui_startDialog as SD
class GUIstartWindow(GUIDialogOrigin, SD.Ui_Dialog):

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

        GUIDialogOrigin.setCustomMask(self)
        GUIDialogOrigin.deleteButton(self)
        
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
class GUIFaqWin(GUIDialogOrigin, FD.Ui_FAQDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        GUIDialogOrigin.setCustomMask(self)
        GUIDialogOrigin.setButtons(self, 50, 10)
        
##AboutProgrammWindow }


##HelpLearnModeWeindow {
import Ui_helpLearnDialog as HD
class GUIhelpLearn(GUIDialogOrigin, HD.Ui_helpLearnDialog)  :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        GUIDialogOrigin.setCustomMask(self)
        GUIDialogOrigin.setButtons(self, 50, 10)
##HelpLearnModeWeindow }


##HelpQueryModeWindow {
import Ui_helpQueryDialog as QD
class GUIhelpQuery(GUIDialogOrigin, QD.Ui_helpQueryDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        GUIDialogOrigin.setCustomMask(self)
        GUIDialogOrigin.setButtons(self, 50, 10)
##HelpQueryModeWindow }


##HelpPropertiesModeWindow {
import Ui_helpPropDialog as PD
class GUIhelpProp(GUIDialogOrigin, PD.Ui_htlpPropDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.setFixedSize(self.size())   
        GUIDialogOrigin.setCustomMask(self)
        GUIDialogOrigin.setButtons(self, 50, 10)
##HelpPropertiesModeWindow {

##SubWindows }