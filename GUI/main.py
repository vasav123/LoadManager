import sys
from PyQt5 import   QtGui, QtCore, QtWidgets
import mainWindow
from dataPreProcessor import *
from recordControl import *
from mainWidgetWrapper import *
from  mainWidgetWrapper import *
import numpy as np
import scipy as sp
import threading
from collectData import *
from queue import Queue
from time import *
import math

mqtt_client = collectData()

class TestWindow():
    dt = 0.005
    a = 0.98
    numSteps = 0
    numWalk = 0
    numRun = 0
    numSprint = 0
    numJumps = 0
    maxJumpHeight = 0
    percent = 0
    score = 0
    maxScore = 1000
    isJump = False
    oldt = 0
    index1 = 0
    #StartTime = time.time()
    isTimer = False
    isWrite = False
    def __init__(self):
        super(TestWindow, self).__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.setStyleSheet(open('test.qss').read())
        self.MainWindow.showMaximized()
        self.ui = mainWindow.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.statsWidget = QtWidgets.QWidget()
        self.statsWidget_obj = mainWidgetWrapper()
        self.statsWidget_obj.setupUi(self.statsWidget)
        
        self.ui.appWidgets.addWidget(self.statsWidget)
        #
        self.ui.appWidgets.setCurrentIndex(0)

        self.statsWidget_obj.back.clicked.connect(self.exitStats)
        self.ui.kawhiButton.clicked.connect(lambda:self.ui.appWidgets.setCurrentIndex(1))
        self.statsWidget_obj.Settings.clicked.connect(self.switchControl)

        mqtt_client.record_widget = self.statsWidget_obj.record_widget
        #Recording Buttons
        self.statsWidget_obj.record_widget.startRecord.clicked.connect(lambda: (mqtt_client.setWriteToFile(True, self.statsWidget_obj.record_widget.CSV_output.toPlainText())))
        self.statsWidget_obj.record_widget.stopRecord.clicked.connect(lambda:  (mqtt_client.setWriteToFile(False, "")))

        #Stats LCD screens
        self.statsWidget_obj.pStats_widget.NumSteps.display(self.numSteps)
        self.statsWidget_obj.pStats_widget.NumRun.display(self.numRun)
        self.statsWidget_obj.pStats_widget.NumWalk.display(self.numWalk)
        self.statsWidget_obj.pStats_widget.NumSprint.display(self.numSprint)
        self.statsWidget_obj.pStats_widget.jumpHeight.display(self.maxJumpHeight)
        self.statsWidget_obj.pStats_widget.NumJumps.display(self.numJumps)
        

        #define Recording functions
    def applyFilter(self,seris, filtype, cutoff, order):#using this in main
                sos = signal.butter(order, cutoff,btype = filtype,analog = False, output="sos", fs=200)
                self.time_series = signal.sosfilt(sos,seris)
                return self.time_series
        
    def switchControl(self):
        if  self.statsWidget_obj.Settings.text() == 'Settings':
            self.statsWidget_obj.playerStats.setCurrentIndex(1)
            self.statsWidget_obj.Settings.setText('Player Stats')
        else:
            self.statsWidget_obj.playerStats.setCurrentIndex(0)
            self.statsWidget_obj.Settings.setText('Settings')
    
    def calculateJumpHeight(self, index1, index2):
