from driveService import DriveService
import time
import os

class TimeLapseService():
    def __init__(self, pauseTime: int, frames: int):
        self.pauseTime = pauseTime
        self.frames = frames
    
    def captureImage(self, imgNumber) -> str:
        fileName = 'image{}.jpg'.format(str(imgNumber).zfill(3))
        errorCode = os.system("raspistill -o images/{}".format(fileName))
        if errorCode > 0:
            raise Exception("No image captured")
        return fileName

    def mainLoop(self):
        # gets images, calls driveService object method push() to send to google drive
        gdrive = DriveService()
        thisFrame = 0
        while thisFrame < self.frames:
            fileName = self.captureImage(thisFrame)
            thisFrame += 1
            startTime = time.time()
            errorCode = gdrive.push(fileName)
            endTime = time.time()
            print('push took{s} seconds and returned error code {e}'.format(s=str(endTime - startTime)),e=errorCode)
            time.sleep(self.pauseTime - 6) #Takes roughly 6 seconds to take a picture - how does this square with drive?
        print("Time Lapse complete with {} frames captured".format(str(self.frames)))