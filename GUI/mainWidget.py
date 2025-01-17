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
        Form.resize(1211, 797)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(99999, 100))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy)
        self.back.setMinimumSize(QtCore.QSize(150, 60))
        self.back.setMaximumSize(QtCore.QSize(90, 60))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("")
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back, 0, QtCore.Qt.AlignLeft)
        self.player = QtWidgets.QLabel(self.widget)
        self.player.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player.sizePolicy().hasHeightForWidth())
        self.player.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(55)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.player.setFont(font)
        self.player.setStyleSheet("font: 75 55pt \"Bitstream Vera Sans\";\n"
"font-weight: bold;\n"
"qproperty-alignment: AlignCenter;")
        self.player.setAlignment(QtCore.Qt.AlignCenter)
        self.player.setObjectName("player")
        self.horizontalLayout.addWidget(self.player, 0, QtCore.Qt.AlignHCenter)
        self.Settings = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Settings.sizePolicy().hasHeightForWidth())
        self.Settings.setSizePolicy(sizePolicy)
        self.Settings.setMinimumSize(QtCore.QSize(150, 60))
        self.Settings.setMaximumSize(QtCore.QSize(9999, 60))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Settings.setFont(font)
        self.Settings.setAutoDefault(False)
        self.Settings.setDefault(False)
        self.Settings.setFlat(False)
        self.Settings.setObjectName("Settings")
        self.horizontalLayout.addWidget(self.Settings, 0, QtCore.Qt.AlignRight)
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
        self.back.setText(_translate("Form", "⬅️"))
        self.player.setText(_translate("Form", "Kawhi Leonard"))
        self.Settings.setText(_translate("Form", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
