# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphs.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(566, 510)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsVie = PlotWidget(Form)
        self.graphicsVie.setObjectName("graphicsVie")
        self.verticalLayout.addWidget(self.graphicsVie)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.accel = QtWidgets.QPushButton(Form)
        self.accel.setObjectName("accel")
        self.horizontalLayout.addWidget(self.accel)
        self.gyro = QtWidgets.QPushButton(Form)
        self.gyro.setObjectName("gyro")
        self.horizontalLayout.addWidget(self.gyro)
        self.mag = QtWidgets.QPushButton(Form)
        self.mag.setObjectName("mag")
        self.horizontalLayout.addWidget(self.mag)
        self.pressure = QtWidgets.QPushButton(Form)
        self.pressure.setObjectName("pressure")
        self.horizontalLayout.addWidget(self.pressure)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.accel.setText(_translate("Form", "Accelormeter"))
        self.gyro.setText(_translate("Form", "Gyroscope"))
        self.mag.setText(_translate("Form", "Magnetometer"))
        self.pressure.setText(_translate("Form", "Pressure"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
