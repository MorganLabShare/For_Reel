# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'For_Reel_v1.ui'
#
# Created: Mon Mar 20 19:38:34 2017
#      by: PyQt4 UI code generator 4.11.2
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
        MainWindow.resize(804, 417)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(8, 9, 790, 400))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(9, 9, 771, 351))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 368, 331))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.frame_4 = QtGui.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(10, 230, 351, 91))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.ManBack = QtGui.QPushButton(self.frame_4)
        self.ManBack.setGeometry(QtCore.QRect(6, 10, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ManBack.setFont(font)
        self.ManBack.setObjectName(_fromUtf8("ManBack"))
        self.ManForth = QtGui.QPushButton(self.frame_4)
        self.ManForth.setGeometry(QtCore.QRect(170, 10, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ManForth.setFont(font)
        self.ManForth.setObjectName(_fromUtf8("ManForth"))
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 341, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.frame_5 = QtGui.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(10, 60, 201, 171))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.DriveMotorSpeedDisplay = QtGui.QLCDNumber(self.frame_5)
        self.DriveMotorSpeedDisplay.setGeometry(QtCore.QRect(10, 41, 171, 61))
        self.DriveMotorSpeedDisplay.setObjectName(_fromUtf8("DriveMotorSpeedDisplay"))
        self.DriveMotorSlider = QtGui.QSlider(self.frame_5)
        self.DriveMotorSlider.setGeometry(QtCore.QRect(10, 110, 181, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.DriveMotorSlider.sizePolicy().hasHeightForWidth())
        self.DriveMotorSlider.setSizePolicy(sizePolicy)
        self.DriveMotorSlider.setMaximum(250)
        self.DriveMotorSlider.setSingleStep(5)
        self.DriveMotorSlider.setOrientation(QtCore.Qt.Horizontal)
        self.DriveMotorSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.DriveMotorSlider.setTickInterval(20)
        self.DriveMotorSlider.setObjectName(_fromUtf8("DriveMotorSlider"))
        self.label = QtGui.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame_6 = QtGui.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(210, 60, 151, 171))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.label_4 = QtGui.QLabel(self.frame_6)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 151, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.MultiplierDisplay = QtGui.QLCDNumber(self.frame_6)
        self.MultiplierDisplay.setGeometry(QtCore.QRect(10, 70, 131, 41))
        self.MultiplierDisplay.setObjectName(_fromUtf8("MultiplierDisplay"))
        self.MultiplierUp = QtGui.QPushButton(self.frame_6)
        self.MultiplierUp.setGeometry(QtCore.QRect(10, 30, 131, 31))
        self.MultiplierUp.setObjectName(_fromUtf8("MultiplierUp"))
        self.MultiplierDown = QtGui.QPushButton(self.frame_6)
        self.MultiplierDown.setGeometry(QtCore.QRect(10, 120, 131, 31))
        self.MultiplierDown.setObjectName(_fromUtf8("MultiplierDown"))
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(384, 10, 381, 331))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 351, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame_13 = QtGui.QFrame(self.frame_3)
        self.frame_13.setGeometry(QtCore.QRect(10, 50, 361, 271))
        self.frame_13.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_13.setObjectName(_fromUtf8("frame_13"))
        self.label_10 = QtGui.QLabel(self.frame_13)
        self.label_10.setGeometry(QtCore.QRect(0, 20, 191, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.TxtTimeDisplay = QtGui.QLCDNumber(self.frame_13)
        self.TxtTimeDisplay.setGeometry(QtCore.QRect(180, 10, 161, 51))
        self.TxtTimeDisplay.setObjectName(_fromUtf8("TxtTimeDisplay"))
        self.frame_14 = QtGui.QFrame(self.frame_13)
        self.frame_14.setGeometry(QtCore.QRect(10, 70, 151, 101))
        self.frame_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_14.setObjectName(_fromUtf8("frame_14"))
        self.TxtTimeDialSeconds = QtGui.QRadioButton(self.frame_14)
        self.TxtTimeDialSeconds.setGeometry(QtCore.QRect(10, 40, 118, 26))
        self.TxtTimeDialSeconds.setObjectName(_fromUtf8("TxtTimeDialSeconds"))
        self.TxtTimeDialMinutes = QtGui.QRadioButton(self.frame_14)
        self.TxtTimeDialMinutes.setGeometry(QtCore.QRect(10, 70, 118, 26))
        self.TxtTimeDialMinutes.setObjectName(_fromUtf8("TxtTimeDialMinutes"))
        self.label_11 = QtGui.QLabel(self.frame_14)
        self.label_11.setGeometry(QtCore.QRect(16, 10, 121, 31))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.TimerUpButton = QtGui.QPushButton(self.frame_13)
        self.TimerUpButton.setGeometry(QtCore.QRect(180, 70, 171, 71))
        self.TimerUpButton.setObjectName(_fromUtf8("TimerUpButton"))
        self.TimerDownButton = QtGui.QPushButton(self.frame_13)
        self.TimerDownButton.setGeometry(QtCore.QRect(180, 170, 171, 71))
        self.TimerDownButton.setObjectName(_fromUtf8("TimerDownButton"))
        self.TxtGoButton = QtGui.QPushButton(self.frame_13)
        self.TxtGoButton.setGeometry(QtCore.QRect(10, 180, 151, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.TxtGoButton.setFont(font)
        self.TxtGoButton.setObjectName(_fromUtf8("TxtGoButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame_7 = QtGui.QFrame(self.tab_2)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.label_5 = QtGui.QLabel(self.frame_7)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 531, 61))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.frame_8 = QtGui.QFrame(self.frame_7)
        self.frame_8.setGeometry(QtCore.QRect(10, 80, 551, 251))
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.frame_9 = QtGui.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_6 = QtGui.QLabel(self.frame_9)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.LeftMotorCW = QtGui.QRadioButton(self.frame_9)
        self.LeftMotorCW.setObjectName(_fromUtf8("LeftMotorCW"))
        self.verticalLayout_3.addWidget(self.LeftMotorCW)
        self.LeftMotorCCW = QtGui.QRadioButton(self.frame_9)
        self.LeftMotorCCW.setObjectName(_fromUtf8("LeftMotorCCW"))
        self.verticalLayout_3.addWidget(self.LeftMotorCCW)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.frame_11 = QtGui.QFrame(self.frame_8)
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName(_fromUtf8("frame_11"))
        self.R2RMotorSpeeds = QtGui.QSlider(self.frame_11)
        self.R2RMotorSpeeds.setGeometry(QtCore.QRect(10, 110, 141, 41))
        self.R2RMotorSpeeds.setMaximum(250)
        self.R2RMotorSpeeds.setSingleStep(5)
        self.R2RMotorSpeeds.setOrientation(QtCore.Qt.Horizontal)
        self.R2RMotorSpeeds.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.R2RMotorSpeeds.setTickInterval(20)
        self.R2RMotorSpeeds.setObjectName(_fromUtf8("R2RMotorSpeeds"))
        self.R2RMotorSpeedDisplay = QtGui.QLCDNumber(self.frame_11)
        self.R2RMotorSpeedDisplay.setGeometry(QtCore.QRect(20, 40, 131, 61))
        self.R2RMotorSpeedDisplay.setObjectName(_fromUtf8("R2RMotorSpeedDisplay"))
        self.label_7 = QtGui.QLabel(self.frame_11)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 141, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.frame_11)
        self.frame_10 = QtGui.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName(_fromUtf8("frame_10"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_8 = QtGui.QLabel(self.frame_10)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.RightMotorCW = QtGui.QRadioButton(self.frame_10)
        self.RightMotorCW.setObjectName(_fromUtf8("RightMotorCW"))
        self.verticalLayout.addWidget(self.RightMotorCW)
        self.RightMotorCCW = QtGui.QRadioButton(self.frame_10)
        self.RightMotorCCW.setObjectName(_fromUtf8("RightMotorCCW"))
        self.verticalLayout.addWidget(self.RightMotorCCW)
        self.horizontalLayout_2.addWidget(self.frame_10)
        self.R2RGO = QtGui.QPushButton(self.frame_7)
        self.R2RGO.setGeometry(QtCore.QRect(570, 20, 181, 91))
        self.R2RGO.setObjectName(_fromUtf8("R2RGO"))
        self.R2RSTOP = QtGui.QPushButton(self.frame_7)
        self.R2RSTOP.setGeometry(QtCore.QRect(570, 120, 181, 91))
        self.R2RSTOP.setObjectName(_fromUtf8("R2RSTOP"))
        self.frame_12 = QtGui.QFrame(self.frame_7)
        self.frame_12.setGeometry(QtCore.QRect(570, 220, 181, 111))
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName(_fromUtf8("frame_12"))
        self.R2RTimerSlider = QtGui.QSlider(self.frame_12)
        self.R2RTimerSlider.setGeometry(QtCore.QRect(10, 80, 160, 26))
        self.R2RTimerSlider.setMaximum(120)
        self.R2RTimerSlider.setSingleStep(5)
        self.R2RTimerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.R2RTimerSlider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.R2RTimerSlider.setTickInterval(10)
        self.R2RTimerSlider.setObjectName(_fromUtf8("R2RTimerSlider"))
        self.label_9 = QtGui.QLabel(self.frame_12)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.R2RTimerDisplay = QtGui.QLCDNumber(self.frame_12)
        self.R2RTimerDisplay.setGeometry(QtCore.QRect(10, 40, 71, 31))
        self.R2RTimerDisplay.setObjectName(_fromUtf8("R2RTimerDisplay"))
        self.R2RTimerButton = QtGui.QPushButton(self.frame_12)
        self.R2RTimerButton.setGeometry(QtCore.QRect(90, 10, 81, 71))
        self.R2RTimerButton.setObjectName(_fromUtf8("R2RTimerButton"))
        self.gridLayout.addWidget(self.frame_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ManBack.setText(_translate("MainWindow", "Manual Back", None))
        self.ManForth.setText(_translate("MainWindow", "Manual Forth", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Parameters</span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Drive Motor Speed</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Speed Multiplier</span></p></body></html>", None))
        self.MultiplierUp.setText(_translate("MainWindow", "Up", None))
        self.MultiplierDown.setText(_translate("MainWindow", "Down", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Tape Treatment</span></p></body></html>", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Time Limit (seconds)</span></p></body></html>", None))
        self.TxtTimeDialSeconds.setText(_translate("MainWindow", "Seconds", None))
        self.TxtTimeDialMinutes.setText(_translate("MainWindow", "Minutes", None))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Dial Control</span></p></body></html>", None))
        self.TimerUpButton.setText(_translate("MainWindow", "UP", None))
        self.TimerDownButton.setText(_translate("MainWindow", "DOWN", None))
        self.TxtGoButton.setText(_translate("MainWindow", "TAPE TREAT GO!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "TAPE TREATMENT", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">MAKE SURE BOTH SWITCHES ON THE BLACK BOX</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">ARE IN THE LEFT POSITION!!!!</span></p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Left Motor Direction</span></p></body></html>", None))
        self.LeftMotorCW.setText(_translate("MainWindow", "Clockwise", None))
        self.LeftMotorCCW.setText(_translate("MainWindow", "CounterClockwise", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Motor Speed</span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Right Motor Direction</span></p></body></html>", None))
        self.RightMotorCW.setText(_translate("MainWindow", "Clockwise", None))
        self.RightMotorCCW.setText(_translate("MainWindow", "CounterClockwise", None))
        self.R2RGO.setText(_translate("MainWindow", "GO", None))
        self.R2RSTOP.setText(_translate("MainWindow", "STOP", None))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Timer</p></body></html>", None))
        self.R2RTimerButton.setText(_translate("MainWindow", "GO TIMER", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "REEL TO REEL MODE", None))

