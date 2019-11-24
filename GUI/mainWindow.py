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
        MainWindow.resize(800, 600)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.page)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.kawhiButton = QtWidgets.QPushButton(self.page)
        self.kawhiButton.setObjectName("kawhiButton")
        self.verticalLayout_2.addWidget(self.kawhiButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.appWidgets.addWidget(self.page)
        self.verticalLayout.addWidget(self.appWidgets)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.appWidgets.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; text-decoration: underline;\">Load Manager</span></p></body></html>"))
        self.kawhiButton.setText(_translate("MainWindow", "Kwahi Leonard"))
        self.pushButton_2.setText(_translate("MainWindow", "Norm Powell"))
        self.pushButton_4.setText(_translate("MainWindow", "Fred VanVleet"))
        self.pushButton_6.setText(_translate("MainWindow", "Pascal Siakam"))
        self.pushButton_5.setText(_translate("MainWindow", "Kyle Lowry"))
        self.pushButton_3.setText(_translate("MainWindow", "Marc Gasol"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
