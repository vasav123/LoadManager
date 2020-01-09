
from PyQt5 import QtCore, QtGui, QtWidgets
import mainWidget
import playerStats
import sys
import graphs
import pyqtgraph as pyg
import numpy as np

class mainWidgetWrapper(mainWidget.Ui_Form):
        def setupUi(self,Form):
                self.count = np.arange(1000)
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
                self.rand_array_1 = np.random.normal(size=1000)
                self.rand_array_2 = np.random.normal(size=1000)

                
                
        def Display_accel(self):
                print("ACCELERATION")
                for x in range(1000):
                        self.graph_widget.graphicsView.plot(self.count,np.random.normal(size=1000),clear=True)
                        self.count=self.count+1
        def Display_gyro(self):
                self.graph_widget.graphicsView.plot(self.count,np.random.normal(size=1000),clear=True)
                self.count=self.count+1
                print("GYRO")
        def Display_mag(self):
                self.graph_widget.graphicsView.plot(self.count,np.random.normal(size=1000),clear=True)
                self.count=self.count+1
                print("MAGNET")
        def Display_pressure(self):
                self.graph_widget.graphicsView.plot(self.count,np.random.normal(size=1000),clear=True)
                self.count=self.count+1
                print("PRESSURE")

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = mainWidgetWrapper()
        ui.setupUi(Form)
        Form.show()
        Form.setStyleSheet(open('test.qss').read())
        sys.exit(app.exec_())
    
