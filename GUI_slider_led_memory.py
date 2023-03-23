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
global ledMsg
ledMsg = "LED Status: "

def setRate(maxCnt):
    #this is pretty much the memAccess file, but with a check if the register(pseudo LED) is on or off
    f = open("/dev/mem", "r+b")
    # = mmap.mmap(f.fileno(), 1000, offset=0x41200000)
    mem = mmap.mmap(f.fileno(), 1000, offset=0x43c00000)
    toMem = maxCnt
    reg   = 0
    
    mem.seek(reg)  
    mem.write(struct.pack('l', toMem))
    
    time.sleep(.5) 
    #END WRITE FUNCTION
    
def readLED():
    #Reads 4th Register offset from 43c00000
    #returns 1 if LED is On, 0 if LED is Off
    f = open("/dev/mem", "r+b")
    # = mmap.mmap(f.fileno(), 1000, offset=0x41200000)
    mem = mmap.mmap(f.fileno(), 1000, offset=0x43c00000)
    reg   = 4
    mem.seek(reg)  
    fromMem = struct.unpack('l', mem.read(4))[0] 
    
    #print str(reg) + " = " + str(fromMem) 
    
    mem.close()
    f.close()
    #here is the check, returns a value based on state
    if(fromMem == 1):
        return 1
    else:
        return 0
    return

class MyWidget(QtGui.QWidget):
        
    def __init__(self):
        super(MyWidget, self).__init__()
        self.ledStatus = None #Added
        self.record_video = RecordVideo(self) #added param
        self.record_video.start_recording()
        self.initUI()
        
    def initUI(self):
        #added a colored square (white to start)
        #color = QtGui.QColor(255, 255, 255)
        #square = QtGui.QFrame(self)
        #square.setGeometry(170, 65, 40, 40)
        #square.setStyleSheet("QWidget { background-color: %s }" %  
            #color.name())
        
        
        rate = QtGui.QScrollBar(QtCore.Qt.Horizontal, self)
        rate.setFocusPolicy(QtCore.Qt.NoFocus)
        rate.setGeometry(30, 40, 100, 30)
        rate.valueChanged[int].connect(self.changeValue)
        rate.setRange(25000000, 100000000)
        rate.setSingleStep(25000000)
        
        self.label = QtGui.QLabel(self)
        self.label.setText('Max Count: 25000000')
        self.label.setGeometry(160, 40, 160, 30)
        
        self.ledStatus = QtGui.QLabel(self)
        #self.ledStatus.setText('LED status: On')
        self.ledStatus.setText(ledMsg)
        self.ledStatus.setGeometry(160, 60, 160, 30)
        
        self.setGeometry(300, 300, 300, 170)
        self.setWindowTitle('LED Max Count Value')
        self.show()
        

        #TODO:

        #Create GUI element that displays LED status based on result of polling function
        #Test on board, if functional create submission video
        
    def changeValue(self, value):
        #placeholder for after function runs
        #ledValue = 0
        #changed this value to be max count since I don't know what the conversion of FPGA cycles/unit time is
        self.label.setText('Max Count: ' + str(value))
        #grabs value from memAccess prototype and holds
        setRate(value)
        
    def updateLEDStatus(self):
        #print('in updateLEDStatus')
        #print(ledMsg)
        self.ledStatus.setText(ledMsg)
        #if(value == 1):
            #self.ledStatus.setText('LED status: On')
        #else:
            #self.ledStatus.setText('LED status: Off')

class RecordVideo(QtCore.QObject):
    #image_data = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, camera_port=0, parent=None):
        super(RecordVideo, self).__init__()
        self.timer = QtCore.QBasicTimer()

    def start_recording(self):
        self.timer.start(100, self)

    def timerEvent(self, event):
        global ledMsg
        if (event.timerId() != self.timer.timerId()):
            return
        if(readLED() == 1):
            ledMsg = "LED status: On"
            #print(ledMsg)
            myWidget.updateLEDStatus()
            #print("On")
        else:
            ledMsg = "LED status: Off"
            #print(ledMsg)
            myWidget.updateLEDStatus()
            #print("Off")
        #print("hello world")





def main():
  app = QtGui.QApplication(sys.argv)
  global myWidget
  myWidget  = MyWidget()
  #while 1:
    #myWidget.updateLEDStatus()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()  
