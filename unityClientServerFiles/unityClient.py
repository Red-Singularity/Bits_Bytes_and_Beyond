# Dr. Kaputa
# simple python link to Unity

import time
import socket 
import binascii
import struct
import sys

values = (640, 480, 1,1,1,1,1,1)
packer = struct.Struct('f f f f f f f f')
packed_data = packer.pack(*values)

host = '192.168.0.11' 
port = 55001
size = 640*480*3 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port)) 

for counter in range(0,10):
    for counter2 in range(0,10):
        x = -1 -counter/20.0
        x2 = counter2/20.0
        values = (640, 480, x,x2,x2,x2,x2,0)
        packer = struct.Struct('f f f f f f f f')
        packed_data = packer.pack(*values)
        
        s.sendall(packed_data) 
        data = s.recv(size) 
        time.sleep(.1)
    
s.close() 
print 'Received:', data