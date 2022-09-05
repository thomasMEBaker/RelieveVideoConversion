
#using https://github.com/kkroening/ffmpeg-python
# API refence https://kkroening.github.io/ffmpeg-python/

#pyuic5 -x testGUI.ui -o test.py

#functions to use - ffmpeg.trim
# generate thumbnail on github
#custom filters

# look at multithreading to not hold onto process

import sys
import ffmpeg
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi

radiobtn_4 = False
radiobtn_6 = False
radiobtn_both = False

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
    print("4K Conversion Complete!")

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
    print("6K Conversion Complete!")

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
        self.FileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.FileBtn.setGeometry(QtCore.QRect(280, 250, 251, 51))
        self.FileBtn.setObjectName("FileBtn")
        self.TitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.TitleLabel.setGeometry(QtCore.QRect(0, 10, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.VideoOutputLabel = QtWidgets.QLabel(self.centralwidget)
        self.VideoOutputLabel.setGeometry(QtCore.QRect(340, 410, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoOutputLabel.setFont(font)
        self.VideoOutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoOutputLabel.setObjectName("VideoOutputLabel")
        self.Radio_4K = QtWidgets.QRadioButton(self.centralwidget)
        self.Radio_4K.setGeometry(QtCore.QRect(250, 450, 82, 17))
        self.Radio_4K.setObjectName("Radio_4K")
        self.Radio_6K = QtWidgets.QRadioButton(self.centralwidget)
        self.Radio_6K.setGeometry(QtCore.QRect(370, 450, 82, 17))
        self.Radio_6K.setObjectName("Radio_6K")
        self.Radio_Both = QtWidgets.QRadioButton(self.centralwidget)
        self.Radio_Both.setGeometry(QtCore.QRect(480, 450, 82, 17))
        self.Radio_Both.setObjectName("Radio_Both")
        self.AdvancedSettingsLabel = QtWidgets.QLabel(self.centralwidget)
        self.AdvancedSettingsLabel.setGeometry(QtCore.QRect(350, 480, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AdvancedSettingsLabel.setFont(font)
        self.AdvancedSettingsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AdvancedSettingsLabel.setObjectName("AdvancedSettingsLabel")
        self.ConvertBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ConvertBtn.setGeometry(QtCore.QRect(220, 610, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ConvertBtn.setFont(font)
        self.ConvertBtn.setObjectName("ConvertBtn")
        self.VideoOutputLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.VideoOutputLabel_2.setGeometry(QtCore.QRect(280, 310, 251, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoOutputLabel_2.setFont(font)
        self.VideoOutputLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoOutputLabel_2.setObjectName("VideoOutputLabel_2")
        self.VideoNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.VideoNameLabel.setGeometry(QtCore.QRect(170, 330, 251, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoNameLabel.setFont(font)
        self.VideoNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoNameLabel.setObjectName("VideoNameLabel")
        self.VideoNameInput = QtWidgets.QLabel(self.centralwidget)
        self.VideoNameInput.setGeometry(QtCore.QRect(420, 330, 251, 31))
        self.VideoNameInput.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoNameInput.setFont(font)
        self.VideoNameInput.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoNameInput.setObjectName("VideoNameInput")
        self.VideoWidthLabel = QtWidgets.QLabel(self.centralwidget)
        self.VideoWidthLabel.setGeometry(QtCore.QRect(170, 350, 251, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoWidthLabel.setFont(font)
        self.VideoWidthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoWidthLabel.setObjectName("VideoWidthLabel")
        self.VideoWidthInput = QtWidgets.QLabel(self.centralwidget)
        self.VideoWidthInput.setGeometry(QtCore.QRect(420, 350, 251, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoWidthInput.setFont(font)
        self.VideoWidthInput.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoWidthInput.setObjectName("VideoWidthInput")
        self.VideoHeightLabel = QtWidgets.QLabel(self.centralwidget)
        self.VideoHeightLabel.setGeometry(QtCore.QRect(170, 370, 251, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoHeightLabel.setFont(font)
        self.VideoHeightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoHeightLabel.setObjectName("VideoHeightLabel")
        self.VideoHeightInput = QtWidgets.QLabel(self.centralwidget)
        self.VideoHeightInput.setGeometry(QtCore.QRect(420, 370, 251, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VideoHeightInput.setFont(font)
        self.VideoHeightInput.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoHeightInput.setObjectName("VideoHeightInput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 80, 231, 161))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.SaveLocationButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveLocationButton.setGeometry(QtCore.QRect(280, 570, 251, 31))
        self.SaveLocationButton.setObjectName("SaveLocationButton")
        self.BitrateInput = QtWidgets.QTextEdit(self.centralwidget)
        self.BitrateInput.setGeometry(QtCore.QRect(400, 530, 101, 31))
        self.BitrateInput.setObjectName("BitrateInput")
        self.BitrateLabel = QtWidgets.QLabel(self.centralwidget)
        self.BitrateLabel.setGeometry(QtCore.QRect(320, 530, 81, 31))
        self.BitrateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BitrateLabel.setObjectName("BitrateLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #MainWindow.setFixedSize(1000,1000) not need but may be usefull
        self.FileBtn.setText(_translate("MainWindow", "Open File"))
        self.TitleLabel.setText(_translate("MainWindow", "ROVR Relieve - Video Conversion Tool"))
        self.VideoOutputLabel.setText(_translate("MainWindow", "Video Output Settings"))
        self.Radio_4K.setText(_translate("MainWindow", "4K Video"))
        self.Radio_6K.setText(_translate("MainWindow", "6K Video"))
        self.Radio_Both.setText(_translate("MainWindow", "Both"))
        self.AdvancedSettingsLabel.setText(_translate("MainWindow", "Advanced Settings"))
        self.ConvertBtn.setText(_translate("MainWindow", "Convert File(s)"))
        self.VideoOutputLabel_2.setText(_translate("MainWindow", "Current Video Information"))
        self.VideoNameLabel.setText(_translate("MainWindow", "Video Name :"))
        self.VideoNameInput.setText(_translate("MainWindow", "n/a"))
        self.VideoWidthLabel.setText(_translate("MainWindow", "Video Width"))
        self.VideoWidthInput.setText(_translate("MainWindow", "n/a"))
        self.VideoHeightLabel.setText(_translate("MainWindow", "Video Height :"))
        self.VideoHeightInput.setText(_translate("MainWindow", "n/a"))
        self.label.setText(_translate("MainWindow", "No Video Image"))
        self.SaveLocationButton.setText(_translate("MainWindow", "Save Location"))
        self.BitrateLabel.setText(_translate("MainWindow", "Bitrate"))

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
        
    def file_btn_clicked (self):
        global fileLocation
        fileList = QFileDialog.getOpenFileNames(None, "Select Directory","D:\\")
        fileLocation = str(fileList[0])
        final_location = fileLocation.replace('[','').replace(']','')
        final_location  = "file:"+final_location[1:-1]
        fileLocation = final_location
        self.videoInformation(fileLocation)


    def location_btn_clicked(self):
        global saveLocation
        directoryPath=QFileDialog.getExistingDirectory(None, "Get Any File");
        #print(directoryPath);
        final_save_location = "file:"+directoryPath
        saveLocation = final_save_location
        print(saveLocation);


    def videoInformation(self,fname):
        probe = ffmpeg.probe(fname)
        video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        width = int(video_stream['width'])
        height = int(video_stream['height'])

        #print("Video Name - "+str(fname))
        #print("Video Width - "+str(width))
        #print("Video Height - "+str(height))
        #print("                           ")

        file_index = len(fname.split('/')) - 1
        filename_short = fname.split('/')
        filename_short = filename_short[file_index]
        
        #print(filename_short)

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
    add_path_variable()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
