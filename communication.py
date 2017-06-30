## define all messages and constants
##
## send pickled objets

## message format
## requestNr | request type | time | data
#
#  OK 
#  Shutdown 
#  GETSPEED         # requests current speed setting
#  RETURNSPEED      # answers current speed setting
#  SETSPEED         # sets a new target speed
#  GETTILT          # requests the current tilt data
#  RETURNTILT       # answers the tilt request
#  GETOBSTACLES     # requests the current detected obstacles
#  RETURNOBSTACLES  # answers the obstacle request
#  GETBATTERY       #
#  RETURNBATTERY    #
#  WARNING          #
#  SETRECORD        #
#  GETRECORDEDSTATS #
#  RETURNRECORDEDSTATS  # 
#  






import pickle
import time
import Queue




requestnumber = 1
receivedMessages = []


toDoList = Queue.Queue()




