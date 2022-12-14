# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videoConversion.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(850, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(850, 900))
        MainWindow.setMaximumSize(QtCore.QSize(850, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.TitleLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy)
        self.TitleLabel.setMinimumSize(QtCore.QSize(480, 30))
        self.TitleLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout_6.addWidget(self.TitleLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.VideoDisplay = QVideoWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoDisplay.sizePolicy().hasHeightForWidth())
        self.VideoDisplay.setSizePolicy(sizePolicy)
        self.VideoDisplay.setMinimumSize(QtCore.QSize(400, 200))
        self.VideoDisplay.setMaximumSize(QtCore.QSize(400, 200))
        self.VideoDisplay.setObjectName("VideoDisplay")
        self.NoVideoWarning = QtWidgets.QLabel(self.VideoDisplay)
        self.NoVideoWarning.setGeometry(QtCore.QRect(10, 10, 380, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NoVideoWarning.sizePolicy().hasHeightForWidth())
        self.NoVideoWarning.setSizePolicy(sizePolicy)
        self.NoVideoWarning.setMinimumSize(QtCore.QSize(350, 100))
        self.NoVideoWarning.setMaximumSize(QtCore.QSize(400, 100))
        self.NoVideoWarning.setAlignment(QtCore.Qt.AlignCenter)
        self.NoVideoWarning.setObjectName("NoVideoWarning")
        self.verticalLayout_3.addWidget(self.VideoDisplay, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton, 0, QtCore.Qt.AlignVCenter)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(150, 25))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(150, 25))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_4.addWidget(self.horizontalSlider, 0, QtCore.Qt.AlignVCenter)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(47, 25))
        self.label.setMaximumSize(QtCore.QSize(47, 25))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.FileBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FileBtn.sizePolicy().hasHeightForWidth())
        self.FileBtn.setSizePolicy(sizePolicy)
        self.FileBtn.setMinimumSize(QtCore.QSize(480, 25))
        self.FileBtn.setMaximumSize(QtCore.QSize(480, 25))
        self.FileBtn.setObjectName("FileBtn")
        self.verticalLayout_8.addWidget(self.FileBtn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.VideoOutputLabel_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoOutputLabel_2.sizePolicy().hasHeightForWidth())
        self.VideoOutputLabel_2.setSizePolicy(sizePolicy)
        self.VideoOutputLabel_2.setMinimumSize(QtCore.QSize(480, 20))
        self.VideoOutputLabel_2.setMaximumSize(QtCore.QSize(480, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoOutputLabel_2.setFont(font)
        self.VideoOutputLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoOutputLabel_2.setObjectName("VideoOutputLabel_2")
        self.verticalLayout_9.addWidget(self.VideoOutputLabel_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.verticalLayout_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.VideoNameLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoNameLabel.sizePolicy().hasHeightForWidth())
        self.VideoNameLabel.setSizePolicy(sizePolicy)
        self.VideoNameLabel.setMinimumSize(QtCore.QSize(160, 25))
        self.VideoNameLabel.setMaximumSize(QtCore.QSize(160, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoNameLabel.setFont(font)
        self.VideoNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoNameLabel.setObjectName("VideoNameLabel")
        self.horizontalLayout.addWidget(self.VideoNameLabel)
        self.VideoWidthLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoWidthLabel.sizePolicy().hasHeightForWidth())
        self.VideoWidthLabel.setSizePolicy(sizePolicy)
        self.VideoWidthLabel.setMinimumSize(QtCore.QSize(160, 25))
        self.VideoWidthLabel.setMaximumSize(QtCore.QSize(160, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoWidthLabel.setFont(font)
        self.VideoWidthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoWidthLabel.setObjectName("VideoWidthLabel")
        self.horizontalLayout.addWidget(self.VideoWidthLabel)
        self.VideoHeightLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoHeightLabel.sizePolicy().hasHeightForWidth())
        self.VideoHeightLabel.setSizePolicy(sizePolicy)
        self.VideoHeightLabel.setMinimumSize(QtCore.QSize(160, 25))
        self.VideoHeightLabel.setMaximumSize(QtCore.QSize(160, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoHeightLabel.setFont(font)
        self.VideoHeightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoHeightLabel.setObjectName("VideoHeightLabel")
        self.horizontalLayout.addWidget(self.VideoHeightLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.VideoNameInput = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoNameInput.sizePolicy().hasHeightForWidth())
        self.VideoNameInput.setSizePolicy(sizePolicy)
        self.VideoNameInput.setMinimumSize(QtCore.QSize(160, 25))
        self.VideoNameInput.setMaximumSize(QtCore.QSize(160, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.VideoNameInput.setFont(font)
        self.VideoNameInput.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoNameInput.setObjectName("VideoNameInput")
        self.horizontalLayout_2.addWidget(self.VideoNameInput, 0, QtCore.Qt.AlignHCenter)
        self.VideoWidthInput = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoWidthInput.sizePolicy().hasHeightForWidth())
        self.VideoWidthInput.setSizePolicy(sizePolicy)
        self.VideoWidthInput.setMinimumSize(QtCore.QSize(160, 25))
        self.VideoWidthInput.setMaximumSize(QtCore.QSize(160, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.VideoWidthInput.setFont(font)
        self.VideoWidthInput.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoWidthInput.setObjectName("VideoWidthInput")
        self.horizontalLayout_2.addWidget(self.VideoWidthInput, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.VideoHeightInput = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoHeightInput.sizePolicy().hasHeightForWidth())
        self.VideoHeightInput.setSizePolicy(sizePolicy)
        self.VideoHeightInput.setMinimumSize(QtCore.QSize(160, 10))
        self.VideoHeightInput.setMaximumSize(QtCore.QSize(160, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.VideoHeightInput.setFont(font)
        self.VideoHeightInput.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoHeightInput.setObjectName("VideoHeightInput")
        self.horizontalLayout_2.addWidget(self.VideoHeightInput, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.VideoOutputLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoOutputLabel.sizePolicy().hasHeightForWidth())
        self.VideoOutputLabel.setSizePolicy(sizePolicy)
        self.VideoOutputLabel.setMinimumSize(QtCore.QSize(480, 20))
        self.VideoOutputLabel.setMaximumSize(QtCore.QSize(480, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoOutputLabel.setFont(font)
        self.VideoOutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoOutputLabel.setObjectName("VideoOutputLabel")
        self.verticalLayout_10.addWidget(self.VideoOutputLabel, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.Radio_6K = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Radio_6K.sizePolicy().hasHeightForWidth())
        self.Radio_6K.setSizePolicy(sizePolicy)
        self.Radio_6K.setMinimumSize(QtCore.QSize(0, 30))
        self.Radio_6K.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Radio_6K.setObjectName("Radio_6K")
        self.verticalLayout_16.addWidget(self.Radio_6K, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.Radio_4K = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Radio_4K.sizePolicy().hasHeightForWidth())
        self.Radio_4K.setSizePolicy(sizePolicy)
        self.Radio_4K.setMinimumSize(QtCore.QSize(0, 30))
        self.Radio_4K.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Radio_4K.setObjectName("Radio_4K")
        self.verticalLayout_17.addWidget(self.Radio_4K, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.Radio_Both = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Radio_Both.sizePolicy().hasHeightForWidth())
        self.Radio_Both.setSizePolicy(sizePolicy)
        self.Radio_Both.setMinimumSize(QtCore.QSize(0, 30))
        self.Radio_Both.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Radio_Both.setObjectName("Radio_Both")
        self.verticalLayout_18.addWidget(self.Radio_Both, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout_18)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.AdvancedSettingsLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AdvancedSettingsLabel.sizePolicy().hasHeightForWidth())
        self.AdvancedSettingsLabel.setSizePolicy(sizePolicy)
        self.AdvancedSettingsLabel.setMinimumSize(QtCore.QSize(480, 0))
        self.AdvancedSettingsLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AdvancedSettingsLabel.setFont(font)
        self.AdvancedSettingsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AdvancedSettingsLabel.setObjectName("AdvancedSettingsLabel")
        self.verticalLayout_11.addWidget(self.AdvancedSettingsLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.verticalLayout_11)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BitrateCheck = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BitrateCheck.sizePolicy().hasHeightForWidth())
        self.BitrateCheck.setSizePolicy(sizePolicy)
        self.BitrateCheck.setObjectName("BitrateCheck")
        self.horizontalLayout_3.addWidget(self.BitrateCheck)
        self.BitrateInput = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BitrateInput.sizePolicy().hasHeightForWidth())
        self.BitrateInput.setSizePolicy(sizePolicy)
        self.BitrateInput.setMinimumSize(QtCore.QSize(200, 25))
        self.BitrateInput.setMaximumSize(QtCore.QSize(240, 25))
        self.BitrateInput.setObjectName("BitrateInput")
        self.horizontalLayout_3.addWidget(self.BitrateInput)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_5.addWidget(self.checkBox)
        self.VideoStart = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoStart.sizePolicy().hasHeightForWidth())
        self.VideoStart.setSizePolicy(sizePolicy)
        self.VideoStart.setMaximumSize(QtCore.QSize(250, 25))
        self.VideoStart.setObjectName("VideoStart")
        self.horizontalLayout_5.addWidget(self.VideoStart)
        self.VideoEnd = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoEnd.sizePolicy().hasHeightForWidth())
        self.VideoEnd.setSizePolicy(sizePolicy)
        self.VideoEnd.setMaximumSize(QtCore.QSize(16777215, 25))
        self.VideoEnd.setObjectName("VideoEnd")
        self.horizontalLayout_5.addWidget(self.VideoEnd)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.SaveLocation = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveLocation.sizePolicy().hasHeightForWidth())
        self.SaveLocation.setSizePolicy(sizePolicy)
        self.SaveLocation.setMinimumSize(QtCore.QSize(480, 50))
        self.SaveLocation.setMaximumSize(QtCore.QSize(16777215, 50))
        self.SaveLocation.setAlignment(QtCore.Qt.AlignCenter)
        self.SaveLocation.setObjectName("SaveLocation")
        self.verticalLayout_13.addWidget(self.SaveLocation, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_12.addLayout(self.verticalLayout_13)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.SaveLocationButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveLocationButton.sizePolicy().hasHeightForWidth())
        self.SaveLocationButton.setSizePolicy(sizePolicy)
        self.SaveLocationButton.setMinimumSize(QtCore.QSize(480, 27))
        self.SaveLocationButton.setMaximumSize(QtCore.QSize(480, 27))
        self.SaveLocationButton.setObjectName("SaveLocationButton")
        self.verticalLayout_14.addWidget(self.SaveLocationButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_15.addLayout(self.verticalLayout_14)
        self.ConvertBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConvertBtn.sizePolicy().hasHeightForWidth())
        self.ConvertBtn.setSizePolicy(sizePolicy)
        self.ConvertBtn.setMinimumSize(QtCore.QSize(480, 35))
        self.ConvertBtn.setMaximumSize(QtCore.QSize(480, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ConvertBtn.setFont(font)
        self.ConvertBtn.setObjectName("ConvertBtn")
        self.verticalLayout_15.addWidget(self.ConvertBtn, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_12.addLayout(self.verticalLayout_15)
        self.verticalLayout.addLayout(self.verticalLayout_12)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.versionLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionLabel.sizePolicy().hasHeightForWidth())
        self.versionLabel.setSizePolicy(sizePolicy)
        self.versionLabel.setMinimumSize(QtCore.QSize(480, 20))
        self.versionLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.versionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.versionLabel.setObjectName("versionLabel")
        self.verticalLayout_4.addWidget(self.versionLabel, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TitleLabel.setText(_translate("MainWindow", "ROVR Relieve - Video Conversion Tool (Beta)"))
        self.NoVideoWarning.setText(_translate("MainWindow", "No Video Selected"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.FileBtn.setText(_translate("MainWindow", "Open File"))
        self.VideoOutputLabel_2.setText(_translate("MainWindow", "Current Video Information"))
        self.VideoNameLabel.setText(_translate("MainWindow", "Video Name :"))
        self.VideoWidthLabel.setText(_translate("MainWindow", "Video Width :"))
        self.VideoHeightLabel.setText(_translate("MainWindow", "Video Height :"))
        self.VideoNameInput.setText(_translate("MainWindow", "n/a"))
        self.VideoWidthInput.setText(_translate("MainWindow", "n/a"))
        self.VideoHeightInput.setText(_translate("MainWindow", "n/a"))
        self.VideoOutputLabel.setText(_translate("MainWindow", "Video Output Settings"))
        self.Radio_6K.setText(_translate("MainWindow", "6K Video"))
        self.Radio_4K.setText(_translate("MainWindow", "4K Video"))
        self.Radio_Both.setText(_translate("MainWindow", "Both"))
        self.AdvancedSettingsLabel.setText(_translate("MainWindow", "Advanced Settings"))
        self.BitrateCheck.setText(_translate("MainWindow", "Bitrate"))
        self.checkBox.setText(_translate("MainWindow", "Trim (Start/End)"))
        self.SaveLocation.setText(_translate("MainWindow", "N/A"))
        self.SaveLocationButton.setText(_translate("MainWindow", "Save Location"))
        self.ConvertBtn.setText(_translate("MainWindow", "Convert File(s)"))
        self.versionLabel.setText(_translate("MainWindow", "V1.0"))
from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
