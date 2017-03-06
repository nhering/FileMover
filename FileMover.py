import shutil
import os
from os import listdir

sourcePath = ""
destinationPath = ""


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


sourcePath = raw_input("Enter the path of the source folder: ")
validatePath(sourcePath)
print(validatePath(sourcePath) + sourcePath)

destinationPath = raw_input("Enter the path of the destination folder: ")
validatePath(destinationPath)
print(validatePath(destinationPath) + destinationPath)

filesInFolder = listdir(sourcePath)

for i in filesInFolder:
    print(sourcePath + "\\" + i)
    shutil.move((sourcePath + "\\" + i), (destinationPath + "\\" + i))
