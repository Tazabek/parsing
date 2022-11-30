import requests
from bs4 import BeautifulSoup as bs

site1 = input('По какому запросу нужно парсить?')
site1 = site1.replace(' ', '+')
url_head = 'https://www.avito.ru'
site = requests.get(f'https://www.avito.ru/all?q={site1}')
html = bs(site.content, 'html.parser')

names = html.find_all('div', class_='iva-item-slider-pYwHo')
for i in names:
    names1 = i.find('a').get('title')
    links = url_head+i.find('a').get('href')
    img_link = i.find('img').get('src')
    print(names1)
    print(links)
    with open('test2/list.txt', 'a', encoding='utf-8') as file:
        file.write(f'{names1}\n{links}\n{img_link}\n\n')
    
    