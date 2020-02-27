
from PyQt5 import QtCore, QtGui, QtWidgets
import recordControl
import sys

class RecordWidgetWrapper(recordControl.Ui_RecordControl):
        def setupUi(self,Form):
                super(recordControl.Ui_RecordControl, self).__init__()
                recordControl.Ui_RecordControl.setupUi(self,Form)
                self.record = QtWidgets.QWidget()
                self.record_widget = recordControl.Ui_RecordControl()
                self.record_widget.setupUi(self.record)

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = RecordWidgetWrapper()
        ui.setupUi(Form)
        Form.show()
        Form.setStyleSheet(open('test.qss').read())
        sys.exit(app.exec_())   
                
