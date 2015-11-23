record1 = {
        'publisher':'Wiley',
        'pub_website':'onlinelibrary.wiley.com',
        'x_title':'string(//*[@class="article-header__title"])',
        'x_abstract':'string(//*[@id="abstract"]/div/p)',
        'x_people':'//*[@class="article-header__authors-item"]',
        'x_depts':'//*[@class="article-header__authors-item"]',
        'x_person':'string(.//*[@class="article-header__authors-name"])',
        'x_dept':'string(.//*[@class="article-header__authors-item-aff-addr"])',
        'x_date':'string(//time[@id="first-published-date"])',
        'date_con':'''
date = datetime.strptime(date,'%d %B %Y')''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    if u'Dr.' in words:
        words.remove(u'Dr.')
    for w in words[:-1]:
        if not(w==u''):
            name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record2 = {
        'publisher':'Wiley',
        'pub_website':'onlinelibrary.wiley.com',
        'x_title':'string(//*[@class="articleTitle"])',
        'x_abstract':'string(//*[@id="abstract"]/div[@class="para"])',
        'x_people':'//*[@id="authors"]/li',
        'x_depts':'//*[@id="authorsAffiliations"]/li',
        'x_person':'text()',
        'x_dept':'p/text()',
        'x_date':'string(//p[@id="publishedOnlineDate"])',
        'date_con':'''
date = datetime.strptime(u' '.join(date.split(' ')[-3:]),'%d %b %Y')
        ''',   
        'name_con':'''
pex2 = []
pexl=[]
for p in pex:
    if type(p)==list:
        pexl+=p
    else:
        pexl.append(p)
for p in pexl:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    p = re.sub(' and','',p )
    words = p.split(" ")
    if u'Dr.' in words:
        words.remove(u'Dr.')
    for w in words[:-1]:
        if not(w==u''):
            name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=filter(lambda x: x!=u' ',pex2)
'''
    }

record3 = {
        'publisher':'ACS',
        'pub_website':'pubs.acs.org',
        'x_title':'string(//*[@class="articleTitle"])',
        'x_abstract':'string(//*[@id="abstractBox"])',
        'x_people':'//*[@id="authors"]/span',
        'x_person':'string(span[1])',
        'x_depts':'//*[@class="affiliations"]/div',
        'x_dept':'string(.)',
        'x_date':'string(//*[@id="pubDate"])',
        'date_con':'''
sp = date.split(' ')
date = datetime.strptime(' '.join([sp[-3]]+[sp[-2][:-1]]+[sp[-1]]),'%B %d %Y')''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record4 = { 'publisher':'American Physical Society',
        'pub_website':'journals.aps.org',
        'x_title':'//div[@id="title"]/descendant::h3/text()',
        'x_abstract':'//meta[@name="description"]/@content',
        'x_people':'//section[@class="article authors open"]/div/p',
        'x_person':'*[1]/text()',
        'x_depts':'//section[@class="article authors open"]/div/ul[@class="no-bullet"]',
        'x_dept':'li/text()',
        'x_date':'//ul[@class="inline-list pub-dates"]/li/text()',
        'date_con':'''
sp = date.split(' ')
date = datetime.strptime(' '.join(sp[1:]),'%d %B %Y')''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record5 = { 'publisher':'Springer',
        'pub_website':'link.springer.com',
        'x_title':'//*[@class="ArticleTitle"]/text()',
        'x_abstract':'string(//*[@id="Abs1"]/p)',
        'x_people':'//ul[@class="AuthorNames"]/li',
        'x_person':'*/span[@class="AuthorName"]/text()',
        'x_depts':'//ul[@class="AuthorNames"]/li',
        'x_dept':'descendant::span[@class="AuthorsName_affiliation"]/span/text()',
        'x_date':'//*[@class="ArticleCitation_Year"]/time/text()',
        'date_con':'''
sp = date.split(' ')
date = datetime.strptime(date,'%d %B %Y')''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record6 = { 'publisher':'Springer',
        'pub_website':'link.springer.com',
        'x_title':'//*[@class="ArticleTitle"]/text()',
        'x_abstract':'string(//*[@id="Abs1"]/p)',
        'x_people':'//ul[@class="AuthorNames"]/li',
        'x_person':'*/span[@class="AuthorName"]/text()',
        'x_depts':'//ul[@class="AuthorNames"]/li',
        'x_dept':'descendant::span[@class="AuthorsName_affiliation"]/span/text()',
        'x_date':'//*[@class="ArticleCitation_Year"]/time/text()',
        'date_con':'''
sp = date.split(' ')
date = datetime.strptime(date,'%B %Y')''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record7 = { 'publisher':'ScienceDirect',
        'pub_website':'www.sciencedirect.com',
        'x_title':'//*[@class="svTitle"]/text()',
        'x_abstract':'string(//*[@class="abstract svAbstract "])',
        'x_people':'//ul[@class="authorGroup noCollab svAuthor"]/li',
        'x_person':'*[@class="authorName svAuthor"]/text()',
        'x_depts':'//ul[@class="affiliation authAffil"]/li',
        'x_dept':'span/text()',
        'x_date':'//dl[@class="articleDates"]/dd/text()',
        'date_con':'''
sp = date.split(' ')
date = datetime.strptime(" ".join(sp[-3:]),'%d %B %Y')''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record8 = { 'publisher':'International Union of Crystallography',
        'pub_website':'scripts.iucr.org',
        'x_title':'string(//*[@class="ica_title"])',
        'x_abstract':'string(//*[@class="ica_abstract"])',
        'x_people':'//*[@class="ica_authors"]/a',
        'x_person':'string(.)',
        'x_depts':'//none-here',#no affiliations given on page
        'x_dept':'//none-here',
        'x_date':'//div[@class="ica_header"]/span[2]/text()',
        'date_con':'''
date = datetime.strptime(date[2:6],'%Y')''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record9 = { 'publisher':'scientific.net',
        'pub_website':'www.scientific.net',
        'x_title':'//div[@class="paper-title"]/div[@class="paper-name"]/text()',
        'x_abstract':'//div[@class="abstract"]/p/text()',
        'x_people':'//div[text()="\r\n                                        Authors\r\n                                    "]/following-sibling::div/a',
        'x_person':'string(.)',
        'x_depts':'//none-here',#no affiliations given on page
        'x_dept':'//none-here',
        'x_date':'//div[text()="\r\n                                        Online since\r\n                                    "]/following-sibling::div/text()',
        'date_con':'''
date = datetime.strptime(date.strip(),'%B %Y')''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record10 = { 'publisher':'jstage',
        'pub_website':'www.jstage.jst.go.jp',
        'x_title':'string(//*[contains(@class,"mod-article-heading")])',
        'x_abstract':'string(//*[contains(@class,"mod-section")]/p)',
        'x_people':'//*[contains(@class,"author")]/a',
        'x_person':'text()',
        'x_depts':'//*[contains(@class,"affiliation")]',
        'x_dept':'text()',
        'x_date':'string(//*[contains(@class,"date")])',
        'date_con':'''
ds = re.sub("[^0-9]", "", date)
dates = [datetime.strptime(ds[i:i+8],'%Y%m%d') for i in range(0,len(ds),8)]
date = min(dates)''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record11 = { 'publisher':'rsc',
        'pub_website':'pubs.rsc.org',
        'x_title':'string(//div[@class="article_chemsoc_txt_s13"])',
        'x_abstract':'string(//div[@class="abstract_new"])',
        'x_people':'//div[@class="peptide_middle"]/div[1]/span',
        'x_person':'a/text()',
        'x_depts':'//div[@class="show_affiliation_section"]/div[position()>2]',
        'x_dept':'div[2]/text()',
        'x_date':'//div[@class="peptide_middle"]/span[last()]/text()[1]',
        'date_con':'''
try:
    d = [i.strip() for i in date.strip().split(' ')]
    p = filter(lambda x: not(x==u''),d)
    date = u' '.join(p[-3:])
    date = datetime.strptime(date,'%d %b %Y')
except:
    pass''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    words = filter(lambda x: not(x==u''),words)
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record12 = { 'publisher':'iop',
        'pub_website':'iopscience.iop.org',
        'x_title':'string(//*[@class="wd-jnl-art-title"])',
        'x_abstract':'string(//div[contains(@class,"wd-jnl-art-abstract")]/p)',
        'x_people':'//span[@data-authors]/span',
        'x_person':'span[@itemprop="name"]/text()',
        'x_depts':'//div[@class="wd-jnl-art-author-affiliations"]/p',
        'x_dept':'text()',
        'x_date':'//div[contains(@class,"wd-jnl-art-dates")]/p/text()',
        'date_con':'''
d= date.strip()
datetime.strptime(' '.join(d.split(u' ')[-3:]),'%d %B %Y')''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    words = filter(lambda x: not(x==u''),words)
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record13 = { 'publisher':'RoyalSociety',
        'pub_website':'rsif.royalsocietypublishing.org',
        'x_title':'//*[@id="page-title"]/text()',
        'x_abstract':'//*[@id="abstract-1"]/p/text()',
        'x_people':'//span[@class="highwire-citation-authors"]/span',
        'x_person':'string(.)',
        'x_depts':'//span[@class="nlm-aff"]',
        'x_dept':'string(.)',
        'x_date':'//span[contains(@class,"highwire-cite-metadata-date")]/text()',
        'date_con':'''
date=datetime.strptime(' '.join(date.split(u' ')[-3:]),"%d %B %Y")''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    words = filter(lambda x: not(x==u''),words)
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record14 = { 'publisher':'RoyalSociety',
        'pub_website':'rspa.royalsocietypublishing.org',
        'x_title':'//*[@id="page-title"]/text()',
        'x_abstract':'//*[@id="abstract-1"]/p/text()',
        'x_people':'//span[@class="highwire-citation-authors"]/span',
        'x_person':'string(.)',
        'x_depts':'//span[@class="nlm-aff"]',
        'x_dept':'string(.)',
        'x_date':'//span[contains(@class,"highwire-cite-metadata-date")]/text()',
        'date_con':'''
date=datetime.strptime(' '.join(date.split(u' ')[-3:]),"%d %B %Y")''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    words = filter(lambda x: not(x==u''),words)
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record15 = { 'publisher':'Scitation',
        'pub_website':'scitation.aip.org',
        'x_title':'string(//*[@class="title-with-crossmark"])',
        'x_abstract':'string(//*[contains(@class,"abstract ")]/descendant::*[@class="articleabstract"]/p[2])',
        'x_people':'//span[contains(@class,"authors")]/a',
        'x_person':'text()',
        'x_depts':'//div[contains(@class,"affiliations")]/a',
        'x_dept':'text()',
        'x_date':'//div[contains(@class,"itemCitation")]/span[3]/text()',
        'date_con':'''
d = date[:-1].split(u" ")
date=datetime.strptime(u' '.join(d[2:4] + [d[-1]]),"%b %d %Y")''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    words = filter(lambda x: not(x==u''),words)
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record16 = { 'publisher':'Nature',
        'pub_website':'www.nature.com',
        'x_title':'//*[@class="article-heading"]/text()',
        'x_abstract':'string(//*[@id="abstract"]/div/p)',
        'x_people':'//*[contains(@class,"authors citation-authors")]/li',
        'x_person':'a[@class="name"]/span/text()',
        'x_depts':'//ol[contains(@class,"affiliations")]/li',
        'x_dept':'h3/text()',
        'x_date':'//*[contains(@class,"citation dates")]/dd[1]/time/text()',
        'date_con':'''
date=datetime.strptime(date.strip(),"%d %B %Y")''',   
        'name_con':'''
pex2 = []
for p in pex:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    words = p.split(" ")
    words = filter(lambda x: not(x==u''),words)
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex2.append(name)
pex=pex2'''
    }

record17 = { 'publisher':'degruyter',
        'pub_website':'www.degruyter.com',
        'x_title':'string(//*[@class="entryTitle"])',
        'x_abstract':'string(//*[@class="articleBody_abstract"]/p)',
        'x_people':'//*[@class="contributors"]/descendant-or-self::*',
        'x_person':'./text()',
        'x_depts':'//*[contains(@class,"NLM_affiliations")]/p',
        'x_dept':'text()',
        'x_date':'//*[contains(@id,"date-received")]/dd/text()',
        'date_con':'''
datetime.strptime(date,"%Y-%m-%d")''',   
        'name_con':'''
pex2=[]
for p in pex:
    if type(p)==list:
        for p1 in p:
            if (len(p1.strip())>3): 
                pex2.append(p1.strip())
    elif p==[]:
        pass
    else:
        if len(p.strip())>3: 
            pex2.append(p.strip())
pex3=[]
for p in pex2:
    name = ""
    p = re.sub(r"\s+", u" ", p, flags=re.UNICODE)
    p = re.sub(',',u'',p)
    p = re.sub('/',u'',p)
    words = p.split(" ")
    words = filter(lambda x: not(x==u''),words)
    if words[0] in [u'Dr.']:
        words.remove(words[0])
    for w in words[:-1]:
        name+=w[0]
    name+=u" "+words[-1]
    pex3.append(name)
pex=pex3'''
    }

