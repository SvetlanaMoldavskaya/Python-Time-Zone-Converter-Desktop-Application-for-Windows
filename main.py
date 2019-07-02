import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QLineEdit, QFormLayout, QVBoxLayout
from PyQt5.QtCore import QSize    

#TimeConverterWindow inherits functionality from QmainWindow
class TimeConverterWindow(QMainWindow):
    #constructor, initializes an instance of TimeConverterWindow
    def __init__(self):
        QMainWindow.__init__(self)
        #because TimeConverterWindow inherits from QMainWindow we can use functions
        #defined in QMainWindow, like setMinimumSize
        self.setMinimumSize(QSize(640, 0))    
        self.setWindowTitle("Time Converter") 

        centralBox = QWidget(self)          
        self.setCentralWidget(centralBox) 
        vertical_layout = QVBoxLayout(self)
        centralBox.setLayout(vertical_layout)

        locationOne = QLineEdit(self)
        locationTwo = QLineEdit(self)
        timeOne = QLineEdit(self)
        timeTwo = QLineEdit(self)
        
        my_layout = QGridLayout()
        
        my_layout.addWidget(locationOne, 0, 0)
        my_layout.addWidget(timeOne, 0, 1)
        my_layout.addWidget(locationTwo, 1, 0)
        my_layout.addWidget(timeTwo, 1, 1)       
        vertical_layout.addLayout(my_layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = TimeConverterWindow()
    mainWin.show()
    sys.exit( app.exec_() )