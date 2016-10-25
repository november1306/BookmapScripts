#definable functions
from sikuli import *
import os

LOAD_TIMEOUT = 30
OPEN_TIMEOUT = 10


#simple import check
def printme( str ):
   popup (str)
   return;

def LoggingSetup(scriptDir):
    #create log file 
    newDir = "logs"; 
    makeDir = os.path.join(scriptDir, newDir);
    if not os.path.exists(makeDir): os.mkdir(makeDir);

    timestring = time.strftime ('%d-%m_%H-%M-%S')
    logsFile = scriptDir + '\\logs\\' + timestring + '.txt'
    #Debug.setUserLogFile(logsFile) 
    Debug.setLogFile (logsFile)

    Settings.ActionLogs = True
    Settings.InfoLogs = True
    Settings.UserLogs = True 
    Settings.UserLogPrefix =os.path.basename(scriptDir)
    Settings.UserLogTime = True
    Settings.DebugLogs = True
    Debug.on(3)
    Debug.log (3, "custom debug message with verb =3")
    Debug.user("beginning of the script")
    Debug.log (1, "custom debug message with verb = 1")
    return;    

def OpenFeedOCR (FEED_MASK):
    click("1475603183991.png")
    feedDialogRegion = wait("1475603222733.png",OPEN_TIMEOUT)
    feedNameRegion = feedDialogRegion.right(400).below(300).wait(FEED_MASK,10)
    #recognizedText =feedDialogRegion.right(400).below(300).text()
    doubleClick(feedNameRegion)
    return;

def OpenFeedInsert (feedName):
    click("LOADFEEDFILE-1.png")
    feedDialogRegion = wait("1475603222733.png",30)
    paste(feedName)
    click("2.png")
    return;

def PinTimer(str2):
    if not exists("1475603309931.png"):
        hover(Pattern("1477429072242.png").targetOffset(-1,15))
        
        wait(3)
        hover("1477426483292.png")
        click("1477426483292.png")
        return;

#not tested
def recognizeAllText (inRegion):
    #imgWithText = Image.create(capture(feedNameRegion)) # creates in memory image of the given region
    #imgWithText1 = Image(imgWithText.resize(3)) # resizes the image with the given factor as decimal number
    #imgWithText2 = Image.convertImageToGrayscale(imgWithText1)
    #recognizedText = imgWithText1.text()
    #popup(recognizedText)
    return;