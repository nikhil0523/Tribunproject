#!/usr/bin/env python
# coding: utf-8

# In[32]:


pip install requests


# In[33]:


pip install bs4


# In[1]:


import requests
from bs4 import BeautifulSoup


# In[34]:


pip install googletrans


# In[16]:


from googletrans import Translator


# In[2]:


url = 'https://www.tribunnews.com/new-economy/2024/08/07/lewat-teknologi-dan-edukasi-gopay-mendukung-pemberantasan-judi-online-di-indonesia'


# In[3]:


response = requests.get(url)
response.raise_for_status()


# In[4]:


soup = BeautifulSoup(response.content, 'html.parser')


# In[5]:


soup


# In[6]:


title_tag = soup.find('h1', {'id': 'arttitle'})
title = title_tag.get_text(strip = True) if title_tag else 'Not Found'


# In[7]:


print(title)


# In[9]:


date_tag = soup.find('div', class_ = 'grey bdr3 pb10 pt10')
date = date_tag.find('time').get_text(strip = True) if date_tag else 'Not Found'


# In[10]:


print(date)


# In[12]:


author_tag = soup.find('div', {'id':'penulis'})
author = author_tag.find('a').get_text(strip = True) if author_tag else 'Not Found'


# In[13]:


print(author)


# In[14]:


body = ''
paras = soup.find_all('p')
for para in paras:
    body += para.get_text(strip = True) + '\n'


# In[15]:


print(body)


# # Translating the original language to English

# In[17]:


translator = Translator()


# In[20]:


Title = translator.translate(title, dest = 'en').text
Date = translator.translate(date, dest = 'en').text
Author = translator.translate(author, dest = 'en').text
Body = translator.translate(body, dest = 'en').text


# In[19]:


print(Title)


# In[21]:


print(f"Title: {Title}")
print(f"Date: {Date}")
print(f"Author: {Author}")
print(f"Content: {Body}")


# # To have a more accurate body content

# In[28]:


body1 = ''
paras = soup.find_all('p')
start_extracting = False
for para in paras:
    text = para.get_text(strip = True)
    if "TRIBUNNEWS.COM" in text:
        start_extracting = True
    if start_extracting:
        body1 += text + '\n'


# In[29]:


print(body1)


# In[30]:


Body1 = translator.translate(body1, dest = 'en').text


# In[31]:


print(f"Title: {Title}")
print(f"Date: {Date}")
print(f"Author: {Author}")
print(f"Content: {Body1}")


# In[ ]:




