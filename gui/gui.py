# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon Jun 26 18:11:37 2017
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
        MainWindow.resize(936, 531)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
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
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 921, 491))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
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
        self.frame.setGeometry(QtCore.QRect(290, 20, 111, 91))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.BatteryLabel = QtGui.QLabel(self.frame)
        self.BatteryLabel.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BatteryLabel.setFont(font)
        self.BatteryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BatteryLabel.setObjectName(_fromUtf8("BatteryLabel"))
        self.batteryState = QtGui.QProgressBar(self.frame)
        self.batteryState.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.batteryState.setToolTip(_fromUtf8(""))
        self.batteryState.setProperty("value", 75)
        self.batteryState.setAlignment(QtCore.Qt.AlignCenter)
        self.batteryState.setInvertedAppearance(False)
        self.batteryState.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.batteryState.setObjectName(_fromUtf8("batteryState"))
        self.batteryImage = QtGui.QLabel(self.frame)
        self.batteryImage.setGeometry(QtCore.QRect(20, 40, 16, 31))
        self.batteryImage.setText(_fromUtf8(""))
        self.batteryImage.setPixmap(QtGui.QPixmap(_fromUtf8("images/348px-Angular_lightningbolt.svg.png")))
        self.batteryImage.setScaledContents(True)
        self.batteryImage.setObjectName(_fromUtf8("batteryImage"))
        self.emergencyStopButton = QtGui.QPushButton(self.tab_riding)
        self.emergencyStopButton.setGeometry(QtCore.QRect(250, 300, 151, 151))
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
        self.frame_3 = QtGui.QFrame(self.tab_riding)
        self.frame_3.setGeometry(QtCore.QRect(0, 20, 271, 91))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
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
        self.msgList = QtGui.QListWidget(self.tab_riding)
        self.msgList.setGeometry(QtCore.QRect(10, 120, 391, 151))
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
        self.frame_2 = QtGui.QFrame(self.tab_riding)
        self.frame_2.setGeometry(QtCore.QRect(420, 20, 471, 441))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.tiltImage = QtGui.QLabel(self.frame_2)
        self.tiltImage.setGeometry(QtCore.QRect(0, 0, 421, 341))
        self.tiltImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tiltImage.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tiltImage.setText(_fromUtf8(""))
        self.tiltImage.setPixmap(QtGui.QPixmap(_fromUtf8("images/heckview.jpg")))
        self.tiltImage.setScaledContents(True)
        self.tiltImage.setObjectName(_fromUtf8("tiltImage"))
        self.steeringImage = QtGui.QLabel(self.frame_2)
        self.steeringImage.setGeometry(QtCore.QRect(0, 0, 421, 381))
        self.steeringImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.steeringImage.setFrameShape(QtGui.QFrame.StyledPanel)
        self.steeringImage.setText(_fromUtf8(""))
        self.steeringImage.setPixmap(QtGui.QPixmap(_fromUtf8("images/topview.jpg")))
        self.steeringImage.setScaledContents(True)
        self.steeringImage.setObjectName(_fromUtf8("steeringImage"))
        self.obstaclesImage = QtGui.QLabel(self.frame_2)
        self.obstaclesImage.setGeometry(QtCore.QRect(0, 0, 421, 381))
        self.obstaclesImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.obstaclesImage.setFrameShape(QtGui.QFrame.StyledPanel)
        self.obstaclesImage.setText(_fromUtf8(""))
        self.obstaclesImage.setPixmap(QtGui.QPixmap(_fromUtf8("images/backyard-obstacle-course-map.jpg")))
        self.obstaclesImage.setScaledContents(True)
        self.obstaclesImage.setObjectName(_fromUtf8("obstaclesImage"))
        self.Compass = Qwt5.QwtCompass(self.frame_2)
        self.Compass.setGeometry(QtCore.QRect(-1, -1, 421, 381))
        self.Compass.setProperty("visibleBackground", True)
        self.Compass.setLineWidth(4)
        self.Compass.setObjectName(_fromUtf8("Compass"))
        self.ControllFrame = QtGui.QFrame(self.tab_riding)
        self.ControllFrame.setGeometry(QtCore.QRect(-10, 300, 251, 161))
        self.ControllFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ControllFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.ControllFrame.setObjectName(_fromUtf8("ControllFrame"))
        self.tiltSlider = QtGui.QSlider(self.ControllFrame)
        self.tiltSlider.setGeometry(QtCore.QRect(50, 130, 191, 22))
        self.tiltSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tiltSlider.setMinimum(-90)
        self.tiltSlider.setMaximum(90)
        self.tiltSlider.setOrientation(QtCore.Qt.Horizontal)
        self.tiltSlider.setObjectName(_fromUtf8("tiltSlider"))
        self.speedSlider = QtGui.QSlider(self.ControllFrame)
        self.speedSlider.setGeometry(QtCore.QRect(20, 10, 22, 141))
        self.speedSlider.setMaximum(40)
        self.speedSlider.setSingleStep(1)
        self.speedSlider.setOrientation(QtCore.Qt.Vertical)
        self.speedSlider.setObjectName(_fromUtf8("speedSlider"))
        self.targetSpeedFrame = QtGui.QFrame(self.ControllFrame)
        self.targetSpeedFrame.setGeometry(QtCore.QRect(50, 10, 81, 71))
        self.targetSpeedFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.targetSpeedFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.targetSpeedFrame.setObjectName(_fromUtf8("targetSpeedFrame"))
        self.targetSpeed = QtGui.QLCDNumber(self.targetSpeedFrame)
        self.targetSpeed.setGeometry(QtCore.QRect(0, 20, 71, 31))
        self.targetSpeed.setObjectName(_fromUtf8("targetSpeed"))
        self.targetSpeedLabel = QtGui.QLabel(self.targetSpeedFrame)
        self.targetSpeedLabel.setGeometry(QtCore.QRect(5, 3, 71, 16))
        self.targetSpeedLabel.setObjectName(_fromUtf8("targetSpeedLabel"))
        self.targetSpeedChanged = QtGui.QLCDNumber(self.targetSpeedFrame)
        self.targetSpeedChanged.setGeometry(QtCore.QRect(0, 20, 71, 31))
        self.targetSpeedChanged.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 0, 0); \n"
