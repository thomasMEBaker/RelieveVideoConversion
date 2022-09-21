
# Written by Tom Baker - Sept 2022
# Python 3.9.12 & QT5
# using https://github.com/kkroening/ffmpeg-python
# API refence https://kkroening.github.io/ffmpeg-python/

#To Do
#hevc output
#error handling 
#change to custom bitrate
#sort layout on other computers e.g. laptop

#issue with trim time on the 4 and 6k conversion - format? Space is causing the issue.

#Testing
# Tidy code
# pyinstaller test
# full installation test

import sys
import ffmpeg
import subprocess
import os
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox

#PY QT imports

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import QUrl

software_version = "Version 0.1"

directorySelected = False

radiobtn_4 = False
radiobtn_6 = False
radiobtn_both = False
play = False
fileSelected = False
fileLocation = ""
saveLocation = ""
videoName = ""
videoWidth = ""
videoHeight = ""
conversionComplete = False
video_length = 0.0

global_checkbox = False
trim_start = ""
trim_end = ""


def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

def generate_thumbnail(fname):
    (
    ffmpeg
    .input(fname, ss=1.00)
    .filter('scale', 600, -1)
    .output("tmp.jpg", vframes=1)
    .run()
    )

def createFileStructure(parent_dir):
    global directorySelected
    main_directory = "RovrConvertedVideos"
   # print(parent_dir)
    x = parent_dir.split("/")
   # print (x)
   # print(len(x)-1)
    if x[len(x)-1] == "RovrConvertedVideos":
        #print ("directory clicked on already")
        directorySelected = True
    else:
        #print ("directory not clicked on")
        directorySelected = False

    if (directorySelected == False):
       # print("Directory not selected - checking if it needs to be made.")
        if(os.path.isdir(parent_dir+"\\"+main_directory)!=True):
           # print("Creating directory")
            path = os.path.join(parent_dir, main_directory)
            os.mkdir(path)
            hmd_sub_directory = "Headset"
            tablet_sub_directory = "Tablet"
            path = os.path.join(parent_dir+"\\"+main_directory, hmd_sub_directory)
            os.mkdir(path)
            path = os.path.join(parent_dir+"\\"+main_directory, tablet_sub_directory)
            os.mkdir(path)
        else:
           # print("No directory creation required")
           # print("Checking sub Headset Folder")
            if(os.path.isdir(parent_dir+"\\"+main_directory+"\\"+"Headset")!=True):
                #print("Creating headset folder")
                path = os.path.join(parent_dir+"\\"+main_directory,"Headset")
                os.mkdir(path)
            if(os.path.isdir(parent_dir+"\\"+main_directory+"\\"+"Tablet")!=True):
                #print("Creating tablet folder")
                
                path = os.path.join(parent_dir+"\\"+main_directory,"Tablet")
                os.mkdir(path) 

    else:
        #print("No directory creation required")
        #print (parent_dir)
        if(os.path.isdir(parent_dir+"\\"+"Headset")!=True):
            #print("Creating headset folder")
            path = os.path.join(parent_dir,"Headset")
            os.mkdir(path)
        if(os.path.isdir(parent_dir+"\\"+"Tablet")!=True):
            #print("Creating tablet folder")
            path = os.path.join(parent_dir,"Tablet")
            os.mkdir(path)

def checkfile(filename,location,fourSix):
    global conversionComplete;
    if fourSix !=True:
        #print("Checking 4K Folder")
        #print(location)
        #print(filename)
        if directorySelected==True:
            #print("Directory selected")
            if (os.path.isfile(location+"//Tablet//"+filename+".mp4")):
                return False
                conversionComplete = False
                #print("File already there")
            else:
                return True
                conversionComplete = True
                #print("File going ahead")
        else:
            #print("Directory not selected")
            
            #print("Directory not selected")
            if (os.path.isfile(location+"/RovrConvertedVideos/Tablet/"+filename+".mp4")):
                return False
                conversionComplete = False
                #print("File already there")

            else:
                return True
                conversionComplete = True
                #print("File going ahead")

    else:
        #print("Checking 6k Folder")
        #print(location)
        #print(filename)
        if directorySelected==True:
            #print("Directory selected")
            if (os.path.isfile(location+"//Headset//"+filename+".mp4")):
                return False
                conversionComplete = False
                #print("File already there")
            else:
                return True
                conversionComplete = True
                #print("File going ahead")
        else:
            #print("Directory not selected")
            
            #print("Directory not selected")
            if (os.path.isfile(location+"/RovrConvertedVideos/Headset/"+filename+".mp4")):
                return False
                conversionComplete = False
                #print("File already there")

            else:
                return True
                conversionComplete = True
                #print("File going ahead")
    
