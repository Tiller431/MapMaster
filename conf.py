import os

def getConf(getVariable):

    # Open the conf file
    with open("conf.txt", "r") as i:
        conf = i.readlines()

    for line in conf:
        try:
            variable = line.split("=")[0]
            value = line.split("=")[1]
        except:
            pass
        if variable == getVariable:
            return value