import curses
import parseLookup

class Windows:
    class templateWin:
        def __init__(self, height, width, startY, startX) -> None:
            self.scr = curses.newwin(height, width,startY, startX)
            # Need screen update check
            self.scrUpdate = False

        def needScrUpdate(self):
            return self.scrUpdate
        
        def resize(self, height, width, startY, startX):
            # move and resize old window 
            self.scr.mvwin(startY, startX)
            self.scr.resize(height, width)    

            self.scr.border()
            self.scr.refresh()        

    class searchBar(templateWin):
        def __init__(self, height, width, startY, startX, dicts:list) -> None:
            """
            command Line at the bottom of the screen 
            commands such as search or settings
            needs to handle user input
            """
            super().__init__(height, width, startY, startX)
            self.dicts = dicts
            self.buf = ''  
            self.scr.bkgd(' ', curses.color_pair(1))

        def buffer(self, char):
            if char == 10 : # Enter
                for dict in self.dicts:
                    dict.updateWord(self.buf)
                # clear buffer
                self.buf = '' 
            elif char == 8: # Backspace
                self.buf = self.buf[:-1]
            elif 20 < char and char < 126: # normal characters
                self.buf += chr(char)

        def update(self):
            self.scr.clear()
            self.scr.addstr(f' > ' + (self.buf if self.buf != '' else 'search'))
            self.scr.refresh()

        def input(self, char):
            self.buffer(char)
            self.update()

        def main(self, command):
            pass
        
    class cambridgeDict(templateWin):
        """
        The main dictionary.
        """
        def __init__(self, height, width, startY, startX) -> None:
            super().__init__(height, width, startY, startX)
            self.word = ''

        def updateWord(self, word):
            definition,enexamp, chexamp = parseLookup.cambridge(word)
            for i in range(len(enexamp)):
                self.scr.addstr(definition[i] + '\n')
                for k in range(len(enexamp[i])):    
                    self.scr.addstr('> '+enexamp[i][k] + '\n')
                    self.scr.addstr('  '+chexamp[i][k] + '\n')
                    self.scr.addstr('\n')
                    self.scr.refresh()
            self.scr.refresh()


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
            self.mainDict = Windows.cambridgeDict(self.mainheight, self.mainwidth, self.mainDictY, self.mainDictX)
            self.secDict = Windows.oxfordCO(self.secheight, self.secwidth, self.secDictY, self.secDictX)
            self.com = Windows.searchBar(self.comheight, self.comwidth, self.comY , self.comX, [self.mainDict])
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
            self.scr.refresh()
            self.com.input(char)
            