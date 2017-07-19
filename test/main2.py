#!/usr/bin/python
# -*- coding: utf-8 -*-



import sys
from PyQt4 import QtCore, QtGui, uic
import gui.ipdialog as ipD
from PyQt4.QtGui import *
import thread
import communicator as com
import backend
import matplotlib
import matplotlib.figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar


 
ipFile = "C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\gui\\dialogIP.ui" # Enter file here.
 
Ui_IPdialog, QtBaseClass = uic.loadUiType(ipFile)

fqzFile = "C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\gui\\dialogFQZ.ui" # Enter file here.
 
Ui_FQZdialog, QtBaseClass = uic.loadUiType(fqzFile)

mainFile= "C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\gui\\MainWindow2-dark.ui" # Enter file here.
 
Ui_Main, QtBaseClass = uic.loadUiType(mainFile)
 
 
class MainWindow(QtGui.QMainWindow, Ui_Main):
    
    updateTilt = QtCore.pyqtSignal(float)
    print(updateTilt)
    
        
    
    # constants for the plot of the obstacles
    # distance / y-coordinate
    OBSTMINDIST = 0
    OBSTMAXDIST = 10
    # range of the plot in the x-coordinate
    OBSTMOSTLEFT = -5
    OBSTMOSTRIGHT = 5
    
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_Main.__init__(self)
        self.setupUi(self)
        
        self.ipd = IPDialog(self)
        self.fzd = FQZDialog(self)
        
        # init variables
        self.host = "localhost"
        self.port = 9999
        self.tgtSpeed = 0
        self.tgtSteer = 0
        
        
        #test mode
        self.connectionEstablished = False
        
        # set graphics
        self.tiltPixmap = QtGui.QPixmap('C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\images\\heckviewinv.png')
        self.tiltImg.setPixmap( self.tiltPixmap)
        self.middleImg.setPixmap( QtGui.QPixmap('C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\images\\middleLine.png'))
        
        self.emergencyStopButton.setIcon(QtGui.QIcon('C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\images\\stop40.png'))
        
        
        #connect all buttons to functions
        self.emergencyStopButton.clicked.connect(self.emergencyStop)
        
        # connect all actions to functions
        self.actionSet_IP.triggered.connect(self.ipDialog)
        self.actionConnect_to_bike.triggered.connect(self.connectToBike)
        self.submitSpeedAndTilt.clicked.connect(self.submitTargets)
        self.actionSet_refresh_rates.triggered.connect(self.fqzDialog)
        
        
        self.updateTilt.connect(self.updateTiltImg, QtCore.Qt.QueuedConnection)
        #~ print(self.updateTilt)
        
        # setup the display
        
        #~ self.obstMap.xlim(-5, 5)
        #~ self.obstMap.ylim(0, 10)
        

        
        
        # test display
        
        #~ self.updateObstacleMap([[1,2,3], [3,5,2], [1,2,7], [3,5,7]])
        #~ self.updateObstacleMap([[1,2,3], [3,5,2], [1,2,7], [3,5,7]])
        #~ self.updateObstacleMap([[1,2,7], [3,5,7]])
        #~ self.updateTiltImg(15)
       
        
        
        
    # open IP dialog
    def ipDialog(self):
        self.ipd.show()
    
    def fqzDialog(self):
        self.fzd.show()
    
    # display a custom message
    def displayWarning(self, msg):
        item = QListWidgetItem(msg)
        self.msgList.addItem(item)
        self.msgList.scrollToBottom()
        
    # send a message to the bike to stop
    # TODO: send message
    def emergencyStop(self):
        self.displayWarning("Emergency stop initiated")
        
        
    #sets the battery state to value (in %)
    # accepts int/float [0,100]    
    def setBatteryState(self, battery):
        self.batteryState.setProperty("value", battery)
    
    # update speed
    def setSpeed(self, speed):
        self.currentSpeed.setProperty("value", speed)
        
    # update steeringAngle
    def setSteeringAngle(self, angle):
        self.currentSteeringAngle.setProperty("value", angle)
    
    # connect to the bike
    def connectToBike(self):
        self.Com = com.Communicator(self.host, self.port, server=False, parent = self)
        #~ self.Com.setUi(self)
        thread.start_new_thread(self.Com.run, ())
        
    def submitTargets(self):
        if self.connectionEstablished:
            self.tgtSpeed = self.speedSlider.value()
            self.tgtSteer = self.steerSlider.value()
        
            self.Com.sendSetTargetSpeed()
            self.Com.sendSetTargetSteerAngle()
        
        else:
            self.displayWarning("Establish connection first")
            self.targetSpeedChanged.show()
            self.targetSpeed.hide()
            self.targetSpeedChanged.show()
            self.targetAngle.hide()
            self.targetAngleChanged.show()

    @QtCore.pyqtSlot(int)
    def updateTiltImg(self, angle = 0 ):

        transformation = QtGui.QTransform()

        transformation.rotate(angle)
        pxmp = self.tiltPixmap
        
        pixmap = pxmp.transformed(transformation)
        self.tiltImg.setPixmap(pixmap)
        self.tiltImg.update()
        
        self.tiltLabel.setText(str(angle)+ "°")

        
    def updateObstacleMap(self, obstData = [[]]):
        
        #~ print(obstData)
        
        # remove the old plot
        self.obstMap.axes.hold(False)
        for obst in obstData:
            #~ obst = [1,6,6]
            self.obstMap.axes.plot([obst[0], obst[1]], [obst[2], obst[2]], 'k-', lw=2)
            # make sure the plot is not overwritten
            self.obstMap.axes.hold(True)
            
        self.obstMap.axes.set_xlim([self.OBSTMOSTLEFT,self.OBSTMOSTRIGHT])
        self.obstMap.axes.set_ylim([self.OBSTMINDIST,self.OBSTMAXDIST])

