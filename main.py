from gui.gui import*
import gui.ipdialog as ipD
from PyQt4.QtGui import *
import thread



import sys
import communicator as com
import thread

MSSTEP = 0.3
speed = 0
lastBatteryState = 0

host = "localhost"
port = 9999
server = False

import sys
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "gui\dialogIP.ui" # Enter file here.
 
Ui_IPdialog, QtBaseClass = uic.loadUiType(qtCreatorFile)
 




def init():
    global Com    

    
    #connect buttons

    ui.emergencyStopButton.clicked.connect(emergencyStop)
    
    ui.submitSpeedAndTilt.clicked.connect(submitTargets)
    
    ui.actionConnect_to_bike.triggered.connect(connectToBike)
    ui.actionSet_IP.triggered.connect(ipDialog)
    
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
    

