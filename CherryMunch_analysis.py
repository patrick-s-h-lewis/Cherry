import requests
import scrapy
from scrapy.http import TextResponse
from datetime import datetime
import re
import pymongo
from pymongo import MongoClient
import json
import signal
import warnings
import sys
import os

def get_paths(publisher,conn,doi):
    ###to do, build database with all of these
    cur = ca.find({'pub_website':publisher})
    if cur.count()==0:
        raise Exception('no publisher website for '+ doi) 
    return cur

def get_publisher(response):
    url = response.url
    publisher = url.split('/')[2]
    return publisher

def handler(signum,frame):
    raise Exception()

def choose_items(items):
    if len(items)==1:
        return items[0]
    else:
        scores=[]
        for it in items:
            score = 0
            for k,v in it.items():
                if type(v)=='str':
                    v=v.strip()
                    if not(v==u''): score+=1
                else:
                    if not(v==[]):
                        score+=1
            scores.append(score)
        return items[scores.index(max(scores))]
        
warnings.filterwarnings("ignore")

mongo_url = 'mongodb://localhost:27017/' #local
#mongo_url = 'mongodb://localhost:6666/' #remote
db = 'Cherry'
coll = 'CherryMunch'
client = MongoClient(mongo_url)
ca = client[db][coll]
ind=0
dead=0
scraped = 'scraped.json'
losses = 'losses.json'
with open(losses,'w') as fd:
    fd.write('[')
with open(scraped,'w') as fd:
    fd.write('[')
    
with open('stuff.json','r') as f:
    j = json.load(f)
    for rec in j:
        print(ind)
        ind+=1
        item = {}
        doi = rec['doi']
        target_stub = 'http://dx.doi.org/'
        target = target_stub + doi
        die = True
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(10)
        try: 
            r = requests.get(target)
            response=TextResponse(r.url,body=r.text, encoding='utf-8')
        ###SENSE Who's publisher this is
            pub = get_publisher(response)
        ###LOAD CORRECT XPATHS:
            try:
                paths_list = get_paths(pub,ca,doi)
                die=False
            except:
                die=True 
            if die:
                print('Missing Publisher Fail')
                rep = {'doi':doi,'error':'missing_pub','pub':pub}
                with open(losses,'a') as fd:
                    json.dump(rep,fd,sort_keys=True,indent=4,ensure_ascii=True)
                    fd.write(',')
        except:
            print('Page Timeout Fail')
            rep = {'doi':doi,'error':'timeout'}
            with open(losses,'a') as fd:
                json.dump(rep,fd,sort_keys=True,indent=4,ensure_ascii=True)
                fd.write(',')
        signal.alarm(0)
        if die:
            dead+=1
        else: 
            items = []
            for paths in paths_list:
                try:
                    title= response.xpath(paths['x_title']).extract()[0]
                    abstract = response.xpath(paths['x_abstract']).extract()[0]
                    people = response.xpath(paths['x_people'])
                    depts = response.xpath(paths['x_depts'])
                    pex=[]
                    dex=[]
                    for person in people:
                        p = person.xpath(paths['x_person']).extract()
                        if not(p==[])and (len(p)==1):
                            pex.append(p[0])
                        else:
                            pex.append(p)
                    for dept in depts:
                        d = dept.xpath(paths['x_dept']).extract()
                        if not(d==[]):
                            dex.append(d[0])
                    exec paths['name_con']
                    date = response.xpath(paths['x_date']).extract()[0]
                    exec paths['date_con']
                    dex = list(set(dex))
                    pex = list(set(pex))
                    item = {
                        'title':re.sub('\n','',title),
                        'authors':pex,
                        'depts':dex,
                        'abstract':re.sub('\n','',abstract),
                        'date': date.strftime('%d %B %Y'),
                        'doi':doi,
                        'publisher':paths['publisher']
                    }
                    items.append(item)
                except:
                    pass
            try:
                item = choose_items(items)
                with open(scraped,'a') as fo:
                    json.dump(item,fo,sort_keys=True,indent=4,ensure_ascii=True)
                    fo.write(',')
            except:
                print('Collection Fail')
                rep = {'doi':doi,'error':'collection','pub':pub}
                with open(losses,'a') as fd:
                    json.dump(rep,fd,sort_keys=True,indent=4,ensure_ascii=True)
                    fd.write(',')
                dead+=1
with open(scraped, 'rb+') as fo:
    fo.seek(-1, os.SEEK_END)
    fo.truncate()
    fo.write(']')
with open(losses, 'rb+') as fd:
    fd.seek(-1, os.SEEK_END)
    fd.truncate()
    fd.write(']')
print('proportion of records not collected: ' + str(dead))
