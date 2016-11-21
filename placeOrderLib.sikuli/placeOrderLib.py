from sikuli import *
import os
import org.sikuli.script.Pattern;



#Settings.OcrLanguage = "eng"


LOAD_TIMEOUT = 30
OPEN_TIMEOUT = 10


#enables Trade Panel and returns it's region
def getTradePanelRegion ():    
    if not exists("1477910269941.png",):
        click("1477910302441.png",OPEN_TIMEOUT)
    tradePanelRegion = find("1477910581517.png")  
    tradePanelRegion.setH(tradePanelRegion.getH() + 800)    
    tradePanelRegion.highlight(2)

    if not tradePanelRegion.exists(Pattern("IEnable.png").similar(0.80)):
        tradePanelRegion.click(Pattern("IEnable-1.png").targetOffset(-27,-1)) 
    return tradePanelRegion; #TPRegion will be used for further operations with TP     

#AFTER FEED OPEN WAIT 5 MIN BEFORE USING THIS  
#returns region right from timeLine where user can click to put orders.
def getTradeArea():
    lineRegion = wait (Pattern("1478386010109.png").similar(0.75),10).left(100).below(60)
    lineRegion.highlight(3)
    timeLineRegion = lineRegion.wait(Pattern("1478387010276.png").similar(0.90),10).right(100).below(500)
    timeLineRegion.setX(timeLineRegion.getX() - 10) 
    timeLineRegion.highlight(3)
    return timeLineRegion;

#returns area with market level for placing orders. PAUSES PLAYBACK!
def getBidArea(timeLineRegion): 
    Settings.MoveMouseDelay = 0
    while True:
        try: 
            click(Pattern("1478746737653.png").similar(0.90))
        except:
            pass
        bidPattern = timeLineRegion.wait(Pattern("1478733458555-1.png").similar(0.51),50)
        bidPattern.highlight(2)
      
        try: 
            click("1478551379630-1.png")
        except:
            pass
        if bidPattern.nearby(2).exists(Pattern("1478733458555-1.png").similar(0.85),5):
            break
        
    return bidPattern;   


#ASK(sell) and verify position, number of contracts, opened sell orders
def addSellOrderASK(tradePanelRegion):
    accumulatedRegion = tradePanelRegion.wait("1478030812087.png",OPEN_TIMEOUT).right(100)
    accumPositionBefore = accumulatedRegion.text()
    tradedContractsRegion = tradePanelRegion.wait("1478043916673.png",OPEN_TIMEOUT).right(100)
    tradedContractsBefore = tradedContractsRegion.text()    
    tradedContractsRegion.highlight(3)

    tradePanelRegion.click("1478029829596.png")
    tradePanelRegion.type(Pattern("1478029885384.png").targetOffset(37,-2), "30")
    ordersRegion = tradePanelRegion.wait("CANCELALL.png").above(50) 
    tradeArea = getTradeArea()
    bidPattern = getBidArea(tradeArea)
    bidPattern.setTargetOffset(0,-10)
    bidPattern.highlight(3)
    rightClick(bidPattern)
    wait(2)
    click("1478732151936.png",10)
    if not tradeArea.exists(Pattern("1478734503292.png").similar(0.90),3):
        popup("should be 300 bids in bids region") 
    if not ordersRegion.exists(Pattern("1478539208452.png").similar(0.90),3):
        popup("should be 300 opened sell orders")    
    accumPositionAfter = accumulatedRegion.text()
    tradedContractsAfter = tradedContractsRegion.text()
    if (accumPositionBefore != accumPositionAfter):
        popup ("Accumulated position before ASK " + str(accumPositionBefore) + "; after " + str(accumPositionAfter))
    if (tradedContractsAfter != tradedContractsBefore):
        popup ("Trade contracts before ASK " + str(tradedContractsBefore) + "; after " + str(tradedContractsAfter))    
    tradePanelRegion.click("1478044408549.png")
    click("1478551412852.png")
    return;    

