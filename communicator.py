import socket
import sys
import pickle
from communication import *
import thread
import time



class Communicator():
    
    HOST, PORT = "10.42.0.1", 9999

    def __init__(self, host, port, toDoList):
        
        self.HOST = host
        self.port = port
        self.toDoList = toDoList
        
        sendEmergencyStop()
        sendGetBattery()
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client()

    def client(self):

        self.sock.connect((self.HOST,self.PORT))

        thread.start_new_thread( self.sender,(self.sock,))
        thread.start_new_thread(self.receiver,(self.sock,))
    
    def server(self):

        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen(1)
    
        conn, addr = self.sock.accept()
        
        thread.start_new_thread( self.sender,(conn,))
        thread.start_new_thread(self.receiver,(conn,))
            
            
    def sender(self, sock):
        #~ global toDoList
    
        while True:
            sock.sendall(self.toDoList.get())
    
    def receiver(self, sock):
        while True:
            incMsg = sock.recv(1024)
            print("incMsg", incMsg)
            msgNr, msgType, timestamp, data = unpackMsg(incMsg)
            processMessage(msgNr, msgType, timestamp, data)
            print(data)
    
    


C = Communicator("10.42.0.1", 9999, toDoList)

input()
