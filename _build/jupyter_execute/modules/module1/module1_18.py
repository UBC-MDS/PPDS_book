#!/usr/bin/env python
# coding: utf-8

# # Selecting a Single Column
# 
# :::{admonition} Watch it
# See the accompanied youtube video at <a href="https://www.youtube.com/embed/W88f5DAl9hk?start=913&end=1005" target="_blank">the link here.</a>
# :::
# 
# Something we often do in data analysis is obtain a single column from
# a dataframe. We can again use `.loc[]` to do this which would look
# something like this in general:
# 
# `dataframe.loc[:, ['column name']]`

# In[1]:


import pandas as pd
import numpy as np

pd.set_option('display.width', 400)
np.set_printoptions(linewidth=400)
pd.set_option('display.max_columns', 15)

cereal = pd.read_csv('cereal.csv')


# So if we here want the column named `type` from our cereal dataframe we
# could use the syntax:

# In[2]:


cereal.loc[:, ['type']]


# This seems a bit long winded and since we do this type of thing often.
# Luckily, Pandas has provided a quicker syntax to use to do the same
# thing.
# 
# 
# <br>
# 
# 
# 
# Instead, selecting a single column can be done without using `.loc[]`
# and we can just specify the dataframe name, followed by double square
# brackets containing the column of interest (`df[['column name']]`).

# In[3]:


cereal[['type']]


# This makes the syntax for selecting the column `type` from the `cereal`
# dataframe very easy.
