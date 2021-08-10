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

        
        self.inputValues = []
        self.targetValues = []

        self.path = ''

        pass
    
    def setPath(self, path):
        self.path = path
        pass

    def getValues(self):
        return [self.inputValues, self.targetValues]

    def loadFromFile(self):
        
       
        filename, fileEx = os.path.splitext(self.path)

        if (fileEx == '.txt'):
            return self.loadFromFileTXT(self.path)
        elif (fileEx == '.xlsx'):
            return self.loadFromFileEXC(self.path)
        elif (fileEx == '.csv'):

            pass
        else:
            print("Некорректное расширение файла!")
            self.correctSignal.emit(False)
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

        self.inputValues = inputValues
        self.targetValues = targetValues
        self.correctSignal.emit(True)
        
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
            print(tempFull)
            for i in range(len(tempFull)):
                tempIn = []
                tempTar = []
                for count in range(len(tempFull[i])):
                    if (count < (len(tempFull[i]) - 1)):
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
            

        self.inputValues = inputValues
        self.targetValues = targetValues
        self.correctSignal.emit(True)
        
    
    def loadFileCSV(self, path):

        pass
    



