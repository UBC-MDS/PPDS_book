#!/usr/bin/env python
# coding: utf-8

# # Sorting dataframes
# 
# :::{admonition} Watch it
# See the accompanied youtube video at <a href="https://www.youtube.com/embed/W88f5DAl9hk?start=1461&end=1513" target="_blank">the link here.</a>
# :::
# 
# When we read in our data, it is generally ordered in the same way it is
# stored.
# 
# We can easily sort the rows of a dataframe based on the values within a
# column.
# 
# The verb that we use for that is `.sort_values()`.

# In[1]:


import pandas as pd
import numpy as np

pd.set_option('display.width', 400)
np.set_printoptions(linewidth=400)
pd.set_option('display.max_columns', 15)

cereal = pd.read_csv('cereal.csv')


# In[2]:


cereal.sort_values(by='rating')


# For example, if we wanted to order the cereals based on rating, we could
# do so by using the argument `by` within the `.sort_values()` verb.
# 
# This allows us to see the cereals with lower ratings on the top.
# 
# What if we wanted the cereals with higher ratings at the top?
# 
# Then we would order them in `descending` order by setting the argument
# `ascending=False`.

# In[3]:


sorted_ratings = cereal.sort_values(by='rating', ascending=False)
sorted_ratings


# Perfect, now we have the highest rated cereals at the top of the
# dataframe.
