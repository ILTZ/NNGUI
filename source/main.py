from PyQt5 import QtWidgets
import sys
import GUI
import os

dirname = os.path.dirname(__file__)
style2 = open(os.path.join(dirname, 'resources/Aqua.qss'))



#Disable DPI scaling
import ctypes
awareness = ctypes.c_int()
errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(0) 

###################################################################################

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(style2.read())
    window = GUI.GUImm()
    #window.show()
    app.exec_()




if __name__ == '__main__':
    main()
  
    
    
   

    pass
    

    

    