class IPDialog(QtGui.QMainWindow, Ui_IPdialog):
    def __init__(self, parent):
        self.parent = parent
        QtGui.QMainWindow.__init__(self)
        Ui_IPdialog.__init__(self)
        self.setupUi(self)
        
        
    def accept(self):
        ip1 = self.IP1_entry.text()
        ip2 = self.IP2_entry.text()
        ip3 = self.IP3_entry.text()
        ip4 = self.IP4_entry.text()
        
        port = self.PORT_entry.text()
        
        try:
            ip1 = int(ip1)
            ip2 = int(ip2)
            ip3 = int(ip3)
            ip4 = int(ip4)
            
            port = int(port)

            if ip1 <= 255 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255 and port <= 65535:

                self.parent.port = port
                self.parent.host = "" + str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4)
        
                msghost = "Ip updated to: "+self.parent.host + "\n Port updated to: "+ str(self.parent.port)
                
                self.parent.displayWarning(msghost)
            
            else:
                self.parent.displayWarning("IP or host not valid")
        
        except:
            self.parent.displayWarning("IP or host not valid")
            
            
        self.close()
    
    def reject(self):
        self.close()
 
class FQZDialog(QtGui.QMainWindow, Ui_FQZdialog):
    def __init__(self, parent):
        self.parent = parent
        QtGui.QMainWindow.__init__(self)
        Ui_FQZdialog.__init__(self)
        self.setupUi(self)
        
        
    def accept(self):
        
        steer = self.steer_entry.text()
        tilt = self.tilt_entry.text()
        objects = self.objects_entry.text()
        position = self.position_entry.text()
        speed = self.speed_entry.text()
        
        msg = "Update intervalls set to:\nSpeed: "+ speed +"\nTilt angle: " + tilt + "\n Objects: " + objects + "\n Position: " + position + "\n Steering angle: " + steer 

        if True:
        #~ try:
            steer = float(steer)
            tilt = float(tilt)
            objects = float(objects)
            position = float(position)
            speed = float(speed)
            
            
        
            self.parent.Com.R.setSpeedFqz(speed)
            self.parent.Com.R.setTiltFqz(tilt)
            self.parent.Com.R.setObjFqz(objects)
            self.parent.Com.R.setSteerFqz(steer)
            self.parent.Com.R.setPosFqz(position)
            
            self.parent.displayWarning(msg)
            
        #~ except:
            #~ self.parent.displayWarning("Update intervalls invalid. Float or int required")
 
        self.close()
    
    def reject(self):
        self.close()
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
