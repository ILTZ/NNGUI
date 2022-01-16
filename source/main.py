from PyQt5 import QtWidgets
import sys
import GUI
import os

## Style for window {
dirname = os.path.dirname(__file__)
style2 = open(os.path.join(dirname, 'resources/Aqua.qss'))
## Style for window }

## Disable DPI scalinf {
import ctypes
awareness = ctypes.c_int()
errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(0) 
## Disable DPI scalinf }



## "Main" func {
def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(style2.read())
    window = GUI.GUImm()
    #window.show()
    app.exec_()
## "Main" func }


if __name__ == '__main__':
    main()
  
    
    
   

    pass
    

    

    