# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Dev\neyroNet\code\NNCopyVsCode\NNGUI\uixml\shield.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1160, 440)
        MainWindow.setSizeIncrement(QtCore.QSize(5, 5))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f:\\Dev\\neyroNet\\code\\NNCopyVsCode\\NNGUI\\uixml\\resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 0, 1141, 391))
        self.tabWidget_2.setMaximumSize(QtCore.QSize(1151, 461))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(False)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(0, -10, 1159, 411))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.inputValuesBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.inputValuesBox.setGeometry(QtCore.QRect(10, 30, 191, 331))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inputValuesBox.setFont(font)
        self.inputValuesBox.setObjectName("inputValuesBox")
        self.inputVal1 = QtWidgets.QTextEdit(self.inputValuesBox)
        self.inputVal1.setGeometry(QtCore.QRect(70, 80, 51, 31))
        self.inputVal1.setMaximumSize(QtCore.QSize(51, 31))
        self.inputVal1.setObjectName("inputVal1")
        self.inputVal2 = QtWidgets.QTextEdit(self.inputValuesBox)
        self.inputVal2.setGeometry(QtCore.QRect(70, 130, 51, 31))
        self.inputVal2.setMaximumSize(QtCore.QSize(51, 31))
        self.inputVal2.setObjectName("inputVal2")
        self.inputVal3 = QtWidgets.QTextEdit(self.inputValuesBox)
        self.inputVal3.setGeometry(QtCore.QRect(70, 180, 51, 31))
        self.inputVal3.setMaximumSize(QtCore.QSize(51, 31))
        self.inputVal3.setObjectName("inputVal3")
        self.inputVal4 = QtWidgets.QTextEdit(self.inputValuesBox)
        self.inputVal4.setGeometry(QtCore.QRect(70, 230, 51, 31))
        self.inputVal4.setMaximumSize(QtCore.QSize(51, 31))
        self.inputVal4.setObjectName("inputVal4")
        self.inputVal5 = QtWidgets.QTextEdit(self.inputValuesBox)
        self.inputVal5.setGeometry(QtCore.QRect(70, 280, 51, 31))
        self.inputVal5.setMaximumSize(QtCore.QSize(51, 31))
        self.inputVal5.setObjectName("inputVal5")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(650, 310, 141, 23))
        self.progressBar.setMaximumSize(QtCore.QSize(141, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.performanceBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.performanceBox.setGeometry(QtCore.QRect(650, 150, 231, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.performanceBox.sizePolicy().hasHeightForWidth())
        self.performanceBox.setSizePolicy(sizePolicy)
        self.performanceBox.setMaximumSize(QtCore.QSize(10000, 100000))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.performanceBox.setFont(font)
        self.performanceBox.setAutoFillBackground(False)
        self.performanceBox.setObjectName("performanceBox")
        self.groupBox_4 = QtWidgets.QGroupBox(self.performanceBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 60, 101, 71))
        self.groupBox_4.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.errorBox = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.errorBox.setGeometry(QtCore.QRect(10, 30, 81, 22))
        self.errorBox.setMaximumSize(QtCore.QSize(81, 22))
        self.errorBox.setWrapping(False)
        self.errorBox.setProperty("showGroupSeparator", False)
        self.errorBox.setDecimals(6)
        self.errorBox.setMinimum(0.0)
        self.errorBox.setMaximum(0.2)
        self.errorBox.setSingleStep(0.0001)
        self.errorBox.setProperty("value", 0.0001)
        self.errorBox.setObjectName("errorBox")
        self.groupBox_5 = QtWidgets.QGroupBox(self.performanceBox)
        self.groupBox_5.setGeometry(QtCore.QRect(110, 60, 111, 71))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.performanceLabel = QtWidgets.QLabel(self.groupBox_5)
        self.performanceLabel.setGeometry(QtCore.QRect(16, 22, 81, 31))
        self.performanceLabel.setMaximumSize(QtCore.QSize(81, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.performanceLabel.setFont(font)
        self.performanceLabel.setText("")
        self.performanceLabel.setObjectName("performanceLabel")
        self.StopBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.StopBtn.setGeometry(QtCore.QRect(530, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.StopBtn.setFont(font)
        self.StopBtn.setObjectName("StopBtn")
        self.learnStartBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.learnStartBtn.setGeometry(QtCore.QRect(530, 160, 101, 41))
        self.learnStartBtn.setMaximumSize(QtCore.QSize(101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.learnStartBtn.setFont(font)
        self.learnStartBtn.setObjectName("learnStartBtn")
        self.learnHelpBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.learnHelpBtn.setGeometry(QtCore.QRect(1030, 20, 91, 41))
        self.learnHelpBtn.setMaximumSize(QtCore.QSize(91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.learnHelpBtn.setFont(font)
        self.learnHelpBtn.setObjectName("learnHelpBtn")
        self.targetValBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.targetValBox.setGeometry(QtCore.QRect(210, 30, 151, 331))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.targetValBox.setFont(font)
        self.targetValBox.setObjectName("targetValBox")
        self.targetVal = QtWidgets.QTextEdit(self.targetValBox)
        self.targetVal.setGeometry(QtCore.QRect(50, 80, 51, 31))
        self.targetVal.setMaximumSize(QtCore.QSize(61, 41))
        self.targetVal.setObjectName("targetVal")
        self.progressBar.raise_()
        self.learnHelpBtn.raise_()
        self.performanceBox.raise_()
        self.inputValuesBox.raise_()
        self.targetValBox.raise_()
        self.learnStartBtn.raise_()
        self.StopBtn.raise_()
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.defQueryBox = QtWidgets.QGroupBox(self.tab_4)
        self.defQueryBox.setGeometry(QtCore.QRect(-10, -10, 1161, 441))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.defQueryBox.setFont(font)
        self.defQueryBox.setTitle("")
        self.defQueryBox.setObjectName("defQueryBox")
        self.targetValBox_2 = QtWidgets.QGroupBox(self.defQueryBox)
        self.targetValBox_2.setGeometry(QtCore.QRect(220, 20, 631, 211))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.targetValBox_2.setFont(font)
        self.targetValBox_2.setObjectName("targetValBox_2")
        self.outputLabel = QtWidgets.QLabel(self.targetValBox_2)
        self.outputLabel.setGeometry(QtCore.QRect(20, 50, 591, 151))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outputLabel.setText("")
        self.outputLabel.setObjectName("outputLabel")
        self.inputValuesBox_2 = QtWidgets.QGroupBox(self.defQueryBox)
        self.inputValuesBox_2.setGeometry(QtCore.QRect(30, 20, 161, 251))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.inputValuesBox_2.setFont(font)
        self.inputValuesBox_2.setFlat(False)
        self.inputValuesBox_2.setCheckable(False)
        self.inputValuesBox_2.setObjectName("inputValuesBox_2")
        self.inputVal1_2 = QtWidgets.QTextEdit(self.inputValuesBox_2)
        self.inputVal1_2.setGeometry(QtCore.QRect(80, 50, 51, 31))
        self.inputVal1_2.setObjectName("inputVal1_2")
        self.inputVal2_2 = QtWidgets.QTextEdit(self.inputValuesBox_2)
        self.inputVal2_2.setGeometry(QtCore.QRect(80, 90, 51, 31))
        self.inputVal2_2.setObjectName("inputVal2_2")
        self.inputVal3_2 = QtWidgets.QTextEdit(self.inputValuesBox_2)
        self.inputVal3_2.setGeometry(QtCore.QRect(80, 130, 51, 31))
        self.inputVal3_2.setObjectName("inputVal3_2")
        self.inputVal4_2 = QtWidgets.QTextEdit(self.inputValuesBox_2)
        self.inputVal4_2.setGeometry(QtCore.QRect(80, 170, 51, 31))
        self.inputVal4_2.setObjectName("inputVal4_2")
        self.inputVal5_2 = QtWidgets.QTextEdit(self.inputValuesBox_2)
        self.inputVal5_2.setGeometry(QtCore.QRect(80, 210, 51, 31))
        self.inputVal5_2.setObjectName("inputVal5_2")
        self.queryBtn = QtWidgets.QPushButton(self.defQueryBox)
        self.queryBtn.setGeometry(QtCore.QRect(50, 290, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.queryBtn.setFont(font)
        self.queryBtn.setFlat(False)
        self.queryBtn.setObjectName("queryBtn")
        self.queryHelpBtn = QtWidgets.QPushButton(self.defQueryBox)
        self.queryHelpBtn.setGeometry(QtCore.QRect(1040, 20, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.queryHelpBtn.setFont(font)
        self.queryHelpBtn.setObjectName("queryHelpBtn")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBoxLink = QtWidgets.QGroupBox(self.tab)
        self.groupBoxLink.setGeometry(QtCore.QRect(10, -10, 1141, 271))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBoxLink.setFont(font)
        self.groupBoxLink.setTitle("")
        self.groupBoxLink.setFlat(True)
        self.groupBoxLink.setObjectName("groupBoxLink")
        self.label = QtWidgets.QLabel(self.groupBoxLink)
        self.label.setGeometry(QtCore.QRect(20, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.hNodesIn = QtWidgets.QTextEdit(self.groupBoxLink)
        self.hNodesIn.setGeometry(QtCore.QRect(110, 70, 61, 31))
        self.hNodesIn.setObjectName("hNodesIn")
        self.label_2 = QtWidgets.QLabel(self.groupBoxLink)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.oNodesIn = QtWidgets.QTextEdit(self.groupBoxLink)
        self.oNodesIn.setGeometry(QtCore.QRect(110, 140, 61, 31))
        self.oNodesIn.setObjectName("oNodesIn")
        self.chLinksBtn = QtWidgets.QPushButton(self.groupBoxLink)
        self.chLinksBtn.setGeometry(QtCore.QRect(20, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.chLinksBtn.setFont(font)
        self.chLinksBtn.setObjectName("chLinksBtn")
        self.groupBox = QtWidgets.QGroupBox(self.groupBoxLink)
        self.groupBox.setGeometry(QtCore.QRect(540, 30, 231, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.loopCount = QtWidgets.QTextEdit(self.groupBox)
        self.loopCount.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.loopCount.setObjectName("loopCount")
        self.epochsGroupBox = QtWidgets.QGroupBox(self.groupBoxLink)
        self.epochsGroupBox.setGeometry(QtCore.QRect(540, 110, 231, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.epochsGroupBox.setFont(font)
        self.epochsGroupBox.setObjectName("epochsGroupBox")
        self.epochsCount = QtWidgets.QTextEdit(self.epochsGroupBox)
        self.epochsCount.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.epochsCount.setObjectName("epochsCount")
        self.epochsLoopsBtn = QtWidgets.QPushButton(self.groupBoxLink)
        self.epochsLoopsBtn.setGeometry(QtCore.QRect(710, 210, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.epochsLoopsBtn.setFont(font)
        self.epochsLoopsBtn.setObjectName("epochsLoopsBtn")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBoxLink)
        self.groupBox_3.setGeometry(QtCore.QRect(770, 30, 231, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.learnRateBox = QtWidgets.QTextEdit(self.groupBox_3)
        self.learnRateBox.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.learnRateBox.setObjectName("learnRateBox")
        self.line = QtWidgets.QFrame(self.groupBoxLink)
        self.line.setGeometry(QtCore.QRect(10, 10, 1000, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBoxLink)
        self.line_2.setGeometry(QtCore.QRect(490, 20, 20, 241))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.groupBoxLink)
        self.line_3.setGeometry(QtCore.QRect(10, 250, 1000, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.groupBoxLink)
        self.line_4.setGeometry(QtCore.QRect(1000, 20, 20, 240))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.groupBoxLink)
        self.line_5.setGeometry(QtCore.QRect(0, 20, 20, 240))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.RerandWeightsBtn = QtWidgets.QPushButton(self.groupBoxLink)
        self.RerandWeightsBtn.setGeometry(QtCore.QRect(190, 210, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.RerandWeightsBtn.setFont(font)
        self.RerandWeightsBtn.setObjectName("RerandWeightsBtn")
        self.hiddenLayerCount1 = QtWidgets.QTextEdit(self.groupBoxLink)
        self.hiddenLayerCount1.setGeometry(QtCore.QRect(350, 70, 61, 31))
        self.hiddenLayerCount1.setObjectName("hiddenLayerCount1")
        self.HiddenLayerCount2 = QtWidgets.QTextEdit(self.groupBoxLink)
        self.HiddenLayerCount2.setGeometry(QtCore.QRect(350, 140, 61, 31))
        self.HiddenLayerCount2.setObjectName("HiddenLayerCount2")
        self.label_6 = QtWidgets.QLabel(self.groupBoxLink)
        self.label_6.setGeometry(QtCore.QRect(270, 30, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.groupBoxLink)
        self.label_8.setGeometry(QtCore.QRect(270, 100, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.chCountBtn = QtWidgets.QPushButton(self.groupBoxLink)
        self.chCountBtn.setGeometry(QtCore.QRect(390, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.chCountBtn.setFont(font)
        self.chCountBtn.setObjectName("chCountBtn")
        self.SaveWeightsBtn = QtWidgets.QPushButton(self.groupBoxLink)
        self.SaveWeightsBtn.setGeometry(QtCore.QRect(1020, 140, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SaveWeightsBtn.setFont(font)
        self.SaveWeightsBtn.setObjectName("SaveWeightsBtn")
        self.LoadWeightsBtn = QtWidgets.QPushButton(self.groupBoxLink)
        self.LoadWeightsBtn.setGeometry(QtCore.QRect(1020, 210, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LoadWeightsBtn.setFont(font)
        self.LoadWeightsBtn.setObjectName("LoadWeightsBtn")
        self.settingsHelpBtn = QtWidgets.QPushButton(self.groupBoxLink)
        self.settingsHelpBtn.setGeometry(QtCore.QRect(1020, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.settingsHelpBtn.setFont(font)
        self.settingsHelpBtn.setObjectName("settingsHelpBtn")
        self.epochsGroupBox.raise_()
        self.label.raise_()
        self.hNodesIn.raise_()
        self.label_2.raise_()
        self.oNodesIn.raise_()
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.hiddenLayerCount1.raise_()
        self.HiddenLayerCount2.raise_()
        self.label_6.raise_()
        self.label_8.raise_()
        self.SaveWeightsBtn.raise_()
        self.LoadWeightsBtn.raise_()
        self.settingsHelpBtn.raise_()
        self.chCountBtn.raise_()
        self.chLinksBtn.raise_()
        self.epochsLoopsBtn.raise_()
        self.RerandWeightsBtn.raise_()
        self.clearBtn = QtWidgets.QPushButton(self.tab)
        self.clearBtn.setGeometry(QtCore.QRect(20, 280, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName("clearBtn")
        self.tabWidget_2.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1160, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.loadFromFile = QtWidgets.QAction(MainWindow)
        self.loadFromFile.setObjectName("loadFromFile")
        self.currentParamBtn = QtWidgets.QAction(MainWindow)
        self.currentParamBtn.setObjectName("currentParamBtn")
        self.FAQbtn = QtWidgets.QAction(MainWindow)
        self.FAQbtn.setObjectName("FAQbtn")
        self.exitAction_2 = QtWidgets.QAction(MainWindow)
        self.exitAction_2.setObjectName("exitAction_2")
        self.menu.addAction(self.loadFromFile)
        self.menu.addAction(self.currentParamBtn)
        self.menu.addSeparator()
        self.menu.addAction(self.FAQbtn)
        self.menu.addSeparator()
        self.menu.addAction(self.exitAction_2)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NeuralNetwork"))
        self.inputValuesBox.setTitle(_translate("MainWindow", "Входные значения"))
        self.performanceBox.setTitle(_translate("MainWindow", "Точность нейросети"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Погрешность"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Значение"))
        self.StopBtn.setText(_translate("MainWindow", "Стоп"))
        self.learnStartBtn.setText(_translate("MainWindow", "Старт"))
        self.learnHelpBtn.setText(_translate("MainWindow", "Помощь"))
        self.targetValBox.setTitle(_translate("MainWindow", "Целевое значение"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Обучение"))
        self.targetValBox_2.setTitle(_translate("MainWindow", "Выходное значение"))
        self.inputValuesBox_2.setTitle(_translate("MainWindow", "Входные значения"))
        self.queryBtn.setText(_translate("MainWindow", "Опрос"))
        self.queryHelpBtn.setText(_translate("MainWindow", "Помощь"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Опрос"))
        self.label.setText(_translate("MainWindow", "Количество входных значений"))
        self.label_2.setText(_translate("MainWindow", "Количество выходных значений"))
        self.chLinksBtn.setText(_translate("MainWindow", "Изменить"))
        self.groupBox.setTitle(_translate("MainWindow", "Количество циклов обучения"))
        self.epochsGroupBox.setTitle(_translate("MainWindow", "Количество эпох"))
        self.epochsLoopsBtn.setText(_translate("MainWindow", "Изменить"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Коэффициент обучения"))
        self.RerandWeightsBtn.setText(_translate("MainWindow", "Сгенерировать\n"
"новые веса"))
        self.label_6.setText(_translate("MainWindow", "Количество нейронов в 1-м\n"
"скрытом слое"))
        self.label_8.setText(_translate("MainWindow", "Количисетво нейронов во 2-м\n"
"скрытом слое"))
        self.chCountBtn.setText(_translate("MainWindow", "Изменить"))
        self.SaveWeightsBtn.setText(_translate("MainWindow", "Сохранить\n"
"веса"))
        self.LoadWeightsBtn.setText(_translate("MainWindow", "Загрузить\n"
"веса"))
        self.settingsHelpBtn.setText(_translate("MainWindow", "Помощь"))
        self.clearBtn.setText(_translate("MainWindow", "Сбросить\n"
"параметры"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Настройки"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.loadFromFile.setText(_translate("MainWindow", "Загрузить внешний файл(.txt, .xlsx)"))
        self.currentParamBtn.setText(_translate("MainWindow", "Просмотреть текущие параметры"))
        self.FAQbtn.setText(_translate("MainWindow", "О программе"))
        self.exitAction_2.setText(_translate("MainWindow", "Закрыть программу"))