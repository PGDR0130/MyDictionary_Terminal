import curses
from scrdraw import Pages, Windows


class Main:
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr
        self.willExit = False

        self.Menu = Pages.mainMenu(self.stdscr)
        self.layout = Pages.mainPage(self.stdscr)
        self.focus = 'mainScr'
        self.lastFocus = 'mainScr'

        # Curses setup
        curses.start_color()
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()

    def keyPress(self, char):
        def changeFocus(focus):
            self.lastFocus = self.focus
            self.focus = focus

        if char != None:
            if char == ord(':') and self.focus != 'com':
                changeFocus('com')
            elif char == 27 :
                changeFocus(self.lastFocus)
            elif char == ord('1'):
                changeFocus('mainScr')
            elif char == ord('2'):
                changeFocus('secScr')

            if self.focus == 'com':
                self.command.input(char)

            elif self.focus == 'mainScr':
                # self.layout.debug(char)
                if char == ord('q'):
                    curses.endwin()
                    self.willExit = True 
                else:
                    self.layout.update(char)

            elif self.focus == 'secScr':
                if char == ord('q'):
                    pass

    def main(self):
        self.Menu.draw()
        self.stdscr.getch()

        self.stdscr.nodelay(True)

        self.layout.draw()

        while(not self.willExit):
            try :
                self.keyPress(self.stdscr.getch())
            except:
                self.keyPress(None)
                    
    

def main():
    stdscr = curses.initscr()
    Run = Main(stdscr)
    Run.main()

if __name__ == '__main__':
    main()