from gui.gui import*
from PyQt4.QtGui import *


import sys
import communicator as com
import thread

MSSTEP = 0.3
speed = 0
lastBatteryState = 0

host = "localhost"
port = 9999
server = False

def init():
    global Com    

    
    #connect buttons

    ui.emergencyStopButton.clicked.connect(emergencyStop)
    
    ui.submitSpeedAndTilt.clicked.connect(submitTargets)
    
    ui.actionConnect_to_bike.triggered.connect(connectToBike)
    
    # set elements invisible
    ui.steeringImage.setVisible(False)
    ui.obstaclesImage.setVisible(False)
    ui.Compass.setVisible(False)
    
    # init communicator
    Com = com.Communicator(host, port, server)
    Com.setUi(ui)

    
def submitTargets():
    pass   
    
def setTiltImage():
    None

def connectToBike():
    

    thread.start_new_thread(Com.run, ())
    

def setSpeed(speed):
    ui.currentSpeed.setProperty("value", speed)

# send a message to the bike to stop
def emergencyStop():
    displayWarning("Emergency stop initiated")

#sets the battery state to value (in %)
# accepts int/float [0,100]
def updateBatteryState(value):
    ui.batteryState.setProperty("value", value)



def displayWarning(msg):
    item = QListWidgetItem(msg)
    ui.msgList.addItem(item)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    init()
    MainWindow.show()
    sys.exit(app.exec_())
    

