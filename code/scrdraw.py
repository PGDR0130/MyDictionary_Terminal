import curses

class Windows:
    class templateWin:
        def __init__(self, height, width, startY, startX) -> None:
            self.startY = startY
            self.startX = startX
            self.width = width 
            self.height = height  
            self.scr = curses.newwin(self.height, self.width, self.startY, self.startX)
            # Need screen update check
            self.scrUpdate = False


    class searchBar(templateWin):
        def __init__(self, height, width, startY, startX, dic) -> None:
            """
            command Line at the bottom of the screen 
            commands such as search or settings
            needs to handle user input
            """
            super().__init__(height, width, startY, startX)
            self.dic = dic
            self.buf = ''  

        def buffer(self, char):
            if char == 10 : # Enter
                self.dic.updateWord(self.buf)
                # clear buffer
                self.buf = '' 
            elif char == 8: # Backspace
                self.buf = self.buf[:-1]
            elif 20 < char and char < 126: # normal characters
                self.buf += chr(char)

        def update(self):
            self.scr.clear()
            self.scr.addstr(f' > {self.buf}')
            self.scr.refresh()

        def input(self, char):
            self.buffer(char)
            self.update()

        def main(self, command):
            pass
        
    class cambridgeDIC(templateWin):
        """
        The main dictionary.
        """
        def __init__(self, height, width, startY, startX) -> None:
            super().__init__(height, width, startY, startX)
            self.word = ''

        def updateWord(self, word):
            self.word = word
            self.scr.addstr(self.word + '\n')
            self.scr.refresh()
            
        def needScrUpdate(self):
            return self.update            

    class oxfordCO(templateWin):
        """
        oxford collocation dictionary -
        1. meaning
        2. usage
        3. example
        """
        def __init__(self, height, width, startY, startX) -> None:
            super().__init__(height, width, startY, startX)
            self.word = ''


class Pages:
    class templatePage:
        def __init__(self, stdscr) -> None:
            #screen 
            self.scr = stdscr
            self.maxY = self.scr.getmaxyx()[0]
            self.maxX = self.scr.getmaxyx()[1]
            self.midX = self.maxX//2
            curses.start_color()

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
        def __init__(self, stdscr) -> None:
            # defult scr
            super().__init__(stdscr)
            # mainDic scr - Cam
            self.mainDicY = 1
            self.mainDicX = 1
            self.mainheight = self.maxY-self.mainDicY - 1
            self.mainwidth = self.midX-self.mainDicX
            self.mainDic = Windows.cambridgeDIC(self.mainheight, self.mainwidth, self.mainDicY, self.mainDicX)
            self.mainDicScr = self.mainDic.scr
            # secondDic scr - coll
            self.secDicY = 1
            self.secDicX = self.midX 
            self.secheight = self.maxY-self.secDicY - 1 
            self.secwidth = self.maxX-self.secDicX -1
            self.secDic = Windows.oxfordCO(self.secheight, self.secwidth, self.secDicY, self.secDicX)
            # top right information
            self.info = " Own Dic. V1 "
            self.infoY = 0
            self.infoX = self.maxX//20
            # searchBar
            self.comY = self.maxY - 1
            self.comX = 0
            self.comheight = 1
            self.comwidth = self.maxX 
            self.com = Windows.searchBar(self.comheight, self.comwidth, self.comY , self.comX, self.mainDic)
            curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)
            self.com.scr.bkgd(' ', curses.color_pair(1))

        def debug(self, char):
            self.mainDicScr.scr.addstr(chr(char))
            self.mainDicScr.scr.refresh()

        def draw(self):
            self.scr.clear()
            self.scr.border()
            # info
            self.scr.addstr(self.infoY, self.infoX, self.info)
            self.scr.refresh()

            self.com.scr.addstr(' > ' + 'searchBar')
            self.com.scr.refresh()

            # self.mainDic.border()
            # self.mainDic.refresh()
            # self.secDic.border()
            # self.secDic.refresh()
        
        def update(self, char):
            self.com.input(char)