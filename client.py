#!/usr/bin/env python 

""" 
A simple echo client 
""" 

import socket 

host = '127.0.0.1'
port = 55002 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port)) 
s.send('Hello, world') 
data = s.recv(size) 
s.close() 
print 'Received:', data