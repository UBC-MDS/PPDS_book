#!/usr/bin/env python
# coding: utf-8

# # Column renaming and column dropping
# 
# :::{admonition} Watch it
# See the accompanied youtube video at <a href="https://www.youtube.com/embed/WCWi1R2CQsY?start=573&end=589" target="_blank">the link here.</a>
# :::

# In[1]:


import pandas as pd
import numpy as np

pd.set_option('display.width', 350)
np.set_printoptions(linewidth=400)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 15)


# Remember our `candybars.csv` dataframe?
# 
# Let’s bring it back and save it as object named `candy`.

# In[2]:


candy = pd.read_csv('candybars.csv')
candy


# ## Column Renaming
# 
# There will be times where you are unsatisfied with the column names and
# you may want to change them.
# 
# The proper syntax to do that is with `.rename()`.
# 
# The column name `available_canada_america` is a bit long.
# 
# Perhaps it would be a good idea to change it to something shorter like
# `availability`.
# 
# Here is how we can accomplish that.

# In[3]:


candy = candy.rename(columns={'available_canada_america':'availability'})
candy


# This code uses something we’ve never seen before - `{}` curly braces,
# also called curly brackets.
# 
# These have a special meaning but for now, you only need to concentrate
# your attention on the fact that the argument `columns` needs to have the
# format shown on the slide.
# 
# ``` python
#  columns={'old column name':'new column name'}
# ```
# 
# You can also rename multiple columns at once by adding a comma between
# the new and old column pairs within the curly brackets.
# 
# It’s important that we always save the dataframe to an object when
# making column changes or the changes will not be saved in our dataframe.

# In[4]:


candy = candy.rename(columns={'available_canada_america':'availability',
                        'weight':'weight_g'})
candy.head()


# ## Column Dropping
# 
# `.drop()` is the verb we use to delete columns in a dataframe.
# 
# Let’s delete the column `coconut` by specifying it in the `columns`
# argument of the `drop` verb.

# In[5]:


candy.drop(columns='coconut')


# In[6]:


candy.drop(columns='coconut')


# If you look again at the code we just wrote you’ll notice we didn’t save
# over the dataframe object, so the dataframe `candy` still will contain
# the `coconut` column.

# In[7]:


candy.head()


# Let’s overwrite the dataframe and remove multiple columns at the same
# time.
# 
# Let’s drop `nougat` and `coconut` together.

# In[8]:


candy = candy.drop(columns=['nougat', 'coconut'])
candy.head()


# We put the columns we want to drop in square brackets and this time we
# will remember to overwrite over the `candy` object.
# 
# Now when we call `candy.head()` it reflects the dropped columns. They’re
# no longer there.
# 
# 
# 
# :::{admonition} Let’s apply what we learned!
# 
# Here is our `fruit_salad` dataframe once again. 
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
# Let's say we run the following code:
# 
# ```python
# fruit_salad.drop(columns = ['colour', 'shape', 'sweetness'])
# fruit_salad = fruit_salad.rename(columns={'location':'country',
#                                           'weight':'weight_g'})
# ```
# 
# Use the dataframe and code above to answer the next 2 questions.
# 
# 
# 1\. After running the code above, How many columns (not including the index) are there in `fruit_salad` ?           
# a) 9      
# b) 4        
# c) 8           
# 
# 2\. After running the code above, which of the following is a column in the dataframe `fruit_salad`?        
# a) `country`     
# b) `location`        
# 
# :::
# 
# ```{admonition} Solutions!
# :class: tip, dropdown
# 
# 1. c) 8   
# 2. a) `country` 
# ```
