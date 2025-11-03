import requests
from bs4 import BeautifulSoup

class news:
    def __init__(self):
        self.city = 'mumbai'
        self.links = []
        self.titles = []
        self.images = []
    def ready(self):
        self.website = f'https://www.freepressjournal.in/{self.city}'
        self.request = requests.get(self.website)
        self.soup = BeautifulSoup(self.request.content,'html.parser')
    def get(self):
        self.links.clear()
        self.titles.clear()
        self.images.clear()
        dictionary = {}
        data1 =self.soup.find(id = 'storyList')
        data = data1.find_all('a')
        image_data = data1.find_all('img')
        for image in image_data:
            self.images.append(image['data-src'])
        
        for i in data:
            title =str(i.text)
            for inty in range(1,20):
                title =title.replace('\n','')
            title = title.replace('... Read More','')
            self.titles.append(title)
            self.links.append(i['href'])
        dictionary['titles'] = self.titles
        dictionary['links'] = self.links
        dictionary['images'] = self.images
        return dictionary

class article:
    def __init__(self,URL):
        self.url = URL
    def ready(self):
        try:
            self.request = requests.get(self.url)
            self.soup = BeautifulSoup(self.request.content,'html.parser')
            self.title = self.soup.find(id = 'heading-1').text
            self.heading = self.soup.find(id = 'heading-2').text
            self.articl = self.soup.find(id = 'fjp-article').find_all('p')
            self.p1 = self.articl[0].text
            self.p2 = self.articl[1].text
            self.p3 = self.articl[2].text
        except:
            pass
        self.image = self.soup.find(id = 'article-leadimage').find('img')['src'].replace('?width=1200','')
if __name__== '__main__':
    articl = article("https://www.freepressjournal.in/mumbai/maharashtra-oath-taking-ceremony-devendra-fadnavis-18th-chief-minister-eknath-shinde-ajit-pawar-dycms")
    articl.ready()