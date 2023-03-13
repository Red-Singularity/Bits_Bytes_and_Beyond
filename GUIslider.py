#Lab4
#BitBytes&Beyond

import cv2
import numpy as np
import copy
import time
import mmap
import struct


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

def blinkLED(maxCnt):
    f = open("/dev/mem", "r+b")
    mem = mmap.mmap(f.fileno(), 1000, offset=0x41200000)
    
    toMem = maxCnt
    reg   = 4
    
    mem.seek(reg)  
    mem.write(struct.pack('l', toMem))
    
    time.sleep(.5) 
    
    mem.seek(reg)  
    fromMem = struct.unpack('l', mem.read(4))[0] 
    
    print str(reg) + " = " + str(fromMem) 
    
    mem.close()
    f.close()
    if(fromMem == 1):
        return 1
    else:
        return 0
    return

class MyWidget(QtGui.QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
    
        self.initUI()
        
    def initUI(self): 
        color = QtGui.QColor(255, 255, 255)
        square = QtGui.QFrame(self)
        square.setGeometry(170, 65, 40, 40)
        square.setStyleSheet("QWidget { background-color: %s }" %  
            color.name())
        
        rate = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        rate.setFocusPolicy(QtCore.Qt.NoFocus)
        rate.setGeometry(30, 40, 100, 30)
        rate.valueChanged[int].connect(self.changeValue)
        rate.setMinimum(10000)
        rate.setMaximum(25000000)
        rate.setSingleStep(10000)
        
        self.label = QtGui.QLabel(self)
        self.label.setText('Max Count: ')
        self.label.setGeometry(160, 40, 160, 30)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('LED Max Count Value')
        self.show()
        
    def changeValue(self, value):
        ledValue = 0
        self.label.setText('Max Count: ' + str(value))
        ledValue = blinkLED(value)
        if(ledValue == 1):
            color.setBlue(0)
            color.setGreen(0)
        else:
            color.setBlue(255)
            color.setGreen(255)
        

def main():
  app = QtGui.QApplication(sys.argv)
  myWidget = MyWidget()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()  
