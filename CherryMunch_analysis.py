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
                v=v.strip()
                if not(v==u''): score+=1
            scores.append(score)
        print(scores)
        return items[scores.index(max(scores))]

        
        
warnings.filterwarnings("ignore")
mongo_url = 'mongodb://localhost:27017/'
db = 'Cherry'
coll = 'CherryMunch'
client = MongoClient(mongo_url)
ca = client[db][coll]
fo = open('scraped.json','w')
fd = open('losses.json','w')


ind=0
dead=0
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
                json.dump({'doi':doi,'error':'missing_pub','pub':pub},fd,sort_keys=True,indent=4,ensure_ascii=False)
        except:
            json.dump({'doi':doi,'error':'timeout'},fd,sort_keys=True,indent=4,ensure_ascii=False)
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
                    item = {
                        'title':title,
                        'authors':pex,
                        'depts':dex,
                        'abstract':abstract,
                        'date': date.strftime('%d %B %Y'),
                        'doi':doi,
                        'publisher':pub
                     }
                     items.append(item)
                except:
                    pass
            try:
                item = choose_items(items)
                a=item['title']
                b=item['abstract']
                c=item['authors']
                d=item['depts']
                e=item['date']
                json.dump(item,fo,sort_keys=True,indent=4,ensure_ascii=False)
            except:
                json.dump({'doi':doi,'error':'collection','pub':pub},fd,sort_keys=True,indent=4,ensure_ascii=False)
                dead+=1
print('proportion of records not collected: ' + str(dead))