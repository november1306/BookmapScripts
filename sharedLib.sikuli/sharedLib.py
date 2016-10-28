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
    click("1477614423279.png")
    wait("Qpenfeedfile.png",3)
    click("Qpenfeedfile.png")
    
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

def getPID (appInst):
    appPID = int(str(appInst).split(":",1)[0].replace("[",""))
    return appPID; 

#Automatic contrast configuration, drag all bars to maximum
def MaxContrast():
    wait("1477431878684.png", OPEN_TIMEOUT) 
    click("1477431878684.png")
    blackCutRegion = wait("BLACKCUTOFF.png",OPEN_TIMEOUT).below(120)
    blackCutRegion.dragDrop("1477434403943.png", Pattern("1477433135713.png").targetOffset(2,-9))

    whiteCutRegion = wait("WHITECUTOFF.png").below(120)
    whiteCutRegion.dragDrop("LJ.png", Pattern("1477435166053.png").targetOffset(-1,-10))

    contrastRegion = wait("1477435003455.png")
    contrastRegion.setX(contrastRegion.getX()-200) 
    contrastRegion.setW(contrastRegion.getW()+400)      
    contrastRegion.setH(contrastRegion.getH()+100)                   
    contrastRegion.dragDrop("LJ.png", Pattern("1477435166053.png").targetOffset(-1,-10))

    largeSizeRegion = wait("LARGESIZEHIG.png")
    largeSizeRegion.setX(largeSizeRegion.getX()-200) 
    largeSizeRegion.setW(largeSizeRegion.getW()+350)      
    largeSizeRegion.setH(largeSizeRegion.getH()+100)          
    largeSizeRegion.dragDrop("LJ.png", Pattern("1477435166053.png").targetOffset(-1,-10))

    brightnessRegion = wait("1477436676009.png")
    brightnessRegion.setX(brightnessRegion.getX()-200) 
    brightnessRegion.setW(brightnessRegion.getW()+400)      
    brightnessRegion.setH(brightnessRegion.getH()+100)          
    brightnessRegion.dragDrop("LJ.png", Pattern("1477435166053.png").targetOffset(-1,-10))

    click(Pattern("DAdjustautom.png").targetOffset(-69,-3))
    

    dialogHeaderRegion = wait("ContrastConf.png",10).right(350)
    dialogHeaderRegion.click("1477436564410.png")
    return;

#Automatic contrast configuration, drag all bars to minimum
def MinContrast():
    wait("1477431878684.png", OPEN_TIMEOUT) 
    click("1477431878684.png")
    blackCutRegion = wait("BLACKCUTOFF.png",OPEN_TIMEOUT).below(120)
    blackCutRegion.dragDrop(Pattern("1477434403943.png").similar(0.55), Pattern("1477525549788.png").similar(0.81).targetOffset(0,-9))

    whiteCutRegion = wait("WHITECUTOFF.png").below(120)
    whiteCutRegion.dragDrop("LJ.png", Pattern("1477525492625.png").similar(0.81).targetOffset(-1,-11))

    contrastRegion = wait("1477435003455.png")
    contrastRegion.setX(contrastRegion.getX()-200) 
    contrastRegion.setW(contrastRegion.getW()+400)      
    contrastRegion.setH(contrastRegion.getH()+100)          
    contrastRegion.dragDrop("LJ.png", Pattern("1477525549788.png").similar(0.81).targetOffset(0,-9))

    largeSizeRegion = wait("LARGESIZEHIG.png")
    largeSizeRegion.setX(largeSizeRegion.getX()-200) 
    largeSizeRegion.setW(largeSizeRegion.getW()+350)      
    largeSizeRegion.setH(largeSizeRegion.getH()+100)          
    largeSizeRegion.dragDrop("LJ.png", Pattern("1477525549788.png").similar(0.81).targetOffset(0,-9))

    brightnessRegion = wait("1477436676009.png")
    brightnessRegion.setX(brightnessRegion.getX()-200) 
    brightnessRegion.setW(brightnessRegion.getW()+400)      
    brightnessRegion.setH(brightnessRegion.getH()+100)          
    brightnessRegion.dragDrop("LJ.png", Pattern("1477525549788.png").similar(0.81).targetOffset(0,-9))

    dialogHeaderRegion = wait("ContrastConf.png",10).right(350)
    dialogHeaderRegion.click("1477436564410.png")
    return;

