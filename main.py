import threading
from PyQt5 import QtWidgets
import sys

import GUI
from threading import Thread

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    window = GUI.GUImm()

    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

    

    