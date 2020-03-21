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

        self.statsWidget_obj.back.clicked.connect(self.exitStats)#lambda:self.ui.appWidgets.setCurrentIndex(0))
        self.ui.kawhiButton.clicked.connect(lambda:self.ui.appWidgets.setCurrentIndex(1))
        self.statsWidget_obj.Record.clicked.connect(self.Switch_control)

        #Recording Buttons
        self.statsWidget_obj.record_widget.startRecord.clicked.connect(self.start_Record)
        self.statsWidget_obj.record_widget.stopRecord.clicked.connect(self.stop_Record)
        self.NumSteps = 0
        self.NumWalk = 0
        self.NumRun = 0
        self.NumSprint = 0
        self.statsWidget_obj.pStats_widget.NumSteps.display(self.NumSteps)
        self.statsWidget_obj.pStats_widget.NumRun.display(self.NumRun)
        self.statsWidget_obj.pStats_widget.NumWalk.display(self.NumWalk)
        self.statsWidget_obj.pStats_widget.NumSprint.display(self.NumSprint)
        self.count=0
        # self.dataSyncTimer = QtCore.QTimer(self.MainWindow)
        # self.dataSyncTimer.setInterval(1000)
        # self.dataSyncTimer.start()
        # self.dataSyncTimer.timeout.connect(self.syncData)

        #define Recording functions
    def start_Record(self):
            mqtt_client.fileName = self.statsWidget_obj.record_widget.CSV_output.toPlainText() +'.csv'
            mqtt_client.writeToFile = True
            print('Outputing Recording to: ' + mqtt_client.fileName)
            
    def applyFilter(self,seris, filtype, cutoff, order):#using this in main
                sos = signal.butter(order, cutoff,btype = filtype,analog = False, output="sos", fs=200)
                self.time_series = signal.sosfilt(sos,seris)
                return self.time_series

    def stop_Record(self):
            mqtt_client.writeToFile = False
            print('Recording Stopped')
        
    def Switch_control(self):
        if  self.statsWidget_obj.Record.text() == 'Record':
            self.statsWidget_obj.playerStats.setCurrentIndex(1)
            self.statsWidget_obj.Record.setText('Player Stats')
        else:
            self.statsWidget_obj.playerStats.setCurrentIndex(0)
            self.statsWidget_obj.Record.setText('Record')

    def syncData(self,dataQ):
        while True:
            if (dataQ.qsize() > 0):
                self.statsWidget_obj.data_l.append(dataQ.get_nowait())
                self.statsWidget_obj.end_num_sample += 1

            if self.statsWidget_obj.end_num_sample>0 and self.statsWidget_obj.end_num_sample%1000 == 0:
                XT = np.array([obj.ax_t for obj in self.statsWidget_obj.data_l])
                ZT = np.array([obj.ay_t for obj in self.statsWidget_obj.data_l])
                YT = np.array([obj.az_t for obj in self.statsWidget_obj.data_l])
                #Filter All 3
                XT_filt =self.applyFilter(XT,'bandpass',[0.1,30],10)
                YT_filt =self.applyFilter(YT,'bandpass',[0.1,30],10)
                ZT_filt =self.applyFilter(ZT,'bandpass',[0.1,30],10)
                #Square all 3
                XT_2 = np.square(XT_filt)
                ZT_2 = np.square(ZT_filt)
                YT_2 = np.square(YT_filt)
                #Find magnitude
                AT_mag = np.sqrt(np.add(XT_2,ZT_2,YT_2))
                #Adjust for Time current Sample is 200hz
                XT_time_adjust = XT_filt*0.005
                ZT_time_adjust = ZT_filt*0.005
                XT_velocity = np.cumsum(XT_time_adjust)
                ZT_velocity = np.cumsum(ZT_time_adjust)
                #Find the magnitude of the velocity
                XT_V2 = np.square(XT_velocity)
                ZT_V2 = np.square(ZT_velocity)
                velocity_MperS = np.sqrt(np.add(XT_V2,ZT_V2))
                #Convert to km/h
                velocity = velocity_MperS*3.6
                self.statsWidget_obj.pStats_widget.aveVelocity.display(int(np.mean(velocity)))
                peaks = signal.find_peaks(AT_mag, height= 1.5, distance = 50)
                print(peaks[0])
                for i in peaks[0]:#5km/h walking, 20 km/h jog, higher than 15 is sprinting
                    speed = velocity[i]
                    print(speed)
                    if speed<5:#walking
                        self.NumSteps = self.NumSteps +1
                        self.statsWidget_obj.pStats_widget.NumSteps.display(self.NumSteps)
                        self.NumWalk = self.NumWalk + 1
                        self.statsWidget_obj.pStats_widget.NumWalk.display(self.NumWalk)
                    elif 5<speed<20:
                        if AT_mag[i]>3.5:#check if it actually is a true peak in jog
                            self.NumSteps = self.NumSteps +1
                            self.statsWidget_obj.pStats_widget.NumSteps.display(self.NumSteps)
                            self.NumRun = self.NumRun + 1
                            self.statsWidget_obj.pStats_widget.NumRun.display(self.NumRun)
                    else:
                        if AT_mag[i]>5.5:#check if it actually is a true peak in sprint
                            self.NumSteps = self.NumSteps +1
                            self.statsWidget_obj.pStats_widget.NumSteps.display(self.NumSteps)
                            self.NumRun = self.NumSprint + 1
                            self.statsWidget_obj.pStats_widget.NumSprint.display(self.NumSprint)

            if (len(self.statsWidget_obj.data_l)>1):
                rot_x_t = math.degrees(math.atan(self.statsWidget_obj.data_l[-1].ay_t/(self.statsWidget_obj.data_l[-1].ax_t**2 + self.statsWidget_obj.data_l[-1].az_t**2)**0.5))
                rot_x_b = math.degrees(math.atan(self.statsWidget_obj.data_l[-1].ay_b/(self.statsWidget_obj.data_l[-1].ax_b**2 + self.statsWidget_obj.data_l[-1].az_b**2)**0.5))
                try:
                    self.statsWidget_obj.data_l[-1].angle_x_t = self.a*(self.statsWidget_obj.data_l[-2].angle_x_t + self.statsWidget_obj.data_l[-1].gx_t*self.dt)+(1-self.a)*rot_x_t
                    self.statsWidget_obj.data_l[-1].angle_x_b = self.a*(self.statsWidget_obj.data_l[-2].angle_x_b + self.statsWidget_obj.data_l[-1].gx_b*self.dt)+(1-self.a)*rot_x_b
                    self.statsWidget_obj.data_l[-1].knee_angle = self.statsWidget_obj.data_l[-1].angle_x_t-self.statsWidget_obj.data_l[-1].angle_x_b
                except Exception as e:
                    print (e)
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
    # window.statsWidget_obj.back.clicked.connect(window.exitStats)
    # window.ui.kawhiButton.clicked.connect(lambda:window.ui.appWidgets.setCurrentIndex(1))
    # window.statsWidget_obj.Record.clicked.connect(lambda:window.ui.appWidgets.setCurrentIndex(2))

    sys.exit(app.exec_())
