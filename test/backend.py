import thread
import time
import threading


#  periodically ads certain requests to the toDoList
class Refresher():
    
    SPEEDFQZ = 0.2
    TILTFQZ = 2.2
    OBJFQZ = 10.2
    STEERFQZ = 0.2
    POSFQZ = 0.2
    ORTFQZ = 0.1
    
    refresh = False
    
    speedLastUpdate = 0
    tiltLastUpdate = 0
    objLastUpdate = 0
    steerLastUpdate = 0
    posLastUpdate = 0
    ortLastUpdate = 0
    
    pause = False
    delay = 0

    
    
    def __init__(self, con):
        self.con = con
        #~ self.start()

        #~ self.start()
    
    def start(self):
        #~ self.refresh = True
        #~ self.update(SPEEDFQZ, self.con.sendGetSpeed)

        self.updateTilt()
        #~ self.updateObj()
        #~ self.update(TILTFQZ, self.con.sendGetTilt)
    
    
    def stop(self):
        self.refresh = False
    
    def pause(self, delay = 1):
        self.pause = True
        self.delay = delay
        
    def updateTilt(self):

        threading.Timer(self.TILTFQZ, self.updateTilt).start()

        self.con.sendGetTilt()
        
    def updateSpeed(self):
        threading.Timer(self.SPEEDFQZ, self.updateSpeed).start()

        self.con.sendGetSpeed()
        
    def updateObj(self):
        threading.Timer(self.OBJFQZ, self.updateObj).start()

        self.con.sendGetObstacles()
        
        
    #~ def updateTilt(self):
        #~ threading.Timer(self.STEERFQZ, self.updateTilt).start()

        #~ self.con.sendGetSteerAngle()
        
    def updateOrientation(self):
        threading.Timer(self.ORTFQZ, self.updateTilt).start()
        self.con.sendGetOrientation()
       
    

        
                #~ self.steerLastUpdate = t
                
            #~ if t > self.ortLastUpdate + self.ORTFQZ:
                #~ self.con.sendGetOrientation()
        
    
    #~ def update(self, intrval, worker_func):
        #~ threading.Timer(interval, update, [interval, worker_func].start()
        
        #~ worker_func()
        
        
        
        
        
        #~ while self.refresh:
            #~ if self.pause:
                #~ time.sleep(self.delay)
                #~ self.pause = False
                
            #~ t = time.time()
            #~ print(t, self.tiltLastUpdate)
            
            #~ if t > self.speedLastUpdate + self.SPEEDFQZ:
                #~ self.con.sendGetSpeed()
                #~ self.speedLastUpdate = t

            
            #~ if t > self.tiltLastUpdate + self.TILTFQZ:
                #~ self.con.sendGetTilt()
                #~ self.tiltLastUpdate = t
                
            #~ if t > self.objLastUpdate + self.OBJFQZ:
                #~ self.con.sendGetObstacles()
                #~ self.objLastUpdate = t
                
            #~ if t > self.steerLastUpdate + self.STEERFQZ:
                #~ self.con.sendGetSteerAngle()
                #~ self.steerLastUpdate = t
                
            #~ if t > self.ortLastUpdate + self.ORTFQZ:
                #~ self.con.sendGetOrientation()
                #~ self.ortLastUpdate = t
      
        
        
        
    def setSpeedFqz(self, fqz):
        self.SPEEDFQZ = fqz
        
    def setTiltFqz(self, fqz):
        self.TILTFQZ = fqz
        
    def setObjFqz(self, fqz):
        self.OBJFQZ = fqz
    
    def setSteerFqz(self, fqz):
        self.STEERFQZ = fqz
    
    def setPosFqz(self, fqz):
        self.POSFQZ = fqz
        
    def setOrtFqz(self, fqz):
        self.ORTFQZ = fqz

