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

    def syncData(self, ax_t,ay_t,az_t,ax_b,ay_b,az_b,fq_q,fh_q,gx_t,gy_t,gz_t,gx_b,gy_b,gz_b, dataQ):
        while True:
            if (dataQ.qsize() > 0): self.statsWidget_obj.data_l.append(dataQ.get_nowait())
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

    pullThread=threading.Thread(target=window.syncData,args=(mqtt_client.ax_t, mqtt_client.ay_t, mqtt_client.az_t,mqtt_client.ax_b, mqtt_client.ay_b, mqtt_client.az_b,mqtt_client.fq_q,mqtt_client.fh_q,mqtt_client.gx_t,mqtt_client.gy_t,mqtt_client.gz_t,mqtt_client.gx_b,mqtt_client.gy_b,mqtt_client.gz_b, mqtt_client.dataQ))
    pullThread.start()
    # window.statsWidget_obj.back.clicked.connect(window.exitStats)
    # window.ui.kawhiButton.clicked.connect(lambda:window.ui.appWidgets.setCurrentIndex(1))
    # window.statsWidget_obj.Record.clicked.connect(lambda:window.ui.appWidgets.setCurrentIndex(2))

    sys.exit(app.exec_())
