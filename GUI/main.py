import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import mainWidget
import playerStats
import pyqtgraph as pyg
import qtgrapher
import numpy as np 



class TestWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(TestWindow, self).__init__()
        self.timer = QtCore.QTimer(self)

        self.ui = example.Ui_MainWindow() # in this and next line you say that you will use all widgets from testUI over self.ui

        self.page2 = QtWidgets.QWidget()
        self.pg2 = page2.Ui_widget()
        self.pg2.setupUi(self.page2)

        self.page3 = QtWidgets.QWidget()
        self.pg3 = qtgrapher.Ui_Form()
        self.pg3.setupUi(self.page3)

        self.ui.setupUi(self)
        
        self.ui.stackedWidget.addWidget(self.page2)
        self.ui.stackedWidget.addWidget(self.page3)
        #so, when you say self.ui.myButton ,that is pushButton in testUI that has name myButton
        self.ui.pushButton.clicked.connect(self.DoSomething)# connect button clicked with action
        self.pg2.Home.clicked.connect(self.goHome);
        self.pg3.pushButton.clicked.connect(self.goHome)

        

    def DoSomething(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        
        self.timer.setInterval(100)
        self.timer.start()
        self.timer.timeout.connect(self.onNewData)
        print(self.ui.stackedWidget.count())

    def goHome(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.timer.stop()

    def onNewData(self):
        self.pg3.graphicsView.plot(np.random.normal(size = 100),np.random.normal(size = 100),clear=True)
        print("timer on going")

        # self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TestWindow()
    window.setStyleSheet(open('test.qss').read())
    window.show()

    sys.exit(app.exec_())
