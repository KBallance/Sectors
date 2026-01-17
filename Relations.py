import pandas
import nltk
from nltk.corpus import PlaintextCorpusReader
import requests as rq
from bs4 import BeautifulSoup

class Relations:
    def __init__(self, sources):
        self.src = sources
        #get file, read contents \
        #request pages \
        #copy content + links seperate \
        #filter links
        #traverse links
        #repeat for D times
        return None
    
    def loopSources(self):
        file = open(self.src)
        link = file.readline()
        #while not(link == ""):
        self.getpage(link)
        link = file.readline()
        
        return None

    
    def getpage(self, link):
        link = link.strip()
        headers = {'User-Agent' : 'KBProjectBot/0.1 (filler@hw.ac.uk)'}
        page = rq.get(link, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        print(page.status_code)
        links = soup.find_all("a")
        contents = soup.find_all("p")

        print(f"{link}: ")
        print(f"links: \n{links}")
        print(f"contents: \n {contents}")

        return None


        
