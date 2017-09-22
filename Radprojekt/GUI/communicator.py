import socket
import sys
import cPickle as pickle

import thread
import time
import threading
import Queue

from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui, uic


######################
# to run at the bike, uncomment:

#~ import GUIPublisher
#~ from communication.msg import controller

#~ import listenerCombined

######################

        

class Communicator():
    
    # sync clocks to get a usefull timeout condition
    # dummy value of 5000 to make sure unsynced clocks don't cause troubles
    TIMEOFFSET = 0
    TIMEOUT = 5000.000
    
    BUFFSIZE = 4096
    EOM = "iIUEOTM!"
    
    # messages are sent in order of their priority smaller number -> higher priority
    TOPPRIORITY = 0          # exclusive for emergency stop to secure a fast processing
    HIGHPRIORITY = 1         # not used yet
    NORMALPRIORITY = 2       # used for everything
    LOWPRIORITY = 3          # not used yet
    
    # digit 0: category of message - 3: speed, 4: tilt...
    
    DUMMY = 0        # a message with this type will do nothing
    OK = 1           # acknowledge the income of a certain message
    SHUTDOWN = 2     # stop the bike now!
    GETSPEED = 30    # requests current speed setting
    RETURNSPEED = 31 # answers current speed setting
    SETTARGETSPEED = 32    # sets a new target speed
    GETTARGETSPEED = 33    # requests a update for target speed - not used
    RETURNTARGETSPEED = 34 # return for GETTARGETSPEED
    GETTILT = 40      # requests the current tilt data
    RETURNTILT = 41   # answers the tilt request
    GETOBSTACLES = 50    # requests the current detected obstacles
    RETURNOBSTACLES = 51 # answers the obstacle request
    GETBATTERY = 60
    RETURNBATTERY = 61
    WARNING = 70
    SETRECORD = 80
    GETRECORDEDSTATS = 81
    RETURNRECORDEDSTATS = 82
    
    GETSTEERANGLE = 90
    RETURNSTEERANGLE = 91
    GETTARGETSTEERANGLE = 92
    RETURNTARGETSTEERANGLE = 93
    SETTARGETSTEERANGLE = 94
    
    GETORIENTATION = 100
    RETURNORIENTATION = 101
    
    GETCAMERAIMAGE = 110
    RETURNCAMERAIMAGE = 111
    
    UPDATELIMITS = 120
    
    SETTARGETS = 130 # [tgtSpeed, tgtAngle]
    
    # track which messages are received multiple times
    requestnumber = 1
    receivedMessages = []
    
    
    isServer = True


    def __init__(self, host = "", port = 9999, server = True, parent = None):
        
        self.HOST = host
        self.PORT = port
        self.isServer = server

        self.toDoList = Queue.PriorityQueue()

        self.lock = thread.allocate_lock()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        

        

        if self.isServer == False:
            self.R = Refresher(self)
            self.UI = parent
            
        else:
            self.L = listenerCombined.listenerCombined()
            listenerCombined.listener("COMM_LISTENER")
    
    # sets the Ui
    # only neccessary for the client/bike
    def setUi(self, UI):
        self.UI = UI
        
    # runs the communicator in Server/Client mode depending on the init type
    def run(self):

        if self.isServer:
 
            #self.Sensor = SensorData()
            
            self.guiPublisher = GUIPublisher.Sender()

            self.server()

        else:
            self.client()
            

    # connects to a server
    def client(self):
        
        try:

            self.sock.connect((self.HOST,self.PORT))
            

            thread.start_new_thread( self.sender,(self.sock,))
            thread.start_new_thread( self.receiver,(self.sock,))

            self.R.start()

            self.UI.connectionEstablished = True
            self.displayWarning("connection established")
        
        except socket.error:
            self.displayWarning("connection failed")
        
        
    
    def server(self):

        self.sock.bind((self.HOST, self.PORT))

        self.sock.listen(1)

        conn, addr = self.sock.accept()

        thread.start_new_thread( self.sender,(conn,))

        thread.start_new_thread( self.receiver,(conn,))

            
            
    def sender(self, sock):

        while True:
            priority, msg = self.toDoList.get()
            self.sendRec(sock, msg+self.EOM)
    
       
    

    def sendRec(self, sock, msg):
        if len(msg) > self.BUFFSIZE:
            chunk = msg[0:self.BUFFSIZE]
            sock.sendall(chunk)
            self.sendRec(sock, msg[self.BUFFSIZE:])
        else:
            sock.sendall(msg)


    def receiver(self, sock):

        msg = ""
        while True:


            msg += sock.recv(self.BUFFSIZE)
            lst = msg.split(self.EOM)
            msg = lst.pop()
            for element in lst:
                msgNr, msgType, timestamp, data = self.unpackMsg(element)
                self.processMessage(msgNr, msgType, timestamp, data)


    

    def getTime(self):
        return time.time()- self.TIMEOFFSET
    
    ########################################################################
    # functions to send messages
    
    ## functions for server and client
    
    def sendOK(self, answerID):
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.OK, answerID)))
        
    ## functions for client/gui
        
    def sendEmergencyStop(self):
        self.toDoList.put((TOPPRIORITY, self.packMsg(self, self.SHUTDOWN, "stop")))
        
    def sendGetSpeed(self): 
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.GETSPEED, None)))
        
    def sendReturnTargetSpeed(self):
        targetSpeed = self.getTargetSpeed()
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.RETURNTARGETSPEED, targetSpeed)))
        
        
    def sendGetTilt(self):
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.GETTILT, None)))
        
    def sendGetObstacles(self): 
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.GETOBSTACLES, None)))
    
    def sendReturnObstacles(self):
        obstacles = self.getObstacles()
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.RETURNOBSTACLES, obstacles)))
        
    def sendGetBattery(self):
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.GETBATTERY, None)))
    
    def sendRecordList(self):
        lst = getRecordList()
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.SETRECORD, lst)))
        
    def sendGetRecordedStats(self):
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.GETRECORDEDSTATS, None)))
        
    def sendGetSteerAngle(self):
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.GETSTEERANGLE, None)))
    
    def sendReturnTargetSteerAngle(self):
        angle = self.getTargetSteerAngle()
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.RETURNTARGETSTEERANGLE, angle)))
        
        
    def sendGetOrientation(self):
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.GETORIENTATION, None)))
        
    def sendGetCameraImage(self):
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.GETCAMERAIMAGE, None)))
        
    def sendUpdateLimits(self):
        
        minTilt, maxTilt = self.getLimits()
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.UPDATELIMITS , [minTilt, maxTilt])))
        
    def sendSetTargets(self):
        targetSpeed = self.getTargetSpeed()
        targetAngle = self.getTargetSteerAngle()
        self.toDoList.put((self.HIGHPRIORITY,  self.packMsg(self.SETTARGETS, [targetSpeed, targetAngle])))

    
    ## functions for server/bike
       
    def sendReturnSpeed(self):
        speed = self.getSpeed()
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.RETURNSPEED, speed)))
        
    def sendGetTargetSpeed(self):
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.GETTARGETSPEED, None)))
    
    def sendReturnTilt(self):
        tilt = self.getTiltAngle()[1]
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.RETURNTILT, tilt))) 
    
    def sendReturnBattery(self): 
        battery = self.getBattery()
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.RETURNBATTERY, battery)))
    
    def sendWarnMsg(self, msg = ""):
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.WARNING, msg)))
    
    def sendReturnRecordedStats(self, stats = [] ):
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.RETURNRECORDEDSTATS, stats)))
        
    def sendReturnSteerAngle(self):
        angle = self.getSteerAngle()
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.RETURNSTEERANGLE, angle)))
    
    def sendGetTargetSteerAngle(self):
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.GETTARGETSTEERANGLE, None)))
        

    
    def sendReturnOrientation(self):
        ox, oy, oz = self.Sensor.getOrientation()
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.RETURNORIENTATION, [ox,oy, oz])))
    
    def sendReturnCameraImage(self):
        self.toDoList.put((self.NORMALPRIORITY,  self.packMsg(self.RETURNCAMERAIMAGE, self.getCameraImage())))
   


    ########################################################################
    # functions to set and get data
    
    def getSteerAngle(self):
        return self.L.getTargets()[1]
        
    def setSteerAngle(self, angle):
        self.UI.updtSteerAngSig.emit(angle)
    
    def getSpeed(self):
        return self.L.getTargets()[0]
        
    def getTargetSpeed(self):
        return self.UI.tgtSpeed
        
    def getTiltAngle(self):
        return self.L.getOrientation()
        
    def getObstacles(self):
        obstacles = self.L.getObstacles()
        return obstacles
    
    def getBattery(self):
        #global L
        return self.L.getBattery()
        pass
        
    def getRecordList(self):
        recordList = [True, True, True, True, True, True]
        return recordList
    
    def getRecordedStats(self):
        tilt = []
        steering = []
        speed = []
        obstacles = []
        
        return [tilt, steering, speed, obstacles]
    
    def getCameraImage(self):
        cF = self.L.getCameraFeed()
        return cF

    def getTargetSteerAngle(self):
        return self.UI.tgtSteer
        
    def getLimits(self):
        return(self.UI.minTilt, self.UI.maxTilt)       
    
    def displayWarning(self, msg):
        item = QListWidgetItem(msg)
        self.UI.msgList.addItem(item)
        
    def setSpeed(self, speed):
        self.UI.updtSpeedSig.emit(speed)
    
    # obsolet method - replaced by setTargets
    def setTargetSpeed(self, speed):     
        self.GUIPublisher.setTargets([speed,0])
    
    # obsolet method - replaced by setTargets
    def setTargetSteerAngle(self, angle):
        self.GUIPublisher.setTargets([0,angle])
    
            
    def updateObstacleMap(self, data):
        self.UI.updtObstSig.emit(data)

    def setTilt(self, tilt):
        self.UI.updtTiltSig.emit(tilt)
        
    def setBattery(self, battery):
        self.UI.updtBatterySig.emit(battery)
        
    def setStatsToRecord(self, stats):
        recordTilt = stats[0]
        recordSteeringAngle = stats[1]
        recordSpeedProfile = stats[2]
        recordObstacles = stats[3]
        
    def setCameraImage(self, data):
        self.UI.updtCameraImageSig.emit([data])
        
    def setUpdateLimits(self, data):
        pass
        
    def setTargets(self, data):
        self.GUIPublisher.setTargets(data)
       
        
    ########################################################################
    # functions to handle and process messages
    
    
    # packs and sends the final message
    def packMsg(self, msgType = DUMMY, data = None):
        self.lock.acquire()
        msgNr = self.requestnumber
        timestamp = self.getTime()
    
        packedData = pickle.dumps([msgNr, msgType, timestamp, data], -1)
        
        self.requestnumber += 1
        self.lock.release()

        return(packedData)
    
    
    
    # in case of invalid msg, the type is returned as False
    def unpackMsg(self, packedData):
        
        [msgNr, msgType, timestamp, data] = pickle.loads(packedData)
        
        
        
        # prevent replay
        
        self.lock.acquire()
        if not (msgNr in self.receivedMessages):
            self.receivedMessages.append(msgNr)
            # don't process old messages
            if self.getTime() - timestamp < self.TIMEOUT:
                self.lock.release()    
                return(msgNr, msgType, timestamp, data)
            
            else:
                print("timeout")
                self.lock.release() 
                return(False, False, None, None)
        print("number used:", msgNr, msgType)
        self.lock.release() 
        return(False, False, None, None)
        
    def processMessage(self, msgNr, msgType, timestamp, data):
        #~ print(msgNr, msgType, data) 
        if msgType == self.OK:
            print("Message with the number " + str(data) + " received")
            
        elif msgType == self.DUMMY:
            pass
            
        elif msgType == self.SHUTDOWN:
            #shutdown
            self.sendOK(msgNr)
            self.setTargets([0,0])
            
        elif msgType == self.GETSPEED:
            self.sendReturnSpeed()
            
        elif msgType == self.RETURNSPEED:
            self.setSpeed(data)
            
        elif msgType == self.SETTARGETSPEED:
            self.setTargetSpeed(data)
            
        elif msgType == self.RETURNTARGETSPEED:
            print('target speed and angle: ', data)
            self.setTargetSpeedAndAngle(data)
        
        elif msgType == self.SETTARGETSTEERANGLE:
            self.setTargetSteerAngle(data)
            
        elif msgType == self.GETTILT:
            self.sendReturnTilt()
            
        elif msgType == self.RETURNTILT:
            self.setTilt(data)
            
        elif msgType == self.GETOBSTACLES:
            self.sendReturnObstacles()
        
        elif msgType == self.RETURNOBSTACLES:
            self.updateObstacleMap(data)
            
        elif msgType == self.GETBATTERY:
            self.sendReturnBattery()
            
        elif msgType == self.RETURNBATTERY:
            self.setBattery(data)
            
        elif msgType == self.WARNING:
            self.displayWarning(data)
            
        elif msgType == self.SETRECORD:
            self.setStatsToRecord(data)
            
        elif msgType == self.GETRECORDEDSTATS:
            tilt = []
            steeringAngle = []
            speed = []
            obstacles = []
            self.sendReturnRecordedStats([tilt, steeringAngle, speed, obstacles])
            
        elif msgType == self.RETURNRECORDEDSTATS:
            tilt = data[0]
            steeringAngle = data[1]
            speed = data[2]
            obstacles = data[3]
            
        elif msgType == self.GETORIENTATION:
            self.sendReturnOrientation()
            
        elif msgType == self.RETURNORIENTATION:
            ox = data[0]
            oy = data[1]
            oz = data[2]
            self.UI.updateTiltImg(ox)
            
        elif msgType == self.GETSTEERANGLE:
            self.sendReturnSteerAngle()
            
        elif msgType == self.RETURNSTEERANGLE:
            self.setSteerAngle(data)
            
        elif msgType == self.GETCAMERAIMAGE:
            self.sendReturnCameraImage()
            
        elif msgType == self.RETURNCAMERAIMAGE:
            self.setCameraImage(data)
            
        elif msgType == self.UPDATELIMITS:
            self.setLimits(data)
            
        elif msgType == self.SETTARGETS:
            self.setTargets(data)
        
