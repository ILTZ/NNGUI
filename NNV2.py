import numpy as np
import scipy.special as ss


#activation func
def sigmoid(x):
    return ss.expit(x)

#def params NN
def_inputN = 5
def_hiddenN = 5
def_outputN = 1
def_learnRate = 0.3
def_learnLoop = 30000
def_epochs = 1

def_hidden1Capacity = 5
def_hidden2Capacity = 5

def randWeights(oNodes, iNodes):
    return np.random.normal(0.0, pow(oNodes, -0.5), (oNodes, iNodes))

class Neiron:
    def __init__(self, iWeights, learnRate):
        self.weights = iWeights
        self.input = []
        self.output = []
        self.error = []
        self.deltaWeights = []
        self.lr = learnRate   
        self.ActivationFunc = lambda x : sigmoid(x)
        
    def query(self, inputArr):
        self.input = np.dot(self.weights, inputArr)
        #self.output = self.ActivationFunc(self.input)
        return self.input
    def setOutput(self):
        self.output = self.ActivationFunc(self.input)
        pass

    def backProp(self, inputError, oWeights):
        self.error = np.dot(oWeights.T, inputError)
        return self.error
    
    def changeWeights(self, inputArr):
        #Что-то из этого было матрицей, а что-то - np.array()
        #из-за чего numpy ругался
        #просто приводим значения к 1-му типу
        #self.output = np.reshape(np.array(self.output), (5,1))
        #self.error = np.reshape(np.array(self.error), (5,1))

        self.weights += self.lr * np.dot((self.error * self.output * (1.0 - self.output)), np.transpose(inputArr))
        return
    ##
    def getWeights(self):
        return self.weights
    def setWeights(self, newWeights):
        self.weights = newWeights

class FinalNeiron:
    def __init__(self, iWeights, learnRate):
        self.weights = iWeights
        self.input = []
        self.output = []
        self.error = []
        self.deltaWeights = []
        self.lr = learnRate   
        self.ActivationFunc = lambda x : sigmoid(x)
        
    def query(self, inputArr, count): 
        #Т.к. у нас несколько весов в масссиве с весами(для каждого нейрона предыдущего слоя),...
        #...то count нужен для выбора этих самых весов.   
        self.input = np.dot(self.weights[count], inputArr)
        return self.input
    def setOutput(self):
        self.output = self.ActivationFunc(self.input)

    def backProp(self, inputError, oWeights):
        self.error = np.dot(oWeights.T, inputError)
        return self.error
    
    def changeWeights(self, inputArr, count):
        self.weights[count] += self.lr * np.dot((self.error * self.output * (1.0 - self.output)), np.transpose(inputArr))
        return
    ##
    def getWeights(self):
        return self.weights
    def setWeights(self, newWeights):
        self.weights = newWeights

