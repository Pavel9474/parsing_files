import requests
from bs4 import BeautifulSoup

url="https://chel.istudio-shop.ru/catalog/iPhone/iPhone-15/"

headers={
    "Accept":"*/*",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
data=[['Наименование', 'Цена']]

def get_soup(url):
    res=requests.get(url,headers)
    return BeautifulSoup(res.content, 'html.parser')
iphones_page=get_soup(url)

for i in iphones_page:
    iphones=iphones_page.find_all('div', class_='product-item')
    for j in iphones:
        title=j.find('div',class_='blk_name').find('span').find(text=True)
        price=j.find('span',class_='cen').find(text=True).strip()
        print(title)
        print(price)
        data.append([title,price])
print(data)
        