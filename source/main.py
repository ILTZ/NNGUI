from PyQt5 import QtWidgets, QtCore
import sys
import GUI
import os

import ctypes
awareness = ctypes.c_int()
errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
print(awareness.value)
errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(0) 
errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
print(awareness.value)


def setScaleDPI():

    pass


def main():
    

    os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    os.environ["QT_SCALE_FACTOR"] = "0"

    
    QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)
    QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_DisableHighDpiScaling, True)

    
    app = QtWidgets.QApplication(sys.argv)
    
    
    

    

    window = GUI.GUImm()
    

    

    #window.show()
    app.exec_()




if __name__ == '__main__':
    main()
  
    
    
   

    pass
    

    

    