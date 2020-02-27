
from PyQt5 import QtCore, QtGui, QtWidgets
import mainWidget
import recordControl
import sys
import graphs
import pyqtgraph as pyg
import numpy as np

class RecordWidgetWrapper(mainWidget.Ui_Form):
        def setupUi(self,Form):
                super(mainWidget.Ui_Form, self).__init__()
                mainWidget.Ui_Form.setupUi(self,Form)
                self.record = QtWidgets.QWidget()
                self.record_widget = recordControl.Ui_RecordControl()
                self.record_widget.setupUi(self.record)
                
                # self.hbox = QtGui.QHBoxLayout()
                self.psbox.addWidget(self.record)

                # self.playerStats.setLayout(self.hbox)

                self.gStats = QtWidgets.QWidget()
                self.graph_widget = graphs.Ui_graphs()
                self.graph_widget.setupUi(self.gStats)

                # self.hbox2 = QtGui.QHBoxLayout()
                self.gbox.addWidget(self.gStats)

                # self.graphs.setLayout(self.hbox2)

                #Declare what the buttons do
                               
                # self.count = np.arange(5000)
                self.timer = QtCore.QTimer(self.gStats)
                # np.random.normal(size=5000)


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = RecordWidgetWrapper()
        ui.setupUi(Form)
        Form.show()
        Form.setStyleSheet(open('test.qss').read())
        sys.exit(app.exec_())   
                
