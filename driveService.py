import os

class DriveService():
    def push(self, fileName: str) -> int:
        outPut = os.system("drive push -no-prompt {}".format(fileName))
        return outPut