import json
import sys
import os
import cv2

from converters.json_converter import transformJson2Obj


def start(file, fileName):
    #read the file
    file = open(file, "r")
    fileContent = file.read()
    file.close()

    #convert to json
    jsonContent = json.loads(fileContent)

    #convert to obj
    objContent, mtlContent, textureImages = transformJson2Obj(fileName, jsonContent)

    #write the obj file
    objFile = open("../output/" + fileName + ".obj", "w")
    objFile.write(objContent)
    objFile.close()

    #write the mtl file
    mtlFile = open("../output/" + fileName + ".mtl", "w")
    mtlFile.write(mtlContent)
    mtlFile.close()

    #write the texture file
    for i in range(len(textureImages)):
        imageName = "../output/" + textureImages[i][0] + str()+ ".png"
        cv2.imwrite(imageName, textureImages[i][1])
    



help = """
    Usage: json2obj ./resources/<input-file>.json
"""

if __name__ == "__main__":
    #get the arguments from the command line
    args = sys.argv[1:]
    #check if there is any argument
    if len(args) == 0:
        raise Exception("No arguments given. please use -h for help.")

    #check if the first argument is help option
    if args[0] == "-h":
        print(help)
        exit(0)
    #check if the first argument is a valid file
    if not os.path.isfile(args[0]):
        raise Exception("The input file file is not valid.")
        
    #get a file name without extension
    fileName = os.path.splitext(args[0])[-2]

    #remove the path from the file name
    fileName = fileName.split("/")[-1]

    start(args[0], fileName)