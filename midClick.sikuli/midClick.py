from sikuli import *
class Region(Region):
    def middleClick(self, psmrl):
        try:
            psmrl = self.find(psmrl).getTarget()
        except:
            pass
        hover(psmrl)
        mouseDown(Button.MIDDLE)
        mouseUp(Button.MIDDLE)
        print "[log] MIDDLE CLICK on", psmrl
class Screen(Screen):
    def middleClick(self, psmrl):
        Region(self.getBounds()).middleClick(psmrl)
def middleClick(psmrl):
    SCREEN.middleClick(psmrl)
SCREEN = Screen(0)