#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re
import shutil
import datetime
from bs4 import BeautifulSoup


# In[2]:


def article_generate(soup,templatehtml):
    substitute=dict()
    # article
    soup.find('div',class_='markdown-preview')['class'].append('post-body')
    soup.find('div',class_='markdown-preview')['for'] = 'html-export'
    # image path
    for i in soup.find('div',class_='markdown-preview').find_all('p',class_='wrapper'):
        i.img['src'] = '/'+i.img['src']
    # article nav
    def nav(soup):
        menu = []
        for i in list(soup.find('div',class_='markdown-preview').descendants):
            if i.name=='h3':
                menu.append([i.get_text(),[]])
            if i.name=='h4':
                menu[-1][-1].append(i.get_text())
        result='<ol class="nav">'
        idl = []
        for x,i in enumerate(menu):
            temp = '<li class="nav-item nav-level-1"><a class="nav-link" href="{}"><span class="nav-number">{}.</span> <span class="nav-text">{}</span></a>'.format('#nav'+str(x+1),x+1,i[0])
            idl.append('nav'+str(x+1))
            if i[1]:
                subtemp = '<ol class="nav-child">'
                for y,j in enumerate(i[1]):
                    subtemp += '<li class="nav-item nav-level-2"><a class="nav-link" href="{}"><span class="nav-number">{}.</span> <span class="nav-text">{}</span></a></li>'.format('#nav'+str(x+1)+'.'+str(y+1),str(x+1)+'.'+str(y+1),j)
                    idl.append('nav'+str(x+1)+'.'+str(y+1))
                subtemp += '</ol>'
                temp+=subtemp
            temp += '</li>'
            result += temp
        result+='</ol>'
        x=0
        for i in soup.find('div',class_='markdown-preview').descendants:
            if i.name=='h3' or i.name=='h4':
                i['id'] = idl[x]
                i.string = idl[x][3:] +'. '+ i.text
                x+=1
        return result
    navhtml = nav(soup)
    
    # subsitute generation
    substitute['title'] = soup.title.get_text()
    substitute['nav'] = navhtml
    substitute['article'] = str(soup.find('div',class_='markdown-preview'))
    ndtag = soup.find('ndtag')
    substitute['category'] = ndtag['category']
    substitute['modify date'] = ndtag['editdate']

    tags = [i.replace('-',' ') for i in ndtag['tag'].split()]
    taghtml=''
    for i in tags:
        taghtml+='<a href="" rel="tag"># {}</a>'.format(i)
    substitute['tags'] = taghtml
    resulthtml=templatehtml
    # make all substitue
    for i in substitute:
        resulthtml=resulthtml.replace('@@begin-{}-end@@'.format(i),substitute[i])
    return resulthtml


# In[3]:


# new article page generate
f = open('./templates/article template.html',encoding='utf-8')
article_template = f.read()
f.close()


# In[4]:


for i in os.listdir('./markdown'):
    if i[-5:]=='.html':
        f = open('./markdown/'+i,'r',encoding='utf-8')
        soup = BeautifulSoup(f.read(),'lxml')
        f.close()
        s = article_generate(soup,article_template)
        soup = BeautifulSoup(s,'lxml')
        category = soup.find('ndtag')['category']
        if category not in os.listdir('./pages/'):
            os.mkdir('./pages/'+category)
        f = open('./pages/{}/{}'.format(category,i),'w',encoding='utf-8')
        f.write(s)
        f.close()
        shutil.move('./markdown/'+i,'./source/'+i)


# In[5]:


# new main page generate
def index_generate(templatehtml):
    category = dict()
    for i in os.listdir('./pages'):
        category[i] = os.listdir('./pages/'+i)
    result = ''
    for i in category:
        result += '<h3>{}</h3>'.format(i)
        result += '<ul>'
        for j in category[i]:
            result += '<li><a class="category" href="{}">{}</a></li>'.format('./pages/{}/{}'.format(i,j),j[:-5])
        result += '</ul>'
    resulthtml = templatehtml.replace('$$begin-edit time-end$$',str(datetime.date.today()))
    resulthtml = resulthtml.replace('$$begin-category content-end$$',result)
#     print(category)
    return resulthtml


# In[6]:


# new article page generate
f = open('./templates/main template.html',encoding='utf-8')
main_template = f.read()
f.close()


# In[7]:


main_html = index_generate(main_template)


# In[8]:


f = open('index.html','w',encoding='utf-8')
f.write(main_html)
f.close()


# In[ ]:





# In[10]:


# footer next and prev button
def footer():
    temp = []
    for i in os.walk('./pages/'):
        for j in i[2]:
            temp.append((j[:-5],i[0]+'/'+j))
    for x in range(len(temp)):
        f = open(temp[x][1],'r',encoding='utf-8')
        oldpage = f.read()
        f.close()
        prevhtml = '' if x==0 else '<a href="{}" rel="prev">< {}</a>'.format(temp[x-1][1][1:],temp[x-1][0])
        nexthtml = '' if x==len(temp)-1 else '<a href="{}" rel="next">{} ></a>'.format(temp[x+1][1][1:],temp[x+1][0])
        newpage = oldpage.replace('@@begin-previous article-end@@',prevhtml)
        newpage = newpage.replace('@@begin-next article-end@@',nexthtml)
        f = open(temp[x][1],'w',encoding='utf-8')
        f.write(newpage)
        f.close()


# In[11]:


footer()


