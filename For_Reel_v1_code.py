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
        self.txtDisplayUpdate(self.TxtTime.value)
    def timeDown(self):
        if self.TxtTimeDialSeconds.isChecked():
            self.TxtTime.value=self.TxtTime.value-1
        elif self.TxtTimeDialMinutes.isChecked():
            self.TxtTime.value=self.TxtTime.value-60
        self.txtDisplayUpdate(self.TxtTime.value)

    #update the txt timer display
    def txtDisplayUpdate(self,timer):
        dispmin,dispsec=divmod(timer,60)
        self.TxtTimeDisplay.display(str(dispmin)+":"+str(dispsec))

    def countDownDisplay(self,timer):
        for i in range(timer):
            if self.stopEverything.value==1:
                break
            timerd=timer-i
            self.txtDisplayUpdate(timerd)
            start = time.time()
            while time.time() - start < 1:
                QtGui.qApp.processEvents()
                time.sleep(0.02)

    # def counterThread(self,timer):
    #     print("starting counterThread")
    #     # QtGui.qApp.processEvents()
    #     while timer > 0:
    #         # QtGui.qApp.processEvents()
    #         if self.stopEverything.value==1:
    #             print("breaking thread")
    #             break
    #         print(timer)
    #
    #     self.testStop()
    #
    # def signalResponse(self,input):
    #     print("signal"+str(input))

    def testGo(self):
        self.stopEverything.value=0
        moGo(self)
        # QtGui.qApp.processEvents()
        #ct = Process(target=self.counterThread, args=(self.TxtTime.value,))
        #ct.start()
        self.countDownDisplay(self.TxtTime.value)
        #watch for the fucking signal
        # upfd = UpdateFuckingDisplay()
        # upfd.run(self.TxtTime.value)
        # self.connect(upfd, upfd.signal, self.signalResponse)
        print("testGo complete")

    def testStop(self):
        self.stopEverything.value=1
        moStop()
        self.txtDisplayUpdate(self.TxtTime.value)




    #Do the actual treatment
    # def txtGo(self):
    #     print("starting TLK")
    #     timerProc=Process(target=self.timedLauncherKiller, \
    #         args=(motorTreat,self.TxtTime.value,self.driveMotorSpeed.value,self.driveMotorSpeedMultiplier.value))
    #     timerProc.start()
    #
    # #This will launch things, then wait and maybe kill them
    # def timedLauncherKiller(self,proc,timer,speed,mult):
    #     print("starting proc: "+str(proc))
    #     QtGui.qApp.processEvents()
    #     procLaunched=Process(target=proc, \
    #         args=(self.TxtTime.value,self.driveMotorSpeed.value,self.driveMotorSpeedMultiplier.value))
    #     print("launching motors")
    #     procLaunched.start()
    #     while timer+1 > 0:
    #         if self.motorFullStop.value==1:
    #             break
    #         print(timer)
    #         self.TxtTimeDisplay.display(timer)
    #         timer -= 1
    #         time.sleep(1)
    #     print("TLK dead")
    #testing the signalling of the threads


    # def tickdown(self,time):
    #     print("tickdown")
    #     dispmin,dispsec=divmod(time,60)
    #     self.TxtTimeDisplay.display(str(dispmin)+":"+str(dispsec))
    #     #start a qthread to countdown on the screen
    #     #consider using them to watch and kill the threads.
    #
    #     #self.TxtTimeDisplay.display(str(dispmin)+":"+str(dispsec))

    #fill in these later
    def r2rGo(self):
        return 0
    def r2rStop(self):
        return 0
    def r2rTimerGo(self):
        return 0

# def txtProc(speed,mult):
#     print("speed: "+str(speed))
#     print("mult: "+str(mult))
#     #ime=TxtTime.value
#     while TxtTime.value >= 0:
#         time.sleep(1)
#         self.TxtTime.value=self.TxtTime.value-1
#         dispmin,dispsec=divmod(self.TxtTime.value,60)
#         self.TxtTimeDisplay.display(str(dispmin)+":"+str(dispsec))
#
# def motorTreat(self,speed,mult):
#     print("starting motors at "+str(speed)+" and mult of "+str(mult))
#     i=0
#     while i < 10:
#         if motorFullStopGlobal.value == 1:
#             break
#         print("motors still going")
#         i += 1
#         time.sleep(1)


#Need to link this to the direction of each of the motors, which should be easy
# They will only change for the R2R mode.
def moGo(self):
    print("motors start")

def moStop():
    print("motors stop")




#BoilerPlateQtGui.qApp.processEvents()QtGui.qApp.processEvents()
def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    #print(form.motorFullStop.value) #note, this works.
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
