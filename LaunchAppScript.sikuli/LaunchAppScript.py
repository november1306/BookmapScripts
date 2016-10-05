import shutil
import org.sikuli.script
import os
import time

#setup preconditions

LOAD_TIMEOUT = 30
OPEN_TIMEOUT = 10

#create log file 
scriptDir = getBundlePath() 
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
#END setup preconditions

App.open("c:\\Program Files\\Bookmap\\BookMap.exe")

waitVanish("1475603091673.png",LOAD_TIMEOUT)

wait("1475603119776.png",LOAD_TIMEOUT)

click("1475603134007.png")

wait("1475603164180.png",OPEN_TIMEOUT)
BMAppInst = App.focus("Bookmap")

click("1475603183991.png")

wait("1475603222733.png",OPEN_TIMEOUT)

doubleClick("1475603236761.png")

waitVanish("1475603255052.png",LOAD_TIMEOUT)
wait("1475603278871.png",LOAD_TIMEOUT)

if not exists("1475603309931.png"):
    hover("1475603331773.png")
    wait(3)
    hover("1475603309931.png")
    click("1475603309931.png")
  
timerRegion = find("1475603411229.png")

Settings.WaitScanRate = 20
Settings.ObserveScanRate = 20 #search image 20 times per second
Settings.MoveMouseDelay = 0
timerRegion.right(100).wait(Pattern("1475603530318.png").similar(0.95),60)
print("13:35:30 recognized")

click("1475603581514.png") 

BookmapWindow = App.focusedWindow()
regionImage = capture(BookmapWindow)
shutil.move(regionImage, os.path.join(r'E:\Projects\Sikuli\screenshots', 'scr1.png'))

click("1475603626004.png")

print("wait for 13:36:10 ")

wait(40)
#click(Pattern("1475494291644.png").targetOffset(7,18))

click(Pattern("1475658917551.png").targetOffset(-18,21))
click("1475603581514.png")

BookmapWindow = App.focusedWindow()
regionImage = capture(BookmapWindow)
shutil.move(regionImage, os.path.join(r'E:\Projects\Sikuli\screenshots', 'scr2.png'))

wait(5)

click("1475603626004.png")

print("rewind back to 13:35:30 ")

wait(3)

#BMAppInst = App.focus("Bookmap Replay")
#BMAppInst.close()
click("1475659041267.png")

wait(5)




        



