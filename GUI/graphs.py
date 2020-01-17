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
        graphs.resize(795, 664)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(graphs.sizePolicy().hasHeightForWidth())
        graphs.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(graphs)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = PlotWidget(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.accel = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accel.sizePolicy().hasHeightForWidth())
        self.accel.setSizePolicy(sizePolicy)
        self.accel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.accel.setObjectName("accel")
        self.horizontalLayout.addWidget(self.accel)
        self.gyro = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gyro.sizePolicy().hasHeightForWidth())
        self.gyro.setSizePolicy(sizePolicy)
        self.gyro.setMaximumSize(QtCore.QSize(16777215, 50))
        self.gyro.setObjectName("gyro")
        self.horizontalLayout.addWidget(self.gyro)
        self.mag = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mag.sizePolicy().hasHeightForWidth())
        self.mag.setSizePolicy(sizePolicy)
        self.mag.setMaximumSize(QtCore.QSize(16777215, 50))
        self.mag.setObjectName("mag")
        self.horizontalLayout.addWidget(self.mag)
        self.pressure = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure.sizePolicy().hasHeightForWidth())
        self.pressure.setSizePolicy(sizePolicy)
        self.pressure.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pressure.setObjectName("pressure")
        self.horizontalLayout.addWidget(self.pressure)
        self.knee_angle = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.knee_angle.sizePolicy().hasHeightForWidth())
        self.knee_angle.setSizePolicy(sizePolicy)
        self.knee_angle.setMaximumSize(QtCore.QSize(16777215, 50))
        self.knee_angle.setObjectName("knee_angle")
        self.horizontalLayout.addWidget(self.knee_angle)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

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
