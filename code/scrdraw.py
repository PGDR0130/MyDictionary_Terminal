import curses

class Windows:
    class templateWin:
        def __init__(self, height, width, startY, startX) -> None:
            self.startY = startY
            self.startX = startX
            self.width = width 
            self.height = height  
            self.scr = curses.newwin(self.height, self.width, self.startY, self.startX)

    class comLine(templateWin):
        def __init__(self, height, width, startY, startX) -> None:
            """
            command Line at the bottom of the screen 
            commands such as search or settings
            needs to handle user input
            """
            super().__init__(height, width, startY, startX)
            self.buf = ''
        
        def buffer(self):
            pass

        def input(self, char):
            pass

        def main(self):
            pass

    class cambridgeDIC(templateWin):
        """
        The main dictionary.
        """
        def __init__(self, height, width, startY, startX) -> None:
            super().__init__(height, width, startY, startX)

    class oxfordCO:
        """
        oxford collocation dictionary -
        1. meaning
        2. usage
        3. example
        """
        def __init__(self, height, width, startY, startX) -> None:
            super.__init__(height, width, startY, startX)
        

class Pages:
    class templatePage:
        def __init__(self, scr) -> None:
            #screen 
            self.scr = scr
            self.maxY = self.scr.getmaxyx()[0]
            self.maxX = self.scr.getmaxyx()[1]
            self.midX = self.maxX//2

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
            self.scr.addstr(self.TitleY, self.TitleX, self.Title)
            # Subtitle - "The best terminal dictionary"
            self.scr.addstr(self.subTitleY, self.subTitleX, self.subTitle)
            # Border 
            self.scr.border('|', '|', '-', '-', 'O', 'O', 'O', 'O')

            self.scr.refresh()

    class mainPage(templatePage):
        def __init__(self, stdscr) -> None:
            # defult scr
            super().__init__(stdscr)
            # mainDic scr - Cam
            self.mainDicY = 1
            self.mainDicX = 1
            self.mainheight = self.maxY-self.mainDicY - 1
            self.mainwidth = self.midX-self.mainDicX
            self.mainDic = Windows.cambridgeDIC(self.mainheight, self.mainwidth, self.mainDicY, self.mainDicX).scr
            # self.mainDic = curses.newwin(self.mainheight, self.mainwidth, self.mainDicY, self.mainDicX)
            # secondDic scr - coll
            self.secDicY = 1
            self.secDicX = self.midX 
            self.secheight = self.maxY-self.secDicY - 1 
            self.secwidth = self.maxX-self.secDicX -1
            self.secDic = curses.newwin(self.secheight, self.secwidth, self.secDicY, self.secDicX)

            # top right information
            self.info = " Own Dic. V1 "
            self.infoY = 0
            self.infoX = self.maxX//20

            self.test = 1

        def debug(self, char):
            self.mainDic.addstr(chr(char))
            self.mainDic.refresh()

        def draw(self):
            self.scr.clear()
            self.scr.border()
            # info
            self.scr.addstr(self.infoY, self.infoX, self.info)
            self.scr.refresh()

            # self.mainDic.border()
            # self.mainDic.refresh()
            # self.secDic.border()
            # self.secDic.refresh()