# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recordControl.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_recordControl(object):
    def setupUi(self, recordControl):
        recordControl.setObjectName("recordControl")
        recordControl.resize(310, 873)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(recordControl.sizePolicy().hasHeightForWidth())
        recordControl.setSizePolicy(sizePolicy)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(recordControl)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame = QtWidgets.QFrame(recordControl)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.TotalSeconds = QtWidgets.QLCDNumber(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TotalSeconds.sizePolicy().hasHeightForWidth())
        self.TotalSeconds.setSizePolicy(sizePolicy)
        self.TotalSeconds.setObjectName("TotalSeconds")
        self.gridLayout.addWidget(self.TotalSeconds, 6, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 1, 1, 1)
        self.startRecord = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        self.startRecord.setFont(font)
        self.startRecord.setObjectName("startRecord")
        self.gridLayout.addWidget(self.startRecord, 3, 0, 1, 2)
        self.stopRecord = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        self.stopRecord.setFont(font)
        self.stopRecord.setObjectName("stopRecord")
        self.gridLayout.addWidget(self.stopRecord, 4, 0, 1, 2)
        self.CSV_output = QtWidgets.QTextEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CSV_output.sizePolicy().hasHeightForWidth())
        self.CSV_output.setSizePolicy(sizePolicy)
        self.CSV_output.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.CSV_output.setFont(font)
        self.CSV_output.setObjectName("CSV_output")
        self.gridLayout.addWidget(self.CSV_output, 2, 0, 1, 2)
        self.Record_Label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Record_Label.setFont(font)
        self.Record_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Record_Label.setObjectName("Record_Label")
        self.gridLayout.addWidget(self.Record_Label, 0, 0, 1, 2)
        self.CSVname = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.CSVname.setFont(font)
        self.CSVname.setObjectName("CSVname")
        self.gridLayout.addWidget(self.CSVname, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_2.addWidget(self.lcdNumber, 1, 1, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setMaximum(250)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout_2.addWidget(self.lcdNumber_2, 3, 1, 1, 1)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider_2.setMaximum(1500)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setInvertedAppearance(False)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout_2.addWidget(self.horizontalSlider_2, 4, 0, 1, 2)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout_2.addWidget(self.lcdNumber_3, 5, 1, 1, 1)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setInvertedAppearance(False)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout_2.addWidget(self.horizontalSlider_3, 6, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_8.addWidget(self.frame)

        self.retranslateUi(recordControl)
        QtCore.QMetaObject.connectSlotsByName(recordControl)

    def retranslateUi(self, recordControl):
        _translate = QtCore.QCoreApplication.translate
        recordControl.setWindowTitle(_translate("recordControl", "Form"))
        self.label_9.setText(_translate("recordControl", "Seconds Elapsed Recording "))
        self.startRecord.setText(_translate("recordControl", "Start Recording"))
        self.stopRecord.setText(_translate("recordControl", "Stop Recording"))
        self.Record_Label.setText(_translate("recordControl", "Record To CSV"))
        self.CSVname.setText(_translate("recordControl", "File Name: "))
        self.label_3.setText(_translate("recordControl", "Weigth"))
        self.label_2.setText(_translate("recordControl", "Heigth"))
        self.label_4.setText(_translate("recordControl", "Max Score"))
        self.label.setText(_translate("recordControl", "Player Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    recordControl = QtWidgets.QWidget()
    ui = Ui_recordControl()
    ui.setupUi(recordControl)
    recordControl.show()
    sys.exit(app.exec_())
