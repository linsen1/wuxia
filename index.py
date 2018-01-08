#coding=utf-8
import requests,bs4
import json,re
import chardet
import pprint
import csv
import datetime
import time

outPutFile=open('World.csv','w',newline='')
outputWriter=csv.writer(outPutFile)
outputWriter.writerow(["post_id","post_name","post_author","post_date","post_type","post_status","post_title","post_content","post_category","post_tags","custom_field"])
url='http://www.hiwuxia.com/0/115/'
res=requests.get(url)
try:
    res.raise_for_status()
    dataContent=bs4.BeautifulSoup(res.text)
    articleList=dataContent.select('.chapterlist li a')
    for item in articleList[0:2]:
        res1=requests.get(url+item.attrs['href'])
        try:
            res1.raise_for_status()
            dataContent1=bs4.BeautifulSoup(res1.text)
            article=dataContent1.select('.content')
            recontent=str(article[0])[str(article[0]).index('<br/>')+11:].lstrip('\n')
            print(recontent)
            outputWriter.writerow(["",item.getText(),"linsen",datetime.datetime.now(),"post","publish",item.getText(),recontent,"World Defying Dan God","World Defying Dan God",""])
        except Exception as exc:
            print('erro:%s' % (exc))
        print(item.attrs['href'])
    outPutFile.close()
except Exception as exc:
    print('erro:%s'%(exc))