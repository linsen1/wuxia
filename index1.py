#coding=utf-8
import requests,bs4
import json,re
import chardet
import pprint
import csv
outPutFile=open('out.csv','w',newline='')
outputWriter=csv.writer(outPutFile)
outputWriter.writerow(["post_id","post_name","post_author","post_date","post_type","post_status","post_title","post_content","post_category","post_tags","custom_field"])
url='http://www.wuxiaworld.com/awe-index/'
res=requests.get(url)
try:
    res.raise_for_status()
    dataContent=bs4.BeautifulSoup(res.text)
    articleList=dataContent.select('.chapterlist li a')
    for item in articleList:
        res1=requests.get(url+item.attrs['href'])
        try:
            res1.raise_for_status()
            dataContent1=bs4.BeautifulSoup(res1.text)
            article=dataContent1.select('.content')
            outputWriter.writerow(["",item.getText().replace('â','\''),"linsen","2017-12-01 0:00","post","publish",item.getText().replace('â','\''),article,"A Will Eternal","A Will Eternal",""])
            pprint.pprint(article[0])
        except Exception as exc:
            print('erro:%s' % (exc))
        print(item.attrs['href'])
    outPutFile.close()
except Exception as exc:
    print('erro:%s'%(exc))