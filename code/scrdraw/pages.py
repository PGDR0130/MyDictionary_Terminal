## typesetting for different pages 
## including Menu, CamDict., settings and more 
import curses
from scrdraw import contentWindow

class templatePage:
    def __init__(self, stdscr) -> None:
        #screen 
        self.scr = stdscr
        self.maxY, self.maxX = self.scr.getmaxyx()
        self.midX = self.maxX//2
        curses.start_color()
    
    def scrSizeUpdater(self):
        self.maxY, self.maxX = self.scr.getmaxyx()
        self.winSizeUpdate()
        self.allWinResize()

class mainMenu(templatePage):
    def __init__(self, stdscr) -> None:
        # screen 
        super().__init__(stdscr)
        # Title 
        self.Title = "\* Own Dictionary v1.0 */"
        self.TitleY = self.maxY//3
        self.TitleX = self.midX - len(self.Title)//2
        # Subtitle
        self.subTitle = "The best terminal dictionary ever made"
        self.subTitleY = self.TitleY + 2
        self.subTitleX = self.midX - len(self.subTitle)//2

    def draw(self) -> None:
        """
        Draw main menu including title, subtitle and more.

        @ To do : add quotes that will change every time
        """
        # displaing outter part of the terminal
        self.scr.clear()
        # Title - "\* Own Dictionary */"
        self.scr.addstr(self.TitleY, self.TitleX, self.Title, curses.color_pair(1) | curses.A_BOLD)
        # Subtitle - "The best terminal dictionary"
        self.scr.addstr(self.subTitleY, self.subTitleX, self.subTitle)
        # Border 
        self.scr.border('|', '|', '-', '-', 'O', 'O', 'O', 'O')

        self.scr.refresh()

class mainPage(templatePage):
    def winSizeUpdate(self):
        #mainDic scr - Cambridge
        self.mainDictY = 1
        self.mainDictX = 1
        self.mainheight = self.maxY-self.mainDictY - 1
        self.mainwidth = self.midX-self.mainDictX
        # secondDic scr - oxford collocation Dict
        self.secDictY = 1
        self.secDictX = self.midX 
        self.secheight = self.maxY-self.secDictY - 1 
        self.secwidth = self.maxX-self.secDictX -1 
        # searchBar
        self.comY = self.maxY - 1
        self.comX = 0
        self.comheight = 1
        self.comwidth = self.maxX
        # top right information
        self.infoY = 0
        self.infoX = self.maxX//20
    
    def allWinResize(self):
        self.mainDict.resize(self.mainheight, self.mainwidth, self.mainDictY, self.mainDictX)
        self.secDict.resize(self.secheight, self.secwidth, self.secDictY, self.secDictX)
        self.com.resize(self.comheight, self.comwidth, self.comY, self.comX)

    def __init__(self, stdscr) -> None:
        # defult scr
        super().__init__(stdscr)
        self.winSizeUpdate()
        # setupwindows
        self.mainDict = contentWindow.cambridgeDict(self.mainheight, self.mainwidth, self.mainDictY, self.mainDictX)
        self.secDict = contentWindow.oxfordCO(self.secheight, self.secwidth, self.secDictY, self.secDictX)
        self.com = contentWindow.searchBar(self.comheight, self.comwidth, self.comY , self.comX, [self.secDict])
        # top right information
        self.info = " Own Dict. V1 "
        # searchBar color 
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)

    def initDraw(self):
        self.scr.clear()
        self.scr.border()
        # info
        self.scr.addstr(self.infoY, self.infoX, self.info)
        self.scr.refresh()
        # searchbar
        self.com.update()
        self.com.scr.refresh()
    
    def update(self, char):
        self.com.input(char)