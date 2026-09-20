from helpers import *
ApplicationRun = False

if __name__ == '__main__':
    initializeFunction = initialize()
    if initializeFunction[0] == "1":
        ApplicationRun = True
    else:
        print(initializeFunction)
    Main(ApplicationRun)