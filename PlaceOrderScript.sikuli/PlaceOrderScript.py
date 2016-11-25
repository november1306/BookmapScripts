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
wheel(Pattern("1480034729663.png").targetOffset(0,200),WHEEL_UP,5)
wait(10)
wheel(Pattern("1480034729663.png").targetOffset(0,200),WHEEL_DOWN,5)

tradePanelRegion = placeOrderLib.getTradePanelRegion()
Debug.user("addSellOrderASK start #1")
placeOrderLib.addSellOrderASK(tradePanelRegion)
Debug.user("addSellOrderBID start #2")
placeOrderLib.addSellOrderBID(tradePanelRegion)
Debug.user("addBuyOrderBID start #3")
placeOrderLib.addBuyOrderBID(tradePanelRegion)
Debug.user("addBuyOrderMKT start #4")
placeOrderLib.addBuyOrderMKT(tradePanelRegion)
Debug.user("cancelOrder start #5")
placeOrderLib.cancelOrder(tradePanelRegion)
Debug.user("cancelAllOrders start #6")
placeOrderLib.cancelAllOrders (tradePanelRegion)


#run scripts
click("1475659041267.png")