 #!/usr/bin/env python

import socket
import pickle
import time



TCP_IP = 'localhost' 
TCP_PORT = 9999
BUFFER_SIZE = 100


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
for i in range(0,30,1):
    MESSAGE = pickle.dumps("Hello, World! " + str(i), -1)
    s.sendall(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    
    print("received data:", (data))
    time.sleep(3)
s.close()


