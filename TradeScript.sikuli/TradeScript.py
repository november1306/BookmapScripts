
LOAD_TIMEOUT = 30
OPEN_TIMEOUT = 15
FEED_NAME = 'feed_Rithmic_20160923_133501_092.bmf'


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

def openTradePanel ():
    wait()
    


