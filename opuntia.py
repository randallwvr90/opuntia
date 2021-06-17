import os
import time
from timeLapseService import TimeLapseService

class TimeLapse():
    pass

def main():
    #Constants
    FRAMES = 5
    PAUSE_TIME = 6

    tls = TimeLapseService(pauseTime = PAUSE_TIME, frames = FRAMES)
    tls.mainLoop()

if __name__ == "__main__":
    main()
