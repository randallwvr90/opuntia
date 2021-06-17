import os
import time

#Constants
FRAMES = 5
PAUSE_TIME = 6

#Take some images spaced evenly by PAUSE_TIME
thisFrame = 0
while thisFrame < FRAMES:
    imgNumber = str(thisFrame).zfill(3)
    os.system("raspistill -o image%s.jpg"%(imgNumber))
    thisFrame += 1
    time.sleep(PAUSE_TIME - 6) #Takes roughly 6 seconds to take a picture