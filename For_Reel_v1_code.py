#!/bin/python

###############
#
# I really wish that the thing wouldn't have crashed earlier
#
##############

from multiprocessing import Process, Value, Lock
from PyQt4 import QtGui
from PyQt4.QtCore import QThread, SIGNAL
import sys
import For_Reel_v1_ui
import os
import time
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import RPi.GPIO as GPIO

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
        #this may not get used
        self.proclist=[]
        #this lets things know when to die
        self.motorFullStop=Value('i', 0)
        self.stopEverything=Value('i',0)

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
        self.TxtGoButton.clicked.connect(self.testGo)
        #emergency stop
        self.TxtStopButton.clicked.connect(self.testStop)
        ### R2R section
        self.LeftMotorCW.setChecked(True)
        self.RightMotorCW.setChecked(True)
        #R2R stop and go buttons
        self.R2RGO.clicked.connect(self.r2rGo)
        self.R2RSTOP.clicked.connect(self.r2rStop)
        #R2R timer go
        self.R2RTimerButton.clicked.connect(self.r2rTimerGo)

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
        self.stopEverything.value=0
        moGo(self,self.driveMotorSpeed.value,2,2)
    def driveMotorForward_STOP(self):
        self.stopEverything.value=1
        moStop()
    def driveMotorBack_GO(self):
        self.stopEverything.value=0
        moGo(self,self.driveMotorSpeed.value,1,1)
    def driveMotorBack_STOP(self):
        self.stopEverything.value=1
        moStop()

    #treatment timer dial movement
    def timeUp(self):
        if self.TxtTimeDialSeconds.isChecked():
            self.TxtTime.value=self.TxtTime.value+1
        elif self.TxtTimeDialMinutes.isChecked():
            self.TxtTime.value=self.TxtTime.value+60
        self.txtDisplayUpdate(self.TxtTime.value,self.TxtTimeDisplay)
    def timeDown(self):
        if self.TxtTimeDialSeconds.isChecked():
            self.TxtTime.value=self.TxtTime.value-1
        elif self.TxtTimeDialMinutes.isChecked():
            self.TxtTime.value=self.TxtTime.value-60
        self.txtDisplayUpdate(self.TxtTime.value,self.TxtTimeDisplay)

    #update either display
    def txtDisplayUpdate(self,timer,disp):
        dispmin,dispsec=divmod(timer,60)
        disp.display(str(dispmin)+":"+str(dispsec))

    #update the LCD without breaking
    def countDownDisplay(self,timer,disp):
        for i in range(timer):
            if self.stopEverything.value==1:
                break
            timerd=timer-i
            self.txtDisplayUpdate(timerd,disp)
            start = time.time()
            while time.time() - start < 1:
                QtGui.qApp.processEvents()
                time.sleep(0.02)

    #I think that this might be necessary for the two motors.
    def moGoMult(self,speed,mult,dir1,dir2):
        while True:
            if self.stopEverything.value==1:
                break


    def testGo(self):
        # Set the auto stop value to zero
        self.stopEverything.value=0
        # Call the moGo command to start the motor at the current speed
        moGo(self,self.driveMotorSpeed.value,2,2)
        #Update the countdown clock with the correct value.        
        self.countDownDisplay(self.TxtTime.value,self.TxtTimeDisplay)

    def testStop(self):
        self.stopEverything.value=1
        moStop()
        self.txtDisplayUpdate(self.TxtTime.value,self.TxtTimeDisplay)

    #fill in these later with the direction parsing
    def r2rGo(self):
        self.stopEverything.value=0
        if self.LeftMotorCW(isChecked):
            print("CW")

        moGo(self,self.R2RMotorSpeed.value)
    def r2rStop(self):
        self.stopEverything.value=1
        moStop()
    def r2rTimerGo(self):
        self.stopEverything.value=0
        moGo(self,self.R2RMotorSpeed.value)
        self.countDownDisplay(self.R2RTime.value,self.R2RTimerDisplay)

# Think about whether or not we need to specify motor mode in the moGo call

