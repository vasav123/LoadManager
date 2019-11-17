# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(778, 550)
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        self.Home = QtWidgets.QPushButton(widget)
        self.Home.setObjectName("Home")
        self.gridLayout.addWidget(self.Home, 0, 0, 1, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.Home.setText(_translate("widget", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
