#!/usr/bin/env python 

""" 
A simple echo client 
""" 

import socket 

ballDataX = 0.75 # ball data x from snickerdoodle in world coordinates
ballDataY = 0.25 # ball data y from snickerdoodle in world coordinates
led = 1 # binary signal if ball is in or out of court
loopTime = 0 # loop time of the snickerdoodle code

reset = 0 # reset buttion
capture = 0 # capture button

captureNumber = 8 # amount of images that has been captured
accuracy = 0 # accuracy in percent of ball location
ballDistance = 0 # distance of the ball from the camera


def main():
    print("starting client")
    host = '192.168.1.4' # ip of pc to connect to
    port = 55002 # port we are communicating on
    size = 1024 # data in bits being sent and received
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))

    # we will be relying on sending data in a specific order for it to be interpretted properly
    # the client (snickerdoodle) will send data first then receive from the host pc
    # data will be sent as text that is then converted back to ints or floats

    # sending data order
    # 1. send ball x coordinate
    # 2. send ball y coordinates
    # 3. send led data (binary 1 or 0) if ball is in court
    # 4. send loop time

    # receiving data order
    # 1. receive reset button status
    # 2. receive capture button status

    # send X
    s.send(bytes(str(ballDataX,"utf-8")))
    data = s.recv(size)
    s.close() 
    print('Received:', float(data))

    # send Y
    s.send(bytes(str(ballDataY, "utf-8")))
    data = s.recv(size)
    s.close() 
    print('Received:', float(data))

    # send led data
    s.send(bytes(str(led,"utf-8")))
    data = s.recv(size)
    s.close() 
    print('Received:', int(data))

    # send loop time (ms)
    s.send(bytes(str(ballDataY, "utf-8")))
    data = s.recv(size)
    s.close()
    print('Received:', int(data))


if __name__ == "__main__": 
    main()