def addSellOrderBID(tradePanelRegion):
    tradePanelRegion.click("1478029829596-1.png")
    tradePanelRegion.click("1478556261979.png") #avoid '0' values, similar to 'O' 
    click("1478554236798.png")
    wait(1)
    accumulatedRegion = tradePanelRegion.wait("1478030812087-1.png",OPEN_TIMEOUT).right(100)
    accumPositionBefore = accumulatedRegion.text()
    tradedContractsRegion = tradePanelRegion.wait("1478043916673-1.png",OPEN_TIMEOUT).right(100)
    tradedContractsBefore = tradedContractsRegion.text()  
    tradedContractsRegion.highlight(3)

    tradePanelRegion.type(Pattern("1478029885384-1.png").targetOffset(37,-2), "12")
    try: 
        click("1478551379630.png");
    except:
        pass
    click("1478554236798.png")
    
    wait(2)
    accumPositionAfter = accumulatedRegion.text()
    tradedContractsAfter = tradedContractsRegion.text()
    ordersRegion = tradePanelRegion.wait("CANCELALL.png").above(50)
    if not ordersRegion.exists(Pattern("1478554588459.png").similar(0.90),3):
        popup("should be 0 opened sell orders ")    
    if (int(accumPositionBefore) - int(accumPositionAfter) != 125 ):
        popup ("Accumulated position before BID " + str(accumPositionBefore) + "; after " + str(accumPositionAfter))
    if (int(tradedContractsAfter) - int(tradedContractsBefore) != 125 ):
        popup ("Trade contracts before BID " + str(tradedContractsBefore) + "; after " + str(tradedContractsAfter))    
    tradePanelRegion.click("1478044408549-1.png")
    return;

#ASK(sell) and verify position, number of contracts, opened sell orders
def addBuyOrderBID(tradePanelRegion):
    accumulatedRegion = tradePanelRegion.wait("1478030812087.png",OPEN_TIMEOUT).right(100)
    accumPositionBefore = accumulatedRegion.text()
    tradedContractsRegion = tradePanelRegion.wait("1478043916673.png",OPEN_TIMEOUT).right(100)
    tradedContractsBefore = tradedContractsRegion.text()    
    tradedContractsRegion.highlight(3)

    tradePanelRegion.click("1478029829596.png")
    tradePanelRegion.type(Pattern("1478029885384.png").targetOffset(37,-2), "30")
    ordersRegion = tradePanelRegion.wait("CANCELALL.png").below(50)
    try: 
        click("1478551379630.png");
    except:
        pass
    click("1478561155999.png")
    wait(1)        
    if not ordersRegion.exists("1478561941813.png",3):
        popup("should be 300 opened buy orders")    
    accumPositionAfter = accumulatedRegion.text()
    tradedContractsAfter = tradedContractsRegion.text()
    if (accumPositionBefore != accumPositionAfter):
        popup ("Accumulated position before BID " + str(accumPositionBefore) + "; after " + str(accumPositionAfter))
    if (tradedContractsAfter != tradedContractsBefore):
        popup ("Trade contracts before BID " + str(tradedContractsBefore) + "; after " + str(tradedContractsAfter))    
    tradePanelRegion.click("1478044408549.png")
    click("1478551412852.png")
    return;    

