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
        graphs.resize(1100, 848)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(graphs.sizePolicy().hasHeightForWidth())
        graphs.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(graphs)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.graphicsView = PlotWidget(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_8.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AT_X = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AT_X.sizePolicy().hasHeightForWidth())
        self.AT_X.setSizePolicy(sizePolicy)
        self.AT_X.setMaximumSize(QtCore.QSize(16777215, 50))
        self.AT_X.setObjectName("AT_X")
        self.verticalLayout.addWidget(self.AT_X)
        self.AT_Y = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AT_Y.sizePolicy().hasHeightForWidth())
        self.AT_Y.setSizePolicy(sizePolicy)
        self.AT_Y.setMaximumSize(QtCore.QSize(16777215, 50))
        self.AT_Y.setObjectName("AT_Y")
        self.verticalLayout.addWidget(self.AT_Y)
        self.T_XY = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_XY.sizePolicy().hasHeightForWidth())
        self.T_XY.setSizePolicy(sizePolicy)
        self.T_XY.setMaximumSize(QtCore.QSize(16777215, 50))
        self.T_XY.setObjectName("T_XY")
        self.verticalLayout.addWidget(self.T_XY)
        self.AT_Z = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AT_Z.sizePolicy().hasHeightForWidth())
        self.AT_Z.setSizePolicy(sizePolicy)
        self.AT_Z.setMaximumSize(QtCore.QSize(16777215, 50))
        self.AT_Z.setObjectName("AT_Z")
        self.verticalLayout.addWidget(self.AT_Z)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.AB_X = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AB_X.sizePolicy().hasHeightForWidth())
        self.AB_X.setSizePolicy(sizePolicy)
        self.AB_X.setMaximumSize(QtCore.QSize(16777215, 50))
        self.AB_X.setObjectName("AB_X")
        self.verticalLayout_5.addWidget(self.AB_X)
        self.AB_Y = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AB_Y.sizePolicy().hasHeightForWidth())
        self.AB_Y.setSizePolicy(sizePolicy)
        self.AB_Y.setMaximumSize(QtCore.QSize(16777215, 50))
        self.AB_Y.setObjectName("AB_Y")
        self.verticalLayout_5.addWidget(self.AB_Y)
        self.B_XY = QtWidgets.QPushButton(graphs)
        self.B_XY.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B_XY.sizePolicy().hasHeightForWidth())
        self.B_XY.setSizePolicy(sizePolicy)
        self.B_XY.setMaximumSize(QtCore.QSize(16777215, 50))
        self.B_XY.setObjectName("B_XY")
        self.verticalLayout_5.addWidget(self.B_XY)
        self.AB_Z = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AB_Z.sizePolicy().hasHeightForWidth())
        self.AB_Z.setSizePolicy(sizePolicy)
        self.AB_Z.setMaximumSize(QtCore.QSize(16777215, 50))
        self.AB_Z.setObjectName("AB_Z")
        self.verticalLayout_5.addWidget(self.AB_Z)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.yaw_t = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yaw_t.sizePolicy().hasHeightForWidth())
        self.yaw_t.setSizePolicy(sizePolicy)
        self.yaw_t.setMaximumSize(QtCore.QSize(16777215, 50))
        self.yaw_t.setObjectName("yaw_t")
        self.verticalLayout_2.addWidget(self.yaw_t)
        self.pitch_t = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pitch_t.sizePolicy().hasHeightForWidth())
        self.pitch_t.setSizePolicy(sizePolicy)
        self.pitch_t.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pitch_t.setObjectName("pitch_t")
        self.verticalLayout_2.addWidget(self.pitch_t)
        self.roll_t = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roll_t.sizePolicy().hasHeightForWidth())
        self.roll_t.setSizePolicy(sizePolicy)
        self.roll_t.setMaximumSize(QtCore.QSize(16777215, 50))
        self.roll_t.setObjectName("roll_t")
        self.verticalLayout_2.addWidget(self.roll_t)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.yaw_b = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yaw_b.sizePolicy().hasHeightForWidth())
        self.yaw_b.setSizePolicy(sizePolicy)
        self.yaw_b.setMaximumSize(QtCore.QSize(16777215, 50))
        self.yaw_b.setObjectName("yaw_b")
        self.verticalLayout_3.addWidget(self.yaw_b)
        self.pitch_b = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pitch_b.sizePolicy().hasHeightForWidth())
        self.pitch_b.setSizePolicy(sizePolicy)
        self.pitch_b.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pitch_b.setObjectName("pitch_b")
        self.verticalLayout_3.addWidget(self.pitch_b)
        self.roll_b = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roll_b.sizePolicy().hasHeightForWidth())
        self.roll_b.setSizePolicy(sizePolicy)
        self.roll_b.setMaximumSize(QtCore.QSize(16777215, 50))
        self.roll_b.setObjectName("roll_b")
        self.verticalLayout_3.addWidget(self.roll_b)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pressure_t = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure_t.sizePolicy().hasHeightForWidth())
        self.pressure_t.setSizePolicy(sizePolicy)
        self.pressure_t.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pressure_t.setObjectName("pressure_t")
        self.verticalLayout_7.addWidget(self.pressure_t)
        self.pressure_b = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure_b.sizePolicy().hasHeightForWidth())
        self.pressure_b.setSizePolicy(sizePolicy)
        self.pressure_b.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pressure_b.setObjectName("pressure_b")
        self.verticalLayout_7.addWidget(self.pressure_b)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem)
        self.knee_angle = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.knee_angle.sizePolicy().hasHeightForWidth())
        self.knee_angle.setSizePolicy(sizePolicy)
        self.knee_angle.setMaximumSize(QtCore.QSize(16777215, 50))
        self.knee_angle.setObjectName("knee_angle")
        self.verticalLayout_6.addWidget(self.knee_angle)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.ButtonPressed = QtWidgets.QLabel(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonPressed.sizePolicy().hasHeightForWidth())
        self.ButtonPressed.setSizePolicy(sizePolicy)
        self.ButtonPressed.setObjectName("ButtonPressed")
        self.verticalLayout_4.addWidget(self.ButtonPressed)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.retranslateUi(graphs)
        QtCore.QMetaObject.connectSlotsByName(graphs)

    def retranslateUi(self, graphs):
        _translate = QtCore.QCoreApplication.translate
        graphs.setWindowTitle(_translate("graphs", "Form"))
        self.AT_X.setText(_translate("graphs", "AT X"))
        self.AT_Y.setText(_translate("graphs", "AT Y"))
        self.T_XY.setText(_translate("graphs", "Top Magnitude X Y"))
        self.AT_Z.setText(_translate("graphs", "AT Z"))
        self.AB_X.setText(_translate("graphs", "AB X"))
        self.AB_Y.setText(_translate("graphs", "AB Y"))
        self.B_XY.setText(_translate("graphs", "Bottom Magnitude X Y"))
        self.AB_Z.setText(_translate("graphs", "AB Z"))
        self.yaw_t.setText(_translate("graphs", "Yaw Top"))
        self.pitch_t.setText(_translate("graphs", "Pitch Top"))
        self.roll_t.setText(_translate("graphs", "Roll Top"))
        self.yaw_b.setText(_translate("graphs", "Yaw Bottom"))
        self.pitch_b.setText(_translate("graphs", "Pitch Bottom"))
        self.roll_b.setText(_translate("graphs", "Roll Bottom"))
        self.pressure_t.setText(_translate("graphs", "Pressure Top"))
        self.pressure_b.setText(_translate("graphs", "Pressure Bottom"))
        self.knee_angle.setText(_translate("graphs", "Knee Angle"))
        self.label.setText(_translate("graphs", "Last Button Pressed:"))
        self.ButtonPressed.setText(_translate("graphs", "No Button Pressed"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    graphs = QtWidgets.QWidget()
    ui = Ui_graphs()
    ui.setupUi(graphs)
    graphs.show()
    sys.exit(app.exec_())
