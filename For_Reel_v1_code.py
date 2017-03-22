#!/bin/python

###############
# I think that I will place the motor stuff in a separate file and import.
# Although it would be easy to do things in here as well.
# I really wish that the thing wouldn't have crashed earlier
#
##############

from multiprocessing import Process, Value, Lock
from PyQt4 import QtGui
from PyQt4.QtCore import QThread, SIGNAL
import sys
import For_Reel_v1_ui
import os
from time import sleep

class timeController(QThread):
    def __init__(self):
        QThread.__init__(self)
    def go(self,time):
        countdownthread=countDownTimer(time)
        countdownthread.start()
        countdownthread.go()
    def die(self):
        countdownthread.die()

class countDownTimer(QThread):

    def __init__(self,time):
        QThread.__init__(self)
        self.time=time
        #self.signal=SIGNAL("timeLeft(int)")
    #def __del__(self):
    #    self.wait()
    def go(self):
        print("qthread running")
        print(self.time)
        while self.time > 0:
            dispmin,dispsec=divmod(self.time,60)
            #print(str(dispmin)+","+str(dispsec))
            #self.dispname.display(str(dispmin)+":"+str(dispsec))
            self.time = self.time-1
            sleep(1)
            print(self.time)
            #self.emit(SIGNAL("timeLeft(int)"), self.time)
        print("qthread finished")
    def die(self):
        self.quit()
        self.wait()
        self.terminate()

class ExampleApp(QtGui.QMainWindow, For_Reel_v1_ui.Ui_MainWindow):
    def __init__(self, parent=None):
      #Initial self
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        #test of the controller
        self.controller=timeController()
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
        #R2R stop and go buttons
        self.R2RGO.clicked.connect(self.r2rGo)
        self.R2RSTOP.clicked.connect(self.r2rStop)
        #R2R timer go
        self.R2RTimerButton.clicked.connect(self.r2rTimerGo)

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
        print("starting TLK")
        timerProc=Process(target=self.timedLauncherKiller, \
            args=(motorTreat,self.TxtTime.value,self.driveMotorSpeed.value,self.driveMotorSpeedMultiplier.value))
        timerProc.start()

    #This will launch things, then wait and maybe kill them
    def timedLauncherKiller(self,proc,time,speed,mult):
        print("starting proc: "+str(proc))
        QtGui.qApp.processEvents()
        procLaunched=Process(target=proc, \
            args=(self.TxtTime.value,self.driveMotorSpeed.value,self.driveMotorSpeedMultiplier.value))
        procLaunched.start()
        #countdownthread=countDownTimer(self.TxtTime.value)
        #self.connect,self.
        #countdownthread.start()
        #self.connect(countdownthread, SIGNAL("timeLeft(int)"), self.tickdown)
        self.controller.go(time)
        while time+1 > 0:
            print(self.controller.isRunning())
            print(time)
            time -= 1
            sleep(1)
    #testing the signalling of the threads


    def tickdown(self,time):
        print("tickdown")
        dispmin,dispsec=divmod(time,60)
        self.TxtTimeDisplay.display(str(dispmin)+":"+str(dispsec))
        #start a qthread to countdown on the screen
        #consider using them to watch and kill the threads.

        #self.TxtTimeDisplay.display(str(dispmin)+":"+str(dispsec))

    #fill in these later
    def r2rGo(self):
        return 0
    def r2rStop(self):
        return 0
    def r2rTimerGo(self):
        return 0

    #stop all motors
    def txtStop(self):
        print("STOP ALL MOTORS")
        self.controller.die
        #timerProc.terminate()
        #timedLauncherKiller.terminate()
        #countdownthread.terminate()
        print(self.controller.isRunning)
        #for proc in self.proclist:
        #    print("killing "+str(proc))
        #    proc.terminate()
        #    proc.join()

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

def motorTreat(self,speed,mult):
    print("starting motors at "+str(speed)+" and mult of "+str(mult))
    i=0
    while i < 10:
        print("motors still going")
        i += 1
        sleep(1)

#BoilerPlate
def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    testval=Value('i',10)
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
