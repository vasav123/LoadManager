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
        graphs.resize(1084, 848)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(graphs.sizePolicy().hasHeightForWidth())
        graphs.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(graphs)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = PlotWidget(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 650))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.a_top = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_top.sizePolicy().hasHeightForWidth())
        self.a_top.setSizePolicy(sizePolicy)
        self.a_top.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        self.a_top.setFont(font)
        self.a_top.setObjectName("a_top")
        self.horizontalLayout.addWidget(self.a_top)
        self.a_bot = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_bot.sizePolicy().hasHeightForWidth())
        self.a_bot.setSizePolicy(sizePolicy)
        self.a_bot.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        self.a_bot.setFont(font)
        self.a_bot.setObjectName("a_bot")
        self.horizontalLayout.addWidget(self.a_bot)
        self.g_bot = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_bot.sizePolicy().hasHeightForWidth())
        self.g_bot.setSizePolicy(sizePolicy)
        self.g_bot.setMinimumSize(QtCore.QSize(100, 0))
        self.g_bot.setMaximumSize(QtCore.QSize(10000, 50))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        self.g_bot.setFont(font)
        self.g_bot.setObjectName("g_bot")
        self.horizontalLayout.addWidget(self.g_bot)
        self.g_top = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_top.sizePolicy().hasHeightForWidth())
        self.g_top.setSizePolicy(sizePolicy)
        self.g_top.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        self.g_top.setFont(font)
        self.g_top.setObjectName("g_top")
        self.horizontalLayout.addWidget(self.g_top)
        self.pressure = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure.sizePolicy().hasHeightForWidth())
        self.pressure.setSizePolicy(sizePolicy)
        self.pressure.setMinimumSize(QtCore.QSize(0, 50))
        self.pressure.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        self.pressure.setFont(font)
        self.pressure.setObjectName("pressure")
        self.horizontalLayout.addWidget(self.pressure)
        self.knee_angle = QtWidgets.QPushButton(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.knee_angle.sizePolicy().hasHeightForWidth())
        self.knee_angle.setSizePolicy(sizePolicy)
        self.knee_angle.setMinimumSize(QtCore.QSize(100, 50))
        self.knee_angle.setMaximumSize(QtCore.QSize(10000, 50))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        self.knee_angle.setFont(font)
        self.knee_angle.setObjectName("knee_angle")
        self.horizontalLayout.addWidget(self.knee_angle)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ButtonPressed = QtWidgets.QLabel(graphs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonPressed.sizePolicy().hasHeightForWidth())
        self.ButtonPressed.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        self.ButtonPressed.setFont(font)
        self.ButtonPressed.setObjectName("ButtonPressed")
        self.verticalLayout.addWidget(self.ButtonPressed)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(graphs)
        QtCore.QMetaObject.connectSlotsByName(graphs)

    def retranslateUi(self, graphs):
        _translate = QtCore.QCoreApplication.translate
        graphs.setWindowTitle(_translate("graphs", "Form"))
        self.a_top.setText(_translate("graphs", "Acceleration Top"))
        self.a_bot.setText(_translate("graphs", "Accleration bottom"))
        self.g_bot.setText(_translate("graphs", "Gyro Bottom"))
        self.g_top.setText(_translate("graphs", "Gyro Top"))
        self.pressure.setText(_translate("graphs", "Pressures"))
        self.knee_angle.setText(_translate("graphs", "Knee Angles"))
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
