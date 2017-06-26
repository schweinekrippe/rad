import socket
import sys
import pickle
from communication import *
import thread
import time

HOST, PORT = "localhost", 9999
sendEmergencyStop()
#~ sendEmergencyStop()
#~ sendGetBattery()
#~ print(toDoList)



def client():
    global sock
    sock.connect((HOST,PORT))
    thread.start_new_thread( sender,(sock,))
    thread.start_new_thread(receiver,(sock,))

def server():
    global sock
    sock.bind((HOST, PORT))
    sock.listen(1)

    conn, addr = sock.accept()
    
    thread.start_new_thread( sender,(conn,))
    thread.start_new_thread(receiver,(conn,))
        
        
def sender(sock):

    global toDoList
    print toDoList
 
    while True:

        if len(toDoList) > 0:
            temp = toDoList
            toDoList = []
            
            for task in temp:
            
                print("task ", task)
                sock.sendall(task)
            
        
        else:
            time.sleep(10)
    
def receiver(sock):
    while True:
        incMsg = sock.recv(1024)
        print("incMsg", incMsg)
        msgNr, msgType, timestamp, data = unpackMsg(incMsg)
        processMessage(msgNr, msgType, timestamp, data)
        print(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client()

input()
