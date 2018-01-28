# -*- coding: utf-8 -*-

from PttWebCrawler.crawler import PttWebCrawler
from multiprocessing import Pool
import threading
import requests
import re
from bs4 import BeautifulSoup as bs







def crawler(title):
    r = requests.get('https://www.ptt.cc/bbs/'+title+'/index.html',cookies={'over18': '1'}, verify=True)
    sp = bs(r.text,'html.parser')
    end = 999999
    for i in sp.find_all('a'): 
        if i.get('href')!= None:
            if re.match('/bbs/'+title+'/index(\d)+.html',i.get('href'))!=None:
                if int(re.findall('[\d]+',i.get('href'))[0])!=1:end = int(re.findall('[\d]+',i.get('href'))[0])+1
    print(end)                  
    c = PttWebCrawler(as_lib=True)
    c.parse_articles(1,1,title)


r = requests.get('https://www.ptt.cc/bbs/hotboards.html',cookies={'over18': '1'}, verify=True)
sp = bs(r.text,'html.parser')
lis = [i.text for i in sp.find_all('div',{'class':"board-name"})]


p = Pool(4)
p.map(crawler, lis)
    