##        ay_t = [obj.ay_t for obj in self.statsWidget_obj.data_l]
##        peak_height,_ = scipy.signal.find_peaks(ay_t,height=4,distance=45)
##        takeoff=[]
##        landing=[]
##
##        for x in range(len(peak_height)):
##                if x%2==0:
##                        takeoff.append(peak_height[x])
##                else:
##                        landing.append(peak_height[x])

        offset_h = 0.12 * 39.3701 #displacement between neutral standing position and takeoff position, converted to inches
        g= 9.81 #gravity
        kh = 1 #constant from research paper

        jump_height=[]
        #for y in range(len(landing)): # you should never have more landings than takeoffs
        airtime = abs((index1-index2))*0.005 #convert to seconds
        height = offset_h + (kh * 1/8 * (airtime**2) * g)*39.3701 #convert to inches
        jump_height.append(height)
        self.maxJumpHeight = max(len(jump_height)>0 and max(jump_height) or 0, self.maxJumpHeight)
        self.numJumps += len(jump_height)
    
    def calculateStats(self):
        XT = np.array([obj.ax_t for obj in self.statsWidget_obj.data_l])
        ZT = np.array([obj.ay_t for obj in self.statsWidget_obj.data_l])
        YT = np.array([obj.az_t for obj in self.statsWidget_obj.data_l])
        #Filter All 3
        XT_filt =self.applyFilter(XT,'lowpass',45,10)
        YT_filt =self.applyFilter(YT,'lowpass',45,10)
        ZT_filt =self.applyFilter(ZT,'lowpass',45,10)
        #Square all 3
        XT_2 = np.square(XT_filt)
        ZT_2 = np.square(ZT_filt)
        YT_2 = np.square(YT_filt)
        #Find magnitude
        AT_mag = np.sqrt(np.add(XT_2,ZT_2,YT_2))
        peaks = signal.find_peaks(AT_mag, height= 2.1, distance=80)
        #I have peaks above 1.5
        #For each peak I need to check the surrond average
        #Check if we are in the middle of a jump
        indexes = peaks[0]
        magnitudes = peaks[1]
        print(indexes)
        if self.isJump == True:
            if len(indexes >0):
                index2 = indexes[0]
                index2 =index2 + 1000
                self.calculateJumpHeight(self.index1,index2)
                np.delete(indexes,0)
            self.isJump = False
        
        for i in range(len(indexes)):#1.5 peak is walking, 4 is jog, 6 is Running
            mag = AT_mag[indexes[i]]
            print(peaks)
            #print("Height " + str(mag))
            if indexes[i]<41 or indexes[i]>959:#what to do if the peaks are at the end of the sequence
                if indexes[i]<41:
                    ave = np.mean(AT_mag[indexes[i]:indexes[i]+80])
                elif indexes[i]>969:
                    ave = np.mean(AT_mag[indexes[i]-80:indexes[i]])
            else:
                ave = np.mean(AT_mag[indexes[i]-40:indexes[i]+40])
            if mag<4.5 and ave<1.5:#walking
                if mag>ave:
                    # print("walk step: Height: " + str(mag) + "peak average" + str(ave)+ "Index: " + str(i))
                    self.numSteps += 1
                    self.numWalk += 1
            elif 4.5<mag<7:#Jogging
                if mag>3*ave:#check if it actually is a true peak in jog
                    # print("Jog step: Height: " + str(mag) + "peak average" + str(ave) + "Index: " + str(i))
                    self.numSteps += 1
                    self.numRun += 1
            else:#Sprinting
                if mag>ave:
                    # print("Sprint step: Height: " + str(mag) + "peak average: " + str(ave)+ "Index: " + str(i))
                    if ave<2.3:#Jump
                        if(indexes[i] == indexes[-1]):#Jump is split by time intervals
                            self.index1 = indexes[i]
                            self.isJump = True
                        else:
                            self.calculateJumpHeight(indexes[i],indexes[i+1])
                            np.delete(indexes,i+1)
                    else:
                        self.numSteps += 1
                        self.numSprint += 1
    
    def calculateKneeAngle(self):
        if (len(self.statsWidget_obj.data_l)>1):
            this_point = self.statsWidget_obj.data_l[-1]
            last_point = self.statsWidget_obj.data_l[-2]
            # use atan2 to prevent dvision by 0
            rot_x_t = math.degrees(math.atan2(this_point.ay_t,(this_point.ax_t**2 + this_point.az_t**2)**0.5))
            rot_x_b = math.degrees(math.atan2(this_point.ay_b,(this_point.ax_b**2 + this_point.az_b**2)**0.5))

            rot_y_t = math.degrees(math.atan2(this_point.ax_t,(this_point.ay_t**2 + this_point.az_t**2)**0.5))
            rot_y_b = math.degrees(math.atan2(this_point.ax_b,(this_point.ay_b**2 + this_point.az_b**2)**0.5))

            rot_z_t = math.degrees(math.atan2((this_point.ax_t**2 + this_point.ay_t**2)**0.5,this_point.az_t))
            rot_z_b = math.degrees(math.atan2((this_point.ax_b**2 + this_point.ay_b**2)**0.5,this_point.az_b))
            
            try:
                # use the complementary filter to prevent drift
                this_point.angle_x_t = self.a*(last_point.angle_x_t + this_point.gx_t*self.dt)+(1-self.a)*rot_x_t
                this_point.angle_x_b = self.a*(last_point.angle_x_b + this_point.gx_b*self.dt)+(1-self.a)*rot_x_b
                
                this_point.angle_y_t = self.a*(last_point.angle_y_t + this_point.gy_t*self.dt)+(1-self.a)*rot_y_t
                this_point.angle_y_b = self.a*(last_point.angle_y_b + this_point.gy_b*self.dt)+(1-self.a)*rot_y_b
                
                this_point.angle_z_t = self.a*(last_point.angle_z_t + this_point.gz_t*self.dt)+(1-self.a)*rot_z_t
                this_point.angle_z_b = self.a*(last_point.angle_z_b + this_point.gz_b*self.dt)+(1-self.a)*rot_z_b
                
                this_point.flexion = this_point.angle_x_t-this_point.angle_x_b
                this_point.abduction = this_point.angle_y_t-this_point.angle_y_b
                this_point.supination = this_point.angle_z_t-this_point.angle_z_b

            except Exception as e:
                print (e)

    def updateStats(self):
        self.statsWidget_obj.pStats_widget.NumSteps.display(self.numSteps)
        self.statsWidget_obj.pStats_widget.NumWalk.display(self.numWalk)
        self.statsWidget_obj.pStats_widget.NumSteps.display(self.numSteps)
        self.statsWidget_obj.pStats_widget.NumRun.display(self.numRun)
        self.statsWidget_obj.pStats_widget.NumSteps.display(self.numSteps)
        self.statsWidget_obj.pStats_widget.NumSprint.display(self.numSprint)
        self.statsWidget_obj.pStats_widget.jumpHeight.display(self.maxJumpHeight)
        self.statsWidget_obj.pStats_widget.NumJumps.display(self.numJumps)
        self.score = self.numWalk + 2*self.numRun + 4*self.numSprint + 2*self.numJumps
        self.statsWidget_obj.pStats_widget.Score.display(self.score)
        self.maxScore = self.statsWidget_obj.record_widget.maxScore.intValue()
        self.percent = (self.score/self.maxScore)*100
        self.statsWidget_obj.pStats_widget.percentPlayed.setValue(int(self.percent))
    
    def syncData(self,dataQ):
        while True:
            if (dataQ.qsize() > 0):
                self.statsWidget_obj.data_l.append(dataQ.get_nowait())
                self.statsWidget_obj.end_num_sample += 1

            if self.statsWidget_obj.end_num_sample>0 and self.statsWidget_obj.end_num_sample%1000 == 0 and self.oldt !=self.statsWidget_obj.end_num_sample:
                self.oldt = self.statsWidget_obj.end_num_sample
                #print(self.statsWidget_obj.end_num_sample)
                self.calculateStats()
                #self.calculateJumpHeight()
                self.updateStats()

            self.calculateKneeAngle()
            # print(len(self.statsWidget_obj.data_l))
            if len(self.statsWidget_obj.data_l)>self.statsWidget_obj.plot_window:
                self.statsWidget_obj.start_num_sample += 1
                del self.statsWidget_obj.data_l[:len(self.statsWidget_obj.data_l)-self.statsWidget_obj.plot_window]
            sleep(0.001)
  

    def exitStats(self):
        self.ui.appWidgets.setCurrentIndex(0)
        self.statsWidget_obj.timer.stop()        

def pushOnQ():
    rc = 0
    while rc == 0:
        rc=mqtt_client.loop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TestWindow()
    pushThread=threading.Thread(target=pushOnQ)
    pushThread.start()

    pullThread=threading.Thread(target=window.syncData,args=(mqtt_client.dataQ,))
    pullThread.start()

    sys.exit(app.exec_())
