#!/usr/bin/env python
# coding: utf-8

# # Slicing Rows using .loc\[\]
# 
# :::{admonition} Watch it
# See the accompanied youtube video at <a href="https://www.youtube.com/embed/W88f5DAl9hk?start=378&end=647" target="_blank">the link here.</a>
# :::
# 
# Congratulations on writing your first code\!
# 
# We have read in our data, and we know the dimensions. Well, now what?
# 
# Let’s go over how we would **index**, **slice**, and **select** certain
# columns or rows of our data.
# 
# Let’s start by importing pandas and loading in a dataset named
# `cereal.csv,` and we will save it as `cereal.`

# In[1]:


import pandas as pd
  
cereal = pd.read_csv('cereal.csv')
cereal.head()


# Attribution:  
# *“[80 Cereals](https://www.kaggle.com/crawford/80-cereals/)” (c) by
# [Chris Crawford](https://www.linkedin.com/in/crawforc3/) is licensed
# under [Creative Commons Attribution-ShareAlike 3.0
# Unported](http://creativecommons.org/licenses/by-sa/3.0/).*
# 
# We can see all the columns and the first 5 rows of the dataframe using
# `.head()`
# 
# However, let’s say we only want certain rows of the dataframe or
# certain columns.
# 
# We talked about how `.head()` will generate the first few rows of a
# dataframe (5 as default), but what if we wanted the rows from 5-10?
# 
# The first column of this dataframe is called the `index.`
# 
# Each row has a label (the index) as well as a position. In this case,
# the index label of an observation is the same as it’s position.
# 
# This doesn’t always have to be the case. We can assign another column as
# the index; however, we will wait to discuss this in the next module.
# 
# Here are the first 15 rows of the dataframe.

# In[2]:


cereal.head(15)


# Let’s talk about observation 4 which is named `Almond Delight`. Its
# index label is `4` as well as it’s index position.
# 
# If you just went and counted those again and started screaming “5\! It’s
# the fifth position”, that’s OK. In the Python language, we start
# counting at position 0 (then 1, 2, 3, and 4 for Almond Delight).
# 
# Now let’s say we want all 5 rows past `Almond Delight`. That means we
# want the rows from `Apple Cinnamon Cheerios` to `Cap'n'Crunch`.
# 
# We will use `.loc[]` with square brackets to cut the dataframe from
# “Apple Cinnamon Cheerios” to “Cap’n’Crunch,” keeping the columns and
# everything between.
# 
# This code is written as `cereal.loc[5:10]`, and it can be interpreted as
# *“Obtain the rows in the dataframe located from `5` to `10`.”*

# In[3]:


cereal.loc[5:10]


# What if we only wanted certain columns now?
# 
# Perhaps we were only interested in the `calories` to `fiber` columns of
# the “Apple Cinnamon Cheerios” to “Cap’n’Crunch” rows?
# 
# We put in the interval of our desired rows first, and then the columns,
# and we separate these values with a comma.
# 
# `.loc[]` is used to slice columns and rows by **label**, and within an
# interval.

# In[4]:


cereal.loc[5:10, 'calories':'fiber']


# The general format to slice both rows and columns together looks like
# this:
# 
# ``` python
# cereal.loc['row name start':'row name end', 'column name start':'column name end']
# ```
# 
# There is a handy shortcut for slices that include the beginning of a
# dataframe to a specified row or column label or a specified row or
# column label to the end of a dataframe.
# 
# For example if we want all the rows up to “Apple Jacks” which has a
# label equal to 6, we could omit the first label in the code all
# together. So we can write `cereal.loc[:6]`.

# In[5]:


cereal.loc[:6]


# Or we can do something similar for the end of a dataframe. Let’s say now
# we want all the rows up to `Apple Jacks` and only the columns from
# `sugars` onward to the end of the dataframe. What we would write in this
# case is `cereal.loc[:6, 'sugars':]`.
# 
# We would omit the ending label this time after the `:` (colon) .

# In[6]:


cereal.loc[:6, 'sugars':]


# :::{admonition} Let’s apply what we learned!
# 
# My dataframe object name is `fruit_salad`.
# 
# ```out
#            name    colour    location    seed   shape  sweetness   water-content  weight
# 0         apple       red     canada    True   round     True          84         100
# 1        banana    yellow     mexico   False    long     True          75         120
# 2    cantaloupe    orange      spain    True   round     True          90        1360
# 3  dragon-fruit   magenta      china    True   round    False          96         600
# 4    elderberry    purple    austria   False   round     True          80           5
# 5           fig    purple     turkey   False    oval    False          78          40
# 6         guava     green     mexico    True    oval     True          83         450
# 7   huckleberry      blue     canada    True   round     True          73           5
# 8          kiwi     brown      china    True   round     True          80          76
# 9         lemon    yellow     mexico   False    oval    False          83          65
# ```
# 
# 1\. If you wanted only the rows from `cantaloupe` to `kiwi`, what would your code look like using index labels?       
# a) `fruit_salad.loc[2, 8]`         
# b) `fruit_salad[2, 8]`            
# c) `fruit_salad[2:8]`               
# d) `fruit_salad.loc[2:8]`                  
#  
# 
# 2\. If you wanted all the rows between `cantaloupe` and `fig` and only columns `name` to `seed`, what would your code look like using index labels?      
# a) `fruit_salad.loc[2:5, "colour":"seed"]`           
# b) `fruit_salad.loc[2:5, "name":"seed"]`                            
# c) `fruit_salad.loc["name":"seed", 2:5]`                   
# d) `fruit_salad[2:8, "name":"seed"]`                    
# 
# :::
# 
# ```{admonition} Solutions!
# :class: tip, dropdown
# 
# 1. d) `fruit_salad.loc[2:8]`          
# 2. b) `fruit_salad.loc[2:5, "name":"seed"]`           
# 
# ```
