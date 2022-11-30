import requests
from bs4 import BeautifulSoup as bs
import csv
import json

url = 'https://roscarservis.ru'
site = requests.get('https://roscarservis.ru/catalog/legkovye')
html = bs(site.content, 'html.parser')

with open('test/shiny.html', 'w', encoding='utf-8') as file:
   file.write(site.text)

with open('test/shiny.html', encoding='utf-8') as file:
   src = file.read()
soup = bs(src, 'lxml')
names = soup.find_all('a', class_='product__name')
img = soup.find('div', class_='catalog__group')

lst = []
lst1 = []
img_links = []
for i in img:
    img1 = str(i).split(',')
    lst.append(img1)
for el in lst:
    if len(el) > 10:
        lst1.append(el)
for els in lst1:
    link = els[20]
    img_links.append(url+str(link).split('"')[3][1:])

n = 0
all = []
for links in names:
    names1 = str(links).split('>')[-2][:-3]
    links1 = url + str(links).split('"')[3]
    all.append(
        {
            'Название' : names1,
            'Ссылка' : links1,
            'Ссылка картинки' : img_links[n]
        }
    )
    n += 1

    with open('test/shin.csv', 'a', encoding='utf-8') as file:
       writer = csv.writer(file)
       writer.writerow(
           (
             names1,
             links1,
             img_links[n]
           )
        )
    if n == 6:
        break

with open('test/shiny.json', 'a', encoding='utf-8') as file:
    json.dump(all, file, indent=4, ensure_ascii=False)

