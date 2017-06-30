import socket
import sys
import pickle

import thread
import time
import Queue

import backend

class Communicator():
    
    HOST, PORT = "10.42.0.1", 9999
    
    TIMEOFFSET = 0
    TIMEOUT = 5.000
    
    
    DUMMY = 0
    OK = 1
    SHUTDOWN = 2
    GETSPEED = 3     # requests current speed setting
    RETURNSPEED = 13 # answers current speed setting
    SETTARGETSPEED = 23    # sets a new target speed
    GETTARGETSPEED = 33
    RETURNTARGETSPEED = 43
    GETTILT = 4      # requests the current tilt data
    RETURNTILT = 14  # answers the tilt request
    GETOBSTACLES = 5 # requests the current detected obstacles
    RETURNOBSTACLES = 15 # answers the obstacle request
    GETBATTERY = 6
    RETURNBATTERY = 16
    WARNING = 7
    SETRECORD = 8
    GETRECORDEDSTATS = 18
    RETURNRECORDEDSTATS = 28
    
    GETSTEERANGLE = 9
    RETURNSTEERANGLE = 9
    GETTARGETSTEERANGLE = 29
    RETURNTARGETSTEERANGLE = 39
    
    requestnumber = 1
    receivedMessages = []


    def __init__(self, host = "localhost", port = 9999, server = True):
        
        self.HOST = host
        self.port = port
        self.toDoList = Queue.Queue()
        self.lock = thread.allocate_lock()
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        if server:
            self.server()
        else:
            self.client()

    def client(self):

        self.sock.connect((self.HOST,self.PORT))
        
        self.R = backend.Refresher(self)

        thread.start_new_thread( self.sender,(self.sock,))
        thread.start_new_thread( self.receiver,(self.sock,))
    
    def server(self):

        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen(1)
    
        conn, addr = self.sock.accept()
        
        thread.start_new_thread( self.sender,(conn,))
        thread.start_new_thread( self.receiver,(conn,))
            
            
    def sender(self, sock):
        #~ global toDoList
    
        while True:
            sock.sendall(self.toDoList.get())
    
    def receiver(self, sock):
        while True:
            incMsg = sock.recv(1024)
            msgNr, msgType, timestamp, data = self.unpackMsg(incMsg)
            self.processMessage(msgNr, msgType, timestamp, data)
    

    def getTime(self):
        return time.time()- self.TIMEOFFSET
    
    ########################################################################
    # functions to send messages
    
    def sendOK(self, answerID):
        self.toDoList.put(self.packMsg(self.OK, answerID))
        
    def sendEmergencyStop(self):
        self.toDoList.put(self.packMsg(self, self.SHUTDOWN, "stop"))
        
    def sendGetSpeed(self): 
        self.toDoList.put(self.packMsg(self.GETSPEED, None))   
         
    def sendReturnSpeed(self, speed = 0):
        self.toDoList.put(self.packMsg(self.RETURNSPEED, speed))
        
    def sendSetTargetSpeed(self, targetSpeed = 0):
        self.toDoList.put(self.packMsg(self.RETURNTARGETSPEED, targetSpeed))
        
    def sendGetTargetSpeed(self):
        self.toDoList.put(self.packMsg(self.GETTARGETSPEED, None))
        
    def sendReturnTargetSpeed(self, targetSpeed = 0): 
        self.toDoList.put(self.packMsg(self.RETURNTARGETSPEED, targetSpeed))
        
    def sendGetTilt(self):
        self.toDoList.put(self.packMsg(self.GETTILT, None))
    
    def sendReturnTilt(self, tilt = 0):
        self.toDoList.put(self.packMsg(self.RETURNTILT, tilt))  
    
    def sendGetObstacles(self):     
        self.toDoList.put(self.packMsg(self.GETOBSTACLES, None))
    
    def sendReturnObstacles(self, obstacles): 
        self.toDoList.put(self.packMsg(self.RETURNOBSTACLES, obstacles))
    
    def sendGetBattery(self):
        self.toDoList.put(self.packMsg(self.GETBATTERY, None))
    
    def sendReturnBattery(self, battery): 
        self.toDoList.put(self.packMsg(self.RETURNBATTERY, battery))
        
    def sendWarnMsg(self, msg = ""):
        self.toDoList.put(self.packMsg(self.WARNING, msg))
    
    
    def sendRecordList(self, lst = [True, True, True, True, True, True]):
        self.toDoList.put(self.packMsg(self.SETRECORD, lst))
        
    def sendGetRecordedStats(self):
        self.toDoList.put(self.packMsg(self.GETRECORDEDSTATS, None))
        
    def sendReturnRecordedStats(self, stats = [] ):
        self.toDoList.put(self.packMsg(self.RETURNRECORDEDSTATS, stats))
        
    def sendGetSteerAngle(self):
        self.toDoList.put(self.packMsg(self.GETSTEERANGLE, None))
    
    def sendReturnSteerAngle(self):
        angle = self.getSteerAngle()
        self.toDoList.put(self.packMsg(self.RETURNSTEERANGLE, angle))
        
    def sendGetTargetSteerAngle(self):
        self.toDoList.put(self.packMsg(self.GETTARGETSTEERANGLE, None))
    
    def sendReturnTargetSteerAngle(self):
        angle = self.getTargetSteerAngle()
        self.toDoList.put(self.packMsg(self.RETURNTARGETSTEERANGLE, angle))

    ########################################################################
    # functions to set and get data
    
    def getSteerAngle(self):
        angle = 0
        return angle
    
    
    
    def displaywarning(self, msg):
        pass
        
    def setSpeed(self, speed):
        pass
    
    def setTargetSpeed(self, speed):
        pass
        
    def updateObstacleMap(self, data):
        pass
        
    def setTilt(self, tilt):
        pass
        
    def setBattery(self, battery):
        pass
        
    def setStatsToRecord(self, stats):
        recordTilt = stats[0]
        recordSteeringAngle = stats[1]
        recordSpeedProfile = stats[2]
        recordObstacles = stats[3]
  
        
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
        if not (msgNr in self.receivedMessages):
            self.receivedMessages.append(msgNr)
            # don't process old messages
            if self.getTime() - timestamp < self.TIMEOUT:
    
                return(msgNr, msgType, timestamp, data)
            
            else:
                print("timeout")
                return(False, False, None, None)
        print("number used:", msgNr, msgType)
        return(False, False, None, None)
        
    def processMessage(self, msgNr, msgType, timestamp, data):    
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
            print("speed: ", data)
            self.setSpeed(data)
            
        elif msgType == self.SETTARGETSPEED:
            self.setTargetSpeed(data)
            
        elif msgType == self.RETURNTARGETSPEED:
            self.setTargetSpeed(data)
            
        elif msgType == self.GETTILT:
            tilt = 0
            self.sendReturnTilt(tilt)
            
        elif msgType == self.RETURNTILT:
            self.setTilt(data)
            
        elif msgType == self.GETOBSTACLES:
            obstacles = []
            self.sendReturnObstacles(obstacles)
        
        elif msgType == self.RETURNOBSTACLES:
            self.updateObstacleMap(data)
            
        elif msgType == self.GETBATTERY:
            battery = 0
            self.sendReturnBattery(battery)
            
        elif msgType == self.RETURNBATTERY:
            self.setBattery(data)
            
        elif msgType == self.WARNING:
            self.displaywarning(data)
            
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

