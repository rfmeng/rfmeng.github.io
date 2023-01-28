#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re
import json
import shutil
import datetime
from bs4 import BeautifulSoup


# In[ ]:


json.dumps({'1':'呵呵'},ensure_ascii=False)


# In[18]:


# from pages
def generate_json():
    pages = []
    result = []
    for i in os.walk('./pages'):
        for j in i[2]:
            # (title, path)
            pages.append((j[:-5],i[0].replace('\\','/')+'/'+j))
            title = j[:-5]
            pagepath = i[0].replace('\\','/')+'/'+j
            f = open(pagepath,'r',encoding='utf-8')
            pagesoup = BeautifulSoup(f.read(),'lxml')
            f.close()
            pagepath = pagepath[1:]
            div = pagesoup.find('div',class_='markdown-preview')
            category = div.ndtag['category']
            createdate = div.ndtag['createdate']
            editdate = div.ndtag['editdate']
            tag = div.ndtag['tag']
            result.append({'title':title,'path':pagepath,'category':category,'createdate':createdate,
                         'editdate':editdate,'tags':tag,'content':div.get_text().replace('\n','  ')})
    return json.dumps(result,ensure_ascii=False)


# In[20]:


temp = generate_json()


# In[22]:


f = open('./algolia/article.json','w',encoding='utf-8')
f.write(temp)
f.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




