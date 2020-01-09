
from PyQt5 import QtCore, QtGui, QtWidgets
import mainWidget
import playerStats
import sys
import graphs
import pyqtgraph as pyg
import numpy as np

class mainWidgetWrapper(mainWidget.Ui_Form):
        lastbutton = ""
        def setupUi(self,Form):
                super(mainWidget.Ui_Form, self).__init__()
                mainWidget.Ui_Form.setupUi(self,Form)
                self.pStats = QtWidgets.QWidget()
                self.pStats_widget = playerStats.Ui_playerStats()
                self.pStats_widget.setupUi(self.pStats)
                
                # self.hbox = QtGui.QHBoxLayout()
                self.psbox.addWidget(self.pStats)

                # self.playerStats.setLayout(self.hbox)

                self.gStats = QtWidgets.QWidget()
                self.graph_widget = graphs.Ui_graphs()
                self.graph_widget.setupUi(self.gStats)

                # self.hbox2 = QtGui.QHBoxLayout()
                self.gbox.addWidget(self.gStats)

                # self.graphs.setLayout(self.hbox2)

                #Declare what the buttons do
                self.graph_widget.accel.clicked.connect(self.Display_accel)
                self.graph_widget.gyro.clicked.connect(self.Display_gyro)
                self.graph_widget.mag.clicked.connect(self.Display_mag)
                self.graph_widget.pressure.clicked.connect(self.Display_pressure)
                self.count = np.arange(5000)
                self.timer = QtCore.QTimer(self.gStats)
                self.array = np.random.normal(size=5000)
                

                
                
        def Display_accel(self):
                self.lastbutton = "accel"
                self.timer.setInterval(40)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                
                
        def Display_gyro(self):
                self.lastbutton = "gyro"
                self.timer.setInterval(40)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                print("GYRO")
        def Display_mag(self):
                self.lastbutton = "mag"
                self.timer.setInterval(40)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
        def Display_pressure(self):
                self.lastbutton = "pressure"
                self.timer.setInterval(40)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)

        def Plotting(self):
                self.graph_widget.graphicsView.plot(self.count,self.array,clear=True)
                for x in range(50):
                        self.array[:-1] = self.array[1:]
                        self.array[-1]=np.random.normal()
                print(self.lastbutton)


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = mainWidgetWrapper()
        ui.setupUi(Form)
        Form.show()
        Form.setStyleSheet(open('test.qss').read())
        sys.exit(app.exec_())
    
