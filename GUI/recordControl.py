# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recordControl.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_playerStats(object):
    def setupUi(self, playerStats):
        playerStats.setObjectName("playerStats")
        playerStats.resize(640, 630)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(playerStats.sizePolicy().hasHeightForWidth())
        playerStats.setSizePolicy(sizePolicy)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(playerStats)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame = QtWidgets.QFrame(playerStats)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Record_Label = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Record_Label.setFont(font)
        self.Record_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Record_Label.setObjectName("Record_Label")
        self.horizontalLayout_5.addWidget(self.Record_Label)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.CSV_output = QtWidgets.QTextEdit(self.groupBox_2)
        self.CSV_output.setGeometry(QtCore.QRect(10, 120, 591, 71))
        self.CSV_output.setObjectName("CSV_output")
        self.CSVname = QtWidgets.QLabel(self.groupBox_2)
        self.CSVname.setGeometry(QtCore.QRect(10, 60, 81, 51))
        self.CSVname.setObjectName("CSVname")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startRecord = QtWidgets.QPushButton(self.groupBox_5)
        self.startRecord.setObjectName("startRecord")
        self.horizontalLayout_2.addWidget(self.startRecord)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.TotalSeconds = QtWidgets.QLCDNumber(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TotalSeconds.sizePolicy().hasHeightForWidth())
        self.TotalSeconds.setSizePolicy(sizePolicy)
        self.TotalSeconds.setObjectName("TotalSeconds")
        self.horizontalLayout_3.addWidget(self.TotalSeconds)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.verticalLayout.addWidget(self.groupBox)
        self.stopRecord = QtWidgets.QPushButton(self.frame)
        self.stopRecord.setObjectName("stopRecord")
        self.verticalLayout.addWidget(self.stopRecord)
        self.horizontalLayout_8.addWidget(self.frame)

        self.retranslateUi(playerStats)
        QtCore.QMetaObject.connectSlotsByName(playerStats)

    def retranslateUi(self, playerStats):
        _translate = QtCore.QCoreApplication.translate
        playerStats.setWindowTitle(_translate("playerStats", "Form"))
        self.Record_Label.setText(_translate("playerStats", "Record To CSV"))
        self.CSVname.setText(_translate("playerStats", "CSV Name:"))
        self.startRecord.setText(_translate("playerStats", "Start Recording"))
        self.label_9.setText(_translate("playerStats", "Seconds Elapsed"))
        self.stopRecord.setText(_translate("playerStats", "Stop Recording"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    playerStats = QtWidgets.QWidget()
    ui = Ui_playerStats()
    ui.setupUi(playerStats)
    playerStats.show()
    sys.exit(app.exec_())
