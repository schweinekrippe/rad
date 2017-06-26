import thread
import time

import asyncore
import socket
import pickle

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        global var
        data = self.recv(100)
        if data:
            self.sendall(str(var))
            #print(pickle.loads(data))

class EchoServer(asyncore.dispatcher):

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
            handler = EchoHandler(sock)






var = 0

def process(name, delay=2):
    global var
    for i in range(5):
        time.sleep(delay)
        print(var)
        var += 1
        
    
thread.start_new_thread( process, ("Thread-1", 5, ) )



server = EchoServer('localhost', 9999)
asyncore.loop()

