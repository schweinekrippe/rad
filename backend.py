import thread
import time
import threading


#  periodically ads certain requests to the toDoList
class Refresher():
    
    SPEEDFQZ = 0.5 #
    TILTFQZ = 0.2 #
    OBJFQZ = 0.2 #
    STEERFQZ = 0.5 #
    BATFQZ = 2 #
    CAMFQZ = 2 #
    
    
    POSFQZ = 0.2
    #~ ORTFQZ = 0.1
    
    
    refresh = False
    
    pause = False
    
    
    delay = 0

    
    
    def __init__(self, con):
        self.con = con
        #~ self.start()

        #~ self.start()
    
    def start(self):
        self.refresh = True
        #~ self.update(SPEEDFQZ, self.con.sendGetSpeed)

        self.updateTilt() #
        self.updateObj() #
        self.updateBattery() #
        self.updateSteer() #
        self.updateSpeed() #
        self.updateCamera() #

    
    
    def stop(self):
        self.refresh = False
    
    #~ def pause(self, delay = 1):
        #~ self.pause = True
        #~ self.delay = delay
        
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
        
    def updateOrientation(self):
        if self.refresh:
            threading.Timer(self.ORTFQZ, self.updateOrientation).start()
            self.con.sendGetOrientation()
       
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
        

