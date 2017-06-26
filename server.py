import socket
import asyncore
import pickle
from communication import *
import thread

class Handler(asyncore.dispatcher_with_send):

    def handle_read(self):

        incMsg = self.recv(100)
        if data:
            print("Server incMsg ", incMsg)
            msgNr, msgType, timestamp, data = unpackMsg(incMsg)
            processMessage(msgNr, msgType, timestamp, data)
            print(data)
            
            
            
            

class Server(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = Handler(sock)
            
            
            
def startServer(host, port):
        global toDoList
        server = Server(host, port)
        asyncore.loop()
        

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    
    thread.start_new_thread( startServer, (HOST, PORT) )

    
while True:
    pass

