## define all messages and constants
##
## send pickled objets

## message format
## requestNr | request type | time | data
#
#  OK | 0
#  Shutdown | 1
#  GETSPEED = 3     # requests current speed setting
#  RETURNSPEED = 13 # answers current speed setting
#  SETSPEED = 23    # sets a new target speed
#  GETTILT = 4      # requests the current tilt data
#  RETURNTILT = 14  # answers the tilt request
#  GETOBSTACLES = 5 # requests the current detected obstacles
#  RETURNOBSTACLES = 15 # answers the obstacle request
#  GETBATTERY = 6
#  RETURNBATTERY = 16
#  
#  






import pickle
import time

TIMEOFFSET = 0
TIMEOUT = 500.000


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


requestnumber = 0
receivedMessages = []
toDoList = []

def getTime():
    return time.time()-TIMEOFFSET

def sendOK(answerID):
    toDoList.append(packMsg(OK, answerID))
    
def sendEmergencyStop():
    toDoList.append(packMsg(SHUTDOWN, "stop"))
    
def sendGetSpeed():	
	toDoList.append(packMsg(GETSPEED, None))   
	 
def sendRetunSpeed(speed = 0):
	toDoList.append(packMsg(RETURNSPEED, speed))
	
def sendSetTargetSpeed(targetSpeed = 0):
	toDoList.append(packMsg(RETURNTARGETSPEED, targetSpeed))
	
def sendGetTargetSpeed():
	toDoList.append(packMsg(GETTARGETSPEED, None))
	
def sendReturnTargetSpeed(targetSpeed = 0)		
	toDoList.append(packMsg(RETURNTARGETSPEED, targetSpeed))
	
def sendGetTilt():
	toDoList.append(packMsg(GETTILT, None)

def sendReturnTilt(tilt = 0):
	toDoList.append(packMsg(RETURNTILT, tilt))	

def sendGetObstacles():		
	toDoList.append(packMsg(GETOBSTACLES, None))

def sendReturnObstacles(obstacles):	
	toDoList.append(packMsg(RETURNOBSTACLES, obstacles))

def sendGetBattery():
	toDoList.append(packMsg(GETBATTERY, None))

def sendReturnBattery(battery):	
	toDoList.append(packMsg(RETURNBATTERY, battery))
	
def sendWarnMsg(msg = ""):
    toDoList.append(packMsg(WARNING, msg))
    
def sendRecordList(lst = [True, True, True, True, True, True]):
    toDoList.append(packMsg(SETRECORD, lst))
    
def sendGetRecordedStats():
	toDoList.append(packMsg(GETRECORDEDSTATS, None))
	
def sendReturnRecordedStats(stats = [] ):
	toDoList.append(packMsg(RETURNRECORDEDSTATS, stats))

   
   
# packs and sends the final message
def packMsg(msgType = DUMMY, data = None):
    global requestnumber
    msgNr = requestnumber
    timestamp = getTime()

    packedData = pickle.dumps([msgNr, msgType, timestamp, data], -1)
    
    requestnumber += 1
    return(packedData)



# in case of invalid msg, the type is returned as False
def unpackMsg(packedData):
    [msgNr, msgType, timestamp, data] = pickle.loads(packedData)
    
    # prevent replay
    if not (msgNr in receivedMessages):
        receivedMessages.append(msgNr)
        # don't process old messages
        print(getTime()- timestamp, TIMEOUT)
        if getTime() - timestamp < TIMEOUT:
            print(msgNr, msgType, timestamp, data)

            return(msgNr, msgType, timestamp, data)
        
        else:
            print("timeout")
            return(False, False, None, None)
    print("number used")
    return(False, False, None, None)
    
def processMessage(msgNr, msgType, timestamp, data):	
    if msgType == OK:
        print("Message with the number " + str(data) + " received")
        
    elif msgType == DUMMY:
        pass
        
    elif msgType == SHUTDOWN:
        #shutdown
        toDoList.append(sendOK(msgNr))
