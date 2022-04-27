from bs4 import BeautifulSoup, NavigableString
import requests, logging

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
cambridge_url = 'https://dictionary.cambridge.org/dictionary/english-chinese-traditional/'

def cambridgeFind(word):
    request = requests.get(cambridge_url+word, headers=headers).text
    soup = BeautifulSoup(request, 'lxml')
    dict = soup.body.find('div', 'pr entry-body__el')
    if dict == None:
        logging.warning('No body found')
        return False

    # Big Blockes
    def getHeader(dict):
        """
        Word 
        part of speech, sound
        """    
        header_block = dict.find('div', 'pos-header dpos-h')
        if header_block == None :
            logging.warning('No header block found')
            return False
        return header_block

    def getAllDefBlock(dict):
        """
        All block with definition (EN, CH) and example sentences (EN, CH)

        return the hole definition block  
        """
        allDef = dict.findAll('div', 'def-block ddef_block')
        if not allDef :
            logging.warning('No defnition block found')
            return False
        return allDef

    # middle
    def getAllDef():
        """
        get different def from different block
        """
        block = getAllDefBlock(dict)
        defs = []
        for i in block :
            # find translated difinition in evey blocks
            defs.append(i.find('span', 'trans dtrans dtrans-se break-cj').text)
        return defs
    
    def getAllExamp():
        """
        get all example sentences, Both English and Chinese are possible
        """
        block = getAllDefBlock(dict)
        difexamps = [] # two dimensional array, the inner list contains same def example
        for examp_block in block :
            # find all sentences in the same def block
            # all examp sentences in the same block have the same def 
            difexamps.append(examp_block.findAll('div', 'examp dexamp'))
        
        def CH():
            """
            get Chinese example sentence 
            """
            currentdef = 0 
            examplist = []
            for samexamps in difexamps:
                examplist.append(list())
                # loop throught difexamps to get the same def example sentence in list
                for exblock in samexamps:
                    # loop through samexamp to get the same def examp
                    examp = exblock.find('span' ,'trans dtrans dtrans-se hdb break-cj').text
                    examplist[currentdef].append(examp)
                currentdef += 1
            return examplist
        
        def EN():
            """
            get English examp sentence
            ( need more resources due to looping through 'span')
            """
            currentsen, currentdef = 0, 0
            examplist = []
            for samexamps in difexamps:
                examplist.append(list())
                for exblock in samexamps:
                    examp = exblock.find('span', 'eg deg')
                    # loop through the span getting pure word also element in class
                    # than assemble them togeter in to a complete sentence
                    examplist[currentdef].append('')
                    for part in examp :
                        # if Ture -> pure words, False -> is class (need .text to grab content)
                        if isinstance(part, NavigableString):
                            examplist[currentdef][currentsen] += part
                        else:
                            examplist[currentdef][currentsen] += part.text
                    currentsen += 1
                currentdef += 1; currentsen = 0 
            return examplist
        return EN(), CH()

    examp = getAllExamp()
    return getAllDef(), examp[0], examp[1]

    # Small Block
    # old 
    """
    def find_PartOfSpeech(dict):
        PartOfSpeech = dict.find('span', 'pos dpos').text
        print(PartOfSpeech)

    def find_more(dict):
        more = dict.findAll('span', 'trans dtrans dtrans-se break-cj')
        for i in more:
            print(i.text)
    """