class Refresher():
    
    SPEEDFQZ = 0.5 #
    TILTFQZ = 0.2 #
    OBJFQZ = 0.2 #
    STEERFQZ = 0.5 #
    BATFQZ = 2 #
    CAMFQZ = 2 #
    
    
    POSFQZ = 0.2
    
    #~ ORTFQZ = 99999
    
    refresh = False
    
    pause = False
    
    
    delay = 0

    
    
    def __init__(self, con):
        self.con = con
    
    def start(self):
        self.refresh = True

        self.updateTilt() #
        self.updateObj() #
        self.updateBattery() #
        self.updateSteer() #
        self.updateSpeed() #
        self.updateCamera() #

    
    
    def stop(self):
        self.refresh = False
        
    def updateTilt(self):
        if self.refresh:
            threading.Timer(self.TILTFQZ, self.updateTilt).start()

            self.con.sendGetTilt()
        
    def updateSpeed(self):
        if self.refresh:
            threading.Timer(self.SPEEDFQZ, self.updateSpeed).start()

            self.con.sendGetSpeed()
        
    def updateObj(self):
        if self.refresh:
            threading.Timer(self.OBJFQZ, self.updateObj).start()

            self.con.sendGetObstacles()
        
        
    def updateSteer(self):
        if self.refresh:
            threading.Timer(self.STEERFQZ, self.updateSteer).start()

            self.con.sendGetSteerAngle()
        
    #~ def updateOrientation(self):
        #~ if self.refresh:
            #~ threading.Timer(self.ORTFQZ, self.updateOrientation).start()
            #~ self.con.sendGetOrientation()
       
    def updateBattery(self):
        if self.refresh:
            threading.Timer(self.BATFQZ, self.updateBattery).start()
            self.con.sendGetBattery()

    def updateCamera(self):
        if self.refresh:
            threading.Timer(self.CAMFQZ, self.updateCamera).start()
            self.con.sendGetCameraImage()

        
        
        
    def setSpeedFqz(self, fqz):
        self.SPEEDFQZ = fqz
        
    def setTiltFqz(self, fqz):
        self.TILTFQZ = fqz
        
    def setObjFqz(self, fqz):
        self.OBJFQZ = fqz
    
    def setSteerFqz(self, fqz):
        self.STEERFQZ = fqz
        
    def setBattFqz(self, fqz):
        self.BATFQZ = fqz
        
    def setCamFqz(self, fqz):
        self.CAMFQZ = fqz
        
    
    
    def setPosFqz(self, fqz):
        self.POSFQZ = fqz
        
    def setOrtFqz(self, fqz):
        self.ORTFQZ = fqz
        

