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
        data_l = []
        plot_window = 1000  #1000*0.005 = 5 secs
        start_num_sample = 0 
        end_num_sample = 0
        def setupUi(self,Form):
                super(mainWidget.Ui_Form, self).__init__()
                mainWidget.Ui_Form.setupUi(self,Form)
                self.pStats = QtWidgets.QWidget()
                self.pStats_widget = playerStats.Ui_playerStats()
                self.pStats_widget.setupUi(self.pStats)
                self.playerStats.addWidget(self.pStats)

                self.record = QtWidgets.QWidget()
                self.record_widget = recordControl.Ui_recordControl()
                self.record_widget.setupUi(self.record)
                self.playerStats.addWidget(self.record)                
                self.playerStats.setCurrentIndex(0)
                self.gStats = QtWidgets.QWidget()
                self.graph_widget = graphs.Ui_graphs()
                self.graph_widget.setupUi(self.gStats)
                self.gbox.addWidget(self.gStats)

                #Declare Start and Stop Recording Functions
                
                #Declare what the buttons do
                self.graph_widget.a_top.clicked.connect(lambda: self.setDisplayProperties("Acceleration Top",-16,16))
                self.graph_widget.a_bot.clicked.connect(lambda: self.setDisplayProperties("Acceleration Bot",-16,16))
                self.graph_widget.g_top.clicked.connect(lambda: self.setDisplayProperties("Gyro Top",-180,180))
                self.graph_widget.g_bot.clicked.connect(lambda: self.setDisplayProperties("Gyro Bot",-180,180))
                self.graph_widget.pressure.clicked.connect(lambda: self.setDisplayProperties("Pressure",0,4096))
                self.graph_widget.knee_angle.clicked.connect(lambda: self.setDisplayProperties("Knee Angle",-200,200))
                # self.graph_widget.velocity.clicked.connect(lambda: self.setDisplayProperties("Velocity",0,20))
                self.timer = QtCore.QTimer(self.gStats)

        def setDisplayProperties(self,lbutton, lb,ub):
            self.lastbutton = lbutton
            self.graph_widget.ButtonPressed.setText(self.lastbutton)
            self.timer.setInterval(5)
            self.timer.start()
            self.timer.timeout.connect(self.Plotting)
            self.graph_widget.graphicsView.setYRange(lb,ub)

        def Plotting(self):
                plotting_array = []
                if self.lastbutton == "Acceleration Top":
                        plotting_array.append([obj.ax_t for obj in self.data_l])
                        plotting_array.append([obj.ay_t for obj in self.data_l])
                        plotting_array.append([obj.az_t for obj in self.data_l])
                elif self.lastbutton == "Acceleration Bot":
                        plotting_array.append([obj.ax_b for obj in self.data_l])
                        plotting_array.append([obj.ay_b for obj in self.data_l])
                        plotting_array.append([obj.az_b for obj in self.data_l])
                elif self.lastbutton == "Gyro Top":
                        plotting_array.append([obj.gx_t for obj in self.data_l])
                        plotting_array.append([obj.gy_t for obj in self.data_l])
                        plotting_array.append([obj.gz_t for obj in self.data_l])
                elif self.lastbutton == "Gyro Bot":
                        plotting_array.append([obj.gx_b for obj in self.data_l])
                        plotting_array.append([obj.gy_b for obj in self.data_l])
                        plotting_array.append([obj.gz_b for obj in self.data_l])
                elif self.lastbutton == "Pressure":
                        plotting_array.append([obj.fq for obj in self.data_l])
                        plotting_array.append([obj.fh for obj in self.data_l])
                elif self.lastbutton == "Knee Angle":
                        plotting_array.append([obj.flexion for obj in self.data_l])
                        plotting_array.append([obj.abduction for obj in self.data_l])
                        plotting_array.append([obj.supination for obj in self.data_l])
                elif self.lastbutton == "Velocity":
                       plotting_array.append([obj.velocity for obj in self.data_l])
                if plotting_array != [] and self.end_num_sample>self.start_num_sample:
                        time = [x * 0.005 for x in range(self.start_num_sample, self.end_num_sample)]
                        while(len(time)!=len(plotting_array[0])):   # if there is a rounding error this will take care of it
                            if (len(time)>len(plotting_array[0])):
                                    del time[-1]
                            elif (len(time)<len(plotting_array[0])):
                                    time.append(time[-1]+ 0.005)
                        # self.graph_widget.graphicsView.plot(time,plotting_array[1],clear=False)
                        self.graph_widget.graphicsView.clear()
                        colors = ['r','g','b']
                        for y_values,color in zip(plotting_array,colors):
                            my_pen = pyg.mkPen(pyg.mkColor(color))
                            self.graph_widget.graphicsView.plot(time,y_values, pen = my_pen)

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = mainWidgetWrapper()
        ui.setupUi(Form)
        Form.show()
        Form.setStyleSheet(open('test.qss').read())
        sys.exit(app.exec_())
    
