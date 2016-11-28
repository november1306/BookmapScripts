import placeOrderLib
reload (placeOrderLib)
import sharedLib
reload (sharedLib)
#define settings
FEED_MASK ="feed_Rithmic_20160923_133501_092.bmf"  #enter unique part of feed file name 
LOAD_TIMEOUT = 30
OPEN_TIMEOUT = 10
#END setup preconditions

sharedLib.LoggingSetup(getBundlePath())

App.open("c:\\Program Files\\Bookmap\\BookMap.exe")

waitVanish("1475603091673.png",LOAD_TIMEOUT+30)

wait("1475603119776.png",LOAD_TIMEOUT)

click("1475603134007.png")
sharedLib.checkUpdate (0)
wait("1475603164180.png",OPEN_TIMEOUT)
BMAppInst = App.focus("Bookmap")
#sharedLib.checkUpdate (0)
#open feed
sharedLib.OpenFeedInsert (FEED_MASK)
#wait for timeline goes top right side
wait(Pattern("1480034729663.png").targetOffset(0,200),10)
wheel(Pattern("1480034729663.png").targetOffset(0,200),WHEEL_UP,6)
wait(3)
wheel(Pattern("1480034729663.png").targetOffset(0,200),WHEEL_DOWN,6)



tradePanelRegion = placeOrderLib.getTradePanelRegion()
Debug.user("stopOrderPlacement default start #1")
placeOrderLib.stopOrderPlacement(tradePanelRegion, 'MKT', "0")
Debug.user("stopOrderInvalid start #2")
placeOrderLib.stopOrderInvalid(tradePanelRegion)
Debug.user("stopOrderPlacement LMT start #3")
placeOrderLib.stopOrderPlacement(tradePanelRegion, "LMT", "0")
Debug.user("stopOrderPlacement LMT positive offset start #4")
placeOrderLib.stopOrderPlacement(tradePanelRegion, "LMT", "15+")
Debug.user("stopOrderPlacement LMT negative offset start #5")
placeOrderLib.stopOrderPlacement(tradePanelRegion, "LMT", "25-")
    
click("1475659041267.png")    
    