import shutil
import os
from os import listdir

sourcePath=""
destinationPath=""

def validatePath(path):
    if(sourcePath == destinationPath):
        exit()
    else:
        if(os.path.exists(path)):
            return("path is valid")
        else:
            return("invalid path")

print("Welcome to File Automation Recursive Copy Utility or FARCU for short.")


sourcePath = input("Enter the path of the source folder: ")
validatePath(sourcePath)
print(validatePath(sourcePath)+":  "+sourcePath)

destinationPath = input("Enter the path of the destination folder: ")
validatePath(destinationPath)
print(validatePath(destinationPath)+":  "+destinationPath)

filesInFolder = listdir(sourcePath)
print(filesInFolder)

for i in filesInFolder:
    print(filesInFolder[i])
    #currentFile = sourcePath + "\\" + files[i]
    #print(currentFile)