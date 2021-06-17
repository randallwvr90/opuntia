import time
import os

class TimeLapseService():
    def __init__(self, pauseTime: int, frames: int):
        self.pauseTime = pauseTime
        self.frames = frames
    
    def captureImage(self, imgNumber):
        imgNumber = str(imgNumber).zfill(3)
        os.system("raspistill -o images/image%s.jpg"%(imgNumber))

    def mainLoop(self):
        thisFrame = 0
        while thisFrame < self.frames:
            self.captureImage(thisFrame)
            thisFrame += 1
            time.sleep(self.pauseTime - 6) #Takes roughly 6 seconds to take a picture
        print("Time Lapse complete with {} frames captured".format(str(self.frames)))