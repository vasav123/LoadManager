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
        graphs.resize(801, 659)
        self.widget = QtWidgets.QWidget(graphs)
        self.widget.setGeometry(QtCore.QRect(11, 11, 781, 641))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = PlotWidget(self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.accel = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accel.sizePolicy().hasHeightForWidth())
        self.accel.setSizePolicy(sizePolicy)
        self.accel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.accel.setObjectName("accel")
        self.horizontalLayout.addWidget(self.accel)
        self.gyro = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gyro.sizePolicy().hasHeightForWidth())
        self.gyro.setSizePolicy(sizePolicy)
        self.gyro.setMaximumSize(QtCore.QSize(16777215, 50))
        self.gyro.setObjectName("gyro")
        self.horizontalLayout.addWidget(self.gyro)
        self.mag = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mag.sizePolicy().hasHeightForWidth())
        self.mag.setSizePolicy(sizePolicy)
        self.mag.setMaximumSize(QtCore.QSize(16777215, 50))
        self.mag.setObjectName("mag")
        self.horizontalLayout.addWidget(self.mag)
        self.pressure = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure.sizePolicy().hasHeightForWidth())
        self.pressure.setSizePolicy(sizePolicy)
        self.pressure.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pressure.setObjectName("pressure")
        self.horizontalLayout.addWidget(self.pressure)
        self.knee_angle = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.knee_angle.sizePolicy().hasHeightForWidth())
        self.knee_angle.setSizePolicy(sizePolicy)
        self.knee_angle.setMaximumSize(QtCore.QSize(16777215, 50))
        self.knee_angle.setObjectName("knee_angle")
        self.horizontalLayout.addWidget(self.knee_angle)
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
        self.knee_angle.setText(_translate("graphs", "Knee Angle"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graphs = QtWidgets.QWidget()
    ui = Ui_graphs()
    ui.setupUi(graphs)
    graphs.show()
    sys.exit(app.exec_())