class neuralNetwork2:
    def __init__(self, inputNodes, hiddenNodes, outputNodes, learnRate):
        self.iNodes = inputNodes
        self.hNodes = hiddenNodes
        self.oNodes = outputNodes
        
        self.lr = learnRate
        self.learnLoops = def_learnLoop
        self.epochs = def_epochs

        self.HiddenLayer1Count = def_hidden1Capacity
        self.HiddenLayer2Count = def_hidden2Capacity
        self.HiddenLayer1 = []
        self.HiddenLayer2 = []
        #Далее на основе входных значений конструктора составляются матрицы весов для каждого нейрона...
        #...+ по установленным значениям заполняются массивы с нейронами для 1-го и 2-го слоев соответственно
        #hidden neir layer #1
        for i in range(self.HiddenLayer1Count):
            self.HiddenLayer1.append(Neiron(randWeights(self.hNodes, self.iNodes), self.lr))
        #hidden neir layer #2
        for i in range(self.HiddenLayer2Count):
            self.HiddenLayer2.append(Neiron(randWeights(self.hNodes, self.hNodes), self.lr))
        #final output neiron/последний нейрон, покач-то, всегда будет 1
        finalWeights = [] #генерится массив с матрицами весов(в зависимости от количества нейронов ..
        #...в предыдущем слое)
        for i in range(self.HiddenLayer2Count):
            finalWeights.append(randWeights(self.oNodes, self.hNodes))

        self.FN = FinalNeiron(finalWeights, self.lr)

    def learnProcess(self, inputArr, targetArr):
        inputs = np.array(inputArr, ndmin = 2).T
        targets = np.array(targetArr, ndmin = 2).T
        
        TempValArr1st = []
        #Настакиваем значения проходящие через нейроны 1-го слоя и сразу же их сигмоидоизируем
        for i in range(self.HiddenLayer1Count):
            temp = sigmoid(self.HiddenLayer1[i].query(inputs))
            TempValArr1st.append(temp)
            self.HiddenLayer1[i].setOutput()

        #Настакиваем значения, приходящие из 1-го слоя для КАЖДОГО нейрона второго слоя...
        TempValArr2nd = []
        for i in range(self.HiddenLayer2Count):
            #temp = np.array(np.mat('0.0;0.0;0.0;0.0;0.0'), subok=True)
            temp = np.zeros((self.hNodes,1))
            for j in range(len(TempValArr1st)):
                temp += self.HiddenLayer2[i].query(TempValArr1st[j])
            #....и прогоняем их через сигмоиду перед отправкой на следующий этап
            TempValArr2nd.append(sigmoid(temp))
            #Также пока-что назначаем им выходные значения
            self.HiddenLayer2[i].output = sigmoid(temp)
                
        #Идет настак финального выходного значения....
        #finalTemp = np.array(np.mat('0.0'), subok=True)
        finalTemp = np.zeros((self.oNodes,1))
        for j in range(len(TempValArr2nd)):
            finalTemp += self.FN.query(TempValArr2nd[j], j)
        #..прогоняется через сигмоиду
        finalTemp = sigmoid(finalTemp)
        self.FN.output = finalTemp
        
        #Финальная ошибка нейронной сети
        FinalError = targets - finalTemp
        self.FN.error = FinalError
        #Смена КАЖДОГО набора весов на финальном нейроне
        for i in range(len(TempValArr2nd)):
            self.FN.changeWeights(TempValArr2nd[i], i)
        
        #Фуууух, сначала вычисляем ошибку на i-ом нейроне 2-го скрытого слоя...
        for i in range(self.HiddenLayer2Count):
            backProp2 = self.HiddenLayer2[i].backProp(FinalError, self.FN.weights[i])
            for j in range(self.HiddenLayer1Count):
                #..далее, эта ошибка передается КАЖДОМУ нейрону 1-го скрытого слоя...
                backProp1 = self.HiddenLayer1[j].backProp(backProp2, self.HiddenLayer2[i].weights)
                #...и тут же меняются веса этого нейрона
                self.HiddenLayer1[j].changeWeights(inputs)
            #затем, меняем веса самого нейрона 2-го слоя, от которого искали ошибку, и процесс повторяется,
            #но уже с i+1 нейроном 2-го слоя
            self.HiddenLayer2[i].changeWeights(TempValArr1st[i])
        
        pass

    def query(self, inputArr):
        inputs = np.array(inputArr, ndmin = 2).T
        TempValArr1st = []
        #Настакиваем значения проходящие через нейроны 1-го слоя и сразу же их сигмоидоизируем
        for i in range(self.HiddenLayer1Count):
            temp = sigmoid(self.HiddenLayer1[i].query(inputs))
            TempValArr1st.append(temp)
            self.HiddenLayer1[i].setOutput()

        #Настакиваем значения, приходящие из 1-го слоя для КАЖДОГО нейрона второго слоя...
        TempValArr2nd = []
        for i in range(self.HiddenLayer2Count):
            temp = np.zeros((self.hNodes,1))
            for j in range(len(TempValArr1st)):
                temp += self.HiddenLayer2[i].query(TempValArr1st[j])
            #....и прогоняем их через сигмоиду перед отправкой на следующий этап
            TempValArr2nd.append(sigmoid(temp))
            #Также покачто назначаем им выходные значения
            self.HiddenLayer2[i].output = sigmoid(temp)
                

        finalTemp = np.zeros((self.oNodes,1))
        for j in range(len(TempValArr2nd)):
            finalTemp += self.FN.query(TempValArr2nd[j], j)
        finalTemp = sigmoid(finalTemp)
        return finalTemp

    def randWeights4H1(self):
        for i in range(self.HiddenLayer1Count):
            self.HiddenLayer1[i].setWeights(randWeights(self.hNodes, self.iNodes))
        pass
    def randWeights4H2(self):
        for i in range(self.HiddenLayer2Count):
            self.HiddenLayer2[i].setWeights(randWeights(self.hNodes, self.hNodes))
        pass
    def randWeights4F(self):
        finalWeights = [] 
        for i in range(self.HiddenLayer2Count):
            finalWeights.append(randWeights(self.oNodes, self.hNodes))
        self.FN.setWeights(finalWeights)
        pass
    
    def reFillHidden1Arr(self):
        self.HiddenLayer1.clear()
        for i in range(self.HiddenLayer1Count):
            self.HiddenLayer1.append(Neiron(randWeights(self.hNodes, self.iNodes), self.lr))
        pass
    def reFillHidden2Arr(self):
        self.HiddenLayer2.clear()
        for i in range(self.HiddenLayer1Count):
            self.HiddenLayer2.append(Neiron(randWeights(self.hNodes, self.hNodes), self.lr))
        pass
    def setDefaultParams(self):
        self.iNodes = def_inputN
        self.hNodes = def_hiddenN
        self.oNodes = def_outputN

        self.lr = def_learnRate
        self.learnLoops = def_learnLoop
        self.epochs = def_epochs


        self.HiddenLayer1Count = def_hidden1Capacity
        self.HiddenLayer2Count = def_hidden2Capacity
        self.reFillHidden1Arr()
        self.reFillHidden2Arr()
        self.randWeights4H1()
        self.randWeights4H2()
        self.randWeights4F()
        pass
    ################
    #Get/set values#
    ################
    def getCurrentWIH(self): #input values count
        return self.iNodes
    def setWIH(self, number):
        self.iNodes = number
    def getCurrentWHH(self): #hiiden nodes
        return self.hNodes
    def setWHH(self, number):
        self.hNodes = number
    def getCurrentWHO(self): #output values count
        return self.oNodes
    def setWHO(self, number):
        self.oNodes = number
    def changeLearnRate(self, newLr): #speedlearn of NN
        for i in range(self.HiddenLayer1Count):
            self.HiddenLayer1[i].lr = newLr
        for i in range(self.HiddenLayer2Count):
            self.HiddenLayer2[i].lr = newLr
        self.FN.lr = newLr
    def getCurrentLearnRate(self):
        return self.lr
    def setLearnRate(self, number):
        self.lr = number
        self.changeLearnRate(self.lr)
    def getCurrentNeironCount(self):
        return [self.HiddenLayer1Count, self.HiddenLayer2Count]
    def setCurrentNeironCount(self, arr):
        self.HiddenLayer1Count = arr[0]
        self.HiddenLayer2Count = arr[1]
        self.reFillHidden1Arr()
        self.randWeights4H1()
        self.reFillHidden2Arr()
        self.randWeights4H2()
        self.randWeights4F()


#x = [1.0, 1.0, 1.0, 1.0, 1.0]
#x2 = [1.0, 1.0, 1.0, 1.0, 0.0]
#y = [1.0]
#y2 = [0.8]
#x3 = [1.0, 1.0, 1.0, 0.0, 0.0]
#y3 = [0.6]

#NN = neuralNetwork2(def_inputN, def_hiddenN, def_outputN, def_learnRate)

#for i in range(def_learnLoop):
#    NN.learnProcess(x,y)

#for i in range(10000):
#    NN.learnProcess(x,y)
#    NN.learnProcess(x2, y2)
#    NN.learnProcess(x3, y3)
#print(NN.query(x))
#print(NN.query(x2))
#print(NN.query(x3))

