from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
url = 'https://dictionary.cambridge.org/dictionary/english-chinese-traditional/example'

def cambridge(word):
    request = requests.get(url, headers=headers).text
    soup = BeautifulSoup(request, 'lxml')
    dict = soup.body.find('div', 'pr entry-body__el')
    # print(dict)


    # Big Blockes
    def getHeader(dict):
        """
        Word 
        part of speech, sound
        """    
        header_block = dict.find('div', 'pos-header dpos-h')
        return header_block

    def getAllDefBlock(dict):
        """
        All block with definition (EN, CH) and example sentence
        """
        allDef = dict.findAll('div', 'def-block ddef_block')
        return allDef


    # middle
    def getAllDef():
        """
        get different def from different block
        """
        block = getAllDefBlock(dict)
        defs = []
        for i in block :
            defs.append(i.find('span', 'trans dtrans dtrans-se break-cj').text)
        print(defs)
    
    def getAllExamp():
        block = getAllDefBlock(dict)
        difdef = [] # different definition block
        for examp_block in block :
            difdef.append(examp_block.findAll('div', 'examp dexamp'))
        
        for difdef in difdef:
            for examp in difdef:
                exampCH = examp.find('span' ,'trans dtrans dtrans-se hdb break-cj').text
                print(exampCH)
            print('------------------')

    # Small Block
    # old 
    """
    def find_PartOfSpeech(dict):
        PartOfSpeech = dict.find('span', 'pos dpos').text
        print(PartOfSpeech)

    def find_meaning(dict):
        Meaning = dict.find('span', 'trans dtrans dtrans-se break-cj').text
        print(Meaning)

    def find_more(dict):
        more = dict.findAll('span', 'trans dtrans dtrans-se break-cj')
        for i in more:
            print(i.text)
    """

    # find_PartOfSpeech(dict)
    # find_more(dict)
    getAllDef()
    getAllExamp()


cambridge('gain')