#!/bin/python

###############
# I think that I will place the motor stuff in a separate file and import.
# Although it would be easy to do things in here as well.
# I really wish that the thing wouldn't have crashed earlier
# 
##############

from multiprocessing import Process, Value, Lock
from PyQt4 import QtGui
import sys
import For_Reel_v1_ui
import os


class ExampleApp(QtGui.QMainWindow, For_Reel_v1_ui.Ui_MainWindow):
	def __init__(self, parent=None):
		#Initial self
		super(ExampleApp, self).__init__(parent)
		self.setupUi(self)
		
		###SET UP OF VARS AND DISPLAY
	
		#set the drive motor initial, disp, slider
		self.driveMotorSpeed=Value('i', 30)
		self.DriveMotorSpeedDisplay.display(self.driveMotorSpeed.value)
		self.DriveMotorSlider.setValue(30)
		#set the drive motor initial, disp, slider
		self.R2RMotorSpeed=Value('i',30)
		self.R2RMotorSpeedDisplay.display(self.R2RMotorSpeed.value)
		self.R2RMotorSpeeds.setValue(30)
		#set the multiplier initial, disp
		self.driveMotorSpeedMultiplier=Value('d', 0.25)
		self.MultiplierDisplay.display(self.driveMotorSpeedMultiplier.value)
    
		###Reactions to GUI things
    
		#change reel slider
		self.R2RMotorSpeeds.valueChanged.connect(self.changeR2RSpeedLCD)
		#change drive speed slider
		self.DriveMotorSlider.valueChanged.connect(self.changeDriveSpeedLCD)
		#click multiplier buttons
		self.MultiplierUp.clicked.connect(self.MultiplierUpfun)
		self.MultiplierDown.clicked.connect(self.MultiplierDownfun)
		#press and release forward
		self.ManForth.pressed.connect(self.driveMotorForward_GO)
		self.ManForth.released.connect(self.driveMotorForward_STOP)
		#press and release back
		#self.ManBack
		
		#Change reel to reel mode speed
		##### !!!!! This needs to be changed around because right now it
		##### supposes that the amount of tape on the reels is eternally equal.
	def changeR2RSpeedLCD(self, i):
		self.R2RMotorSpeed.value=self.R2RMotorSpeeds.value()
		self.R2RMotorSpeedDisplay.display(self.R2RMotorSpeed.value)
	#Change the motor speed
	def changeDriveSpeedLCD(self, i):
		self.driveMotorSpeed.value=self.DriveMotorSlider.value()
		self.DriveMotorSpeedDisplay.display(self.driveMotorSpeed.value)
		#Multiplier (step skip factor)
	def MultiplierUpfun(self, i):
		self.driveMotorSpeedMultiplier.value=self.driveMotorSpeedMultiplier.value*2
		self.MultiplierDisplay.display(self.driveMotorSpeedMultiplier.value)
	def MultiplierDownfun(self, i):
		self.driveMotorSpeedMultiplier.value=self.driveMotorSpeedMultiplier.value/2
		self.MultiplierDisplay.display(self.driveMotorSpeedMultiplier.value)
		#drive motor manual forward button
	def driveMotorForward_GO(self):
		print("motor forward at "+str(self.driveMotorSpeed.value)+"!!!!!!!")
	def driveMotorForward_STOP(self):
		print("motor forward STOPPPPPP!!!!")
		
	#drive motor manual backwards button
	def driveMotorForward_GO(self):
		print("motor back at "+str(self.driveMotorSpeed.value)+"!!!!!!!")
	def driveMotorForward_STOP(self):
		print("motor back STOPPPPPP!!!!")
		
		
		
def main():
	app = QtGui.QApplication(sys.argv)
	form = ExampleApp()

	form.show()
	app.exec_()

if __name__ == '__main__':
	main()

