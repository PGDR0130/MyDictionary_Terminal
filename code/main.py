import curses
from curses import wrapper
from tkinter import Menu
from scrdraw import mainPage, mainMenu

class Main:
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr

        # Curses setup
        curses.noecho()
        curses.cbreak()
        # self.stdscr.nodelay(True)

    def main(self):
        Menu = mainMenu(self.stdscr)
        Menu.draw()
        self.stdscr.getch()

        layout = mainPage(self.stdscr)
        layout.main()
        self.stdscr.getch()




def main(stdscr):
    Run = Main(stdscr)
    Run.main()

if __name__ == '__main__':
    wrapper(main)