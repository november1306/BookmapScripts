import org.sikuli.script.TextRecognizer as TR
import sharedLib
reload (sharedLib)

#Settings.OcrReadText = True
#Settings.OcrTextRead = True; 
#Settings.OcrTextSearch = True;
Settings.OcrLanguage = "eng"
TR.reset()

#define settings
FEED_LIST = ['feed_Rithmic_20160923_133501_092.bmf', 
        'feed_Rithmic_20160926_081021_103.bmf', 
        'feed_Rithmic_20160928_103103_012.bmf',
        'feed_Rithmic_20160923_133501_092.bmf',
        'feed_Rithmic_20160926_081021_103.bmf', 
        'feed_Rithmic_20160928_103103_012.bmf',
        ]
LOAD_TIMEOUT = 30
OPEN_TIMEOUT = 15


#create log file 
scriptDir = getBundlePath() 
sharedLib.LoggingSetup (scriptDir)
#END setup preconditions

appInst = App.open("c:\\Program Files\\Bookmap\\BookMap.exe")

waitVanish("1475603091673.png",LOAD_TIMEOUT)

wait("1475603119776.png",LOAD_TIMEOUT)

click("1475603134007.png")

wait("1475603164180.png",OPEN_TIMEOUT)
BMAppInst = App.focus("Bookmap")



#for feedName in FEED_LIST:
sharedLib.OpenFeedInsert (feedName)

waitVanish("1475603255052.png",LOAD_TIMEOUT)
wait("1475603278871.png",LOAD_TIMEOUT)
    
   

def MaxContrast():
    wait("1477431878684.png", OPEN_TIMEOUT) 
    click("1477431878684.png")
    blackCutRegion = wait("BLACKCUTOFF-1.png",OPEN_TIMEOUT).below(100)
    blackCutRegion.highlight(3)
    .click(Pattern("1477433135713.png").targetOffset(2,-9))
    blackCutRegion.dragDrop("1477434403943.png", Pattern("1477433135713.png").targetOffset(2,-9))
    
    wait(3)
    return;

MaxContrast()


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
