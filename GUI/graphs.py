# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphs.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_graphs(object):
    def setupUi(self, graphs):
        graphs.setObjectName("graphs")
        graphs.resize(566, 510)
        self.verticalLayout = QtWidgets.QVBoxLayout(graphs)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = PlotWidget(graphs)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.accel = QtWidgets.QPushButton(graphs)
        self.accel.setObjectName("accel")
        self.horizontalLayout.addWidget(self.accel)
        self.gyro = QtWidgets.QPushButton(graphs)
        self.gyro.setObjectName("gyro")
        self.horizontalLayout.addWidget(self.gyro)
        self.mag = QtWidgets.QPushButton(graphs)
        self.mag.setObjectName("mag")
        self.horizontalLayout.addWidget(self.mag)
        self.pressure = QtWidgets.QPushButton(graphs)
        self.pressure.setObjectName("pressure")
        self.horizontalLayout.addWidget(self.pressure)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(graphs)
        QtCore.QMetaObject.connectSlotsByName(graphs)

    def retranslateUi(self, graphs):
        _translate = QtCore.QCoreApplication.translate
        graphs.setWindowTitle(_translate("graphs", "Form"))
        self.accel.setText(_translate("graphs", "Accelormeter"))
        self.gyro.setText(_translate("graphs", "Gyroscope"))
        self.mag.setText(_translate("graphs", "Magnetometer"))
        self.pressure.setText(_translate("graphs", "Pressure"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graphs = QtWidgets.QWidget()
    ui = Ui_graphs()
    ui.setupUi(graphs)
    graphs.show()
    sys.exit(app.exec_())
