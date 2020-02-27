import sys
from PyQt5 import   QtGui, QtCore, QtWidgets
import mainWindow
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
        self.ui.appWidgets.setCurrentIndex(0)
        self.statsWidget_obj.back.clicked.connect(lambda:self.ui.appWidgets.setCurrentIndex(0))
        self.ui.kawhiButton.clicked.connect(lambda:self.ui.appWidgets.setCurrentIndex(1))
        self.statsWidget_obj.Record.clicked.connect(lambda:self.ui.appWidgets.setCurrentIndex(2))
        # self.dataSyncTimer = QtCore.QTimer(self.MainWindow)
        # self.dataSyncTimer.setInterval(1000)
        # self.dataSyncTimer.start()
        # self.dataSyncTimer.timeout.connect(self.syncData)
    def syncData(self, at_q,ab_q,fq_q,fh_q,yt_q,pt_q,rt_q,yb_q,pb_q,rb_q):
        while True:
            if (at_q.qsize() > 0):self.statsWidget_obj.at_a += at_q.get_nowait() 
            if (ab_q.qsize() > 0):self.statsWidget_obj.ab_a += ab_q.get_nowait() 
            if (fq_q.qsize() > 0):self.statsWidget_obj.fq_a += fq_q.get_nowait() 
            if (fh_q.qsize() > 0):self.statsWidget_obj.fh_a += fh_q.get_nowait() 
            if (yt_q.qsize() > 0):self.statsWidget_obj.yt_a += yt_q.get_nowait() 
            if (pt_q.qsize() > 0):self.statsWidget_obj.pt_a += pt_q.get_nowait() 
            if (rt_q.qsize() > 0):self.statsWidget_obj.rt_a += rt_q.get_nowait() 
            if (yb_q.qsize() > 0):self.statsWidget_obj.yb_a += yb_q.get_nowait() 
            if (pb_q.qsize() > 0):self.statsWidget_obj.pb_a += pb_q.get_nowait() 
            if (rb_q.qsize() > 0):self.statsWidget_obj.rb_a += rb_q.get_nowait() 
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

    pullThread=threading.Thread(target=window.syncData,args=(mqtt_client.at_q, mqtt_client.ab_q,mqtt_client.fq_q,mqtt_client.fh_q,mqtt_client.yt_q,mqtt_client.pt_q,mqtt_client.rt_q,mqtt_client.yb_q,mqtt_client.pb_q,mqtt_client.rb_q))
    pullThread.start()

    sys.exit(app.exec_())
