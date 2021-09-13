#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.set_option('display.max_rows', 100)


# In[3]:


df = pd.read_csv('cereal.csv', index_col=0)


# In[4]:


df = df.loc[:,['mfr','sugars']]


# In[5]:


df.groupby('mfr').get_group('K')


# In[6]:


candy = pd.read_csv('../../../../data/candybars.csv', index_col=0)
candy


# In[7]:


candy2 = pd.read_csv('../../../../data/candybars2.csv', index_col=0)
candy2_sorted= candy2.sort_values('calories')
candy2_sorted


# In[8]:


pd.concat([candy, candy2_sorted], axis=0).head(20)


# In[9]:


df = pd.read_csv('cereal.csv')


# In[10]:


# Read in the dataset 
hockey_players = pd.read_csv('../../../../data/canucks.csv')


# Display the dataframe
hockey_players.head()


# In[11]:


list(hockey_players.columns)


# In[12]:


columns_hockey = hockey_players.columns 


# In[13]:


list(columns_hockey)


# In[14]:


hockey_shape = hockey_players.shape


# In[15]:


hockey_shape


# In[16]:


hockey_players


# In[17]:


df[['calories','fiber']]


# In[18]:


penalty_players = hockey_players.loc[[10, 21, 2], ['Height', 'Weight', 'Salary', 'Country']]


# In[19]:


penalty_players.shape


# In[20]:


penalty_players.columns


# In[21]:


penalty_players.index


# In[22]:


star_players = hockey_players.loc[7:19, 'Player':'Country']

# Display it

star_players


# In[23]:


star_players.shape


# In[24]:


star_players.index


# In[25]:


benched_players = hockey_players.loc[3:9]

# Display it

benched_players


# In[26]:


benched_players.shape


# In[27]:


rich_players = hockey_players.sort_values(by='Salary', ascending=False)

# Display it

rich_players


# In[28]:


rich_players.index


# In[ ]:




