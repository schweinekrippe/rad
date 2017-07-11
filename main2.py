import sys
from PyQt4 import QtCore, QtGui, uic
import gui.ipdialog as ipD
from PyQt4.QtGui import *
import thread
import communicator as com
 
ipFile = "C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\gui\\dialogIP.ui" # Enter file here.
 
Ui_IPdialog, QtBaseClass = uic.loadUiType(ipFile)

fqzFile = "C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\gui\\dialogFQZ.ui" # Enter file here.
 
Ui_FQZdialog, QtBaseClass = uic.loadUiType(fqzFile)

mainFile= "C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\gui\\MainWindow2-dark.ui" # Enter file here.
 
Ui_Main, QtBaseClass = uic.loadUiType(mainFile)
 
class MainWindow(QtGui.QMainWindow, Ui_Main):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_Main.__init__(self)
        self.setupUi(self)
        
        self.ipd = IPDialog(self)
        selg.fzd = FQZDialog(self)
        
        # init variables
        self.host = "localhost"
        self.port = 9999
        self.tgtSpeed = 0
        self.tgtSteer = 0
        
        #test mode
        self.connectionEstablished = True
        
        # set graphics
        self.tiltImg.setPixmap( QtGui.QPixmap('C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\images\\heckviewinv.png'))
        self.middleImg.setPixmap( QtGui.QPixmap('C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\images\\middleLine.png'))
        
        self.emergencyStopButton.setIcon(QtGui.QIcon('C:\\Users\\Topfpflanze\\Documents\\pystuff\\rad\\images\\stop40.png'))
        
        
        #connect all buttons to functions
        self.emergencyStopButton.clicked.connect(self.emergencyStop)
        
        # connect all actions to functions
        self.actionSet_IP.triggered.connect(self.ipDialog)
        self.actionConnect_to_bike.triggered.connect(self.connectToBike)
        self.submitSpeedAndTilt.clicked.connect(self.submitTargets)
        
        
        # init the communication module
        
        
        self.Com = com.Communicator(self.host, self.port, server=False)
        self.Com.setUi(self)
        
        
    # open IP dialog
    def ipDialog(self):
        self.ipd.show()
    
    # display a custom message
    def displayWarning(self, msg):
        item = QListWidgetItem(msg)
        self.msgList.addItem(item)
        
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

    def updateTiltImg(self, angle = 0 ):
        transformation = QtGui.QTransform()

        transformation.rotate(angle)
        
        pixmap = self.tiltImg.transformed(transformation)
        self.tiltImage.setPixmap(pixmap)
        self.tiltImage.update()
        
        


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
        
                msghost = "Ip updated to: "+self.parent.host
                msgport = "Port updated to: "+ str(self.parent.port)

                self.parent.displayWarning(msghost)
                self.parent.displayWarning(msgport)
            
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
        Ui_IPdialog.__init__(self)
        self.setupUi(self)
        
        
    def accept(self):
        steerAngle = self.steer_entry.text()
        tiltAngle = self.tilt_entry.text()
        objects = self.objects_entry.text()
        position = self.pposition_entry.text()
        speed = self.speed_entry.text()
        
        
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
        
                msghost = "Ip updated to: "+self.parent.host
                msgport = "Port updated to: "+ str(self.parent.port)

                self.parent.displayWarning(msghost)
                self.parent.displayWarning(msgport)
            
            else:
                self.parent.displayWarning("IP or host not valid")
        
        except:
            self.parent.displayWarning("IP or host not valid")
            
            
        self.close()
    
    def reject(self):
        self.close()
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
