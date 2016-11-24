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

wait("1475603164180.png",OPEN_TIMEOUT)
BMAppInst = App.focus("Bookmap")
sharedLib.checkUpdate (0)
#open feed
sharedLib.OpenFeedInsert (FEED_MASK)
#wait for timeline goes top right side
wait(30)
popup("time to get region")
tradePanelRegion = getTradePanelRegion()
#1
popup("run scr #1")
addSellOrderASK(tradePanelRegion)
#2
popup("run scr #2")
addSellOrderBID(tradePanelRegion)
#3
addBuyOrderBID(tradePanelRegion)
#4
addBuyOrderMKT(tradePanelRegion)
#5
cancelOrder(tradePanelRegion)
#6
cancelAllOrders (tradePanelRegion)


#run scripts
click("1475659041267.png")