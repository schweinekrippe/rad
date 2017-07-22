import pickle
import numpy
import socket
import thread
from PIL import Image, ImageQt

import random
import cv2


#~ def server():
    #~ sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #~ sock.bind(("localhost", 9999))
    #~ sock.listen(1)
    #~ conn, addr = sock.accept()
    
    #~ a = ""
    #~ incMsg = "0"
    
    #~ while incMsg[0] == "0":
        #~ incMsg = conn.recv(1024)
        #~ a += (incMsg[1:])

    

    #~ a = pickle.loads(a)
    


    #~ c = numpy.fromstring(a)
    #~ print("c", c)



#~ def client():
    #~ b = numpy.ones(33)
    

    #~ b = b.tostring()
    #~ print(len(b))


    #~ a = pickle.dumps(b)
    #~ print(len(a))
    
    
    #~ sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #~ sock.connect(("localhost", 9999))
    
    #~ lenMsg = len(a)
    #~ arr = []
    
    
    #~ for i in range (0, lenMsg, 1023):
        #~ if i >= lenMsg - 1023:
                    #~ arr.append(bytes(1)+a[i:i + 1023])
                
        #~ else:
            #~ arr.append(bytes(0)+a[i:i + 1023])
            
                
        #~ for element in arr:
            #~ sock.sendall(element)


#~ thread.start_new_thread(server,())

#~ client()

#~ input()

#~ print("dumped", a)
#~ a = pickle.loads(a)
#~ print("loaded", a)

#~ c = numpy.fromstring(a)
#~ print("c", c)

#~ print(c + numpy.ones(3))


buffsize = 1024



def server():
    global buffsize
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 9999))
    sock.listen(1)
    conn, addr = sock.accept()
    
    a = ""
    incMsg = "0"
    
    while incMsg[0] == "0":
        incMsg = conn.recv(buffsize)
        a += (incMsg[1:])
        
    print(len(a))
    
    


    a = pickle.loads(a)
    print("after load", len(a))
    a = numpy.fromstring(a, dtype='uint8')
    a = a.reshape((798, 192, 3))

    print("after from string", len(a))
    cv2.imshow('image',a)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 


def client():
    global buffsize
    
    #~ a = ""
    #~ for i in range(0,1024,1):
        #~ a += "1"
        
    img = cv2.imread('C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\images\\heckview.png')
    print(img)
    print(type(img))
    
    
    
    img = img.tostring()
    print(len(img))
    #~ print(img)
    a = pickle.dumps(img, -1)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 9999))
    
    lenMsg = len(a)
    arr = []
    
    
    for i in range (0, lenMsg, buffsize-1):
        if i >= lenMsg - buffsize-1:
            arr.append(bytes(1)+a[i:i + buffsize-1])
                
        else:
            arr.append(bytes(0)+a[i:i + buffsize -1])
        
    length = 0
    for elmt in arr:
        length += len(arr)
            
    print(len(a))
        
        
                
    for element in arr:
        sock.sendall(element)
thread.start_new_thread(server,())

client()

input()
