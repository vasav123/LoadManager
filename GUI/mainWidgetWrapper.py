
from PyQt5 import QtCore, QtGui, QtWidgets
import mainWidget
import playerStats
import recordControl
from collectData import *
import sys
import graphs
import pyqtgraph as pyg
import numpy as np

class mainWidgetWrapper(mainWidget.Ui_Form):
        lastbutton = ""
        ax_t = []
        ay_t = []
        az_t = []
        ax_b = []
        ay_b = []
        az_b = []
        fq_a = []
        fh_a = []
        gx_t = []
        gy_t = []
        gz_t = []
        gx_b = []
        gy_b = []
        gz_b = []
        knee_angle = [0]

        angle_x_t = [0]
        angle_x_b = [0]

        plotting_array = None
        size = 0
        plot = 0
        def setupUi(self,Form):
                super(mainWidget.Ui_Form, self).__init__()
                mainWidget.Ui_Form.setupUi(self,Form)
                self.pStats = QtWidgets.QWidget()
                self.pStats_widget = playerStats.Ui_playerStats()
                self.pStats_widget.setupUi(self.pStats)
                
                # self.hbox = QtGui.QHBoxLayout()
                self.playerStats.addWidget(self.pStats)

                self.record = QtWidgets.QWidget()
                self.record_widget = recordControl.Ui_recordControl()
                self.record_widget.setupUi(self.record)
                self.playerStats.addWidget(self.record)
                
                self.playerStats.setCurrentIndex(0)
                # self.playerStats.setLayout(self.hbox)

                self.gStats = QtWidgets.QWidget()
                self.graph_widget = graphs.Ui_graphs()
                self.graph_widget.setupUi(self.gStats)

                # self.hbox2 = QtGui.QHBoxLayout()
                self.gbox.addWidget(self.gStats)

                #Declare Start and Stop Recording Functions
                
                #Declare what the buttons do
                self.graph_widget.AT_X.clicked.connect(self.Display_AT_X)
                self.graph_widget.AT_Y.clicked.connect(self.Display_AT_Y)
                self.graph_widget.AT_Z.clicked.connect(self.Display_AT_Z)
                self.graph_widget.AB_X.clicked.connect(self.Display_AB_X)
                self.graph_widget.AB_Y.clicked.connect(self.Display_AB_Y)
                self.graph_widget.AB_Z.clicked.connect(self.Display_AB_Z)
                self.graph_widget.T_XY.clicked.connect(self.Display_T_XY)
                self.graph_widget.B_XY.clicked.connect(self.Display_B_XY)
                self.graph_widget.gx_t.clicked.connect(self.Display_gx_t)
                self.graph_widget.gy_t.clicked.connect(self.Display_gy_t)
                self.graph_widget.gz_t.clicked.connect(self.Display_gz_t)
                self.graph_widget.gx_b.clicked.connect(self.Display_gx_b)
                self.graph_widget.gy_b.clicked.connect(self.Display_gy_b)
                self.graph_widget.gz_b.clicked.connect(self.Display_gz_b)
                self.graph_widget.pressure_t.clicked.connect(self.Display_pressure_t)
                self.graph_widget.pressure_b.clicked.connect(self.Display_pressure_b)
                self.graph_widget.knee_angle.clicked.connect(self.Display_knee_angle)
                
                # self.count = np.arange(5000)
                self.timer = QtCore.QTimer(self.gStats)
                #self.plotting_array = self.at_a
                # np.random.normal(size=5000)

        def Display_AT_X(self):
                self.lastbutton = "Acceleration Top X"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.ax_t
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-16,16)

        def Display_AT_Y(self):
                self.lastbutton = "Acceleration Top Y"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.ay_t
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-16,16)

        def Display_AT_Z(self):
                self.lastbutton = "Acceleration Top Z"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.az_t
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-16,16)

        def Display_T_XY(self):
                self.lastbutton = "NOT COMPUTED"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.az_t
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-16,16)

        def Display_AB_X(self):
                self.lastbutton = "Acceleration Bottom X"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.ax_b
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-16,16)

        def Display_AB_Y(self):
                self.lastbutton = "Acceleration Bottom Y"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.ay_b
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-16,16)

        def Display_AB_Z(self):
                self.lastbutton = "Acceleration Bottom Z"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.az_b
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-16,16)

        def Display_B_XY(self):
                self.lastbutton = "NOT COMPUTED"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.gx_t
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-16,16)

        
        def Display_gx_t(self):
                self.lastbutton = "Gyro X Top"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.gx_t
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-180,180)
                
        def Display_gy_t(self):
                self.lastbutton = "Gyro Y Top"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.gy_t
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-180,180)

        def Display_gz_t(self):
                self.lastbutton = "Gyro Z Top"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.gz_t
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-180,180)
        def Display_gx_b(self):
                self.lastbutton = "Gyro X Bottom"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.gx_b
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-180,180)
                
        def Display_gy_b(self):
                self.lastbutton = "Gyro Y Bottom"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.gy_b
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-180,180)

        def Display_gz_b(self):
                self.lastbutton = "Gyro Z Bottom"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.gz_b
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-180,180)

        def Display_pressure_t(self):
                self.lastbutton = "Pressure Top"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.fq_a
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(0,4096)
        def Display_pressure_b(self):
                self.lastbutton = "Pressure Bottom"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.fh_a
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(0,4096)

        def Display_knee_angle(self):
                self.lastbutton = "Knee Angle"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.knee_angle
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(0,200)

        def Plotting(self):
                self.size = len(self.plotting_array)-1
                self.plot = self.size - 100
                if self.size>100:
                        self.graph_widget.graphicsView.plot(range(len(self.plotting_array[self.plot+1::])),self.plotting_array[self.plot:self.size],clear=True)
                else:
                        self.graph_widget.graphicsView.plot(range(len(self.plotting_array)),self.plotting_array,clear=True)
                # print(self.lastbutton)
                # for x in range(50):
                #         self.array[:-1] = self.array[1:]
                #         self.array[-1]=np.random.normal()


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = mainWidgetWrapper()
        ui.setupUi(Form)
        Form.show()
        Form.setStyleSheet(open('test.qss').read())
        sys.exit(app.exec_())
    
