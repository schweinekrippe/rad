#!/usr/bin/python
# -*- coding: utf-8 -*-



import sys
from PyQt4 import QtCore, QtGui, uic

#~ import gui.ipdialog as ipD
from PyQt4.QtGui import *
import thread
import communicator as com
import matplotlib
import matplotlib.figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from PIL import Image, ImageQt
import numpy
import cv2

########################################################################
# GUI files
########################################################################
 
ipFile = "UI//dialogIP.ui" # Enter file here.
 
Ui_IPdialog, QtBaseClass = uic.loadUiType(ipFile)

fqzFile = "UI//dialogFQZ.ui" # Enter file here.
 
Ui_FQZdialog, QtBaseClass = uic.loadUiType(fqzFile)

limFile = "UI//dialogLIM.ui"

Ui_LIMdialog, QtBaseClass = uic.loadUiType(limFile)

mainFile= "UI//MainWindow.ui" # Enter file here.
 
Ui_Main, QtBaseClass = uic.loadUiType(mainFile)



########################################################################
# Images
########################################################################


 
 
class MainWindow(QtGui.QMainWindow, Ui_Main):
    
    updtTiltSig = QtCore.pyqtSignal(float)
    updtObstSig = QtCore.pyqtSignal(list)
    updtSpeedSig = QtCore.pyqtSignal(float)
    updtBatterySig = QtCore.pyqtSignal(float)
    updtSteerAngSig = QtCore.pyqtSignal(float)
    updtCameraImageSig = QtCore.pyqtSignal(list)
    
    # constants for the plot of the obstacles
    # distance / y-coordinate
    OBSTMINDIST = 0
    OBSTMAXDIST = 7
    # range of the plot in the x-coordinate
    OBSTMOSTLEFT = -5
    OBSTMOSTRIGHT = 5
    
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_Main.__init__(self)
        self.setupUi(self)
        
        self.ipd = IPDialog(self)
        self.fzd = FQZDialog(self)
        self.lmd = LIMDialog(self)
        
        # init variables
        self.host = "10.42.0.1"
        self.port = 9999
        self.tgtSpeed = 0
        self.tgtSteer = 0
        
        self.maxTilt = 30
        self.minTilt = 0
               
        
        #test mode
        self.connectionEstablished = False
        
        # set graphics
        self.tiltPixmap = QtGui.QPixmap('Images//heckviewinv.png')
        self.tiltImg.setPixmap( self.tiltPixmap)
        self.middleImg.setPixmap( QtGui.QPixmap('Images//middleLine.png'))
        
        self.emergencyStopButton.setIcon(QtGui.QIcon('Images//stop40.png'))
        
        
        #connect all buttons to functions
        self.emergencyStopButton.clicked.connect(self.emergencyStop)
        
        # connect all actions to functions
        self.actionSet_IP.triggered.connect(self.ipDialog)
        self.actionConnect_to_bike.triggered.connect(self.connectToBike)
        self.submitSpeedAndTilt.clicked.connect(self.submitTargets)
        self.actionSet_refresh_rates.triggered.connect(self.fqzDialog)
        self.actionSet_limits.triggered.connect(self.limDialog)
        
        
        self.updtTiltSig.connect(self.updateTiltImg, QtCore.Qt.QueuedConnection)
        self.updtObstSig.connect(self.updateObstacleMap, QtCore.Qt.QueuedConnection)
        self.updtSpeedSig.connect(self.setSpeed, QtCore.Qt.QueuedConnection)
        self.updtBatterySig.connect(self.setBatteryState, QtCore.Qt.QueuedConnection)
        self.updtSteerAngSig.connect(self.setSteeringAngle, QtCore.Qt.QueuedConnection)
        self.updtCameraImageSig.connect(self.setCameraImage, QtCore.Qt.QueuedConnection)
        
        # setup the display
        

        self.obstMap.axes.set_xlim([self.OBSTMOSTLEFT,self.OBSTMOSTRIGHT])
        self.obstMap.axes.set_ylim([self.OBSTMINDIST,self.OBSTMAXDIST])
        self.obstMap.axes.grid()

        
        
        
    # open IP dialog
    def ipDialog(self):
        self.ipd.show()
    
    def fqzDialog(self):
        self.fzd.show()
        
    def limDialog(self):
        self.lmd.show()
    
    # display a custom message
    def displayWarning(self, msg):
        item = QListWidgetItem(msg)
        self.msgList.addItem(item)
        self.msgList.scrollToBottom()
        
    # send a message to the bike to stop
    def emergencyStop(self):
        if self.connectionEstablished:
            self.displayWarning("Emergency stop initiated")
            self.Com.sendEmergencyStop()
        else:
            self.displayWarning("can't send STOP if not connected")
        
        
    #sets the battery state to value (in %)
    # accepts int/float [0,100]
    @QtCore.pyqtSlot(float) 
    def setBatteryState(self, battery):
        self.batteryState.setProperty("value", battery)
    
    # update speed
    @QtCore.pyqtSlot(float)
    def setSpeed(self, speed):
        self.currentSpeed.setProperty("value", speed)
        
    # update steeringAngle
    @QtCore.pyqtSlot(float)
    def setSteeringAngle(self, angle):
        #~ print("angle", angle)
        self.currentSteeringAngle.setProperty("value", angle)
    
    # connect to the bike
    def connectToBike(self):
        self.Com = com.Communicator(self.host, self.port, server=False, parent = self)
        thread.start_new_thread(self.Com.run, ())
        
    
    def submitTargets(self):
        if self.connectionEstablished:
            self.tgtSpeed = self.speedSlider.value()
            self.tgtSteer = self.steerSlider.value()
        
            self.Com.sendSetTargets()
            
            self.steerSlider.setValue(0)
            self.targetAngle.show()
            self.targetAngleChanged.hide()
        
        else:
            self.displayWarning("Establish connection first")
            self.targetSpeedChanged.show()
            self.targetSpeed.hide()
            self.targetSpeedChanged.show()
            self.targetAngle.hide()
            self.targetAngleChanged.show()

    @QtCore.pyqtSlot(float)
    def updateTiltImg(self, angle = 0 ):

        transformation = QtGui.QTransform()

        transformation.rotate(angle)
        pxmp = self.tiltPixmap
        
        pixmap = pxmp.transformed(transformation)
        self.tiltImg.setPixmap(pixmap)
        self.tiltImg.update()
        
        self.tiltLabel.setText(str(int(angle)) +  u' °')

    @QtCore.pyqtSlot(list)   
    def updateObstacleMap(self, obstData):
        
        #~ print("obstData:", obstData)
        
        # remove the old plot and set the plot up
        self.obstMap.axes.clear()
        self.obstMap.axes.hold(True)
        self.obstMap.axes.set_xlim([self.OBSTMOSTLEFT,self.OBSTMOSTRIGHT])
        self.obstMap.axes.set_ylim([self.OBSTMINDIST,self.OBSTMAXDIST])
        self.obstMap.axes.grid()
        
        for obst in obstData:
            self.obstMap.axes.plot([obst[0], obst[1]], [obst[2], obst[2]], 'k-', lw=2)
            
        self.obstMap.axes.figure.canvas.draw_idle()
    @QtCore.pyqtSlot(list)   
    def setCameraImage(self, data):   
        
        # for whtever reasons 6 bytes are added
        data = numpy.fromstring(data[0], dtype='uint8')[:-6]
        
        # rgb
        #~ dim = 3
        #~ imageFormat = QtGui.QImage.Format_RGB888
        
        # grayscale
        dim = 1
        imageFormat = QtGui.QImage.Format_Indexed8
        
        
        data = data.reshape((480, 640, dim))
        height, width = data.shape[:2]
        
        # cv images are BGR -> Convert to RGB
        #~ data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        
        

        img = QtGui.QImage(data, width, height, width*dim, imageFormat)
        self.cameraPixmap = QtGui.QPixmap.fromImage(img)

        self.cameraLabel.setPixmap(self.cameraPixmap)
        self.cameraLabel.update()
        

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
        
        battery = self.battery_entry.text()
        camera = self.camera_entry.text()
        
        msg = "Update intervalls set to:\nSpeed: "+ speed +"\nTilt angle: " + tilt + \
                    "\n Objects: " + objects + "\n Position: " + position + "\n Steering angle: " + steer \
                    + "\n Battery: " + battery + "\n Camera: " + camera

        if self.parent.connectionEstablished:
            try:
                steer = float(steer)
                tilt = float(tilt)
                objects = float(objects)
                position = float(position)
                speed = float(speed)
                battery = float(battery)
                camera = float(camera)
                
                
            
                self.parent.Com.R.setSpeedFqz(speed)
                self.parent.Com.R.setTiltFqz(tilt)
                self.parent.Com.R.setObjFqz(objects)
                self.parent.Com.R.setSteerFqz(steer)
                self.parent.Com.R.setPosFqz(position)
                self.parent.Com.R.setBattFqz(battery)
                self.parent.Com.R.setCamFqz(camera)
                
                self.parent.displayWarning(msg)
                
            except:
                self.parent.displayWarning("Update intervalls invalid. Float or int required")
                
        else:
            self.parent.displayWarning("Establish connection first")
 
        self.close()
    
    def reject(self):
        self.close()
 
class LIMDialog(QtGui.QMainWindow, Ui_LIMdialog):
    def __init__(self, parent):
        self.parent = parent
        QtGui.QMainWindow.__init__(self)
        Ui_LIMdialog.__init__(self)
        self.setupUi(self)
        
        
    def accept(self):
        # upper bound
        ub = self.maxTilt_entry.text()
        # lower bound
        lb = self.minTilt_entry.text()
        
        if self.parent.connectionEstablished:
            try:
                self.maxTilt = float(ub)
                self.minTilt = float(lb)

                self.parent.Com.sendUpdateLimits()
            except:
                self.parent.displayWarning("The limits need to be float or int")
        
        else:
            self.parent.displayWarning("Establish connection first")

        self.close()
    
    def reject(self):
        self.close()
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
