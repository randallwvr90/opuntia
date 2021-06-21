import os

class DriveService():
    def push(self, fileName: str) -> int:
        output = os.system("drive push -no-prompt {}".format(fileName))
        return output