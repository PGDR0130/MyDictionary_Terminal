
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
        self.subTitleY = self.TitleY + 1
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


class update:
    def __init__(self, scr) -> None:
        self.scr = scr

    def updateBorder(self):
        """
        Border that will be constintly updating all the time 
        """
        self.scr.border('|', '|', '-', '-', 'O', 'O', 'O', 'O')
        self.scr.refresh()