def setBlackCutOff (size):
    wait("1477431878684.png", OPEN_TIMEOUT) 
    click("1477431878684.png")
    blackCutRegion = wait("BLACKCUTOFF.png",OPEN_TIMEOUT).below(120)
    blackCutRegion.click(Pattern("DExactsixe.png").targetOffset(-34,4))
    blackCutRegion.click(Pattern("1477596245682.png").similar(0.80))
    type(Key.BACKSPACE, KEY_CTRL) #clear before input
    type(str(size))

    dialogHeaderRegion = wait("ContrastConf.png",10).right(350)
    dialogHeaderRegion.click("1477436564410.png")
    return;    

def setWhiteCutOff (size):
    wait("1477431878684.png", OPEN_TIMEOUT) 
    click("1477431878684.png")
    blackCutRegion = wait("BLACKCUTOFF.png",OPEN_TIMEOUT).below(120)
    blackCutRegion.click(Pattern("DExactsixe.png").targetOffset(-34,4))
    blackCutRegion.click(Pattern("1477596245682.png").similar(0.80))
    type(Key.BACKSPACE, KEY_CTRL) #clear before input
    type(str(size))

    dialogHeaderRegion = wait("ContrastConf.png",10).right(350)
    dialogHeaderRegion.click("1477436564410.png")
    return;      

def resetContrastDefault():
    wait("1477431878684.png", OPEN_TIMEOUT) 
    click("1477431878684.png")
    blackCutRegion = wait("BLACKCUTOFF.png",OPEN_TIMEOUT).below(120)
    blackCutRegion.highlight(1)    
    if blackCutRegion.exists(Pattern("IExact.png").similar(0.95),10):
        blackCutRegion.click(Pattern("IExact.png").similar(0.95).targetOffset(-20,1),10)
  
    blackCutRegion.dragDrop(Pattern("1477434403943.png").similar(0.55), Pattern("1477608116192-1.png").similar(0.85).targetOffset(-1,-9))

    whiteCutRegion = wait("WHITECUTOFF.png").below(120)
    whiteCutRegion.highlight(1)
    if whiteCutRegion.exists(Pattern("IExact.png").similar(0.95),10):
        whiteCutRegion.click(Pattern("IExact.png").similar(0.95).targetOffset(-16,-1),10)
    whiteCutRegion.dragDrop("LJ.png", Pattern("1477608490907-1.png").similar(0.85).targetOffset(-1,-9))

    contrastRegion = wait("1477435003455.png")
    contrastRegion.setX(contrastRegion.getX()-200) 
    contrastRegion.setW(contrastRegion.getW()+400)      
    contrastRegion.setH(contrastRegion.getH()+100)          
    contrastRegion.highlight(1)
    contrastRegion.dragDrop("LJ.png", Pattern("1477608610890-1.png").similar(0.85).targetOffset(-1,-11))

    largeSizeRegion = wait("LARGESIZEHIG.png")
    largeSizeRegion.setX(largeSizeRegion.getX()-200) 
    largeSizeRegion.setW(largeSizeRegion.getW()+350)      
    largeSizeRegion.setH(largeSizeRegion.getH()+100)          
    largeSizeRegion.highlight(3)
    largeSizeRegion.dragDrop("LJ.png", Pattern("1477608610890-1.png").similar(0.85).targetOffset(-1,-11))

    brightnessRegion = wait("1477436676009.png")
    brightnessRegion.setX(brightnessRegion.getX()-200) 
    brightnessRegion.setW(brightnessRegion.getW()+400)      
    brightnessRegion.setH(brightnessRegion.getH()+100)          
    brightnessRegion.highlight(3)
    brightnessRegion.dragDrop("LJ.png", Pattern("1477608610890-1.png").similar(0.85).targetOffset(-1,-11))

    if exists(Pattern("Adjustautoma.png").similar(0.98)):
        click(Pattern("Adjustautoma.png").targetOffset(-138,-2))

    dialogHeaderRegion = wait("ContrastConf.png",10).right(350)
    dialogHeaderRegion.click("1477436564410.png")
    return;

def 
#not tested
def recognizeAllText (inRegion):
    #imgWithText = Image.create(capture(feedNameRegion)) # creates in memory image of the given region
    #imgWithText1 = Image(imgWithText.resize(3)) # resizes the image with the given factor as decimal number
    #imgWithText2 = Image.convertImageToGrayscale(imgWithText1)
    #recognizedText = imgWithText1.text()
    #popup(recognizedText)
    return;

#resetContrastDefault()
