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
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.NumJumps = QtWidgets.QLCDNumber(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumJumps.sizePolicy().hasHeightForWidth())
        self.NumJumps.setSizePolicy(sizePolicy)
        self.NumJumps.setObjectName("NumJumps")
        self.horizontalLayout_7.addWidget(self.NumJumps)
        self.label_2 = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.groupBox_7)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.NumSteps = QtWidgets.QLCDNumber(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumSteps.sizePolicy().hasHeightForWidth())
        self.NumSteps.setSizePolicy(sizePolicy)
        self.NumSteps.setObjectName("NumSteps")
        self.horizontalLayout_6.addWidget(self.NumSteps)
        self.label = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.NumMinutes = QtWidgets.QLCDNumber(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumMinutes.sizePolicy().hasHeightForWidth())
        self.NumMinutes.setSizePolicy(sizePolicy)
        self.NumMinutes.setObjectName("NumMinutes")
        self.horizontalLayout_5.addWidget(self.NumMinutes)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.NumImpacts = QtWidgets.QLCDNumber(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumImpacts.sizePolicy().hasHeightForWidth())
        self.NumImpacts.setSizePolicy(sizePolicy)
        self.NumImpacts.setObjectName("NumImpacts")
        self.horizontalLayout_4.addWidget(self.NumImpacts)
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.TimeSpentLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TimeSpentLabel.setFont(font)
        self.TimeSpentLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TimeSpentLabel.setObjectName("TimeSpentLabel")
        self.verticalLayout.addWidget(self.TimeSpentLabel)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.NumRun = QtWidgets.QLCDNumber(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumRun.sizePolicy().hasHeightForWidth())
        self.NumRun.setSizePolicy(sizePolicy)
        self.NumRun.setObjectName("NumRun")
        self.horizontalLayout.addWidget(self.NumRun)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.NumSprint = QtWidgets.QLCDNumber(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumSprint.sizePolicy().hasHeightForWidth())
        self.NumSprint.setSizePolicy(sizePolicy)
        self.NumSprint.setObjectName("NumSprint")
        self.horizontalLayout_2.addWidget(self.NumSprint)
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
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
        self.NumWalk = QtWidgets.QLCDNumber(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NumWalk.sizePolicy().hasHeightForWidth())
        self.NumWalk.setSizePolicy(sizePolicy)
        self.NumWalk.setObjectName("NumWalk")
        self.horizontalLayout_3.addWidget(self.NumWalk)
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
        self.ProgressbarLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ProgressbarLabel.setFont(font)
        self.ProgressbarLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ProgressbarLabel.setObjectName("ProgressbarLabel")
        self.verticalLayout.addWidget(self.ProgressbarLabel)
        self.LoadPercent = QtWidgets.QProgressBar(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadPercent.sizePolicy().hasHeightForWidth())
        self.LoadPercent.setSizePolicy(sizePolicy)
        self.LoadPercent.setMinimumSize(QtCore.QSize(100, 10))
        self.LoadPercent.setMaximumSize(QtCore.QSize(450, 40))
        self.LoadPercent.setBaseSize(QtCore.QSize(1200, 10))
        self.LoadPercent.setProperty("value", 24)
        self.LoadPercent.setFormat("")
        self.LoadPercent.setObjectName("LoadPercent")
        self.verticalLayout.addWidget(self.LoadPercent)
        self.horizontalLayout_8.addWidget(self.frame)

        self.retranslateUi(playerStats)
        QtCore.QMetaObject.connectSlotsByName(playerStats)

    def retranslateUi(self, playerStats):
        _translate = QtCore.QCoreApplication.translate
        playerStats.setWindowTitle(_translate("playerStats", "Form"))
        self.label_2.setText(_translate("playerStats", "Jumps           "))
        self.label.setText(_translate("playerStats", "Steps            "))
        self.label_5.setText(_translate("playerStats", "Minutes"))
        self.label_3.setText(_translate("playerStats", "High Acceleration Impacts"))
        self.TimeSpentLabel.setText(_translate("playerStats", "Type of Step:"))
        self.label_7.setText(_translate("playerStats", "Running"))
        self.label_8.setText(_translate("playerStats", "Sprinting"))
        self.label_9.setText(_translate("playerStats", "Walking"))
        self.ProgressbarLabel.setText(_translate("playerStats", "Percentage Of Limit Played"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    playerStats = QtWidgets.QWidget()
    ui = Ui_playerStats()
    ui.setupUi(playerStats)
    playerStats.show()
    sys.exit(app.exec_())
