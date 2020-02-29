
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
        at_a = []
        ab_a = []
        fq_a = []
        fh_a = []
        yt_a = []
        pt_a = []
        rt_a = []
        yb_a = []
        pb_a = []
        rb_a = []
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
                self.graph_widget.accel_t.clicked.connect(self.Display_accel_t)
                self.graph_widget.accel_b.clicked.connect(self.Display_accel_b)
                self.graph_widget.yaw_t.clicked.connect(self.Display_yaw_t)
                self.graph_widget.yaw_b.clicked.connect(self.Display_yaw_b)
                self.graph_widget.pitch_t.clicked.connect(self.Display_pitch_t)
                self.graph_widget.pitch_b.clicked.connect(self.Display_pitch_b)
                self.graph_widget.roll_t.clicked.connect(self.Display_roll_t)
                self.graph_widget.roll_b.clicked.connect(self.Display_roll_b)
                self.graph_widget.pressure_t.clicked.connect(self.Display_pressure_t)
                self.graph_widget.pressure_b.clicked.connect(self.Display_pressure_b)
                self.graph_widget.knee_angle.clicked.connect(self.Display_knee_angle)
                
                # self.count = np.arange(5000)
                self.timer = QtCore.QTimer(self.gStats)
                self.plotting_array = self.at_a
                # np.random.normal(size=5000)
                
                
        def Display_accel_t(self):
                self.lastbutton = "Acceleration Top"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.at_a
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(0,5)
                
        def Display_accel_b(self):
                self.lastbutton = "Acceleration Bottom"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.ab_a
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(0,5)

        def Display_yaw_t(self):
                self.lastbutton = "Yaw Top"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.yt_a
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-180,180)
                
        def Display_yaw_b(self):
                self.lastbutton = "Yaw Bottom"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.yb_a
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-180,180)

        def Display_pitch_t(self):
                self.lastbutton = "Pitch Top"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.pt_a
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-180,180)
        def Display_pitch_b(self):
                self.lastbutton = "Pitch Bottom"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.pb_a
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-180,180)

        def Display_roll_t(self):
                self.lastbutton = "Roll Top"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.rt_a
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(-180,180)
        def Display_roll_b(self):
                self.lastbutton = "Roll Bottom"
                self.graph_widget.ButtonPressed.setText(self.lastbutton)
                self.plotting_array = self.rb_a
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
                self.plotting_array = self.fq_a
                self.timer.setInterval(5)
                self.timer.start()
                self.timer.timeout.connect(self.Plotting)
                #Set Axis Range
                self.graph_widget.graphicsView.setYRange(0,120)

        def Plotting(self):
                self.size = len(self.plotting_array)-1
                self.plot = self.size - 100
                if self.size>100:
                        self.graph_widget.graphicsView.plot(range(len(self.plotting_array[self.plot:self.size])),self.plotting_array[self.plot:self.size],clear=True)
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
    
