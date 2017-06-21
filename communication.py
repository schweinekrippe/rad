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
SETSPEED = 23    # sets a new target speed
GETTILT = 4      # requests the current tilt data
RETURNTILT = 14  # answers the tilt request
GETOBSTACLES = 5 # requests the current detected obstacles
RETURNOBSTACLES = 15 # answers the obstacle request
GETBATTERY = 6
RETURNBATTERY = 16


requestnumber = 0
receivedMessages = []
toDoList = []

def getTime():
    return time.time()-TIMEOFFSET

def sendOK(answerID):
    toDoList.append(packMsg(OK, answerID))

def sendWarnMsg(msg):
    pass
    
def sendEmergencyStop():
    toDoList.append(packMsg(2, "stop"))
    
def sendRecordList(lst = []):
    pass
   
   
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
