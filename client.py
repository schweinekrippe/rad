import socket
import sys
import pickle
from communication import *

HOST, PORT = "localhost", 9999
data = sendEmergencyStop()
print("sended data", data)
# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data)

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

[msgNr, msgType, timestamp, data] = unpackMsg(received)
print("unpackedData:", msgNr, msgType, timestamp, data)
print(processMessage(msgNr, msgType, timestamp, data))