def addBuyOrderMKT(tradePanelRegion):
    tradePanelRegion.click("1478029829596-1.png")
    tradePanelRegion.click("1478556261979.png") #avoid '0' values, similar to 'O' 
    click("1478563060538.png")
    wait(1)
    accumulatedRegion = tradePanelRegion.wait("1478030812087-1.png",OPEN_TIMEOUT).right(100)
    accumPositionBefore = accumulatedRegion.text()
    tradedContractsRegion = tradePanelRegion.wait("1478043916673-1.png",OPEN_TIMEOUT).right(100)
    tradedContractsBefore = tradedContractsRegion.text()  
    tradedContractsRegion.highlight(3)

    tradePanelRegion.type(Pattern("1478029885384-1.png").targetOffset(37,-2), "12")
    try: 
        click("1478551379630.png");
    except:
        pass
    click("1478563060538.png")
    
    wait(2)
    accumPositionAfter = accumulatedRegion.text()
    tradedContractsAfter = tradedContractsRegion.text()
    ordersRegion = tradePanelRegion.wait("CANCELALL.png").below(50)
    if not ordersRegion.exists("1478563090904.png",3):
        popup("should be 0 opened sell orders ")    
    if (int(accumPositionAfter) - int(accumPositionBefore) != 125 ):
        popup ("Accumulated position before MKT " + str(accumPositionBefore) + "; after " + str(accumPositionAfter))
    if (int(tradedContractsAfter) - int(tradedContractsBefore) != 125 ):
        popup ("Trade contracts before MKT " + str(tradedContractsBefore) + "; after " + str(tradedContractsAfter))    
    tradePanelRegion.click("1478044408549-1.png")
    return;

def cancelOrder(tradePanelRegion):
    accumulatedRegion = tradePanelRegion.wait("1478030812087.png",OPEN_TIMEOUT).right(100)
    accumPositionBefore = accumulatedRegion.text()
    tradedContractsRegion = tradePanelRegion.wait("1478043916673.png",OPEN_TIMEOUT).right(100)
    tradedContractsBefore = tradedContractsRegion.text()    
    tradedContractsRegion.highlight(3)

    tradePanelRegion.click("1478029829596.png")
    tradePanelRegion.type(Pattern("1478029885384.png").targetOffset(37,-2), "12")
    ordersRegion = tradePanelRegion.wait("CANCELALL.png").below(50)
    try: 
        click("1478551379630.png");
    except:
        pass
    click("1478561155999.png")
    wait(1)      

    if not ordersRegion.exists("1478567678527.png",3):
        popup("should be 120 opened sell orders")   

    tradeActionsRegion = getTradeArea ()
    tradeActionsRegion.wait("1478568043504.png")
    mouseMove(tradeActionsRegion.wait("1478568043504.png")) #click middle mouse button to cancel
    mouseDown(Button.MIDDLE)
    mouseUp(Button.MIDDLE)    
    if not ordersRegion.exists("1478568136744.png",3):
        popup("should be 0 opened sell orders after cancel")   
    accumPositionAfter = accumulatedRegion.text()
    tradedContractsAfter = tradedContractsRegion.text()
    if (accumPositionBefore != accumPositionAfter):
        popup ("Accumulated position before ASK " + accumPositionBefore + "; after " + accumPositionAfter)
    if (tradedContractsAfter != tradedContractsBefore):
        popup ("Trade contracts before ASK " + tradedContractsBefore + "; after " + tradedContractsAfter)    
    tradePanelRegion.click("1478044408549.png")
    click("1478551412852.png")
    return;    

def cancelAllOrders (tradePanelRegion):
    tradePanelRegion.click("1478029829596-2.png")
    tradePanelRegion.type(Pattern("1478029885384-2.png").targetOffset(37,-2), "5")
    try: 
        click("1478551379630.png");
    except:
        pass
    click("1478050123560.png")
    click("1478048731123-1.png")
    wait(2)
    ordersRegion = wait("ordersRegion-1.png")
    ordersRegion.below(50).wait("1478050141623.png",OPEN_TIMEOUT)
    ordersRegion.above(50).wait("1478050160883.png",OPEN_TIMEOUT)
    ordersRegion.click("ordersRegion-1.png")
    ordersRegion.below(50).wait(Pattern("1478048480929.png").similar(0.90),LOAD_TIMEOUT)
    ordersRegion.above(50).wait(Pattern("1478049149745.png").similar(0.85),LOAD_TIMEOUT)
    click ("1478050316359.png")
    tradePanelRegion.click("1478044408549-2.png")
    return;    

