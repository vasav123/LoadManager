import sys
from PyQt5 import   QtGui, QtCore, QtWidgets
import mainWindow
from  mainWidgetWrapper import *
import numpy as np
import threading
from collectData import *

mqtt_client = None

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


def pushOnQ():
    mqtt_client = collectData()
    rc = 0
    while rc == 0:
        rc=test.loop()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TestWindow()

    

    pushThread=threading.Thread(target=pushOnQ)
    pushThread.start()
    

    sys.exit(app.exec_())
