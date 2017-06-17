## define all messages and constants
##
## send pickled objets

## message format
## requestNr | request type | time | data
#
#  OK | 0
#  Shutdown | 1
#  
#  
#  
#  
#  
#  
#  





import pickle
import time

TIMEOFFSET = 0


DUMMY = 0
OK = 1
SHUTDOWN = 2
GETSPEED = 3     # requests current speed setting
RETURNSPEED = 13 # answers current speed setting
SETSPEED = 23    # sets a new target speed
GETTILT = 4      # requests the current tilt data
RETURNTILT = 14  # answers the tilt request
GETOBSTACLES = 5 # requests the current detected obstacles
RETURNOBSTACLES = 15 # answers the obstacle request
GETBATTERY = 6
RETURNBATTERY = 16


requestnumber = 0

def getTime():
    return time.time()-TIMEOFFSET

def sendOK(answerID):
    sendMessage(OK, answerID)

def sendTurnMsg(data):
    pass

def sendWarnMsg(msg):
    pass
    
def sendEmergencyStop():
    pass
    
def sendRecordList(lst = []):
    pass
   
def sendMessage(msgTyp = DUMMY, data = None):
    msgNr = requestnumber
    timestamp = getTime()
    packedData = pickle.dumps(data)
    
    requestnumber += 1
    
