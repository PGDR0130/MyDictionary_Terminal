import curses
from curses import wrapper
from scrdraw import mainPage, mainMenu

class input:
    def __init__(self, stdscr) -> None:
        self.scr = stdscr
        self.buffer = ''

        # for main
        self.run = True
        self.focus = 'com'
        self.update = True

    def push(self, char):
        """
        handle the input 
        """
        if (char == None): self.update = False
        else : self.update = True

        if (self.focus == 'com'):
            if (char == 'Key_Esc'):
                self.run = False

    def get_run(self):
        """
        return bool to determine keep running or not
        """
        return self.run

    def get_update(self):
        return self.update

class Main:
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr
        self.exit = True

        # Curses setup
        curses.noecho()
        curses.cbreak()

    def main(self):
        Menu = mainMenu(self.stdscr)
        layout = mainPage(self.stdscr)
        Menu.draw()
        self.stdscr.getch()
        
        self.stdscr.nodelay(True)
        
        send = input(self.stdscr)
        layout.draw()
        while (send.get_run()):
            try :
                send.push(self.stdscr.getkey())
            except:
                send.push(None)

            if send.get_update():
                layout = mainPage(self.stdscr)
                layout.draw()
                    
    



def main(stdscr):
    Run = Main(stdscr)
    Run.main()

if __name__ == '__main__':
    wrapper(main)