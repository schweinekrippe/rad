# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sat Jun 17 11:45:37 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(539, 522)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/heckview.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 521, 481))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_analyis = QtGui.QWidget()
        self.tab_analyis.setObjectName(_fromUtf8("tab_analyis"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_analyis)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 100, 171))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tiltCheckbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.tiltCheckbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tiltCheckbox.setAutoFillBackground(False)
        self.tiltCheckbox.setChecked(True)
        self.tiltCheckbox.setObjectName(_fromUtf8("tiltCheckbox"))
        self.verticalLayout.addWidget(self.tiltCheckbox)
        self.steeringCheckbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.steeringCheckbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.steeringCheckbox.setAutoFillBackground(False)
        self.steeringCheckbox.setChecked(True)
        self.steeringCheckbox.setObjectName(_fromUtf8("steeringCheckbox"))
        self.verticalLayout.addWidget(self.steeringCheckbox)
        self.speedCheckbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.speedCheckbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.speedCheckbox.setAutoFillBackground(False)
        self.speedCheckbox.setChecked(True)
        self.speedCheckbox.setObjectName(_fromUtf8("speedCheckbox"))
        self.verticalLayout.addWidget(self.speedCheckbox)
        self.obstaclesCheckbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.obstaclesCheckbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.obstaclesCheckbox.setAutoFillBackground(False)
        self.obstaclesCheckbox.setChecked(True)
        self.obstaclesCheckbox.setObjectName(_fromUtf8("obstaclesCheckbox"))
        self.verticalLayout.addWidget(self.obstaclesCheckbox)
        self.checkBox_5 = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_5.setAutoFillBackground(False)
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.verticalLayout.addWidget(self.checkBox_5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_analyis, _fromUtf8(""))
        self.tab_testing = QtGui.QWidget()
        self.tab_testing.setObjectName(_fromUtf8("tab_testing"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.tab_testing)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 101, 201))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget.addTab(self.tab_testing, _fromUtf8(""))
        self.tab_riding = QtGui.QWidget()
        self.tab_riding.setObjectName(_fromUtf8("tab_riding"))
        self.frame = QtGui.QFrame(self.tab_riding)
        self.frame.setGeometry(QtCore.QRect(40, 30, 151, 91))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.BatteryLabel = QtGui.QLabel(self.frame)
        self.BatteryLabel.setGeometry(QtCore.QRect(0, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BatteryLabel.setFont(font)
        self.BatteryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BatteryLabel.setObjectName(_fromUtf8("BatteryLabel"))
        self.batteryState = QtGui.QProgressBar(self.frame)
        self.batteryState.setGeometry(QtCore.QRect(0, 30, 151, 41))
        self.batteryState.setToolTip(_fromUtf8(""))
        self.batteryState.setProperty("value", 75)
        self.batteryState.setAlignment(QtCore.Qt.AlignCenter)
        self.batteryState.setInvertedAppearance(False)
        self.batteryState.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.batteryState.setObjectName(_fromUtf8("batteryState"))
        self.batteryImage = QtGui.QLabel(self.frame)
        self.batteryImage.setGeometry(QtCore.QRect(40, 40, 16, 21))
        self.batteryImage.setText(_fromUtf8(""))
        self.batteryImage.setPixmap(QtGui.QPixmap(_fromUtf8("images/348px-Angular_lightningbolt.svg.png")))
        self.batteryImage.setScaledContents(True)
        self.batteryImage.setObjectName(_fromUtf8("batteryImage"))
        self.emergencyStopButton = QtGui.QPushButton(self.tab_riding)
        self.emergencyStopButton.setGeometry(QtCore.QRect(40, 140, 151, 151))
        self.emergencyStopButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/Stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emergencyStopButton.setIcon(icon1)
        self.emergencyStopButton.setIconSize(QtCore.QSize(100, 100))
        self.emergencyStopButton.setCheckable(False)
        self.emergencyStopButton.setChecked(False)
        self.emergencyStopButton.setAutoDefault(False)
        self.emergencyStopButton.setFlat(False)
        self.emergencyStopButton.setObjectName(_fromUtf8("emergencyStopButton"))
        self.frame_2 = QtGui.QFrame(self.tab_riding)
        self.frame_2.setGeometry(QtCore.QRect(40, 300, 151, 151))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.incSpeedButton = QtGui.QPushButton(self.frame_2)
        self.incSpeedButton.setGeometry(QtCore.QRect(50, 22, 51, 51))
        self.incSpeedButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/500px-Aiga_uparrow_inv.svg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.incSpeedButton.setIcon(icon2)
        self.incSpeedButton.setIconSize(QtCore.QSize(50, 50))
        self.incSpeedButton.setAutoRepeat(True)
        self.incSpeedButton.setObjectName(_fromUtf8("incSpeedButton"))
        self.decSpeedButton = QtGui.QPushButton(self.frame_2)
        self.decSpeedButton.setGeometry(QtCore.QRect(50, 70, 51, 51))
        self.decSpeedButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/500px-Aiga_downarrow_inv.svg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.decSpeedButton.setIcon(icon3)
        self.decSpeedButton.setIconSize(QtCore.QSize(50, 50))
        self.decSpeedButton.setAutoRepeat(True)
        self.decSpeedButton.setObjectName(_fromUtf8("decSpeedButton"))
        self.turnRightButton = QtGui.QPushButton(self.frame_2)
        self.turnRightButton.setGeometry(QtCore.QRect(100, 50, 51, 51))
        self.turnRightButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("images/500px-Aiga_rightarrow_inv.svg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.turnRightButton.setIcon(icon4)
        self.turnRightButton.setIconSize(QtCore.QSize(50, 50))
        self.turnRightButton.setAutoRepeat(True)
        self.turnRightButton.setObjectName(_fromUtf8("turnRightButton"))
        self.turnLeftButton = QtGui.QPushButton(self.frame_2)
        self.turnLeftButton.setGeometry(QtCore.QRect(0, 50, 51, 51))
        self.turnLeftButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("images/500px-Aiga_leftarrow_inv.svg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.turnLeftButton.setIcon(icon5)
        self.turnLeftButton.setIconSize(QtCore.QSize(50, 50))
        self.turnLeftButton.setAutoRepeat(True)
        self.turnLeftButton.setObjectName(_fromUtf8("turnLeftButton"))
        self.frame_3 = QtGui.QFrame(self.tab_riding)
        self.frame_3.setGeometry(QtCore.QRect(230, 30, 271, 91))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.currentSpeed = QtGui.QLCDNumber(self.frame_3)
        self.currentSpeed.setGeometry(QtCore.QRect(3, 2, 141, 81))
        self.currentSpeed.setFrameShape(QtGui.QFrame.NoFrame)
        self.currentSpeed.setDigitCount(5)
        self.currentSpeed.setProperty("value", 0.0)
        self.currentSpeed.setObjectName(_fromUtf8("currentSpeed"))
        self.kmhLabel = QtGui.QLabel(self.frame_3)
        self.kmhLabel.setGeometry(QtCore.QRect(150, 10, 111, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(36)
        self.kmhLabel.setFont(font)
        self.kmhLabel.setObjectName(_fromUtf8("kmhLabel"))
        self.tilt = QtGui.QFrame(self.tab_riding)
        self.tilt.setGeometry(QtCore.QRect(230, 300, 171, 141))
        self.tilt.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tilt.setFrameShadow(QtGui.QFrame.Raised)
        self.tilt.setObjectName(_fromUtf8("tilt"))
        self.tiltImage = QtGui.QLabel(self.tilt)
        self.tiltImage.setGeometry(QtCore.QRect(0, 0, 171, 141))
        self.tiltImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tiltImage.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tiltImage.setText(_fromUtf8(""))
        self.tiltImage.setPixmap(QtGui.QPixmap(_fromUtf8("images/heckview.jpg")))
        self.tiltImage.setScaledContents(True)
        self.tiltImage.setObjectName(_fromUtf8("tiltImage"))
        self.steeringImage = QtGui.QLabel(self.tilt)
        self.steeringImage.setGeometry(QtCore.QRect(0, 0, 171, 141))
        self.steeringImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.steeringImage.setFrameShape(QtGui.QFrame.StyledPanel)
        self.steeringImage.setText(_fromUtf8(""))
        self.steeringImage.setPixmap(QtGui.QPixmap(_fromUtf8("images/topview.jpg")))
        self.steeringImage.setScaledContents(True)
        self.steeringImage.setObjectName(_fromUtf8("steeringImage"))
        self.obstaclesImage = QtGui.QLabel(self.tilt)
        self.obstaclesImage.setGeometry(QtCore.QRect(0, 0, 171, 141))
        self.obstaclesImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.obstaclesImage.setFrameShape(QtGui.QFrame.StyledPanel)
        self.obstaclesImage.setText(_fromUtf8(""))
        self.obstaclesImage.setPixmap(QtGui.QPixmap(_fromUtf8("images/backyard-obstacle-course-map.jpg")))
        self.obstaclesImage.setScaledContents(True)
        self.obstaclesImage.setObjectName(_fromUtf8("obstaclesImage"))
        self.msgList = QtGui.QListWidget(self.tab_riding)
        self.msgList.setGeometry(QtCore.QRect(230, 140, 271, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.msgList.setFont(font)
        self.msgList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msgList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.msgList.setProperty("showDropIndicator", False)
        self.msgList.setDragEnabled(False)
        self.msgList.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.msgList.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.msgList.setMovement(QtGui.QListView.Static)
        self.msgList.setViewMode(QtGui.QListView.ListMode)
        self.msgList.setModelColumn(0)
        self.msgList.setObjectName(_fromUtf8("msgList"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.tab_riding)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(410, 300, 93, 141))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(5, 6, -1, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tiltButton = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.tiltButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tiltButton.setChecked(True)
        self.tiltButton.setObjectName(_fromUtf8("tiltButton"))
        self.verticalLayout_3.addWidget(self.tiltButton)
        self.steeringButton = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.steeringButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.steeringButton.setChecked(False)
        self.steeringButton.setObjectName(_fromUtf8("steeringButton"))
        self.verticalLayout_3.addWidget(self.steeringButton)
        self.obstaclesButton = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.obstaclesButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.obstaclesButton.setChecked(False)
        self.obstaclesButton.setObjectName(_fromUtf8("obstaclesButton"))
        self.verticalLayout_3.addWidget(self.obstaclesButton)
        self.videoButton = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.videoButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.videoButton.setChecked(False)
        self.videoButton.setObjectName(_fromUtf8("videoButton"))
        self.verticalLayout_3.addWidget(self.videoButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_riding, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 539, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuConfig = QtGui.QMenu(self.menuBar)
        self.menuConfig.setObjectName(_fromUtf8("menuConfig"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionSet_IP = QtGui.QAction(MainWindow)
        self.actionSet_IP.setObjectName(_fromUtf8("actionSet_IP"))
        self.actionLock_settings = QtGui.QAction(MainWindow)
        self.actionLock_settings.setObjectName(_fromUtf8("actionLock_settings"))
        self.menuConfig.addAction(self.actionSet_IP)
        self.menuConfig.addAction(self.actionLock_settings)
        self.menuBar.addAction(self.menuConfig.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.tiltButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.tiltImage.setVisible)
        QtCore.QObject.connect(self.steeringButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.steeringImage.setVisible)
        QtCore.QObject.connect(self.obstaclesButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.obstaclesImage.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.emergencyStopButton)
        MainWindow.setTabOrder(self.emergencyStopButton, self.msgList)
        MainWindow.setTabOrder(self.msgList, self.incSpeedButton)
        MainWindow.setTabOrder(self.incSpeedButton, self.turnLeftButton)
        MainWindow.setTabOrder(self.turnLeftButton, self.turnRightButton)
        MainWindow.setTabOrder(self.turnRightButton, self.decSpeedButton)
        MainWindow.setTabOrder(self.decSpeedButton, self.tiltButton)
        MainWindow.setTabOrder(self.tiltButton, self.steeringButton)
        MainWindow.setTabOrder(self.steeringButton, self.obstaclesButton)
        MainWindow.setTabOrder(self.obstaclesButton, self.videoButton)
        MainWindow.setTabOrder(self.videoButton, self.speedCheckbox)
        MainWindow.setTabOrder(self.speedCheckbox, self.tiltCheckbox)
        MainWindow.setTabOrder(self.tiltCheckbox, self.checkBox_5)
        MainWindow.setTabOrder(self.checkBox_5, self.steeringCheckbox)
        MainWindow.setTabOrder(self.steeringCheckbox, self.obstaclesCheckbox)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Bike Client", None))
        self.tiltCheckbox.setText(_translate("MainWindow", "Tilt angle", None))
        self.steeringCheckbox.setText(_translate("MainWindow", "Steering angle", None))
        self.speedCheckbox.setText(_translate("MainWindow", "Speed profile", None))
        self.obstaclesCheckbox.setText(_translate("MainWindow", "Ostacles", None))
        self.checkBox_5.setText(_translate("MainWindow", "Ostacles", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_analyis), _translate("MainWindow", "Analysis", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_testing), _translate("MainWindow", "Testing", None))
        self.BatteryLabel.setText(_translate("MainWindow", "Battery", None))
        self.kmhLabel.setText(_translate("MainWindow", "Km/h", None))
        self.msgList.setSortingEnabled(False)
        self.tiltButton.setText(_translate("MainWindow", "tilt", None))
        self.steeringButton.setText(_translate("MainWindow", "steering", None))
        self.obstaclesButton.setText(_translate("MainWindow", "obstacles", None))
        self.videoButton.setText(_translate("MainWindow", "video", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_riding), _translate("MainWindow", "Riding", None))
        self.menuConfig.setTitle(_translate("MainWindow", "Config", None))
        self.actionSet_IP.setText(_translate("MainWindow", "Set IP", None))
        self.actionLock_settings.setText(_translate("MainWindow", "Lock settings", None))

