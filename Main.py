import ffmpeg
#using https://github.com/kkroening/ffmpeg-python
# API refence https://kkroening.github.io/ffmpeg-python/

#functions to use - ffmpeg.trim
# generate thumbnail on github
#custom filters

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

def main():
    videoInformation("Waterfall")
    #convertion4k("Waterfall")
    #convertion6k("Waterfall")
    #cropInputFile('Waterfall')

if __name__ == "__main__":
    main()
