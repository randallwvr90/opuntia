from timeLapseService import TimeLapseService

# drive push -no-prompt <filepath>
# this is the shell command to push a file to the google drive. I think it might need to be done 
# with the working directory set to the initialized google drive directory - so that might need
# to be opuntia/

def main():
    #Constants
    FRAMES = 200
    PAUSE_TIME = 120

    tls = TimeLapseService(pauseTime = PAUSE_TIME, frames = FRAMES)
    tls.mainLoop()

if __name__ == "__main__":
    main()
