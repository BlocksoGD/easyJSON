import json

#easyJSON v1.0
#Open to suggestions and improvements!
## NOTE: This module does not handle exceptions. Use try/except in your code.

def getJson(path):
    with open(path, "r") as file:
        return json.load(file)

def writeJson(data, path, indent=0, returnMessage = False):
    with open(path, "w") as file:
        json.dump(data, file, indent=indent)
        if returnMessage:
            print("Successfully saved!")

#MADE BY BLOCKSO