#import datacrawl
from urllib.request import urlopen
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
url="https://www.dotabuff.com"
section='/esports/teams'

headers = {
    'User-Agent': 'My User Agent 1.0'
}
def request(url,section):
    response = requests.get(url+section, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
soup=request(url,section)
myset = set([url+link.get('href')
             for link in soup.findAll('a',{'class': 'esports-team esports-link team-link'})])
print(list(myset)[0])

#myset = set([url+link.get('href')
 #            for link in soup.findAll('a',{'class': ''})])
