 #!/usr/bin/env python

import socket
import pickle



TCP_IP = 'localhost' 
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = pickle.dumps("Hello, World!", -1, fix_imports=True)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)
