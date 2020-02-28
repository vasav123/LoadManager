
from PyQt5 import QtCore, QtGui, QtWidgets
import recordWidget
import recordControl
import graphs
import sys

class RecordWidgetWrapper(recordWidget.Ui_Form):
        def setupUi(self,Form):
                super(recordWidget.Ui_Form, self).__init__()
                recordWidget.Ui_Form.setupUi(self,Form)
                self.record = QtWidgets.QWidget()
                self.record_widget = recordControl.Ui_recordControl()
                self.record_widget.setupUi(self.record)

                self.psbox.addWidget(self.record)

                self.gStats = QtWidgets.QWidget()
                self.graph_widget = graphs.Ui_graphs()
                self.graph_widget.setupUi(self.gStats)

                self.gbox.addWidget(self.gStats)

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = RecordWidgetWrapper()
        ui.setupUi(Form)
        Form.show()
        Form.setStyleSheet(open('test.qss').read())
        sys.exit(app.exec_())   
                
