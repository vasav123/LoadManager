# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1830, 1002)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.appWidgets = QtWidgets.QStackedWidget(self.centralwidget)
        self.appWidgets.setEnabled(True)
        self.appWidgets.setObjectName("appWidgets")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout = QtWidgets.QGridLayout(self.page)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(600, 436))
        self.pushButton_6.setMaximumSize(QtCore.QSize(600, 436))
        self.pushButton_6.setStyleSheet("qproperty-icon:url(); /* empty image */\n"
"qproperty-iconSize: 16px 16px; /* space for the background image*/\n"
"background-image: url(\"Images/Pascal.png\") 0 0 0 0 stretch stretch;\n"
"background-repeat: no-repeat;\n"
"\n"
"")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 5, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(600, 436))
        self.pushButton_5.setMaximumSize(QtCore.QSize(600, 436))
        self.pushButton_5.setStyleSheet("qproperty-icon:url(); /* empty image */\n"
"qproperty-iconSize: 16px 16px; /* space for the background image*/\n"
"background-image: url(\"Images/Kyle.png\") 0 0 0 0 stretch stretch;\n"
"background-repeat: no-repeat;\n"
"\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 5, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(600, 436))
        self.pushButton_4.setMaximumSize(QtCore.QSize(600, 436))
        self.pushButton_4.setStyleSheet("qproperty-icon:url(); /* empty image */\n"
"qproperty-iconSize: 16px 16px; /* space for the background image*/\n"
"background-image: url(\"Images/Freddy.png\") 0 0 0 0 stretch stretch;\n"
"background-repeat: no-repeat;\n"
"\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(600, 436))
        self.pushButton_2.setMaximumSize(QtCore.QSize(600, 436))
        self.pushButton_2.setStyleSheet("qproperty-icon:url(); /* empty image */\n"
"qproperty-iconSize: 16px 16px; /* space for the background image*/\n"
"background-image: url(\"Images/Norm.png\") 0 0 0 0 stretch stretch;\n"
"background-repeat: no-repeat;\n"
"\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setStyleSheet("font: 75 60pt \"Bitstream Vera Sans\";\n"
"font-weight: bold;\n"
"qproperty-alignment: AlignCenter;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 3)
        self.kawhiButton = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kawhiButton.sizePolicy().hasHeightForWidth())
        self.kawhiButton.setSizePolicy(sizePolicy)
        self.kawhiButton.setMinimumSize(QtCore.QSize(600, 436))
        self.kawhiButton.setMaximumSize(QtCore.QSize(600, 436))
        self.kawhiButton.setStyleSheet("qproperty-icon:url(); /* empty image */\n"
"qproperty-iconSize: 16px 16px; /* space for the background image*/\n"
"background-image: url(\"Images/Kawhi.png\") ;\n"
"background-repeat: no-repeat;\n"
"\n"
"")
        self.kawhiButton.setText("")
        self.kawhiButton.setObjectName("kawhiButton")
        self.gridLayout.addWidget(self.kawhiButton, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(600, 436))
        self.pushButton_3.setMaximumSize(QtCore.QSize(600, 436))
        self.pushButton_3.setStyleSheet("qproperty-icon:url(); /* empty image */\n"
"qproperty-iconSize: 16px 16px; /* space for the background image*/\n"
"background-image: url(\"Images/Marc.png\") 0 0 0 0 stretch stretch;\n"
"background-repeat: no-repeat;\n"
"\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 5, 3, 1, 1)
        self.appWidgets.addWidget(self.page)
        self.verticalLayout.addWidget(self.appWidgets)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.appWidgets.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Load Manager"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
