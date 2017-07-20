import socket
import sys
import pickle

import thread
import time
import Queue

import backend
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui, uic

import random

class SensorData():
    fakedata = range(-90, 90, 5)
    i = 0
    
    fakeObst = [[[1,2,3],[4,5,6]],[[1,3,2]],[[1,7,4]],[[3,2,0.5]]]
    j = 0
    
    switch = True
    def getOrientation(self):
        #~ print(len(self.fakedata), self.i)
        data = self.fakedata[self.i]
        self.i += 1
        if self.i == 35:
            self.i = 0
            
        
        return [0, data, 0]
        
    def getLinAcc(self):
        pass
    
    
    def getObstacles(self):
        data = self.fakeObst[self.j]
        self.j += 1
        if self.j == 3:
            self.j = 0
        return data
    
    def getBattery(self):
        return(random.random()*100)
        
    def getSpeed(self):
        return(random.random()*35)
        
    def getSteer(self):
        return(random.random()*180 -90)
        
    def getCamera(self):
        if self.switch:
            self.switch = False        
            return(open('C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\images\\heckview.png', "rb").read())
            
        
        else:
            self.switch = True   
            return(open('C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\images\\heckviewinv.png', "rb").read())
        



class Communicator():
    

    
    TIMEOFFSET = 0
    TIMEOUT = 5000.000
    
    
    DUMMY = 0
    OK = 1
    SHUTDOWN = 2
    GETSPEED = 30     # requests current speed setting
    RETURNSPEED = 31 # answers current speed setting
    SETTARGETSPEED = 32    # sets a new target speed
    GETTARGETSPEED = 33
    RETURNTARGETSPEED = 34
    GETTILT = 40      # requests the current tilt data
    RETURNTILT = 41  # answers the tilt request
    GETOBSTACLES = 50 # requests the current detected obstacles
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
    
    requestnumber = 1
    receivedMessages = []
    
    
    isServer = True


    def __init__(self, host = "", port = 9999, server = True, parent = None):
        
        self.HOST = host
        self.PORT = port
        self.isServer = server

        self.toDoList = Queue.Queue()

        self.lock = thread.allocate_lock()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if self.isServer == False:
            self.R = backend.Refresher(self)
            self.UI = parent
            #~ print(parent)
        
        self.Sensor = SensorData()
        
        
    
    # sets the Ui
    # only neccessary for the client/bike
    def setUi(self, UI):
        self.UI = UI
        #~ print("UI set")
        
    # runs the communicator in Server/Client mode depending on the init type
    def run(self):

        if self.isServer:
 
            self.Sensor = SensorData()

            self.server()

        else:
            self.client()
            
        #~ self.sendGetTilt()

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
        #~ global toDoList
    
        while True:
            msg = self.toDoList.get()
            
            arr = []
            lenMsg = len(msg)
            for i in range (0, lenMsg, 1023):
                if i >= lenMsg - 1023:
                    arr.append(bytes(1)+msg[i:i + 1023])
                
                else:
                    arr.append(bytes(0)+msg[i:i + 1023])
            
                
            for element in arr:
                sock.sendall(element)
            
            
    
    def receiver(self, sock):
        while True:
            
            msg = ""
            incMsg = "0"
    
            while incMsg[0] == "0":
                incMsg = sock.recv(1024)
                msg += (incMsg[1:])
            
            #~ incMsg = sock.recv(1024)
            try:
                msgNr, msgType, timestamp, data = self.unpackMsg(msg)
                self.processMessage(msgNr, msgType, timestamp, data)
            except:
                pass
                #~ self.UI.displayWarning("Command lost")
    

    def getTime(self):
        return time.time()- self.TIMEOFFSET
    
    ########################################################################
    # functions to send messages
    
    ## functions for server and client
    
    def sendOK(self, answerID):
        self.toDoList.put(self.packMsg(self.OK, answerID))
        
    ## functions for client/gui
        
    def sendEmergencyStop(self):
        self.toDoList.put(self.packMsg(self, self.SHUTDOWN, "stop"))
        
    def sendGetSpeed(self): 
        self.toDoList.put(self.packMsg(self.GETSPEED, None)) 
        
    def sendSetTargetSpeed(self):
        targetSpeed = self.getTargetSpeed()
        self.toDoList.put(self.packMsg(self.RETURNTARGETSPEED, targetSpeed))
        self.UI.displayWarning("target speed: "+str(targetSpeed))
        
    def sendReturnTargetSpeed(self):
        targetSpeed = self.getTargetSpeed()
        self.toDoList.put(self.packMsg(self.RETURNTARGETSPEED, targetSpeed))
        
        
    def sendGetTilt(self):
        self.toDoList.put(self.packMsg(self.GETTILT, None))
        
    def sendGetObstacles(self): 
        self.toDoList.put(self.packMsg(self.GETOBSTACLES, None))
    
    def sendReturnObstacles(self):
        obstacles = self.getObstacles()
        self.toDoList.put(self.packMsg(self.RETURNOBSTACLES, obstacles))
        
    def sendGetBattery(self):
        self.toDoList.put(self.packMsg(self.GETBATTERY, None))
    
    def sendRecordList(self):
        lst = getRecordList()
        self.toDoList.put(self.packMsg(self.SETRECORD, lst))
        
    def sendGetRecordedStats(self):
        self.toDoList.put(self.packMsg(self.GETRECORDEDSTATS, None))
        
    def sendGetSteerAngle(self):
        self.toDoList.put(self.packMsg(self.GETSTEERANGLE, None))
    
    def sendReturnTargetSteerAngle(self):
        angle = self.getTargetSteerAngle()
        self.toDoList.put(self.packMsg(self.RETURNTARGETSTEERANGLE, angle))
        
    def sendSetTargetSteerAngle(self):
        targetAngle = self.getTargetSteerAngle()
        self.toDoList.put(self.packMsg(self.SETTARGETSTEERANGLE, targetAngle))
        self.UI.displayWarning("target Angle: "+str(targetAngle))
        
    def sendGetOrientation(self):
        self.toDoList.put(self.packMsg(self.GETORIENTATION, None))
        
    def sendGetCameraImage(self):
        self.toDoList.put(self.packMsg(self.GETCAMERAIMAGE, None))
        
    def sendUpdateLimits(self):
        
        minTilt, maxTilt = self.getLimits()
        self.toDoList.put(self.packMsg(self.UPDATELIMITS , [minTilt, maxTilt]))

    
    ## functions for server/bike
       
    def sendReturnSpeed(self):
        speed = self.getSpeed()
        self.toDoList.put(self.packMsg(self.RETURNSPEED, speed))
        
    def sendGetTargetSpeed(self):
        self.toDoList.put(self.packMsg(self.GETTARGETSPEED, None))
    
    def sendReturnTilt(self):
        tilt = self.getTiltAngle()[1]
        self.toDoList.put(self.packMsg(self.RETURNTILT, tilt)) 
    
    def sendReturnBattery(self): 
        battery = self.getBattery()
        self.toDoList.put(self.packMsg(self.RETURNBATTERY, battery))
    
    def sendWarnMsg(self, msg = ""):
        self.toDoList.put(self.packMsg(self.WARNING, msg))
    
    def sendReturnRecordedStats(self, stats = [] ):
        self.toDoList.put(self.packMsg(self.RETURNRECORDEDSTATS, stats))
        
    def sendReturnSteerAngle(self):
        angle = self.getSteerAngle()
        self.toDoList.put(self.packMsg(self.RETURNSTEERANGLE, angle))
    
    def sendGetTargetSteerAngle(self):
        self.toDoList.put(self.packMsg(self.GETTARGETSTEERANGLE, None)) 
        

    
    def sendReturnOrientation(self):
        ox, oy, oz = self.Sensor.getOrientation()
        self.toDoList.put(self.packMsg(self.RETURNORIENTATION, [ox,oy, oz]))
    
    def sendReturnCameraImage(self):
        self.toDoList.put(self.packMsg(self.RETURNCAMERAIMAGE, self.getCameraImage()))
   


    ########################################################################
    # functions to set and get data
    
    def getSteerAngle(self):
        return self.Sensor.getSteer()
        
    def setSteerAngle(self, angle):
        self.UI.updtSteerAngSig.emit(angle)
    
    def getSpeed(self):
        return self.Sensor.getSpeed()
        
    def getTargetSpeed(self):
        return self.UI.tgtSpeed
        
    def getTiltAngle(self):
        return self.Sensor.getOrientation()
        
    def getObstacles(self):
        obstacles = self.Sensor.getObstacles()
        return obstacles
    
    def getBattery(self):
        return self.Sensor.getBattery()
        
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
        return self.Sensor.getCamera()

    def getTargetSteerAngle(self):
        return self.UI.tgtSteer
        
    def getLimits(self):
        print(5)
        return(self.UI.minTilt, self.UI.maxTilt)       
    
    def displayWarning(self, msg):
        item = QListWidgetItem(msg)
        self.UI.msgList.addItem(item)
        
    def setSpeed(self, speed):
        self.UI.updtSpeedSig.emit(speed)
    
    def setTargetSpeed(self, speed):
        print("target speed: ", speed)
        
    def setTargetSteerAngle(self, angle):
        print("target steer angle: ", angle)
        
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
            
        elif msgType == self.GETSPEED:
            self.sendReturnSpeed()
            
        elif msgType == self.RETURNSPEED:
            self.setSpeed(data)
            
        elif msgType == self.SETTARGETSPEED:
            print("target speed:", data)
            self.setTargetSpeed(data)
            
        elif msgType == self.RETURNTARGETSPEED:
            self.setTargetSpeed(data)
        
        elif msgType == self.SETTARGETSTEERANGLE:
            print("target angle:", data)
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

