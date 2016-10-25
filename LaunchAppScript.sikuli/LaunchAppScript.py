import sharedLib
reload (sharedLib)
import shutil
import org.sikuli.script
import os
import time


#define settings
FEED_MASK ="3501"  #enter unique part of feed file name 
LOAD_TIMEOUT = 30
OPEN_TIMEOUT = 10
#END setup preconditions

sharedLib.LoggingSetup(getBundlePath())

App.open("c:\\Program Files\\Bookmap\\BookMap.exe")

waitVanish("1475603091673.png",LOAD_TIMEOUT)

wait("1475603119776.png",LOAD_TIMEOUT)

click("1475603134007.png")

wait("1475603164180.png",OPEN_TIMEOUT)
BMAppInst = App.focus("Bookmap")

#open feed
sharedLib.OpenFeedOCR (FEED_MASK)


waitVanish("1475603255052.png",LOAD_TIMEOUT)
wait("1475603278871.png",LOAD_TIMEOUT)

#sharedLib.PinTimer()

  
timerRegion = find(Pattern("1475603411229.png").similar(0.50))

Settings.WaitScanRate = 20
Settings.ObserveScanRate = 20 #search image 20 times per second
Settings.MoveMouseDelay = 0
timerRegion.right(100).wait(Pattern("1475603530318.png").similar(0.95),60)
print("13:35:30 recognized")

click("1477429729088.png")  

BookmapWindow = App.focusedWindow()
regionImage = capture(BookmapWindow)
shutil.move(regionImage, os.path.join(r'E:\Projects\Sikuli\reports\screenshots', 'scr1.png'))

click()

print("wait for 13:36:10 ")

wait(40)
#click(Pattern("1475494291644.png").targetOffset(7,18))

click(Pattern("1475658917551.png").targetOffset(-18,21))
click("1477429729088.png")

BookmapWindow = App.focusedWindow()
regionImage = capture(BookmapWindow)
shutil.move(regionImage, os.path.join(r'E:\Projects\Sikuli\reports\screenshots', 'scr2.png'))

wait(5)

click("1477429771364.png")

print("rewind back to 13:35:30 ")

wait(3)

#BMAppInst = App.focus("Bookmap Replay")
#BMAppInst.close()
click("1475659041267.png")

wait(5)




        



