#!/bin/python
from multiprocessing import Process, Value, Lock
from PyQt4 import QtGui
import sys
import For_Reel_v1_ui
import os


class ExampleApp(QtGui.QMainWindow, For_Reel_v1_ui.Ui_MainWindow):
  def __init__(self, parent=None):
    super(ExampleApp, self).__init__(parent)
    self.setupUi(self)
    #~ Let's get the global stuff that we will need set up.
    self.driveMotorSpeed=Value('i', 30)
    self.DriveMotorSpeedDisplay.display(self.driveMotorSpeed.value)
    self.driveMotorSpeedMultiplier=Value('d', 0.25)
    self.MultiplierDisplay.display(self.driveMotorSpeedMultiplier.value)
    
    self.DriveMotorSlider.valueChanged.connect(self.changeDriveSpeedLCD)
    self.MultiplierUp.clicked.connect(self.MultiplierUpfun)
    self.MultiplierDown.clicked.connect(self.MultiplierDownfun)
    
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


def main():
  app = QtGui.QApplication(sys.argv)
  form = ExampleApp()

  form.show()
  app.exec_()

if __name__ == '__main__':
	main()

