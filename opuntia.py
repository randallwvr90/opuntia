import os
import time
from timeLapseService import TimeLapseService

class TimeLapse():
    pass

def main():
    print("sup")
    #Constants
    FRAMES = 5
    PAUSE_TIME = 6

    tls = TimeLapseService(pauseTime = PAUSE_TIME, frames = FRAMES)
    tls.mainLoop()

   """  #Take some images spaced evenly by PAUSE_TIME
    thisFrame = 0
    while thisFrame < FRAMES:
        imgNumber = str(thisFrame).zfill(3)
        os.system("raspistill -o images/image%s.jpg"%(imgNumber))
        thisFrame += 1
        time.sleep(PAUSE_TIME - 6) #Takes roughly 6 seconds to take a picture """

if __name__ == "__main__":
    main()
