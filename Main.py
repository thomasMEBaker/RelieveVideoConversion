import ffmpeg
import sys
import subprocess
import os

#using https://github.com/kkroening/ffmpeg-python
# API refence https://kkroening.github.io/ffmpeg-python/

#pyuic5 -x testGUI.ui -o test.py

#functions to use - ffmpeg.trim
# generate thumbnail on github
#custom filters

def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

def videoInformation(fname):
    probe = ffmpeg.probe(fname + ".mp4")
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    width = int(video_stream['width'])
    height = int(video_stream['height'])

    print("Video Name - "+str(fname))
    print("Video Width - "+str(width))
    print("Video Height - "+str(height))
    print("                           ")
    
def convertion4k(fname):
    #resoltuion at 4096/2048
    stream = ffmpeg.input(fname+'.mp4')
    stream = ffmpeg.filter(stream,"scale",4096,2048)
    stream = ffmpeg.output(stream, fname+'4K_Tablet.mp4')
    ffmpeg.run(stream)
    print("4K Conversion Complete!")

def convertion6k(fname):
    #resoltuion at 5760/2880
    stream = ffmpeg.input(fname+'.mp4')
    stream = ffmpeg.filter(stream,"scale",5760,2880)
    stream = ffmpeg.output(stream, fname+'6K_Headset.mp4')
    ffmpeg.run(stream)
    print("6K Conversion Complete!")

def cropInputFile(fname):
    #stream = ffmpeg.input(fname+'.mp4').filter('trim',duration=33.3) to just give an overall length
    stream = ffmpeg.input(fname+'.mp4').filter('trim',start=33.3,end=50.0) #not 100% working
    stream = ffmpeg.output(stream, fname+'_trimmed.mp4')
    ffmpeg.run(stream)
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

def main():
    sys.excepthook = show_exception_and_exit
    add_path_variable()
    #print("Subprocess Exists - " + str(module_exists("subprocess")))
    if (module_exists("ffmpeg")):
        #print("ffmpeg Exists - " + str(module_exists("ffmpeg")))
        videopath = input(str("Please enter video path"))
        videoInformation(videopath)
        #convertion4k(videopath)
        #convertion6k(videopath)
        #cropInputFile(videopath)
        input("Press any button to exit")
    else:
        print("Module Not Found - " + str(module_exists("ffmpeg")))
        input("Press any button to exit")
        

if __name__ == "__main__":
    main()
