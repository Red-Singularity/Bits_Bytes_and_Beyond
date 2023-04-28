#!/usr/bin/env python 

""" 
A simple echo server 
""" 

import socket 

def main():
    print("starting")
    host = '192.168.1.4' 
    port = 55002 
    backlog = 5 
    size = 1024 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host,port)) 
    print("waitining for connection")
    s.listen(backlog) 
    while 1: 
        client, address = s.accept() 
        print ("connection made")
        data = client.recv(size) 
        if data: 
            client.send(data) 
        client.close()

if __name__ == "__main__": 
    main()