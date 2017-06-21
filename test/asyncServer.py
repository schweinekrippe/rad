import asyncore
import socket
import pickle

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(100)
        if data:
            self.sendall(data)
            print(pickle.loads(data))

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

server = EchoServer('localhost', 9999)
asyncore.loop()

