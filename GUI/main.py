import sys
from PyQt5 import   QtGui, QtCore, QtWidgets
import mainWindow
from recordControl import *
from mainWidgetWrapper import *
from  mainWidgetWrapper import *
import numpy as np
import threading
from collectData import *
from queue import Queue
from time import *

mqtt_client = collectData()

class TestWindow():
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

    def syncData(self, ax_t,ay_t,az_t,ax_b,ay_b,az_b,fq_q,fh_q,gx_t,gy_t,gz_t,gx_b,gy_b,gz_b):
        while True:
            if (ax_t.qsize() > 0):self.statsWidget_obj.ax_t += ax_t.get_nowait()
            if (ay_t.qsize() > 0):self.statsWidget_obj.ay_t += ay_t.get_nowait()
            if (az_t.qsize() > 0):self.statsWidget_obj.az_t += az_t.get_nowait()
            if (ax_b.qsize() > 0):self.statsWidget_obj.ax_b += ax_b.get_nowait()
            if (ay_b.qsize() > 0):self.statsWidget_obj.ay_b += ay_b.get_nowait()
            if (az_b.qsize() > 0):self.statsWidget_obj.az_b += az_b.get_nowait()
            if (fq_q.qsize() > 0):self.statsWidget_obj.fq_a += fq_q.get_nowait() 
            if (fh_q.qsize() > 0):self.statsWidget_obj.fh_a += fh_q.get_nowait() 
            if (gx_t.qsize() > 0):self.statsWidget_obj.gx_t += gx_t.get_nowait() 
            if (gy_t.qsize() > 0):self.statsWidget_obj.gy_t += gy_t.get_nowait() 
            if (gz_t.qsize() > 0):self.statsWidget_obj.gz_t += gz_t.get_nowait() 
            if (gx_b.qsize() > 0):self.statsWidget_obj.gx_b += gx_b.get_nowait() 
            if (gy_b.qsize() > 0):self.statsWidget_obj.gy_b += gy_b.get_nowait() 
            if (gz_b.qsize() > 0):self.statsWidget_obj.gz_b += gz_b.get_nowait()
            if len(self.statsWidget_obj.ax_t)>1000:
                del self.statsWidget_obj.ax_t[:800]
                del self.statsWidget_obj.ay_t[:800]
                del self.statsWidget_obj.az_t[:800]
                del self.statsWidget_obj.ax_b[:800]
                del self.statsWidget_obj.ay_b[:800]
                del self.statsWidget_obj.az_b[:800]
                del self.statsWidget_obj.fq_a[:800]
                del self.statsWidget_obj.fh_a[:800]
                del self.statsWidget_obj.gx_t[:800]
                del self.statsWidget_obj.gy_t[:800]
                del self.statsWidget_obj.gz_t[:800]
                del self.statsWidget_obj.gx_b[:800]
                del self.statsWidget_obj.gy_b[:800]
                del self.statsWidget_obj.gz_b[:800]
##                
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

    pullThread=threading.Thread(target=window.syncData,args=(mqtt_client.ax_t, mqtt_client.ay_t, mqtt_client.az_t,mqtt_client.ax_b, mqtt_client.ay_b, mqtt_client.az_b,mqtt_client.fq_q,mqtt_client.fh_q,mqtt_client.gx_t,mqtt_client.gy_t,mqtt_client.gz_t,mqtt_client.gx_b,mqtt_client.gy_b,mqtt_client.gz_b))
    pullThread.start()
    # window.statsWidget_obj.back.clicked.connect(window.exitStats)
    # window.ui.kawhiButton.clicked.connect(lambda:window.ui.appWidgets.setCurrentIndex(1))
    # window.statsWidget_obj.Record.clicked.connect(lambda:window.ui.appWidgets.setCurrentIndex(2))

    sys.exit(app.exec_())
