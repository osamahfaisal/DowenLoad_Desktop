# if i want change in desgin and save in the coding 


from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType  # for the path of  ui file 

import os
from os import path
import sys


# import ui file 
FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__), "GUI_App.ui"))



class MainWindow(QMainWindow,FORM_CLASS):   # inherate  QMainWindow where is path = FORM_CLASS
    def __init__(self, parent=None):
        super(MainWindow , self).__init__(parent)
        # QMainWindow.__init__(self)
        self.setupUi(self)
        
        


    

if __name__=="__main__":
    app =QApplication(sys.argv)
    window=MainWindow()
    window.show()
    app.exec_()
    # main()
    
    