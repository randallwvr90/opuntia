from driveService import DriveService
import time
import os

class TimeLapseService():
    def __init__(self, pauseTime: int, frames: int):
        self.pauseTime = pauseTime
        self.frames = frames
    
    def captureImage(self, imgNumber):
        imgNumber = str(imgNumber).zfill(3)
        errorCode = os.system("raspistill -o images/image%s.jpg"%(imgNumber))
        if errorCode > 0:
            raise Exception("No image captured")

    def mainLoop(self):
        # gets images, calls driveService object method push() to send to google drive
        gdrive = DriveService()
        thisFrame = 0
        while thisFrame < self.frames:
            self.captureImage(thisFrame)
            fileName = 'image{}.jpg'.format(time.time())
            thisFrame += 1
            startTime = time.time()
            errorCode = gdrive.push(fileName)
            endTime = time.time()
            print('push took{s} seconds and returned error code {e}'.format(s=str(endTime - startTime)),e=errorCode)
            time.sleep(self.pauseTime - 6) #Takes roughly 6 seconds to take a picture - how does this square with drive?
        print("Time Lapse complete with {} frames captured".format(str(self.frames)))