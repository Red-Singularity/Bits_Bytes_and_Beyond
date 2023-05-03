#!/usr/bin/env python 

""" 
A simple echo server 
""" 

import socket # for wifi communication
import sys
from PyQt4 import QtWidgets 
from esd2_GUI import * # import everything from ui python file

ui = Ui_TabWidget()

ballDataX = 0 # ball data x from snickerdoodle
ballDataY = 0 # ball data y from snickerdoodle
led = 0 # binary signal if ball is in or out of court
loopTime = 0 # loop time of the snickerdoodle code

reset = 0 # reset buttion
capture = 0 # capture button

captureNumber = 8 # amount of images that has been captured
accuracy = 0 # accuracy in percent of ball location
ballDistance = 0 # distance of the ball from the camera

def Create_Plot():
    #creates the plot that is displayed as a widget
    print("plot started")

def Update_UI():
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_TabWidget()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
 
def Wifi_Comms():
    print("starting server")
    host = '192.168.1.4' # ip of the host pc on the local network
    port = 55002 # port thart we are communicating on can be anything above 
    backlog = 5 # specifies the number of pending connections the queue will hold.
    size = 1024 # data in bits being sent and received

    # we will be relying on sending data in a specific order for it to be interpretted properly
    # the client (snickerdoodle) will send data first then receive from the host pc
    # data will be sent as text that is then converted back to ints or floats

    # sending data order
    # 1. receive ball x coordinate
    # 2. receive ball y coordinates
    # 3. receive led data (binary 1 or 0) if ball is in court
    # 4. receive loop time

    # receiving data order
    # 1. send reset button status
    # 2. send capture button status


    while 1: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.bind((host,port))
        print("waiting for connection")
        s.listen(backlog) # listen for a connection
        client, address = s.accept() 
        print ("connection made")
        data = client.recv(size) # receive data from client
        ballDataX = float(data)
        print("Ball X: ", ballDataX)
        client.send(data) #send data back to client as echo
        client.close()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.bind((host,port))
        print("waiting for connection")
        s.listen(backlog) # listen for a connection
        client, address = s.accept() 
        print ("connection made")
        data = client.recv(size) # receive data from client
        ballDataY = float(data)
        print("Ball Y: ", ballDataY)
        client.send(data) #send data back to client as echo
        client.close()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.bind((host,port))
        print("waiting for connection")
        s.listen(backlog) # listen for a connection
        client, address = s.accept() 
        print ("connection made")
        data = client.recv(size) # receive data from client
        led = int(data)
        print("LED: ", led)
        client.send(data) #send data back to client as echo
        client.close()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.bind((host,port))
        print("waiting for connection")
        s.listen(backlog) # listen for a connection
        client, address = s.accept() 
        print ("connection made")
        data = client.recv(size) # receive data from client
        loopTime = int(data)
        print("Loop Time: ", loopTime)
        client.send(data) #send data back to client as echo
        client.close()

def main():
    Update_UI()
    # Wifi_Comms()
    # Create_Plot()


if __name__ == "__main__": 
    main()