import numpy as np
import scipy.special as ss
from threading import Thread

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
        
    def query(self, inputArr):
        self.input = np.dot(self.weights, inputArr)
        self.output = sigmoid(self.input)
        return self.output
    
    def backProp(self, inputError, oWeights):
        self.error = np.dot(oWeights.T, inputError)
        return self.error
    
    def changeWeights(self, inputArr):
        self.weights += self.lr * np.dot((self.error * self.output * (1.0 - self.output)), np.transpose(inputArr))
        return
    ##
    def getWeights(self):
        return self.weights
    def setWeights(self, newWeights):
        self.weights = newWeights

class neuralNetwork:
    def __init__(self, inputNodes, hiddenNodes, outputNodes, learnRate):
        self.iNodes = inputNodes
        self.hNodes = hiddenNodes
        self.oNodes = outputNodes
        
        self.lr = learnRate
        self.learnLoops = def_learnLoop
        self.epochs = def_epochs
        #Далее на основе входных значений конструктора составляются матрицы весов для каждого нейрона
        #hidden neir #1
        self.HN = Neiron(np.random.normal(0.0, pow(self.hNodes, -0.5), (self.hNodes, self.iNodes)), learnRate)
        #hidden neir #2
        self.HN2 = Neiron(np.random.normal(0.0, pow(self.hNodes, -0.5), (self.hNodes, self.hNodes)), learnRate)
        #final output neiron
        self.FN = Neiron(np.random.normal(0.0, pow(self.oNodes, -0.5), (self.oNodes, self.hNodes)), learnRate)

        
        
        
    #default work process
    def query(self, inputArr):
        #Стандартный рабочий процесс предполагает простой опрос каждого нейрона сети
        hiddenOut = self.HN.query(inputArr)
        hiddenOut2 = self.HN2.query(hiddenOut)
        finalOut = self.FN.query(hiddenOut2)
        return finalOut
  
    #no coments
    def learnProcess(self, inputArr, targetArr):
        #Код написан следующим образом для большей наглядности
        #Приведение матриц к "правильной" форме
        for epochs in range(self.epochs):
            for count in range(self.learnLoops):
                for i,t in zip(inputArr, targetArr):
                    inputs = np.array(i, ndmin = 2).T
                    targets = np.array(t, ndmin = 2).T
                    #default query
                    hiddenOut = self.HN.query(inputs)
                    hiddenOut2 = self.HN2.query(hiddenOut)
                    finalOut = self.FN.query(hiddenOut2)
                    #errors
                    finalError = targets - finalOut
                    #Т.к. это выходной нейрон, для него ошибка расчитывается иначе, чем для скрытых
                    self.FN.error = finalError
                    hiddenError2 = self.HN2.backProp(finalError, self.FN.weights)
                    hiddenError1 = self.HN.backProp(hiddenError2, self.HN2.weights)
                    #Смена весов на каждом нейроне
                    self.FN.changeWeights(hiddenOut2)
                    self.HN2.changeWeights(hiddenOut)
                    self.HN.changeWeights(inputs)  
        print("Traning succes")
        pass
    def handLearnProcess(self, inputArr, targetArr):
        for epochs in range(self.epochs):
            for count in range(self.learnLoops):
                inputs = np.array(inputArr, ndmin = 2).T
                targets = np.array(targetArr, ndmin = 2).T
                #default query
                hiddenOut = self.HN.query(inputs)
                hiddenOut2 = self.HN2.query(hiddenOut)
                finalOut = self.FN.query(hiddenOut2)
                #errors
                finalError = targets - finalOut
                #Т.к. это выходной нейрон, для него ошибка расчитывается иначе, чем для скрытых
                self.FN.error = finalError
                hiddenError2 = self.HN2.backProp(finalError, self.FN.weights)
                hiddenError1 = self.HN.backProp(hiddenError2, self.HN2.weights)
                #Смена весов на каждом нейроне
                self.FN.changeWeights(hiddenOut2)
                self.HN2.changeWeights(hiddenOut)
                self.HN.changeWeights(inputs)  
        print("Train succes")
        pass

    def learn(self, inputArr, targetArr, param):
        
        if(param == 0):
            th = Thread(target = self.handLearnProcess, args=[inputArr, targetArr])
        elif (param == 1):
            th = Thread(target = self.learnProcess, args= [inputArr, targetArr])

        th.start()



        pass

    #Сброс значений до дефолтных(см. после <import>-ов)
    def setDefaultParams(self):
        self.iNodes = def_inputN
        self.hNodes = def_hiddenN
        self.oNodes = def_outputN

        self.lr = def_learnRate
        self.learnLoops = def_learnLoop
        self.epochs = def_epochs

        self.HN.weights = randWeights(self.hNodes, self.iNodes)
        self.HN2.weights = randWeights(self.hNodes, self.hNodes)
        self.FN.weights = randWeights(self.oNodes, self.hNodes)
        pass
    #После изменения связей сети потребуется перегенерить матрицы весов для нейронов
    def reRandWIHWeights(self):
        self.HN.setWeights(randWeights(self.hNodes, self.iNodes))
        self.HN2.setWeights(randWeights(self.hNodes, self.hNodes))
    def reRandWHOWeights(self):
        self.FN.setWeights(randWeights(self.oNodes, self.hNodes))
    #Гетеры/сетеры внутренних параметров сети
    #Входные ноды(количество входных значений)
    def getCurrentWIH(self):
        return self.iNodes
    def setWIH(self, number):
        self.iNodes = number
    #Скрытые ноды(для скрытых нейронов число связей меж друг другом всегда равно указанному значению)
    def getCurrentWHH(self):
        return self.hNodes
    def setWHH(self, number):
        self.hNodes = number
    #Выходные ноды(число значений на выходе)
    def getCurrentWHO(self):
        return self.oNodes
    def setWHO(self, number):
        self.oNodes = number
    #Количество циклов обучения(зачем, если циклы идут внутри MainMenu? да я хз)
    def getCurrentLearnLoops(self):
        return self.learnLoops
    def setLearnLoops(self, number):
        self.learnLoops = number
    #Коэффициент обучения(искусственно замедляем сеть, чтобы не переобучилась)
    def changeLearnRate(self, newLr):
        self.HN.lr = newLr
        self.HN2.lr = newLr
        self.FN.lr = newLr
    def getCurrentLearnRate(self):
        return self.lr
    def setLearnRate(self, number):
        self.lr = number
        self.changeLearnRate(number)
    
    




#inputN = 5
#hiddenN = 5
#outputN = 1
#learnRate = 0.3

#nn = neuralNetwork(inputN, hiddenN, outputN, learnRate)

#Данные для тренировки/опроса
#x = [1.0, 1.0, 1.0, 1.0, 1.0]
#x2 = [-1.0, -1.0, -1.0, -1.0, -1.0]
#Целевые значения при вышеприведенных данных 
#y = [1.0]
#y2 = [0.0]

#x3 = [1.0, 1.0, 0.0, -1.0, -1.0]
#Тренировка на 30к циклов(больше уже "переучивается")
#for i in range(30000):
#    nn.learnProcess(x, y)
#for i in range(30000):
#    nn.learnProcess(x2, y2)

#Вывод в консоль после тренировки
#print(nn.query(x))
#print(nn.query(x2))
#print(nn.query(x3))