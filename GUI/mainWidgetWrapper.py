
from PyQt5 import QtCore, QtGui, QtWidgets
import mainWidget
import playerStats
import graphs

class mainWidgetWrapper(mainWidget.Ui_Form):
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = mainWidgetWrapper()
    ui.setupUi(Form)
    Form.show()
    Form.setStyleSheet(open('test.qss').read())
    sys.exit(app.exec_())