"}"))
        self.targetSpeedChanged.setObjectName(_fromUtf8("targetSpeedChanged"))
        self.targetAngleFrame = QtGui.QFrame(self.ControllFrame)
        self.targetAngleFrame.setGeometry(QtCore.QRect(150, 10, 81, 71))
        self.targetAngleFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.targetAngleFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.targetAngleFrame.setObjectName(_fromUtf8("targetAngleFrame"))
        self.targtAngle = QtGui.QLCDNumber(self.targetAngleFrame)
        self.targtAngle.setGeometry(QtCore.QRect(0, 20, 71, 31))
        self.targtAngle.setObjectName(_fromUtf8("targtAngle"))
        self.targetAngleLabel = QtGui.QLabel(self.targetAngleFrame)
        self.targetAngleLabel.setGeometry(QtCore.QRect(5, 0, 61, 20))
        self.targetAngleLabel.setObjectName(_fromUtf8("targetAngleLabel"))
        self.targtAngleChanged = QtGui.QLCDNumber(self.targetAngleFrame)
        self.targtAngleChanged.setGeometry(QtCore.QRect(0, 20, 71, 31))
        self.targtAngleChanged.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(255, 0, 0); \n"
"}"))
        self.targtAngleChanged.setObjectName(_fromUtf8("targtAngleChanged"))
        self.submitSpeedAndTilt = QtGui.QPushButton(self.ControllFrame)
        self.submitSpeedAndTilt.setGeometry(QtCore.QRect(50, 90, 171, 31))
        self.submitSpeedAndTilt.setObjectName(_fromUtf8("submitSpeedAndTilt"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.tab_riding)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(840, 20, 71, 381))
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
        self.videoButton_2 = QtGui.QRadioButton(self.verticalLayoutWidget_3)
        self.videoButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.videoButton_2.setChecked(False)
        self.videoButton_2.setObjectName(_fromUtf8("videoButton_2"))
        self.verticalLayout_3.addWidget(self.videoButton_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab_riding, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 936, 21))
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
        QtCore.QObject.connect(self.speedSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.targetSpeed.display)
        QtCore.QObject.connect(self.speedSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.targetSpeedChanged.display)
        QtCore.QObject.connect(self.speedSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.targetSpeed.hide)
        QtCore.QObject.connect(self.submitSpeedAndTilt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.targetSpeed.show)
        QtCore.QObject.connect(self.submitSpeedAndTilt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.targetSpeedChanged.hide)
        QtCore.QObject.connect(self.speedSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.targetSpeedChanged.show)
        QtCore.QObject.connect(self.tiltSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.targtAngle.hide)
        QtCore.QObject.connect(self.tiltSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.targtAngleChanged.display)
        QtCore.QObject.connect(self.tiltSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.targtAngle.display)
        QtCore.QObject.connect(self.tiltSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.targtAngleChanged.show)
        QtCore.QObject.connect(self.submitSpeedAndTilt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.targtAngle.show)
        QtCore.QObject.connect(self.submitSpeedAndTilt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.targtAngleChanged.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.emergencyStopButton)
        MainWindow.setTabOrder(self.emergencyStopButton, self.msgList)
        MainWindow.setTabOrder(self.msgList, self.tiltButton)
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
        self.targetSpeedLabel.setText(_translate("MainWindow", "target speed", None))
        self.targetAngleLabel.setText(_translate("MainWindow", "target angle", None))
        self.submitSpeedAndTilt.setText(_translate("MainWindow", "submit", None))
        self.tiltButton.setText(_translate("MainWindow", "tilt", None))
        self.steeringButton.setText(_translate("MainWindow", "steering", None))
        self.obstaclesButton.setText(_translate("MainWindow", "obstacles", None))
        self.videoButton.setText(_translate("MainWindow", "video", None))
        self.videoButton_2.setText(_translate("MainWindow", "compass", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_riding), _translate("MainWindow", "Riding", None))
        self.menuConfig.setTitle(_translate("MainWindow", "Config", None))
        self.actionSet_IP.setText(_translate("MainWindow", "Set IP", None))
        self.actionLock_settings.setText(_translate("MainWindow", "Lock settings", None))

from PyQt4 import Qwt5

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

