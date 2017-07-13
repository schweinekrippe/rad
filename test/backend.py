import thread
import time


#  periodically ads certain requests to the toDoList
class Refresher():
    
    SPEEDFQZ = 0.2
    TILTFQZ = 0.2
    OBJFQZ = 0.2
    STEERFQZ = 0.2
    POSFQZ = 0.2
    
    refresh = False
    
    speedLastUpdate = 0
    tiltLastUpdate = 0
    objLastUpdate = 0
    steerLastUpdate = 0
    posLastUpdate = 0
    
    pause = False
    delay = 0

    
    
    def __init__(self, con):
        self.con = con
        #~ self.start()
        thread.start_new_thread(self.updater, ())
    
    def start(self):
        self.refresh = True
    
    def stop(self):
        self.refresh = False
    
    def pause(self, delay = 1):
        self.pause = True
        self.delay = delay
    
    def updater(self):
        while self.refresh:
            if self.pause:
                time.sleep(self.delay)
                self.pause = False
                
            t = time.time()
            
            if t > self.speedLastUpdate + self.SPEEDFQZ:
                self.con.sendGetSpeed()
                self.speedLastUpdate = t
                
            if t > self.tiltLastUpdate + self.TILTFQZ:
                self.con.sendGetTilt()
                self.tiltLastUpdate = t
                
            if t > self.objLastUpdate + self.OBJFQZ:
                self.con.sendGetObstacles()
                self.objLastUpdate = t
                
            if t > self.steerLastUpdate + self.STEERFQZ:
                self.con.sendGetSteerAngle()
                self.steerLastUpdate = t
            
        
        
        
    def setSpeedFqz(self, fqz):
        self.SPEEDFQZ = fqz
        
    def setTiltFqz(self, fqz):
        self.SPEEDFQZ = fqz
        
    def setObjFqz(self, fqz):
        self.OBJFQZ = fqz
    
    def setSteerFqz(self, fqz):
        self.STEERFQZ = fqz
    
    def setPosFqz(self, fqz):
        self.POSFQZ = fqz

