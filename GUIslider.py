#Lab4
#BitBytes&Beyond

import cv2
import numpy as np
import copy

import sys
from PyQt4 import QtCore, QtGui

b = 60
f = 6
ps = .006
xNumPix = 752
yNumPix = 480
cxLeft = xNumPix/2
cxRight = xNumPix/2
cyLeft = yNumPix/2
cyRight = yNumPix/2

class MyWidget(QtGui.QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
    
        self.initUI()
        
    def initUI(self): 

        rate = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        rate.setFocusPolicy(QtCore.Qt.NoFocus)
        rate.setGeometry(30, 40, 100, 30)
        rate.valueChanged[int].connect(self.changeValue)
        
        self.label = QtGui.QLabel(self)
        self.label.setText('Freq (Hz)')
        self.label.setGeometry(160, 40, 80, 30)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('LED Frequency')
        self.show()
        
    def changeValue(self, value):
    
        self.label.setText('Freq (Hz)')

def main():
  app = QtGui.QApplication(sys.argv)
  myWidget = MyWidget()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()  