def moGo(self,speed,dir1,dir2):
    #Here is where to change the motor directions.
    if dir1 == "1":
    	driveMotor.run(Adafruit_MotorHAT.FORWARD)
    elif dir1 == "2":
    	driveMotor.run(Adafruit_MotorHAT.BACKWARD)
    print("starting motor diag")
    driveMotor.setSpeed(speed)
    #~ moGoMultOutsideProc=Process(target=moGoMultOutside,args=(self,speed,dir1,dir2))
    moGoMultOutside(self,speed,dir1,dir2)
    #slaveMotor.setSpeed(speed)
    #slaveProcFun(self,speed,dir2)
    #slaveDriver(self,dir2)

def moGoMultOutside(self,speed,dir1,dir2):
	print("speed "+str(speed)+" dir "+str(dir1))
	mult=self.driveMotorSpeedMultiplier.value
	#Here is where the things are defined.
	driveDelay=mult*64/1600
	waitDelay=(1-mult)*64/1600
	#~ print("Motor started at "+str(speed)+"; stopper is at "+str(self.stopEverything.value))
	#print(driveDelay,waitDelay)
	if dir1 == 1:
		#print("motorback")
		driveMotor.run(Adafruit_MotorHAT.FORWARD)
	elif dir1 == 2:
		#print("motorforward")
		driveMotor.run(Adafruit_MotorHAT.BACKWARD)
	while True:
		if self.stopEverything.value==1:
			#print("multgostopbreak")
			break
		driveMotor.setSpeed(speed)
		#~ print("GO")
		start = time.time()
		#~ print(driveDelay, waitDelay)
		while time.time() - start < driveDelay :
			#~ print("motorGO")
			QtGui.qApp.processEvents()
			time.sleep(0.02)
		driveMotor.setSpeed(0)
		#~ print("STOP")
		while time.time() - start < waitDelay :
			#~ print("motorSTOP")
			QtGui.qApp.processEvents()
			time.sleep(0.02)

def droMoStop():
    print("Drive Motor Stop")
    #driveMotor.setSpeed(0)
    #driveMotor.run(Adafruit_MotorHAT.RELEASE)

def moStop():
    print("motors stop")
    #~ self.stopEverything.value=1
    turnOffMotors()

def moGoR2R(self,speed,dir1,dir2):
    print("still working on this")
    return 0


def slaveDriver(self,dir2):
    print("slave motor start subprocess")
    slaveProc=Process(target=slaveProcFun, args=(self,dir2))
    slaveProc.start()
    #while 1

def slaveProcFun(self,speed,dir2):
	print("this is the slave process")
	slaveMotor.setSpeed(speed)
	mult=self.driveMotorSpeedMultiplier.value
	driveDelay=mult*64/1600
	waitDelay=(1-mult)*64/1600
	if dir2 == 1:
		slaveMotor.run(Adafruit_MotorHAT.FORWARD)
	elif dir2 == 2:
		slaveMotor.run(Adafruit_MotorHAT.BACKWARD)
	while True:
		print("this is the actual slave loop")
		print("pin 19 = "+str(GPIO.input(19)))
		print("pin 16 = "+str(GPIO.input(16)))
		print("pin 13 = "+str(GPIO.input(13)))
		if self.stopEverything.value==1:
			break
		slaveMotor.setSpeed(speed)
		start = time.time()
		while time.time() - start < driveDelay :
			QtGui.qApp.processEvents()
			time.sleep(0.02)
		slaveMotor.setSpeed(0)
		while time.time() - start < waitDelay :
			QtGui.qApp.processEvents()
			time.sleep(0.02)
		

#Low level switch setupUi
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# Low level motor setup
mh = Adafruit_MotorHAT(addr=0x60)
driveMotor=mh.getMotor(4)
slaveMotor=mh.getMotor(3)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)


#BoilerPlateQtGui.qApp.processEvents()QtGui.qApp.processEvents()
def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    #print(form.motorFullStop.value) #note, this works.
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
