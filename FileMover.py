import shutil
import os
from os import listdir
import time

sourcePath = ""
destinationPath = ""

#Currently set to 24 hours ago. This can be used later to accept a user entered time for validating if a file should be moved or not.
moveTime = time.time() - 86400

#checks the source and destination paths given to ensure they are valid and not equal to each other
def validatePath(path):
    if (sourcePath == destinationPath):
        print("Source and destination are the same. Exiting")
        exit()
    else:
        if (os.path.exists(path)):
            return ("Valid path:  ")
        else:
            return ("invalid path. Exiting")
            exit()

#prompt for source path
sourcePath = raw_input("Enter the path of the source folder: ")
validatePath(sourcePath)
print(validatePath(sourcePath) + sourcePath)

#prompt for destination path
destinationPath = raw_input("Enter the path of the destination folder: ")
validatePath(destinationPath)
print(validatePath(destinationPath) + destinationPath)

filesInFolder = listdir(sourcePath)

for i in filesInFolder:
    fileCreateTime = os.path.getctime(sourcePath + "\\" + i)
    if (fileCreateTime < moveTime):
        shutil.move((sourcePath + "\\" + i), (destinationPath + "\\" + i))
        print(i + "\nhas been moved.\n")
    else:
        print(i + "\nhas not been moved.\n")

