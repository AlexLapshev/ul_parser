import requests
from bs4 import BeautifulSoup
import csv


def writer_csv(desc,item_name,link,price,file):

    res = []
    res.append(item_name)
    res.append(desc)
    res.append(price)
    res.append(link)
    w = csv.writer(file, delimiter=';')
    w.writerow(res)


with open('phones.csv', 'w', newline='') as phones_csv:
    for i in range(1, 7):
        r = requests.get('https://www.ulmart.ru/catalog/communicators?pageNum={}'.format(i))
        soup = BeautifulSoup(r.text, 'html.parser')

        table = soup.find('div', {'id': 'catalogGoodsBlock'})
        items = table.findAll('div', {'class': 'b-box__i'})

        for item in items:

            desc = item.find('div', {'class': 'b-product__descr'}).text
            price = item.find('span', {'class': 'b-price__num js-price'}).text.strip()
            item = item.find('a', {'class': 'must_be_href js-gtm-product-click'})
            link = 'http://ulmart.ru' + item['href']
            item_name = item.text.strip().split('Смартфон')[-1]

            writer_csv(desc, item_name,link,price, phones_csv)
