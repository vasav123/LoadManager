# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recordWidget.ui'
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
        self.widget.setMaximumSize(QtCore.QSize(99999, 50))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.back_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_2.sizePolicy().hasHeightForWidth())
        self.back_2.setSizePolicy(sizePolicy)
        self.back_2.setMaximumSize(QtCore.QSize(100, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.back_2.setFont(font)
        self.back_2.setObjectName("back_2")
        self.gridLayout.addWidget(self.back_2, 0, 0, 2, 1)
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
        self.gridLayout.addWidget(self.player, 0, 1, 2, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playerStats = QtWidgets.QFrame(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerStats.sizePolicy().hasHeightForWidth())
        self.playerStats.setSizePolicy(sizePolicy)
        self.playerStats.setMaximumSize(QtCore.QSize(375, 16777215))
        self.playerStats.setObjectName("playerStats")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.playerStats)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.psbox = QtWidgets.QHBoxLayout()
        self.psbox.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.psbox.setSpacing(9)
        self.psbox.setObjectName("psbox")
        self.horizontalLayout_7.addLayout(self.psbox)
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
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.back_2.setText(_translate("Form", "←"))
        self.player.setText(_translate("Form", "Kawhi Leonard"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