def closeFlatten (tradePanelRegion):
    tradePanelRegion.click("1478029829596-1.png")
    tradePanelRegion.click("1478556261979.png") #avoid '0' values, similar to 'O' 
    click("1478563060538.png")
    wait(1)
    accumulatedRegion = tradePanelRegion.wait("1478030812087-1.png",OPEN_TIMEOUT).right(100)
    accumPositionBefore = accumulatedRegion.text()
    tradePanelRegion.click("1478029829596-2.png")
    tradePanelRegion.type(Pattern("1478029885384-2.png").targetOffset(37,-2), "5")
    try: 
        click("1478551379630.png");
    except:
        pass
    click("1478050123560.png")
    click("1478048731123-1.png")
    wait(2)
    ordersRegion = wait("ordersRegion-1.png")
    ordersRegion.below(50).wait(Pattern("1478050141623.png").similar(0.80),OPEN_TIMEOUT)
    ordersRegion.above(50).wait(Pattern("1478050160883.png").similar(0.80),OPEN_TIMEOUT)
    tradePanelRegion.click("1478044408549-2.png")
    ordersRegion.below(50).wait(Pattern("1478048480929.png").similar(0.90),LOAD_TIMEOUT)
    ordersRegion.above(50).wait(Pattern("1478049149745.png").similar(0.85),LOAD_TIMEOUT)
    click ("1478050316359.png")
    if not accumulatedRegion.exists("0.png"):
        popup ("Trade contracts should be = 0")   
    return;    

def reopenTradePanel(tradePanelRegion):
    tradePanelRegion.click("1478029829596-2.png")
    tradePanelRegion.type(Pattern("1478029885384-2.png").targetOffset(37,-2), "5")
    try: 
        click("1478551379630.png");
    except:
        pass
    click("1478050123560.png")
    click("1478048731123-1.png")
    wait(2)
    ordersRegion = wait("ordersRegion-1.png")
    ordersRegion.below(50).wait(Pattern("1478050141623.png").similar(0.80),OPEN_TIMEOUT)
    ordersRegion.above(50).wait(Pattern("1478050160883.png").similar(0.80),OPEN_TIMEOUT)
    tradePanelRegion.click(Pattern("IEnable-2.png").targetOffset(-29,-4))
    click("1478652661409.png",3)
    hover("1478652920321.png")
    
    wait (2)
    click("1477910302441.png")   
    tradePanelRegion.click (Pattern("DEnable.png").targetOffset(-28,0))        
    ordersRegion.below(50).wait(Pattern("1478050141623.png").similar(0.80),OPEN_TIMEOUT)
    ordersRegion.above(50).wait(Pattern("1478050160883.png").similar(0.80),OPEN_TIMEOUT)
    click ("1478050316359.png")
    tradePanelRegion.click("1478044408549-2.png")
    return;    

#stopLimit is string with sign after. stop Limit = '45+' | '23' | '0'  orderType = ['MKT','LMT']
def stopOrderPlacement(tradePanelRegion, orderType, stopLimit):

    sizeLabelRegion = tradePanelRegion.wait("1479422013709.png")
    #set Stop Limit:
    sizeLabelRegion.setTargetOffset(40,-55) 
    hover(sizeLabelRegion)
    btnsRegion = tradePanelRegion.wait(Pattern("1479646292969-1.png").targetOffset(3,-1),5)
    dragDrop(sizeLabelRegion, btnsRegion)
    type(stopLimit)
    #switch Order type:
    sizeLabelRegion.setTargetOffset(0,-55)
    click(sizeLabelRegion)
    

    wait (Pattern("1479422176562.png").targetOffset(0,-20),5)
    if orderType == 'MKT':    
        tradePanelRegion.click(Pattern("1479422176562.png").targetOffset(0,-20),10)
    elif  orderType == 'LMT':
        tradePanelRegion.click(Pattern("1479422176562.png").targetOffset(0,18),10)
    else:
        popup("order Type not recognized")

 
    
    tradeArea = getTradeArea()
    bidPattern = getBidArea(tradeArea)
    bidPattern.setTargetOffset(0,-50)
   
    tradePanelRegion.click("1478029829596-6.png")
    tradePanelRegion.type(Pattern("1478029885384-6.png").targetOffset(37,-2), "30")
    ordersRegion = tradePanelRegion.wait("CANCELALL-4.png").below(50)
    click(bidPattern, KEY_SHIFT)
    click("1479400952850-3.png")

 # click shift+RMB below market price
    bidPattern.setTargetOffset(0,50)
   
    tradePanelRegion.click("1478029829596-6.png")
    tradePanelRegion.type(Pattern("1478029885384-6.png").targetOffset(37,-2), "50")
    ordersRegion = tradePanelRegion.wait("CANCELALL-4.png").below(50)
    rightClick(bidPattern, KEY_SHIFT)
    click("1479400952850-3.png")
    
    click("1478551412852-4.png")
    if not tradeArea.exists("1479400329787-3.png",5):
        popup(" order 300 did not appear in trade area")   
    if not tradeArea.exists("1479404640320-2.png",5):
        popup(" order 500 did not appear in trade area")      
    tradePanelRegion.click("1478044408549-6.png")
    return;   

