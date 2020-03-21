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

            if (len(self.statsWidget_obj.data_l)>1):
                mag_xz = np.sqrt(self.statswidget_obj.data_1[-1].ax_t**2 + self.statswidget_obj.data_1[-1].az_t**2)
                if mag_xz<0.34:
                    self.count = self.count +1
                    if self.count>100:
                        self.count = 0
                        self.statsWidget_obj.data_l[-1].velocity = 0
                else:
                    self.count = 0
    
                rot_x_t = math.degrees(math.atan(self.statsWidget_obj.data_l[-1].ay_t/(self.statsWidget_obj.data_l[-1].ax_t**2 + self.statsWidget_obj.data_l[-1].az_t**2)**0.5))
                rot_x_b = math.degrees(math.atan(self.statsWidget_obj.data_l[-1].ay_b/(self.statsWidget_obj.data_l[-1].ax_b**2 + self.statsWidget_obj.data_l[-1].az_b**2)**0.5))
                try:
                    self.statsWidget_obj.data_1[-1].velocity = self.statsWidget_obj.data_1[-2].velocity
                    self.statsWidget_obj.data_l[-1].angle_x_t = self.a*(self.statsWidget_obj.data_l[-2].angle_x_t + self.statsWidget_obj.data_l[-1].gx_t*self.dt)+(1-self.a)*rot_x_t
                    self.statsWidget_obj.data_l[-1].angle_x_b = self.a*(self.statsWidget_obj.data_l[-2].angle_x_b + self.statsWidget_obj.data_l[-1].gx_b*self.dt)+(1-self.a)*rot_x_b
                    self.statsWidget_obj.data_l[-1].knee_angle = self.statsWidget_obj.data_l[-1].angle_x_t-self.statsWidget_obj.data_l[-1].angle_x_b
                    if (len(self.statsWidget_obj.data_l)>2):
                        self.statsWidget_obj.data_1[-1].velocity = self.statsWidget_obj.data_1[-2].velocity + mag_xz*0.005
                    else:
                        self.statsWidget_obj.data_1[-1].velocity = 0
                except Exception as e:
                    print (e)
            if len(self.statsWidget_obj.data_l)>self.statsWidget_obj.plot_window:
                self.statsWidget_obj.start_num_sample += 1
                del self.statsWidget_obj.data_l[:len(self.statsWidget_obj.data_l)-self.statsWidget_obj.plot_window]
            sleep(0.01)

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
