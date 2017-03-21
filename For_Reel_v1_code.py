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
from time import sleep

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
        #set the R2R timer slider,disp,init
        self.R2RTime=Value('i',60)
        self.R2RTimerDisplay.display(self.R2RTime.value)
        self.R2RTimerSlider.setValue(60)
        #set the multiplier initial, disp
        self.driveMotorSpeedMultiplier=Value('d', 0.25)
        self.MultiplierDisplay.display(self.driveMotorSpeedMultiplier.value)
        #set the treatment timer disp,dial
        self.TxtTime=Value('i', 0)
        self.TxtTimeDisplay.display("00:00")
        self.TxtTimeDialMinutes.setChecked(True)
        self.proclist=[]

        ###Reactions to GUI things

        #change reel slider
        self.R2RMotorSpeeds.valueChanged.connect(self.changeR2RSpeedLCD)
        #change drive speed slider
        self.DriveMotorSlider.valueChanged.connect(self.changeDriveSpeedLCD)
        #change R2R timer slider
        self.R2RTimerSlider.valueChanged.connect(self.changeR2RTimer)
        #click multiplier buttons
        self.MultiplierUp.clicked.connect(self.MultiplierUpfun)
        self.MultiplierDown.clicked.connect(self.MultiplierDownfun)
        #press and release forward
        self.ManForth.pressed.connect(self.driveMotorForward_GO)
        self.ManForth.released.connect(self.driveMotorForward_STOP)
        #press and release back
        self.ManBack.pressed.connect(self.driveMotorBack_GO)
        self.ManBack.released.connect(self.driveMotorBack_STOP)
        #change the tapetreatment timer dial
        self.TimerUpButton.clicked.connect(self.timeUp)
        self.TimerDownButton.clicked.connect(self.timeDown)
        #start the treatment
        self.TxtGoButton.clicked.connect(self.txtGo)
        #emergency stop
        self.TxtStopButton.clicked.connect(self.txtStop)
    #Change reel to reel mode speed
    ##### !!!!! This needs to be changed around because right now it
    ##### supposes that the amount of tape on the reels is eternally equal.
    #Change R2R speed
    def changeR2RSpeedLCD(self, i):
        self.R2RMotorSpeed.value=self.R2RMotorSpeeds.value()
        self.R2RMotorSpeedDisplay.display(self.R2RMotorSpeed.value)

    #Change the drive motor speed
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

    #R2R timer slider
    def changeR2RTimer(self, i):
        self.R2RTime.value=self.R2RTimerSlider.value()
        self.R2RTimerDisplay.display(self.R2RTime.value)

    #drive motor manual buttons first tab
    def driveMotorForward_GO(self):
        print("motor forward at "+str(self.driveMotorSpeed.value)+"!!!!!!!")
    def driveMotorForward_STOP(self):
        print("motor forward STOPPPPPP!!!!")
    def driveMotorBack_GO(self):
        print("motor backward at "+str(self.driveMotorSpeed.value)+"!!!!!!!")
    def driveMotorBack_STOP(self):
        print("motor backward STOPPPPPP!!!!")
    def driveMotorForward_GO(self):
        print("motor back at "+str(self.driveMotorSpeed.value)+"!!!!!!!")
    def driveMotorForward_STOP(self):
        print("motor back STOPPPPPP!!!!")

#treatment timer dial movement
    def timeUp(self):
        if self.TxtTimeDialSeconds.isChecked():
            self.TxtTime.value=self.TxtTime.value+1
        elif self.TxtTimeDialMinutes.isChecked():
            self.TxtTime.value=self.TxtTime.value+60
        dispmin,dispsec=divmod(self.TxtTime.value,60)
        self.TxtTimeDisplay.display(str(dispmin)+":"+str(dispsec))
    def timeDown(self):
        if self.TxtTimeDialSeconds.isChecked():
            self.TxtTime.value=self.TxtTime.value-1
        elif self.TxtTimeDialMinutes.isChecked():
            self.TxtTime.value=self.TxtTime.value-60
        dispmin,dispsec=divmod(self.TxtTime.value,60)
        self.TxtTimeDisplay.display(str(dispmin)+":"+str(dispsec))

    #Do the actual treatment
    def txtGo(self):
        print("starting treatment")
        #self.proclist.append("test")
        print("motor speed: "+str(self.driveMotorSpeed.value))
        print("time (sec): "+str(self.TxtTime.value))
        print("starting motor")
        txtProcActual=Process(target=txtProc, \
            args=(self.driveMotorSpeed.value,self.driveMotorSpeedMultiplier.value))
        txtProcActual.start()

        #### Need to abstract by one step. Set up a function for starting a
        # timer process which will start the motor process.
        # The timer process launch the countdown and the motor process.
        # If the timer runs out, the process will die.
        # Also, need to make a kill button to stop the process.
        #   - That will stop motors and kill process.

        sleep(self.TxtTime.value+1)
        if txtProcActual.is_alive():
            txtProcActual.terminate()
            print("killing all motors")
            self.TxtTime.value=0
            dispmin,dispsec=divmod(self.TxtTime.value,60)
            self.TxtTimeDisplay.display(str(dispmin)+":"+str(dispsec))

    #stop all motors
    def txtStop(self):
        print("STOP ALL MOTORS")
        for proc in self.proclist:
            print("killing "+str(proc))
            proc.terminate()
            proc.join()

#the processing thread for treatment
def txtProc(speed,mult):
    print("speed: "+str(speed))
    print("mult: "+str(mult))
    #ime=TxtTime.value
    while TxtTime.value >= 0:
        sleep(1)
        self.TxtTime.value=self.TxtTime.value-1
        dispmin,dispsec=divmod(self.TxtTime.value,60)
        self.TxtTimeDisplay.display(str(dispmin)+":"+str(dispsec))

#BoilerPlate
def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    testval=Value('i',10)
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
