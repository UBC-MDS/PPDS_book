#!/usr/bin/env python
# coding: utf-8

# # Reading arguments
# 
# :::{admonition} Watch it
# See the accompanied youtube video at <a href="https://www.youtube.com/embed/WCWi1R2CQsY?start=272&end=471" target="_blank">the link here.</a>
# :::

# In[1]:


import pandas as pd
import numpy as np

pd.set_option('display.width', 350)
np.set_printoptions(linewidth=400)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 15)


# ## Arguments
# 
# When we load in our data we use different arguments to make sure it’s
# organized how we want it.
# 
# `delimiter` is an argument we have already discussed that instructs on
# how to separate each value in the data.
# 
# This is only the tip of the iceberg.
# 
# There are many others that are helpful when reading in our data, such as
# `index_col`, `header`, `nrows`, and `usecols`.
# 
# Here, we are going to introduce different arguments for `pd.read_csv()`
# and `pd.read_excel()`:
# 
#   - `index_col`
#   - `header`
#   - `nrows`
#   - `usecols`
# 
# If you wish to know more, you can find the documentation at the
# following links:
# 
#   - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html" target="_blank">`pd.read_csv()`</a>
#   - <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html" target="_blank">`pd.read_excel()`</a>
# 
# ## index\_col
# 
# `index_col` is an argument that indicates which column will be
# acting as the index label.
# 
# In most of the cases we have encountered, we did not use this argument
# and instead relied on the pandas default, which is to use ascending
# integers for the index.
# 
# We can, however, specify a column in the data to become the index.
# 
# It’s in our best interest that the column we choose have unique values.
# 
# For our `cereal.csv` let’s specify the `name` column as our index.

# In[2]:


df = pd.read_csv('cereal.csv', index_col="name")
df.head()


# The `index_col` argument also take in positions.
# 
# The `name` column in our data is in the 0th position so we can also
# specify the index like we show here with `index_col=0`.

# In[3]:


df = pd.read_csv('cereal.csv', index_col=0)
df.head()


# ## header
# 
# We have been lucky up until now that all the data we have loaded in has
# been particularly straightforward.
# 
# Sometimes with data, there are a few lines of text explaining important
# points about the file.
# 
# 
# We do not want to include this in our dataframe and therefore we need to
# specify exactly when our dataframe begins.
# 
# This is where `header` comes in.
# 
# Take a look at
# <a href="https://github.com/UBC-MDS/MCL-DSCI-511-programming-in-python/blob/master/slides/candybars-h.csv" target="_blank">`candybars-h.csv`
# </a> below as an example.
# 
# <img src='../imgs/module2/header_textedit.png'  alt="404 image"/> 
# 
# If we look at the data with a regular text editor, the data doesn’t
# start until the 3rd line which would be the equivalent of position 2
# (since we begin counting from 0).
# 
# If we load this dataset without any arguments, we get this as the
# output.

# In[4]:


candybars = pd.read_csv('candybars-h.csv')
candybars


# We see that there are no clear column names and things are quite a
# mess\!
# 
# If we use `header=2` to indicate that the data actually begins at
# position 2, then things start to look much better.

# In[5]:


candybars = pd.read_csv('candybars-h.csv', header=2)
candybars


#  
# 
# ## nrows
# 
# `nrows` is an argument in `pd.read_csv()` that is useful when you only
# want to load in part of the dataframe.
# 
# Perhaps the file you have is large and you only want a sample of it.
# 
# `nrows` will limit the number of rows that you read in.

# In[6]:


candybars = pd.read_csv('candybars.csv', nrows=7)
candybars


# This code loads in only the first 7 rows of our candybar dataset.
# 
# 
# ## usecols
# 
# Similarly to how `nrows` specifies how many rows to read in, `usecols`
# selects which columns to load from the data.
# 
# Perhaps the only columns relevant to our analysis are the columns
# `name`, `weight` and `available_canada_america`.
# 
# We can forgo the other columns when reading the data in.
# 
# In a similar way to selecting columns using `.iloc[]`, we specify the
# desired column indices in square brackets.

# In[7]:


candybars = pd.read_csv('candybars.csv', usecols=[0, 1, 10])
candybars


# The `usecols` argument accepts either index positions or labels so we
# could also use the column names in square brackets as shown here.

# In[8]:


candybars = pd.read_csv('candybars.csv', usecols=['name', 'weight', 'available_canada_america'])
candybars


# :::{admonition} Let’s apply what we learned!
# 
#  
# 1\.Which argument will assign the index when reading in your data with `pd.read_excel()`?                                
# a) `header`       
# b) `ncols`          
# c) `index_col`             
#  
# 2\. Which argument will select only specific columns of the data file with `pd.read_csv()`?      
# a) `header`      
# b) `nrows`          
# c) `usecols`       
# 
# :::
# 
# ```{admonition} Solutions!
# :class: tip, dropdown
# 
# 1. c) `index_col`       
# 2. c) `usecols`            
# ```
