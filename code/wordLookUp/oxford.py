from bs4 import BeautifulSoup, NavigableString
import requests, logging

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
oxford_url = 'https://www.freecollocation.com/search?word='

def oxford(word):
    """
    return different usage 


    result :
        first layer --> oraginze with part of speech 
            second layer -->  { [0]first list  --> words to use
                                [1]second list --> example sentences
                              }
    """
    result = []
    request = requests.get(oxford_url+word, headers=headers).text
    soup = BeautifulSoup(request, 'lxml')
    dict = soup.body.find('div', 'item')

    difmeans = dict.findAll('p', class_ = '')
    # putting infomation into result on part of speech a time
    for i in range(len(difmeans)) :
        difmean = difmeans[i]
        result.append(list())
        result[i].append('')
        result[i].append('')

        # find words to use 
        for w in difmean.findAll('b'):
            result[i][0] += ', ' if result[i][0] != '' else ''
            result[i][0] += w.text.strip().replace(' | ', ', ')
        # find example sentences
        for s in difmean.findAll('i'):
            result[i][1] += '\n' if result[i][1] != '' else ''
            result[i][1] += s.text.strip()

    
    print(result)

oxford('find')