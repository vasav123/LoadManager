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
                XB = np.array([obj.ax_b for obj in self.statsWidget_obj.data_l])
                ZB = np.array([obj.az_b for obj in self.statsWidget_obj.data_l])
                YB = np.array([obj.ay_b for obj in self.statsWidget_obj.data_l])
                XB_2 = np.square(XB)
                ZB_2 = np.square(ZB)
                YB_2 = np.square(YB)
                XZB_mag = np.sqrt(np.add(XB_2,ZB_2))
                #Multiply the time in
                XZB_mag_adjust = XZB_mag*0.005
                AB_mag = np.sqrt(np.add(XB_2,ZB_2,YB_2))
                AB_mag_filtered = self.applyFilter(AB_mag,'lowpass', 15, 8)
                #signal.detrend or applyFilter(A_mag,'highpass', 1, 10)
                #A_mag_filter = sp.signal.detrend(A_mag)
                velocity_MperS = np.cumsum(XZB_mag_adjust)
                #velo_filtered = sp.signal.detrend(velocity_MperS)
                velo_filtered = self.applyFilter(velocity_MperS,'highpass', 0.11, 10)
                velo_kmH = velo_filtered*3.6
                #print(type(velo_kmH)) tpye nd
                #Find all peaks above 1.5 mag
                peaks = signal.find_peaks(AB_mag_filtered, height= 1.4, distance = 80)
                print(peaks[0])
                for i in peaks[0]:#5km/h walking, 20 km/h jog, higher than 15 is sprinting
                    speed = velo_kmH[i]
                    print(speed)
                    if speed<5:#walking
                        self.NumSteps = self.NumSteps +1
                        self.statsWidget_obj.pStats_widget.NumSteps.display(self.NumSteps)
                        self.NumWalk = self.NumWalk + 1
                        self.statsWidget_obj.pStats_widget.NumWalk.display(self.NumWalk)
                    elif 5<speed<20:
                        if AB_mag_filtered[i]>4:#check if it actually is a true peak in jog
                            self.NumSteps = self.NumSteps +1
                            self.statsWidget_obj.pStats_widget.NumSteps.display(self.NumSteps)
                            self.NumRun = self.NumRun + 1
                            self.statsWidget_obj.pStats_widget.NumRun.display(self.NumRun)
                    else:
                        if AB_mag_filtered[i]>6:#check if it actually is a true peak in sprint
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
