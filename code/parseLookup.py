from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
url = 'https://dictionary.cambridge.org/dictionary/english-chinese-traditional/example'

def cambridge(word):
    request = requests.get(url, headers=headers).text
    soup = BeautifulSoup(request, 'lxml')
    dict = soup.body.find('div', 'pr entry-body__el')
    # print(dict)

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

    find_PartOfSpeech(dict)
    find_more(dict)


cambridge('gain')