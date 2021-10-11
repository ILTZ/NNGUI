from PyQt5.QtWidgets import QFileDialog, QMainWindow
from PyQt5.QtCore import QObject, pyqtSignal
import pandas as pd


import os





class FileUpLoader(QObject):
    correctSignal = pyqtSignal(bool)
    correctSimbols = pyqtSignal(str, str)


    def __init__(self):
        QObject.__init__(self)

        
        self.inputValues = []
        self.targetValues = []

        self.path = ''

        self.countTarget = 0


        pass
    
    def showPathWindow(self):
        self.pathWindow.show()
        pass

    def setCountOfTargets(self, val):
        if (val > 1):
            self.countTarget = val
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
            #return self.loadFileCSV(self.path)
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
                #floatTarget = float(stringTarg)
                floatTarget = [float(x) for x in stringTarg.split(',')]


            except:
                self.correctSimbols.emit("Некорректные данные в файле!", "error")
                return

            inputValues.append(floatVal)
            targetValues.append(floatTarget)

        n.close()

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
                    if (count < (len(tempFull[i]) - self.countTarget)):
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
        
    #In development
    def loadFileCSV(self, path):
        inputValues = []
        targetValues = []

        traningDataFile = open(path, 'r')
        traningDataList = traningDataFile.readlines()
        traningDataFile.close()


        try:
            for record in traningDataList:
                tempInput = []
                tempTarget = []
                allValuse = record.split(',')
                for i in range(len(allValuse)):
                    if i == len(allValuse):
                        tempTarget.append(float(allValuse[i]))
                    else:
                        tempInput.append(float(allValuse[i]))
                inputValues.append(tempInput)
                targetValues.append(tempTarget)
        except:
            self.correctSimbols.emit("Некорректные данные в файле!", 'error')
            return

        self.inputValues = inputValues
        self.targetValues = targetValues
        self.correctSignal.emit(True)

        pass
    



