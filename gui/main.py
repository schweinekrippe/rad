from gui import*
from PyQt4.QtGui import *

import sys

MSSTEP = 0.3
speed = 0
lastBatteryState = 0



def init():
    ui.incSpeedButton.pressed.connect(incspeed)
    ui.decSpeedButton.pressed.connect(decspeed)
    ui.emergencyStopButton.clicked.connect(emergencyStop)
    ui.steeringImage.setVisible(False)
    ui.obstaclesImage.setVisible(False)
    displayWarning("custom message")
    updateBatteryState(33.67)
    
def setTiltImage():
    None

# replace by function sending a message to the bike to increase the speed
def incspeed():
    global speed, MSSTEP
    speed += MSSTEP
    if speed < 0.001 and speed > -0.001:
        speed = 0
    ui.currentSpeed.setProperty("value", speed)

# replace by function sending a message to the bike to decrease the speed
def decspeed():
    global speed, MSSTEP
    speed -= MSSTEP
    if speed < 0.001 and speed > -0.001:
        speed = 0
    ui.currentSpeed.setProperty("value", speed)

def setSpeed(speed):
    ui.currentSpeed.setProperty("value", speed)

# send a message to the bike to stop
def emergencyStop():
    displayWarning("Emergency stop initiated")

#sets the battery state to value (in %)
# accepts int/float [0,100]
def updateBatteryState(value):
    ui.batteryState.setProperty("value", value)

def turnLeft():
    None

def turnRight():
    None

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
