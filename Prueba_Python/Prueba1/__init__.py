import requests
from  bs4 import BeautifulSoup
website= "https://www.pccomponentes.com"
result=requests.get(website)
content=result.text
soup=BeautifulSoup(content,'html.parser')
#inicio=soup.find_all("pre")
print(soup.title)
print(soup)