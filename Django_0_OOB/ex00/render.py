import sys
import os
import re

def render(fileName):
    if not fileName.endswith(".template") or not os.path.isfile(fileName):
        exit("Argument file is not a template or do not exist")
    if not os.path.isfile("settings.py"):
        exit("settings.py do not exist")

    settingsValues = []

    with open("settings.py", "r") as settings:
        for args in settings:
            settingsValues.append(args.replace("\"", "").strip().split("="))
    for i in range(len(settingsValues)):
        settingsValues[i][0] = settingsValues[i][0].strip()
        settingsValues[i][1] = settingsValues[i][1].strip()

    # if not os.path.isfile("MyCv.html"):
    #     open("MyCv.html", "x")

    with open("MyCv.html", "w") as html, open(fileName, "r") as template:
        for line in template:
            for i in range(len(settingsValues)):
                line = line.replace("{" + settingsValues[i][0] + "}", settingsValues[i][1])
            html.write(line)

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            exit("Wrong numbers of arguments")
        render(sys.argv[1])
    except Exception as e:
        print(str(e))