def convertion4k(fname):
    #resoltuion at 4096/2048
    global conversionComplete
    createFileStructure(saveLocation)
    stream = ffmpeg.input(fname)
    stream = ffmpeg.filter(stream,"scale",4096,2048)
    mp4_removal = os.path.splitext(fname)[0]
    name_size = len(mp4_removal.split('/')) - 1
    filename_split = mp4_removal.split('/')
    name = filename_split[name_size]
    if checkfile(name,saveLocation,False) == False:
        conversionComplete = False
    else:
        if directorySelected:
            if global_checkbox:
                valueCheck = str('ffmpeg -ss '+ trim_start +' -to ' + trim_end + ' -i ' + '"' + fname[5:] + '"' + ' -vf scale=4096:2048 -c:v libx264 -c:a copy ' +saveLocation+'//Tablet//' +name+ '.mp4')
                #and if you want to retain aspect ratio just give height as -1 and it will automatically resize based on the width e.g. -vf scale="720:-1"
                print(valueCheck)
                subprocess.call([valueCheck])
                #os.system(valueCheck)
                conversionComplete = True
            else:
                stream = ffmpeg.output(stream, saveLocation+"//Tablet//"+name+".mp4")
                ffmpeg.run(stream)
                conversionComplete = True
        else:
            if global_checkbox:
                valueCheck = str('ffmpeg -ss '+ trim_start +' -to ' + trim_end + ' -i ' + "'" + fname[5:] + "'" + ' -vf scale=4096:2048 -c:v libx264 -c:a copy ' +saveLocation+'/RovrConvertedVideos/Tablet/'+name+'.mp4')
                print(valueCheck)
                #os.system(valueCheck)
                subprocess.call([valueCheck])
                conversionComplete = True
            else:
                stream = ffmpeg.output(stream, saveLocation+"/RovrConvertedVideos/Tablet/"+name+".mp4")
                ffmpeg.run(stream)
                conversionComplete = True

def convertion6k(fname):
    #resoltuion at 5760/2880
    global conversionComplete
    createFileStructure(saveLocation)
    stream = ffmpeg.input(fname)
    stream = ffmpeg.filter(stream,"scale",5760,2880)
    mp4_removal = os.path.splitext(fname)[0]
    name_size = len(mp4_removal.split('/')) - 1
    filename_split = mp4_removal.split('/')
    name = filename_split[name_size]
    if checkfile(name,saveLocation,True) == False:
            conversionComplete = False
    else:
        if directorySelected:
            if global_checkbox:
               valueCheck = str("ffmpeg -ss "+ trim_start +" -to " + trim_end + " -i " + fname[5:] + " -vf scale=5760:2880 -c:v libx264 -c:a copy " +saveLocation+"//Headset//" +name+'.mp4')
               print(valueCheck)
               os.system(valueCheck)
               conversionComplete = True
            else:
                stream = ffmpeg.output(stream, saveLocation+"//Tablet//"+name+".mp4")
                ffmpeg.run(stream)
                conversionComplete = True
        else:
            if global_checkbox:
                valueCheck = str("ffmpeg -ss "+ trim_start +" -to " + trim_end + " -i " + fname[5:] + " -vf scale=5760:2880 -c:v libx264 -c:a copy " +saveLocation+"/RovrConvertedVideos/Headset/"+name+'.mp4')
                print(valueCheck)
                os.system(valueCheck)
                conversionComplete = True
            else:
                stream = ffmpeg.output(stream, saveLocation+"/RovrConvertedVideos/Tablet/"+name+".mp4")
                ffmpeg.run(stream)
                conversionComplete = True
def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True

