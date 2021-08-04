from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os

class FileUpLoader:
    def __init__(self):

        pass
    
    def loadFromFile(self, parent):
        
        name = QFileDialog.getOpenFileName(parent, 'Open file', '/home')[0]
        filename, fileEx = os.path.splitext(name)

        if (fileEx == '.txt'):
            return self.loadFromFileTXT(name)
        elif (fileEx == '.xlsx'):
            return self.loadFromFileEXC(name)
        else:
            print("Некорректное расширение файла!")
            return


        pass

    def loadFromFileTXT(self, path):
        inputValues = []
        targetValues = []
        #name = QFileDialog.getOpenFileName(parent, 'Open file', '/home')[0]
        try:
            n = open(path, 'r')
        except:
            print("Ошибка при открытии файла.")
            return 

        stringVal = ""
        stringTarg = ""
        for line in n:
            stringVal = line.split('\t')[0]
            stringTarg = line.split('\t')[1]

            floatVal = [float(x) for x in stringVal.split(',')]

            inputValues.append(floatVal)
            targetValues.append(float(stringTarg))

        print(inputValues)
        print(targetValues)

        return [inputValues, targetValues]
    pass

    def loadFromFileEXC(self, path):

        pass
    



