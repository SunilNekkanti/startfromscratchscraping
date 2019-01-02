from bs4 import BeautifulSoup
import requests
import re
import prettytable

url = "http://indianroommates.sulekha.com/offered_male_roommates_in-and-near_chandler-az"
pt = prettytable.PrettyTable()
base_url  = "http://indianroommates.sulekha.com"
reqObject  = requests.get(url)

byteContent = reqObject.content

textContent = reqObject.text

soup = BeautifulSoup(textContent, 'html.parser')

listings = []
for link in soup.find_all('a', id=re.compile(r'title')):
    secreq = requests.get(base_url + link.get('href'))
    digsoup = BeautifulSoup(secreq.text, 'html.parser')

    for details in digsoup.find_all('div', id='desc350'):
        print(details.text)

    for details in digsoup.find_all('article', class_='roomdetails'):
        print(details.text)
