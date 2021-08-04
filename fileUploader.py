from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QObject, pyqtSignal
import pandas as pd
import numpy
import os

class FileUpLoader(QObject):
    correctSignal = pyqtSignal(bool)
    correctSimbols = pyqtSignal(str, str)
    def __init__(self):
        QObject.__init__(self)

        pass
    
    def loadFromFile(self, parent):
        
        name = QFileDialog.getOpenFileName(parent, 'Open file', '/home')[0]
        filename, fileEx = os.path.splitext(name)

        if (fileEx == '.txt'):
            return self.loadFromFileTXT(name)
        elif (fileEx == '.xlsx'):
            return self.loadFromFileEXC(name)
        elif (fileEx == '.csv'):

            pass
        else:
            print("Некорректное расширение файла!")
            return


        pass

    def loadFromFileTXT(self, path):
        inputValues = []
        targetValues = []

        try:
            n = open(path, 'r')
        except:
            print("Ошибка при открытии файла.")
            self.correctSignal.emit(False)
            return 

        stringVal = ""
        stringTarg = ""
        for line in n:
            stringVal = line.split('\t')[0]
            stringTarg = line.split('\t')[1]

            try:
                floatVal = [float(x) for x in stringVal.split(',')]
                floatTarget = float(stringTarg)
            except:
                self.correctSimbols.emit("Некорректные данные в файле!", "error")
                return

            inputValues.append(floatVal)
            targetValues.append(floatTarget)

        print(inputValues)
        print(targetValues)

        self.correctSignal.emit(True)
        return [inputValues, targetValues]
    pass

    def loadFromFileEXC(self, path):
        inputValues = []
        targetValues = []
        file = pd.DataFrame()

        try:
            file = pd.read_excel(path)
        except:
            print("UncorrectPath")
            self.correctSignal.emit(False)
            return
        
        try:
            tempFull = file.values.tolist()
            for i in range(len(tempFull)):
                tempIn = []
                tempTar = []
                for count in range(len(tempFull[i])):
                    if (count < 5):
                        x = float(tempFull[i][count])
                        tempIn.append(x)
                    else:
                        x = float(tempFull[i][count])
                        tempTar.append(x)
                inputValues.append(tempIn)
                targetValues.append(tempTar)
        except:
            self.correctSimbols.emit("Некорректные данные в файле!", 'error')
            return
            
        self.correctSignal.emit(True)
        return [inputValues, targetValues]
    
    def loadFileCSV(self, path):

        pass
    



