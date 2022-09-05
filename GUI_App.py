
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import urllib.request

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 283)
        MainWindow.setMinimumSize(QtCore.QSize(640, 283))
        MainWindow.setMaximumSize(QtCore.QSize(640, 312))
        MainWindow.setStyleSheet(
            
            #  styling main window 
            
                    "QMainWindow{\n"  # here if we want to style all thangs in the same  object type with same styling 

                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                    "}\n"


                    "QLabel{\n"
                    "    color: rgb(255, 255, 255);\n"
                    "    font: 75 12pt \"MS Shell Dlg 2\";\n"
                    "}\n"



                    "QLineEdit{\n"
                    "\n"
                    "background-color: rgb(255, 255, 0);\n"
                    "	font: 75 10pt \"MS Shell Dlg 2\";\n"


                    "	color: rgb(170, 0, 0);"
                    "}\n"


                    "QPushButton{\n"
                    "    background-color: rgb(255, 255, 0);\n"
                    "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                    "    color: rgb(170, 0, 0);\n"
                    "    \n"
                    "    \n"
                    "}")
                            
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 441, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet(
            
            #  styling linetext 1
                        "QLineEdit{\n"  # here if we want to styling one element 

                        "    background-color: rgb(255, 255, 100);\n"
                        "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                        "    color: rgb(170, 0, 0);\n"

                        "}")
                                
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 90, 341, 31))
        self.lineEdit_2.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 101, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 90, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 200, 151, 31))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(170, 140, 451, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(True)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionOk = QtWidgets.QAction(MainWindow)
        self.actionOk.setObjectName("actionOk")
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionOk)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




#  function

    def handelPregress(self , blocknum , blocksize , totalsize):
       pass


    def dowenLoad(self):
        
        url=self.lineEdit.text()
        save_location=self.lineEdit_2.text()
        
        urllib.request.urlretrieve(url, save_location,self.handelPregress )
        # QMessageBox.information(self ,"Dowenload Complete" ,"Dowenload Finshed")
        QMessageBox.information(self, "QMessageBox.information()",
                                        "Download the selected item.")
        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        






    #  change name of varaible and connect element with function
    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "URL"))
        self.label_2.setText(_translate("MainWindow", "Location "))
        self.pushButton.setText(_translate("MainWindow", "browse"))
        self.pushButton_2.setText(_translate("MainWindow", "Start Download "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOk.setText(_translate("MainWindow", "Ok"))
        
        # connection function 
        
        
        # when you connect method with other method we not use () withh it 
        self.pushButton_2.clicked.connect(self.dowenLoad)        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

