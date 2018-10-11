import scrapy
import json
import scrapy
import re
import urllib
import requests
import copy
urls = "http://arxiv.org/list/cs/recent"
ress = requests.get(urls)
payload=ress.text
titile = re.findall('<span class="descriptor">Title:</span>(.*?)</div>',payload,re.S)
author = re.findall('<span class="descriptor">Authors:</span>(.*?)</div>',payload,re.S)
link = re.findall('<a href="/pdf/(.*?)title="Download PDF">',payload,re.S)
subject=re.findall('<span class="primary-subject">(.*?)</span>',payload,re.S)
urlfirebase ="https://inf551-project-f2b8e.firebaseio.com/"
di=dict()
result=dict()
for i in range(0,len(titile)):
        au = []
        di['title']=titile[i][:-2]
        di['link']=('arxiv.org/pdf/'+link[i])[:-2]
        di['subject']=subject[i]
        di['date']='Thu,11 Oct 2018 '
        author2 = re.findall('">(.*?)</a>', author[i], re.S)
        for item in author2:
                au.append(item)
        di['author']=copy.deepcopy(au)
        result[str(i)]=copy.deepcopy(di)

urls = "https://arxiv.org/list/cs/pastweek?skip=154&show=75"
ress = requests.get(urls)
payload=ress.text
titile = re.findall('<span class="descriptor">Title:</span>(.*?)</div>',payload,re.S)
author = re.findall('<span class="descriptor">Authors:</span>(.*?)</div>',payload,re.S)
link = re.findall('<a href="/pdf/(.*?)title="Download PDF">',payload,re.S)
subject=re.findall('<span class="primary-subject">(.*?)</span>',payload,re.S)
urlfirebase ="https://inf551-project-f2b8e.firebaseio.com/arxiv.json"
for i in range(0,len(titile)):
        au = []
        di['title']=titile[i][:-2]
        di['link']=('arxiv.org/pdf/'+link[i])[:-2]
        di['subject']=subject[i]
        di['date']='Thu,10 Oct 2018 '
        author2 = re.findall('">(.*?)</a>', author[i], re.S)
        for item in author2:
                au.append(item)
        di['author']=copy.deepcopy(au)
        result[str(i+25)]=copy.deepcopy(di)

jsonfile= json.dumps(result)
f = open('result.txt', 'w')
f.write(jsonfile)
res =requests.post(urlfirebase,data=jsonfile)