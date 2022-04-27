## Draw window for content such as a specific dict. or some useful information
import curses
import logging
from wordLookUp.cambridge import cambridgeFind


logging = logging.getLogger(__name__)

class templateWin:
    def __init__(self, height, width, startY, startX) -> None:
        self.scr = curses.newwin(height, width,startY, startX)
        self.height = height
        self.width = width
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

    def forceClear(self):
        """
        clear() and erase() methond couldnt clear chinese word properly,
        due to the difference of the width between Chinese characters and English characters
        this is going to cover the previous rendered characters and clear it to blank.

        Notice : can't cover things up with space!!
        """
        self.scr.move(0, 0)
        for i in range(self.height - 1):
            self.scr.addstr(i,0, '_'*self.width)
            self.scr.refresh()
            self.scr.clear()
            self.scr.addstr(self.height//2, self.width//2 - len('Loading...')//2, 'Loading...')
        

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
            logging.debug('push update word to dicts')
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

    def updateWord(self, word): 
        logging.debug(f'{self.__class__} updating word')
        self.forceClear()
        definition, enexamp, chexamp = cambridgeFind(word)
        logging.info(f'{self.__class__} get info successfully')    
        self.scr.clear()
        self.scr.refresh()
        self.scr.move(0, 0)
        if not not definition:
            for i in range(len(enexamp)):
                self.scr.addstr(definition[i] + '\n')
                for k in range(len(enexamp[i])):    
                    self.scr.addstr('> '+enexamp[i][k] + '\n')
                    self.scr.addstr('  '+chexamp[i][k] + '\n' )
                self.scr.addstr('<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n')
        else :
            self.addchstr(self.height//2, self.width-len('No words found')//2,'No words found')
        self.scr.refresh()
        logging.info(f'Successfully display new word "{word}" ')


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
    
    def updateWord(self, word):
        self.forceClear()


