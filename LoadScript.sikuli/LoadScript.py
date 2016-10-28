import org.sikuli.script.TextRecognizer as TR
import sharedLib
reload (sharedLib)

#Settings.OcrReadText = True
#Settings.OcrTextRead = True; 
#Settings.OcrTextSearch = True;
Settings.OcrLanguage = "eng"
TR.reset()

#define settings
ADD_FEED_DURATION = 2*60
WAIT_BEFORE_ACTIONS = 10
WAIT_BETWEEN_ACTIONS = 5
DEF_BLACK_CUT_OFF = 30
DEF_WHITE_CUT_OFF = 70
LOAD_TIMEOUT = 30
OPEN_TIMEOUT = 15

FEED_LIST = ['feed_Rithmic_20160923_133501_092.bmf', 
        'feed_Rithmic_20160926_081021_103.bmf', 
        'feed_Rithmic_20160928_103103_012.bmf',
        'feed_Rithmic_20160923_133501_092.bmf',
        'feed_Rithmic_20160926_081021_103.bmf', 
        'feed_Rithmic_20160928_103103_012.bmf',
        ]



#create log file 
scriptDir = getBundlePath() 
sharedLib.LoggingSetup (scriptDir)
#END setup preconditions

appNP = App.open("c:\\Program Files\\Bookmap\\BookMap.exe")

waitVanish("1475603091673.png",LOAD_TIMEOUT)

wait("1475603119776.png",LOAD_TIMEOUT)

click("1475603134007.png")

wait("1475603164180.png",OPEN_TIMEOUT)
BMAppInst = App.focus("Bookmap")


for feedName in FEED_LIST:
    sharedLib.OpenFeedInsert (feedName)
    waitVanish("1475603255052.png",LOAD_TIMEOUT)
    wait (WAIT_BEFORE_ACTIONS)
    sharedLib.MaxContrast()
    wait(WAIT_BETWEEN_ACTIONS)
    sharedLib.MinContrast()
    wait(WAIT_BETWEEN_ACTIONS) 
    sharedLib.setBlackCutOff (DEF_BLACK_CUT_OFF)
    wait(WAIT_BETWEEN_ACTIONS) 
    sharedLib.setWhiteCutOff (DEF_WHITE_CUT_OFF)
    wait(WAIT_BETWEEN_ACTIONS)   
    sharedLib.resetContrastDefault()
    wait(ADD_FEED_DURATION)

BMAppInst.close()
exit()


#register observer for feed end
feedEndRegion=wait("RAY.png",30).bellow(200)

def feedEndHandler(event):
    popup("end of the feed")
    feedEndRegion.stopObserver()
    exit()
#feedEndRegion.onAppear("1477268904338.png" #, feedEndHandler) # or any other onEvent()
#feedEndRegion.observe(FOREVER) # observes for 10 seconds

click("1475659041267.png")
popup("THE END")

exit()
