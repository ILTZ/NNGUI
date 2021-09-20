from PyQt5 import QtWidgets
import sys
import GUI



#Disable DPI scaling
import ctypes
awareness = ctypes.c_int()
errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(0) 

###################################################################################

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = GUI.GUImm()
    #window.show()
    app.exec_()




if __name__ == '__main__':
    main()
  
    
    
   

    pass
    

    

    