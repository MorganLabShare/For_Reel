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
    self.DriveMotorSlider.valueChanged.connect(self.changeDriveSpeedLCD)
    self.MultiplierUp.clicked.connect(self.MultiplierUp)
    self.MultiplierDown.clicked.connect(self.MultiplierDown)

  #~ This will detect a change in the drive motor speed slider and change the 
  #~ proper things for that.
  def changeDriveSpeedLCD(self, i):
    #~ driveMotorSpeed.value=self.DriveMotorSlider.value()
    self.DriveMotorSpeedDisplay.display(self.DriveMotorSlider.value())
  
  def MultiplierUp(self, i):
    self.MutiplierDisplay.display(CurrentMultiplier.value)
    
    
    
    
  def MultiplierDown(self, i):
    
  

def main():
  app = QtGui.QApplication(sys.argv)
  form = ExampleApp()
  #~ Let's get the global stuff that we will need set up.
  driveMotorSpeed=Value('i', 0)
  driveMotorSpeedMultiplier('i', 0.25)
  form.show()
  app.exec_()

if __name__ == '__main__':
	main()

