
from email import message


class mainMenu:
    def __init__(self, scr) -> None:
        # screen
        self.scr = scr
        self.maxY = self.scr.getmaxyx()[0]
        self.maxX = self.scr.getmaxyx()[1]
        self.midX = self.maxX//2
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
        self.scr.addstr(self.TitleY, self.TitleX, self.Title)
        # Subtitle - "The best terminal dictionary"
        self.scr.addstr(self.subTitleY, self.subTitleX, self.subTitle)

        self.scr.refresh()


<<<<<<< HEAD
class mainPage:
    def __init__(self, stdscr) -> None:
        # defult scr
        self.scr = stdscr
        self.maxY = self.scr.getmaxyx()[0]
        self.maxX = self.scr.getmaxyx()[1]
        self.midX = self.maxX//2

        # mainDic scr - Cam
        self.mainDicY = 1
        self.mainDicX = 1
        self.mainheight = self.maxY-self.mainDicY - 1
        self.mainwidth = self.maxX-self.mainDicX - 1
        self.mainDic = curses.newwin(self.mainheight, self.mainwidth, self.mainDicY, self.mainDicX)
        # secondDic scr - coll
        self.secDicY = 1
        self.secDicX = self.midX + 1
        self.secheight = self.maxY-self.secDicY - 1 
        self.secwidth = self.maxX-self.secDicX - 1
        self.secDic = curses.newwin(self.secheight, self.secwidth, self.secDicY, self.secDicX)

        # top right information
        self.info = " Own Dic. V1 "
        self.infoY = 0
        self.infoX = self.maxX//20

    def draw(self):
        self.scr.clear()
        self.scr.border()
        # info
        self.scr.addstr(self.infoY, self.infoX, self.info)
        self.scr.refresh()

        self.mainDic.border()
        self.secDic.border()
        self.mainDic.refresh()
        self.secDic.refresh()


class comLine:
    def __init__(self, stdscr) -> None:
        """
        command Line at the bottom of the screen 
        commands such as search or settings
        needs to handle user input
        """
        self.scr = stdscr

    def input(self):
        pass

    def main(self):
        pass
=======
class update:
    def __init__(self, scr) -> None:
        self.scr = scr

    def updateBorder(self):
        """
        Border that will be constintly updating all the time 
        """
        self.scr.border('|', '|', '-', '-', 'O', 'O', 'O', 'O')
        self.scr.refresh()
>>>>>>> parent of b605152 (mainPage almost done)
