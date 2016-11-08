from sikuli import *
import os



#Settings.OcrLanguage = "eng"


LOAD_TIMEOUT = 30
OPEN_TIMEOUT = 10



#AFTER FEED OPEN WAIT 5 MIN BEFORE USING THIS  
#returns region right from timeLine where user can click to put orders.
def getTradeArea ():
    lineRegion = wait (Pattern("1478386010109.png").similar(0.75),10).left(100).below(60)
    lineRegion.highlight(3)
    timeLineRegion = lineRegion.wait(Pattern("1478387010276.png").similar(0.90),10).right(100).below(500)
    timeLineRegion.setX(timeLineRegion.getX() - 10) 
    timeLineRegion.highlight(3)
    return timeLineRegion;

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

#ASK(sell) and verify position, number of contracts, opened sell orders
def addSellOrderASK(tradePanelRegion):
    accumulatedRegion = tradePanelRegion.wait("1478030812087.png",OPEN_TIMEOUT).right(100)
    accumPositionBefore = accumulatedRegion.text()
    tradedContractsRegion = tradePanelRegion.wait("1478043916673.png",OPEN_TIMEOUT).right(100)
    tradedContractsBefore = tradedContractsRegion.text()    
    tradedContractsRegion.highlight(3)

    tradePanelRegion.click("1478029829596.png")
    tradePanelRegion.type(Pattern("1478029885384.png").targetOffset(37,-2), "30")
    bidsRegion = tradePanelRegion.wait("bidsRegion.png").above(50)
    click("1478551379630.png")
    click("1478048731123.png")
    wait(1)        
    if not bidsRegion.exists(Pattern("1478539208452.png").similar(0.90),3):
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
    click("1478551379630.png")
    click("1478554236798.png")
    
    wait(2)
    accumPositionAfter = accumulatedRegion.text()
    tradedContractsAfter = tradedContractsRegion.text()
    bidsRegion = tradePanelRegion.wait("bidsRegion.png").above(50)
    if not bidsRegion.exists(Pattern("1478554588459.png").similar(0.90),3):
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
    bidsRegion = tradePanelRegion.wait("bidsRegion.png").below(50)
    try: 
        click("1478551379630.png");
    except:
        pass
    click("1478561155999.png")
    wait(1)        
    if not bidsRegion.exists("1478561941813.png",3):
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
    click("1478551379630.png")
    click("1478563060538.png")
    
    wait(2)
    accumPositionAfter = accumulatedRegion.text()
    tradedContractsAfter = tradedContractsRegion.text()
    bidsRegion = tradePanelRegion.wait("bidsRegion.png").below(50)
    if not bidsRegion.exists("1478563090904.png",3):
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
    bidsRegion = tradePanelRegion.wait("bidsRegion.png").below(50)
    click("1478551379630.png")
    click("1478561155999.png")
    wait(1)      

    if not bidsRegion.exists("1478567678527.png",3):
        popup("should be 120 opened sell orders")   

    tradeActionsRegion = getTradeArea ()
    tradeActionsRegion.wait("1478568043504.png")
    mouseMove(tradeActionsRegion.wait("1478568043504.png")) #click middle mouse button to cancel
    mouseDown(Button.MIDDLE)
    mouseUp(Button.MIDDLE)    
    if not bidsRegion.exists("1478568136744.png",3):
        popup("should be 0 opened sell orders after cancel")   
    accumPositionAfter = accumulatedRegion.text()
    tradedContractsAfter = tradedContractsRegion.text()
    if (accumPositionBefore != accumPositionAfter):
        popup ("Accumulated position before ASK " + str(accumPositionBefore) + "; after " + str(accumPositionAfter))
    if (tradedContractsAfter != tradedContractsBefore):
        popup ("Trade contracts before ASK " + str(tradedContractsBefore) + "; after " + str(tradedContractsAfter))    
    tradePanelRegion.click("1478044408549.png")
    click("1478551412852.png")
    return;    
#clickTradeArea ();    
TDreg = getTradePanelRegion()
cancelOrder(TDreg);

