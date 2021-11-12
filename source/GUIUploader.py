from Ui_FUIfu import Ui_UploaderGUI
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QBoxLayout, QDialog, QFileDialog, QGroupBox, QHBoxLayout, QLabel, QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QScrollBar

class UploaderDialog(QDialog, Ui_UploaderGUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 

        self.path = ""
        self.targetCount = 0
        self.acepted = False

        self.pathBtn.clicked.connect(self.getPath)

        self.aceptBtn.clicked.connect(self.acept_Act)
        self.cancleBtn.clicked.connect(self.reject_Act)

    

    def getPath(self):
        path = QFileDialog.getOpenFileName(self, 'Open file', filter=("TextFiles (*.txt *.xlsx)"))
        if (path[0] == ""):
            print("UnLoaded")
            return

        try:
            self.targetCount = int(self.spinBox.value())
        except:
            pass

        self.targetCount = int(self.spinBox.value())

        self.path = path[0]
        self.pathTE.setText(self.path)
        pass

    def getPathString(self):
        return self.path
        pass

    def getTargetCount(self):
        return self.targetCount
        pass

    def setAcept(self, param):
        self.acepted = param
        pass

    def getAcepted(self):
        return self.acepted

    def closeWindow(self):
        try:
            self.targetCount = int(self.spinBox.value())
        except:
            pass

        self.close()
        self.deleteLater()
        pass

    def reject_Act(self):
        self.closeWindow()
        pass

    def acept_Act(self):
        self.setAcept(True)
        self.closeWindow()
        pass