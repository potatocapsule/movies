#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[16]:


#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)


# In[7]:


movies = pd.read_csv('Downloads/archive/IMDb movies.csv')
movies.head()


# In[29]:


movies.drop(columns = ['original_title', 'writer', 'production_company','actors','description'])


# In[25]:


ratings = pd.read_csv('Downloads/archive/IMDb ratings.csv')
ratings.head()


# In[31]:


plt.hist(movies.avg_vote)


# In[38]:


movies[['title', 'avg_vote']]


# In[48]:


movies.iloc[2:4, 1:5]


# In[52]:


for i,r in movies.iterrows():
    print (i,r['title'])


# In[74]:


movies.loc[movies['avg_vote'] >8]


# In[ ]:




