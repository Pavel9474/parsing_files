
from requests import Session
from bs4 import BeautifulSoup
import time, random

base_url="https://scrapingclub.com/exercise/list_infinite_scroll/"

headers={"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

def main(base_url):
    s=Session()
    s.headers.update(headers)
    count=1
    pagination=0
    while True:
        if count>1:
            url=base_url+'?page='+str(count)
        else:
            url=base_url
        response=s.get(url)
        # with open('data.html','w', encoding='utf-8') as r:
        #     r.write(response.text)
        soup= BeautifulSoup(response.text, 'lxml')
        if count==1:
            pagination=int(((soup.find('nav', class_='pagination').find_all('a'))[-2]).text)
            print(pagination)

        cards=soup.find_all('div', class_="w-full rounded border post")
        for card in cards:
            name=card.find('h4').text
            price=card.find('h5').text
            print(name,price)
        print(count)
        time.sleep(random.choice([5,7,9]))
        if count==pagination:
            break
        count+=1

        




main(base_url)