def stopOrderInvalid(tradePanelRegion):

    tradeArea = getTradeArea()
    bidPattern = getBidArea(tradeArea)
    bidPattern.setTargetOffset(0,50)
   
    tradePanelRegion.click("1478029829596-3.png")
    tradePanelRegion.type(Pattern("1478029885384-3.png").targetOffset(37,-2), "30")
    ordersRegion = tradePanelRegion.wait("CANCELALL-1.png").below(50)
    click(bidPattern, KEY_SHIFT)
    click("1479400952850.png")
    errorRegion = wait(Pattern("Orderplaceme.png").targetOffset(62,19),10)
    click(errorRegion)
    
 # click shift+RMB below market price
    bidPattern.setTargetOffset(0,-50)
   
    tradePanelRegion.click("1478029829596-3.png")
    tradePanelRegion.type(Pattern("1478029885384-3.png").targetOffset(37,-2), "50")
    ordersRegion = tradePanelRegion.wait("CANCELALL-1.png").below(50)
    rightClick(bidPattern, KEY_SHIFT)
    click("1479400952850.png")
    errorRegion = wait(Pattern("Orderplaceme.png").targetOffset(62,19),10)
    click(errorRegion)
    
    click("1478551412852-1.png")
    if tradeArea.exists("1479400329787.png",3):
        popup(" invalid order 300 appeared in trade area")   
    if tradeArea.exists("1479404640320.png",3):
        popup(" invalid order 500 appeared in trade area")      
    tradePanelRegion.click("1478044408549-3.png")
    return;    

def WTFISTHIS(tradePanelRegion):
    accumulatedRegion = tradePanelRegion.wait("1478030812087.png",OPEN_TIMEOUT).right(100)
    accumPositionBefore = accumulatedRegion.text()
    tradedContractsRegion = tradePanelRegion.wait("1478043916673.png",OPEN_TIMEOUT).right(100)
    tradedContractsBefore = tradedContractsRegion.text()    
    tradedContractsRegion.highlight(3)

    tradePanelRegion.click("1478029829596.png")
    tradePanelRegion.type(Pattern("1478029885384.png").targetOffset(37,-2), "30")
    ordersRegion = tradePanelRegion.wait("CANCELALL.png").above(50)
    try: 
        click("1478551379630.png");
    except:
        pass
    click("1478048731123.png")
    wait(1)        
    if not ordersRegion.exists(Pattern("1478539208452.png").similar(0.90),3):
        popup("should be 300 opened sell orders")    
    accumPositionAfter = accumulatedRegion.text()
    tradedContractsAfter = tradedContractsRegion.text()
    if (accumPositionBefore != accumPositionAfter):
        popup ("Accumulated position before ASK " + str(accumPositionBefore) + "; after " + str(accumPositionAfter))
    if (tradedContractsAfter != tradedContractsBefore):
        popup ("Trade contracts before ASK " + str(tradedContractsBefore) + "; after " + str(tradedContractsAfter))    
    tradePanelRegion.click("1478044408549.png")
    click()
    return;   

#addSellOrderASK(getTradePanelRegion());
