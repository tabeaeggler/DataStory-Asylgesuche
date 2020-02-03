#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests
import os


# In[33]:


if not os.path.exists('Data'):
    os.makedirs('Data')
    
for i in range(1994, 2019):
    i = str(i)
    url = "https://www.sem.admin.ch/dam/data/sem/publiservice/statistik/asylstatistik/{}/12/7-20-Bew-Asylgesuche-J-d-{}-12.xlsx".format(i,i)
    r = requests.get(url) 
    with open ('./Data/' + 'data_' + str(i) + '.xlsx','wb') as f: 
        f.write(r.content)


# In[ ]:




