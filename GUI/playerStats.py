# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playerStats.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_playerStats(object):
    def setupUi(self, playerStats):
        playerStats.setObjectName("playerStats")
        playerStats.resize(413, 897)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(playerStats.sizePolicy().hasHeightForWidth())
        playerStats.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QtWidgets.QGridLayout(playerStats)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(playerStats)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.NumSprint = QtWidgets.QLCDNumber(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumSprint.sizePolicy().hasHeightForWidth())
        self.NumSprint.setSizePolicy(sizePolicy)
        self.NumSprint.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.NumSprint.setObjectName("NumSprint")
        self.gridLayout_3.addWidget(self.NumSprint, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 1, 1, 1)
        self.NumRun = QtWidgets.QLCDNumber(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumRun.sizePolicy().hasHeightForWidth())
        self.NumRun.setSizePolicy(sizePolicy)
        self.NumRun.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.NumRun.setObjectName("NumRun")
        self.gridLayout_3.addWidget(self.NumRun, 1, 0, 1, 1)
        self.NumWalk = QtWidgets.QLCDNumber(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumWalk.sizePolicy().hasHeightForWidth())
        self.NumWalk.setSizePolicy(sizePolicy)
        self.NumWalk.setStyleSheet("border: none;\n"
"")
        self.NumWalk.setObjectName("NumWalk")
        self.gridLayout_3.addWidget(self.NumWalk, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 5, 0, 1, 2)
        self.percentPlayed = QtWidgets.QProgressBar(playerStats)
        self.percentPlayed.setProperty("value", 0)
        self.percentPlayed.setObjectName("percentPlayed")
        self.gridLayout_4.addWidget(self.percentPlayed, 7, 0, 1, 2)
        self.label_15 = QtWidgets.QLabel(playerStats)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 8, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(playerStats)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 6, 0, 1, 2)
        self.groupBox_8 = QtWidgets.QGroupBox(playerStats)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox_8)
        self.lcdNumber_2.setStyleSheet("border:none;")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout_2.addWidget(self.lcdNumber_2, 2, 0, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_8)
        self.lcdNumber.setStyleSheet("border:none;")
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_2.addWidget(self.lcdNumber, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 1, 1, 1)
        self.jumpHeight = QtWidgets.QLCDNumber(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jumpHeight.sizePolicy().hasHeightForWidth())
        self.jumpHeight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.jumpHeight.setFont(font)
        self.jumpHeight.setStyleSheet("border:none;")
        self.jumpHeight.setObjectName("jumpHeight")
        self.gridLayout_2.addWidget(self.jumpHeight, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 1, 1, 1)
        self.jumpHeight_2 = QtWidgets.QLCDNumber(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jumpHeight_2.sizePolicy().hasHeightForWidth())
        self.jumpHeight_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(6)
        self.jumpHeight_2.setFont(font)
        self.jumpHeight_2.setStyleSheet("border:none;")
        self.jumpHeight_2.setLineWidth(1)
        self.jumpHeight_2.setObjectName("jumpHeight_2")
        self.gridLayout_2.addWidget(self.jumpHeight_2, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_8, 1, 0, 1, 2)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(playerStats)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout_4.addWidget(self.lcdNumber_4, 8, 1, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(playerStats)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.NumMinutes = QtWidgets.QLCDNumber(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumMinutes.sizePolicy().hasHeightForWidth())
        self.NumMinutes.setSizePolicy(sizePolicy)
        self.NumMinutes.setStyleSheet("border:none;")
        self.NumMinutes.setObjectName("NumMinutes")
        self.gridLayout.addWidget(self.NumMinutes, 2, 0, 1, 1)
        self.NumJumps = QtWidgets.QLCDNumber(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumJumps.sizePolicy().hasHeightForWidth())
        self.NumJumps.setSizePolicy(sizePolicy)
        self.NumJumps.setStyleSheet("border:none;")
        self.NumJumps.setObjectName("NumJumps")
        self.gridLayout.addWidget(self.NumJumps, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.NumSteps = QtWidgets.QLCDNumber(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumSteps.sizePolicy().hasHeightForWidth())
        self.NumSteps.setSizePolicy(sizePolicy)
        self.NumSteps.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.NumSteps.setObjectName("NumSteps")
        self.gridLayout.addWidget(self.NumSteps, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.Score = QtWidgets.QLCDNumber(self.groupBox_7)
        self.Score.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Score.setObjectName("Score")
        self.gridLayout.addWidget(self.Score, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_7, 3, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(playerStats)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 2, 0, 1, 2)
        self.TimeSpentLabel = QtWidgets.QLabel(playerStats)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TimeSpentLabel.sizePolicy().hasHeightForWidth())
        self.TimeSpentLabel.setSizePolicy(sizePolicy)
        self.TimeSpentLabel.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.TimeSpentLabel.setFont(font)
        self.TimeSpentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TimeSpentLabel.setObjectName("TimeSpentLabel")
        self.gridLayout_4.addWidget(self.TimeSpentLabel, 4, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(playerStats)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 2)

        self.retranslateUi(playerStats)
        QtCore.QMetaObject.connectSlotsByName(playerStats)

    def retranslateUi(self, playerStats):
        _translate = QtCore.QCoreApplication.translate
        playerStats.setWindowTitle(_translate("playerStats", "Form"))
        self.label_7.setText(_translate("playerStats", "Running"))
        self.label_8.setText(_translate("playerStats", "Jogging"))
        self.label_9.setText(_translate("playerStats", "Walking"))
        self.label_15.setText(_translate("playerStats", "Calories Burned"))
        self.label_14.setText(_translate("playerStats", "Percent Played"))
        self.label_11.setText(_translate("playerStats", "Supination"))
        self.label_4.setText(_translate("playerStats", "Jump Height (In)"))
        self.label_10.setText(_translate("playerStats", "Abduction"))
        self.label_6.setText(_translate("playerStats", "Flexion"))
        self.label.setText(_translate("playerStats", "Steps            "))
        self.label_5.setText(_translate("playerStats", "Minutes"))
        self.label_2.setText(_translate("playerStats", "Jumps           "))
        self.label_3.setText(_translate("playerStats", "Score"))
        self.label_13.setText(_translate("playerStats", "Activity Tracker"))
        self.TimeSpentLabel.setText(_translate("playerStats", "Type of Steps"))
        self.label_12.setText(_translate("playerStats", "Max Values"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    playerStats = QtWidgets.QWidget()
    ui = Ui_playerStats()
    ui.setupUi(playerStats)
    playerStats.show()
    sys.exit(app.exec_())
