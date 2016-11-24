from sikuli import *
import os


def CustomNotes ():
    CNColumnRegion = wait("1479679398544.png",10).below(650)
    rightClick(CNColumnRegion)
    wait(1)
    click("Insertcolumn.png")
    rightClick(CNColumnRegion) 
    click(Pattern("0CustomNotes.png").targetOffset(-71,1))
    
    CNHeaderRegion = wait("1479704364476.png",10)
    CNHeaderRegion.setTargetOffset(0,30)
    click(CNHeaderRegion)
    type ('firstNote')
    click("1479680584525.png")
    CNHeaderRegion.setTargetOffset(0,60)
    click(CNHeaderRegion)
    wait(1)
    type ('secondNote')
    click("1479680584525.png")
    CNHeaderRegion.setTargetOffset(0,100)
    click(CNHeaderRegion)
    type ('thirdNote')
    click("1479680584525.png")
    CNColumnRegion.wait("first.png",5)
    CNColumnRegion.hover("first.png")
    
    CNColumnRegion.click(Pattern("1479710449673.png").targetOffset(35,0))
    wait(1)
    if CNColumnRegion.exists("first.png"):
        popup ("first note was not deleted") 
    CNColumnRegion.wait("1479709538111.png",5)
    CNColumnRegion.hover("1479709538111.png")
    
    CNColumnRegion.click(Pattern("1479710285947.png").targetOffset(34,0))
    wait(1)
    if CNColumnRegion.exists("1479709538111.png"):
        popup ("second note was not deleted") 
    CNColumnRegion.wait("third.png",5)
    rightClick(CNHeaderRegion) 
    click("Clearallnote.png")
    click(Pattern("1479709743252.png").similar(0.80),5)
    wait(1)
    if CNColumnRegion.exists("third.png"):
        popup ("third note was not deleted") 
    rightClick(CNHeaderRegion) 
    click("Hidecolumn.png",5) 
return;

def checkStudiesConf ():
    click ("1479763566688.png")
    
    if not exists("Icebergdetec.png", 10):
        popup("Studies Configuration dialog is incorrect")     
    click ("1479763613401.png")
return;