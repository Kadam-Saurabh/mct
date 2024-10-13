#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


url = "https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time-in-python"


# In[3]:


response = requests.get(url)
html_content = response.text


# In[4]:


soup = BeautifulSoup(html_content, 'html.parser')


# In[5]:


question = soup.find('h1').get_text(strip=True)
print(f"Question: {question}\n")


# In[6]:


answers = soup.find_all('div', class_='answer')


# In[7]:


for i, answer in enumerate(answers, start=1):
    # Get the answer text
    answer_text = answer.find('div', class_='s-prose js-post-body').get_text(strip=True)
    print(f"Answer {i}:\n{answer_text}\n")


# In[ ]:




