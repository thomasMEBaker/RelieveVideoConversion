
#using https://github.com/kkroening/ffmpeg-python
# API refence https://kkroening.github.io/ffmpeg-python/

#pyuic5 -x testGUI.ui -o test.py

#functions to use - ffmpeg.trim
#custom filters

#To Do
# - Multiprocess or sub process?
# - end of media file to change play/pause
# - get rid of old media file if changed
# - Tidy code
# - Version Number
# - possible option to trim
# - change bitrate
# pyinstaller test
# full installation test

import sys
import ffmpeg
import os
from multiprocessing import Process, Queue
#PY QT imports

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import QUrl

radiobtn_4 = False
radiobtn_6 = False
radiobtn_both = False
play = False
fileLocation = ""
saveLocation = ""
videoName = ""
videoWidth = ""
videoHeight = ""

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
    
def convertion4k(fname):
    #resoltuion at 4096/2048
    stream = ffmpeg.input(fname)
    stream = ffmpeg.filter(stream,"scale",4096,2048)
    mp4_removal = os.path.splitext(fname)[0]
    name_size = len(mp4_removal.split('/')) - 1
    filename_split = mp4_removal.split('/')
    name = filename_split[name_size]
    stream = ffmpeg.output(stream, saveLocation+"/"+name+'4K_Tablet.mp4')
    ffmpeg.run(stream)
    #print("4K Conversion Complete!")

def convertion6k(fname):
    #resoltuion at 5760/2880
    stream = ffmpeg.input(fname)
    stream = ffmpeg.filter(stream,"scale",5760,2880)
    mp4_removal = os.path.splitext(fname)[0]
    name_size = len(mp4_removal.split('/')) - 1
    filename_split = mp4_removal.split('/')
    name = filename_split[name_size]
    stream = ffmpeg.output(stream, saveLocation+"/"+name+'6K_Headset.mp4')
    ffmpeg.run(stream)
    #print("6K Conversion Complete!")

def cropInputFile(fname):
    #not currently implemented! 
    #stream = ffmpeg.input(fname+'.mp4').filter('trim',duration=33.3) to just give an overall length
    #stream = ffmpeg.input(fname+'.mp4').filter('trim',start=33.3,end=50.0) #not 100% working
    #stream = ffmpeg.output(stream, fname+'_trimmed.mp4')
    #ffmpeg.run(stream)
    print("6K Conversion Complete!")

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
    print(directory)

    os.environ['PATH'] += sep + directory
    
    path = os.environ.get('PATH')
    print(path)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(908, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout.addWidget(self.TitleLabel)
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
        self.NoVideoWarning.setGeometry(QtCore.QRect(10, 10, 380, 180))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NoVideoWarning.sizePolicy().hasHeightForWidth())
        self.NoVideoWarning.setSizePolicy(sizePolicy)
        self.NoVideoWarning.setMinimumSize(QtCore.QSize(350, 180))
        self.NoVideoWarning.setMaximumSize(QtCore.QSize(400, 200))
        self.NoVideoWarning.setAlignment(QtCore.Qt.AlignCenter)
        self.NoVideoWarning.setObjectName("NoVideoWarning")
        self.verticalLayout_3.addWidget(self.VideoDisplay, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_4.addWidget(self.horizontalSlider)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.FileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.FileBtn.setObjectName("FileBtn")
        self.verticalLayout.addWidget(self.FileBtn)
        self.VideoOutputLabel_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoOutputLabel_2.setFont(font)
        self.VideoOutputLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoOutputLabel_2.setObjectName("VideoOutputLabel_2")
        self.verticalLayout.addWidget(self.VideoOutputLabel_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.VideoNameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoNameLabel.setFont(font)
        self.VideoNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoNameLabel.setObjectName("VideoNameLabel")
        self.horizontalLayout.addWidget(self.VideoNameLabel)
        self.VideoWidthLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoWidthLabel.setFont(font)
        self.VideoWidthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoWidthLabel.setObjectName("VideoWidthLabel")
        self.horizontalLayout.addWidget(self.VideoWidthLabel)
        self.VideoHeightLabel = QtWidgets.QLabel(self.centralwidget)
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
        self.VideoNameInput.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoNameInput.setFont(font)
        self.VideoNameInput.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoNameInput.setObjectName("VideoNameInput")
        self.horizontalLayout_2.addWidget(self.VideoNameInput)
        self.VideoWidthInput = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoWidthInput.setFont(font)
        self.VideoWidthInput.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoWidthInput.setObjectName("VideoWidthInput")
        self.horizontalLayout_2.addWidget(self.VideoWidthInput)
        self.VideoHeightInput = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoHeightInput.setFont(font)
        self.VideoHeightInput.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoHeightInput.setObjectName("VideoHeightInput")
        self.horizontalLayout_2.addWidget(self.VideoHeightInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.VideoOutputLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoOutputLabel.setFont(font)
        self.VideoOutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoOutputLabel.setObjectName("VideoOutputLabel")
        self.verticalLayout.addWidget(self.VideoOutputLabel)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Radio_6K = QtWidgets.QRadioButton(self.centralwidget)
        self.Radio_6K.setObjectName("Radio_6K")
        self.verticalLayout_2.addWidget(self.Radio_6K, 0, QtCore.Qt.AlignHCenter)
        self.Radio_4K = QtWidgets.QRadioButton(self.centralwidget)
        self.Radio_4K.setObjectName("Radio_4K")
        self.verticalLayout_2.addWidget(self.Radio_4K, 0, QtCore.Qt.AlignHCenter)
        self.Radio_Both = QtWidgets.QRadioButton(self.centralwidget)
        self.Radio_Both.setObjectName("Radio_Both")
        self.verticalLayout_2.addWidget(self.Radio_Both, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.AdvancedSettingsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AdvancedSettingsLabel.setFont(font)
        self.AdvancedSettingsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AdvancedSettingsLabel.setObjectName("AdvancedSettingsLabel")
        self.verticalLayout.addWidget(self.AdvancedSettingsLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.BitrateLabel = QtWidgets.QLabel(self.centralwidget)
        self.BitrateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BitrateLabel.setObjectName("BitrateLabel")
        self.horizontalLayout_3.addWidget(self.BitrateLabel)
        self.BitrateInput = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BitrateInput.sizePolicy().hasHeightForWidth())
        self.BitrateInput.setSizePolicy(sizePolicy)
        self.BitrateInput.setMaximumSize(QtCore.QSize(600, 50))
        self.BitrateInput.setObjectName("BitrateInput")
        self.horizontalLayout_3.addWidget(self.BitrateInput)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.SaveLocation = QtWidgets.QLabel(self.centralwidget)
        self.SaveLocation.setAlignment(QtCore.Qt.AlignCenter)
        self.SaveLocation.setObjectName("SaveLocation")
        self.verticalLayout.addWidget(self.SaveLocation)
        self.SaveLocationButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveLocationButton.setObjectName("SaveLocationButton")
        self.verticalLayout.addWidget(self.SaveLocationButton)
        self.ConvertBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ConvertBtn.setFont(font)
        self.ConvertBtn.setObjectName("ConvertBtn")
        self.verticalLayout.addWidget(self.ConvertBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 22))
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
        self.label.setText("0:0:0")
        self.label.setEnabled(False)
        self.horizontalSlider.setEnabled(False)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TitleLabel.setText(_translate("MainWindow", "ROVR Relieve - Video Conversion Tool"))
        self.NoVideoWarning.setText(_translate("MainWindow", "No Video Selected"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.FileBtn.setText(_translate("MainWindow", "Open File"))
        self.VideoOutputLabel_2.setText(_translate("MainWindow", "Current Video Information"))
        self.VideoNameLabel.setText(_translate("MainWindow", "Video Name :"))
        self.VideoWidthLabel.setText(_translate("MainWindow", "Video Width"))
        self.VideoHeightLabel.setText(_translate("MainWindow", "Video Height :"))
        self.VideoNameInput.setText(_translate("MainWindow", "n/a"))
        self.VideoWidthInput.setText(_translate("MainWindow", "n/a"))
        self.VideoHeightInput.setText(_translate("MainWindow", "n/a"))
        self.VideoOutputLabel.setText(_translate("MainWindow", "Video Output Settings"))
        self.Radio_6K.setText(_translate("MainWindow", "6K Video"))
        self.Radio_4K.setText(_translate("MainWindow", "4K Video"))
        self.Radio_Both.setText(_translate("MainWindow", "Both"))
        self.AdvancedSettingsLabel.setText(_translate("MainWindow", "Advanced Settings"))
        self.BitrateLabel.setText(_translate("MainWindow", "Bitrate"))
        self.SaveLocation.setText(_translate("MainWindow", "N/A"))
        self.SaveLocationButton.setText(_translate("MainWindow", "Save Location"))
        self.ConvertBtn.setText(_translate("MainWindow", "Convert File(s)"))

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

    def media_end(self):
            if self.mediaplayer.state() == QMediaPlayer.EndOfMedia:
                print("end of media")

    def position_changed(self,position):
        self.horizontalSlider.setValue(position)
        
    def duration_changed(self,duration):
        self.horizontalSlider.setRange(0,duration)

    def set_position(self, position):
        self.mediaplayer.setPosition(position)

    def print_position(self,position):

        millis = int(position)
        seconds=(millis/1000)%60
        seconds = int(seconds)
        minutes=(millis/(1000*60))%60
        minutes = int(minutes) 
        self.label.setText(str(minutes)+":"+str(seconds)+":"+str(millis))

    def end_media(self,status):
        if self.mediaplayer.state() == QMediaPlayer.EndOfMedia:
            print("Bingo")

    
    def file_btn_clicked (self):
        global fileLocation
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
        else:
            self.pushButton.setEnabled(False)
            self.pushButton.setEnabled(False)
            self.horizontalSlider.setEnabled(False)
            self.label.setEnabled(False)
            self.mediaplayer.setMedia(QMediaContent())
            print("Cancel")



    def location_btn_clicked(self):
        global saveLocation
        directoryPath=QFileDialog.getExistingDirectory(None, "Get Any File");
        final_save_location = "file:"+directoryPath
        saveLocation = final_save_location
        print(saveLocation);
        saveLocation = saveLocation[5:]
        self.SaveLocation.setText(str(saveLocation))


    def videoInformation(self,fname):
        probe = ffmpeg.probe(fname)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        width = int(video_stream['width'])
        height = int(video_stream['height'])

        file_index = len(fname.split('/')) - 1
        filename_short = fname.split('/')
        filename_short = filename_short[file_index]
        

        self.VideoNameInput.setText(str(filename_short))
        self.VideoWidthInput.setText(str(width))
        self.VideoHeightInput.setText(str(height))
            

    def convert_btn_clicked (self):        
        if (radiobtn_4 == True):
            convertion4k(fileLocation)
        elif (radiobtn_6 == True):
            convertion6k(fileLocation)
        elif (radiobtn_both == True):
            convertion4k(fileLocation)
            convertion6k(fileLocation)

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
            
if __name__ == "__main__":
    sys.excepthook = show_exception_and_exit
    #queue = Queue()
    #p = Process(target=add_path_variable(), args=(queue, 1))
    #p.start()
    #p.join()
    #result = queue.get()

    
    """
 
    p.join() # this blocks until the process terminates
    result = queue.get()
    print result

    """
    
    add_path_variable()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
