#!/usr/bin/env python

import socket
import pickle


TCP_IP = 'localhost'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    print(data)
    if not data: break
    print("received data:", pickle.loads(data))
    conn.send(data)  # echo
    
conn.close()
