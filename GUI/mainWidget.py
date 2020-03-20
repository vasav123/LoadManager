# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1211, 798)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setEnabled(True)
        self.widget.setMaximumSize(QtCore.QSize(99999, 70))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setMaximumSize(QtCore.QSize(100, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back)
        self.player = QtWidgets.QLabel(self.widget)
        self.player.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player.sizePolicy().hasHeightForWidth())
        self.player.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.player.setFont(font)
        self.player.setAlignment(QtCore.Qt.AlignCenter)
        self.player.setObjectName("player")
        self.horizontalLayout.addWidget(self.player)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.plotSlider = QtWidgets.QSlider(self.widget)
        self.plotSlider.setMinimum(100)
        self.plotSlider.setMaximum(1000)
        self.plotSlider.setProperty("value", 500)
        self.plotSlider.setOrientation(QtCore.Qt.Horizontal)
        self.plotSlider.setObjectName("plotSlider")
        self.verticalLayout_2.addWidget(self.plotSlider)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.Record = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Record.sizePolicy().hasHeightForWidth())
        self.Record.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Record.setFont(font)
        self.Record.setObjectName("Record")
        self.horizontalLayout.addWidget(self.Record)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playerStats = QtWidgets.QStackedWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerStats.sizePolicy().hasHeightForWidth())
        self.playerStats.setSizePolicy(sizePolicy)
        self.playerStats.setMaximumSize(QtCore.QSize(350, 16777215))
        self.playerStats.setObjectName("playerStats")
        self.horizontalLayout_2.addWidget(self.playerStats)
        self.graphs = QtWidgets.QFrame(self.widget_2)
        self.graphs.setObjectName("graphs")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.graphs)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.gbox = QtWidgets.QHBoxLayout()
        self.gbox.setSpacing(0)
        self.gbox.setObjectName("gbox")
        self.horizontalLayout_8.addLayout(self.gbox)
        self.horizontalLayout_2.addWidget(self.graphs)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        self.playerStats.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.back.setText(_translate("Form", "←"))
        self.player.setText(_translate("Form", "Kawhi Leonard"))
        self.label.setText(_translate("Form", "Plot Length:"))
        self.Record.setText(_translate("Form", "Record"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
