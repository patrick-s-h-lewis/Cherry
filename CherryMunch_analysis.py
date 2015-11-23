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

warnings.filterwarnings("ignore")


def handler(signum,frame):
    raise Exception()

mongo_url = 'mongodb://localhost:27017/'
db = 'Cherry'
coll = 'CherryMunch'
client = MongoClient(mongo_url)
ca = client[db][coll]

ind=0
dead=0
with open('stuff.json','r') as f:
    j = json.load(f)
    for rec in j:
        if ind%100==0:
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
                print('I Died with DOI '+str(doi)+" and publisher " + str(pub))
        except:
            print('timeout die with '+str(doi))
        signal.alarm(0)
        if die:
            dead+=1
        else: 
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
                        'date': date,
                        'doi':doi,
                        'publisher':pub
                     }
                except:
                    pass
            try:
                a=item['title']
                b=item['abstract']
                c=item['authors']
                d=item['depts']
                e=item['date']
            except:
                print('I Died with DOI '+str(doi)+"and publisher" + str(pub))
                print(item)
print('proportion of records not collected: ' + str(dead))