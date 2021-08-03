from PyQt5.QtWidgets import QFileDialog, QMessageBox


class FileUpLoader:
    def __init__(self):

        pass
    
    def loadFromFileTXT(self):
        inputValues = []
        targetValues = []
        name = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        try:
            n = open(name, 'r')
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



        return zip(inputValues, targetValues)
    pass

    def loadFromFileEXC(self):

        pass
    



