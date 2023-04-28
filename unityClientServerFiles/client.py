#!/usr/bin/env python 

""" 
A simple echo client 
""" 

import socket 

def main():
    print("starting client")
    host = '192.168.1.4'
    port = 55002 
    size = 1024 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((host,port)) 
    s.send('Hello, world') 
    data = s.recv(size) 
    s.close() 
    print ('Received:'), data

if __name__ == "__main__": 
    main()