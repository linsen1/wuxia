#coding=utf-8
import requests,bs4
import json,re
import chardet
import pprint
import csv
import datetime
import time
outPutFile=open('city.csv','w',newline='')
outputWriter=csv.writer(outPutFile)
outputWriter.writerow(["post_id","post_name","post_author","post_date","post_type","post_status","post_title","post_content","post_category","post_tags","custom_field"])
url='http://www.wuxiaworld.com/cos-index/'
res=requests.get(url)
try:
    res.raise_for_status()
    dataContent = bs4.BeautifulSoup(res.text)

    articleList = dataContent.select('div[itemprop] p a')
    for item in articleList[2:]:
        print(item.attrs['href'])
        title=item.getText()
        res1 = requests.get(item.attrs['href'])
        res1.raise_for_status()
        dataContent1 = bs4.BeautifulSoup(res1.text)
        article = dataContent1.select('div[itemprop]')
        contens=article[0]
        outResult1=contens
        try:
            contens=str(article[0])[str(article[0]).index('<hr')+6:]
            outResult1 = contens[0:contens.rindex('<p>')]
        except Exception as exc:
            print('erro:%s' % (exc))
        outputWriter.writerow(["", title, "linsen", datetime.datetime.now(), "post", "publish",
                                   title, outResult1, "City of Sin", "City of Sin", ""])
        print('success')
    outPutFile.close()
except Exception as exc:
    print('erro:%s' % (exc))