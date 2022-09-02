import sqlite3 as sq
import re

import random
import requests
from bs4 import BeautifulSoup as bs4

# def ww():
#     url='http://hd.utorr.xyz/'
#     r=requests.get(url=url)
#     print(r)
# ww()

def film_torr():
    headers = {
        'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    url = 'http://hd.utorr.xyz/'
    session = requests.Session()
    req = session.get(url, headers=headers)
    news_list = []
    try:
        if req.status_code == 200:
            soup = bs4(req.content, 'html.parser')
            divs = soup.find_all('div',attrs= {'class':'post'})
            for div in divs:
                title = (div.find('a')).text
                href = div.find('a')['href']
                rating=div.find('div',attrs= {'class':'frate frate-kp'}).text
                img = div.find('img')['src']
                url_img = url + img
                news_list.append ([href,title,rating.replace('"',''),url_img])
        else:
            print('Ошибка')
    except Exception:
        print('Ошибка URL')

    return news_list


