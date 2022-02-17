import curses
from curses import wrapper
from scrdraw import mainMenu, update

def setup(stdscr):
    pass

def main(stdscr):


    # Draw menu
    Menu = mainMenu(stdscr)
    Menu.draw()
    # Draw border
    Border = update(stdscr)
    Border.updateBorder()

    stdscr.getch()

wrapper(main)