def add_path_variable():
    if sys.platform == 'win32':
        sep = ';'
    else:
        sep = ':'

    directory = os.getcwd()
    directory = directory + "\FFmpeg\\bin"
    #print(directory)

    os.environ['PATH'] += sep + directory
    
    path = os.environ.get('PATH')
    #print(path)

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

        #Media player
        self.mediaplayer = QMediaPlayer(None,QMediaPlayer.VideoSurface)
        
        self.mediaplayer.setVideoOutput(self.VideoDisplay)

        self.mediaplayer.positionChanged.connect(self.position_changed)
        self.mediaplayer.durationChanged.connect(self.duration_changed)
        self.horizontalSlider.sliderMoved.connect(self.set_position)

        self.mediaplayer.positionChanged.connect(self.end_media)
        

        self.mediaplayer.positionChanged.connect(self.print_position)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.VideoStart.textChanged.connect(lambda: self.videoStartUpdate())
        self.VideoEnd.textChanged.connect(lambda: self.videoEndUpdate())

        
        #open file button
        self.FileBtn.clicked.connect(lambda: self.file_btn_clicked())

        #save location button
        self.SaveLocationButton.clicked.connect(lambda: self.location_btn_clicked())

        #convert files button
        self.ConvertBtn.clicked.connect(lambda: self.convert_btn_clicked())
        
        self.Radio_4K.clicked.connect(lambda: self.radio_check())
        self.Radio_6K.clicked.connect(lambda: self.radio_check())
        self.Radio_Both.clicked.connect(lambda: self.radio_check())

        #push button/play needs updating
        self.pushButton.setText("Play")
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(lambda: self.playVideo())

        #needs formatting to minutes and seconds etc
        self.label.setText("00:00:00")
        self.label.setEnabled(False)
        self.horizontalSlider.setEnabled(False)

        #version number
        self.versionLabel.setText(str(software_version))

        self.checkBox.clicked.connect(lambda: self.trim_check())
        self.VideoStart.setEnabled(False)
        self.VideoEnd.setEnabled(False)

        self.checkBox.clicked.connect(lambda: self.trim_check())

        self.BitrateCheck.clicked.connect(lambda: self.bitrate_check())
        self.BitrateInput.setEnabled(False)

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

    def videoStartUpdate(self):
        global trim_start
        trim_start = self.VideoStart.toPlainText()
        #print(trim_start)

    def videoEndUpdate(self):
        global trim_end
        trim_end = self.VideoEnd.toPlainText()
        #print(trim_end)

    def bitrate_check(self):
        if self.BitrateCheck.isChecked():
            self.BitrateInput.setEnabled(True)
        else:
            self.BitrateInput.setEnabled(False)


    def trim_check(self):
        global global_checkbox
        if self.checkBox.isChecked():
            self.VideoStart.setEnabled(True)
            self.VideoEnd.setEnabled(True)
    
            RemainingSec = video_length % (24 * 3600)
            HoursGet = RemainingSec // 3600
            RemainingSec %= 3600
            MinutesGet = RemainingSec // 60
            self.VideoStart.setText("00:00:0")
            self.VideoEnd.setText("00:"+str(int(MinutesGet)) + ":" + str(int(video_length%60)))
            global_checkbox = True
        else:
            self.VideoStart.setEnabled(False)
            self.VideoEnd.setEnabled(False)
            self.VideoStart.setText("")
            self.VideoEnd.setText("")
            global_checkbox = False
            
    def radio_check(self):
        global radiobtn_4
        global radiobtn_6
        global radiobtn_both
        if self.Radio_4K.isChecked():
            radiobtn_4 = True
            radiobtn_6 = False
            radiobtn_both = False
        if self.Radio_6K.isChecked():
            radiobtn_6 = True
            radiobtn_4 = False
            radiobtn_both = False
        if self.Radio_Both.isChecked():
            radiobtn_both = True
            radiobtn_6 = False
            radiobtn_4 = False

    def playVideo(self):
        global play
        if self.mediaplayer.state() == QMediaPlayer.PlayingState:
            self.mediaplayer.pause()
            play = True
            #print("Pause")
            self.pushButton.setText("Play")
        
        else:
            self.mediaplayer.play()
            #print("Play")
            self.pushButton.setText("Pause")

    def position_changed(self,position):
        self.horizontalSlider.setValue(position)
        
    def duration_changed(self,duration):
        self.horizontalSlider.setRange(0,duration)

    def set_position(self, position):
        self.mediaplayer.setPosition(position)

    def print_position(self,position):
        seconds=(position/1000.0)
        RemainingSec = seconds % (24 * 3600)
        HoursGet = RemainingSec // 3600
        RemainingSec %= 3600
        MinutesGet = RemainingSec // 60
        self.label.setText(str(int(MinutesGet)) + ":" + str(int(seconds%60)))

    def end_media(self,status):
        if self.mediaplayer.state() == 0:
            play = True
            self.pushButton.setText("Play")

    
    def file_btn_clicked (self):
        global fileLocation
        global fileSelected
        fileList = QFileDialog.getOpenFileNames(None, "Select Directory","D:\\")
        if str(fileList[0]) !='[]':
            fileLocation = str(fileList[0])
            final_location = fileLocation.replace('[','').replace(']','')
            final_location  = "file:"+final_location[1:-1]
            fileLocation = final_location
            self.videoInformation(fileLocation)
            self.mediaplayer.setMedia(QMediaContent(QUrl.fromLocalFile(str(fileLocation))))
            self.pushButton.setEnabled(True)
            self.horizontalSlider.setEnabled(True)
            self.label.setEnabled(True)
    
            self.mediaplayer.play()
            self.mediaplayer.pause()
            fileSelected = True
        else:
            self.pushButton.setEnabled(False)
            self.pushButton.setEnabled(False)
            self.horizontalSlider.setEnabled(False)
            self.label.setEnabled(False)
            self.mediaplayer.setMedia(QMediaContent())
            print("Cancel")
            fileSelected = False

    def location_btn_clicked(self):
        global saveLocation
        global directorySelected
        directorySelected = False
        directoryPath=QFileDialog.getExistingDirectory(None, "Get Any File");
        final_save_location = "file:"+directoryPath
        saveLocation = final_save_location
        print(saveLocation);
        saveLocation = saveLocation[5:]
        self.SaveLocation.setText(str(saveLocation))


    def videoInformation(self,fname):
        global video_length
        probe = ffmpeg.probe(fname)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        width = int(video_stream['width'])
        height = int(video_stream['height'])
        video_length = float(video_stream['duration'])
        

        file_index = len(fname.split('/')) - 1
        filename_short = fname.split('/')
        filename_short = filename_short[file_index]

        self.VideoNameInput.setText(str(filename_short))
        self.VideoWidthInput.setText(str(width))
        self.VideoHeightInput.setText(str(height))
        

    def convert_btn_clicked (self):
        print(radiobtn_4)
        print(radiobtn_6)
        print(radiobtn_both)
        if fileSelected != True:
            self.pop_up_UI(" ","Plesae select a file to convert.")

        elif radiobtn_4 == True or radiobtn_6 == True or radiobtn_both == True:
            self.worker = WorkerThread()
            self.worker.start()
            MainWindow.setEnabled(False)
            self.worker.finished.connect(self.evt_worker_finished)
        else:
            self.pop_up_UI(" ","Plesae select a video output resolution.")

    def evt_worker_finished(self):
        #this will indicate that the video conversion is complete and the loading screen can be removed 
        #print("Worker Thread Complete")
        MainWindow.setEnabled(True)

        #UI pop up to say the video has been converted
        self.video_pop_up("Success!","The video was converted successfully.")
        

    def add_path_variable():
        if sys.platform == 'win32':
            sep = ';'
        else:
            sep = ':'

        directory = os.getcwd() 
        directory = directory + "\FFmpeg\\bin"
        print(directory)

        os.environ['PATH'] += sep + directory
    
        path = os.environ.get('PATH')
        print(path)

    def video_pop_up(self,titleText,bodyText):
        global conversionComplete
        if conversionComplete:
            msg = QMessageBox()
            msg.setWindowTitle(titleText)
            msg.setText(bodyText)
            x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("There is a file with the same name in the directory, please remove and re convert.")
            x = msg.exec_()
        conversionComplete = False
            
    def pop_up_UI(self,titleText,bodyText):
        msg = QMessageBox()
        msg.setWindowTitle(titleText)
        msg.setText(bodyText)
        x = msg.exec_()
        

class WorkerThread(QThread):
    def run (self):
        if (radiobtn_4 == True):
            convertion4k(fileLocation)
        elif (radiobtn_6 == True):
            convertion6k(fileLocation)
        elif (radiobtn_both == True):
            convertion4k(fileLocation)
            convertion6k(fileLocation)

if __name__ == "__main__":
    sys.excepthook = show_exception_and_exit
    add_path_variable()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
