'''
Created on 17 oct 2022

@author: zorro
'''
from bs4 import BeautifulSoup
import cloudscraper
scraper = cloudscraper.create_scraper(delay=10,browser={'custom': 'ScraperBot/1.0',})
url = 'https://www.facebook.com/profile.php?id=100005602149811'
req = scraper.get(url)
soup = BeautifulSoup(req.content,'html.parser')
nombre = soup.find('h1','x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz')
estudios=soup.find_all('span','x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h')
amigos=[]
aux=soup.find_all(class_='x12upk82 xdt5ytf x78zum5 xod5an3')
for a in aux:
    aux2=soup.find_all(class_='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u')
    amigos.append(aux2)
print("NOMBRE")
print(nombre.text)
print("Amigos:")
print(amigos)
print(aux)
print(soup.find('span','xt0psk2'))