#!/usr/bin/env python
# coding: utf-8

# # Summary Statistics
# 
# :::{admonition} Watch it
# See the accompanied youtube video at <a href="https://www.youtube.com/embed/W88f5DAl9hk?start=1518&end=1770" target="_blank">the link here.</a>
# :::
# 
# Now we’ve learned about how to get the data in to the shape and size
# that we desire, now we ca have some fun with it\!
# 
# We usually like to learn from it. One place we can start is summary
# statistics, so we can calculate interesting values for each of the
# variables or columns in our dataframe.
# 
# Let’s start by doing this for the cereal dataset again.

# In[1]:


import pandas as pd
import numpy as np

pd.set_option('display.width', 400)
np.set_printoptions(linewidth=400)
pd.set_option('display.max_columns', 15)


# In[2]:


cereal = pd.read_csv('cereal.csv')
cereal.head(15)


# ## Numerical and Categorical Columns
# 
# Before we go further, let’s quickly discuss the 2 different types of
# data.
# 
# ### Categorical data
# 
# Categorical data consists of qualitative observations such as
# characteristics - things generally containing names or words.
# 
# **Examples**
# 
#   - Colours
#   - Names
# 
# 
# ### Numerical data
# 
# These data are usually expressed with numbers.
# 
# **Examples**
# 
#   - Measurements
#   - Quantities
# 
# 
# 
# Our columns in our dataframe are considered one of the two of these.
# 
# ## Pandas `.describe()`
# 
# Pandas has a lot up its sleeve but one of the most useful methods is
# called `.describe()` and it does exactly that. it *describes* our data.
# 
# Let’s try it out on our cereal dataset.
# 
# By default `df.describe()` only shows numerical columns.

# In[3]:


cereal.describe()


# Let’s talk a little bit about the output of `.describe()`.
# 
# On the left-hand side we see a new column. This column contains the
# names of the different summary statistics that `.describes()` gives us
# back for our dataset. Let’s talk about them each individually:
# 
# - `count`: The number of non-NA/null observations.
# - `mean`: The mean of column
# - `std` : The standard deviation of a column
# - `min`: The min value for a column
# - `max`: The max value for a column
# - By default the 25, 50 and 75 percentile of the observations
# 
# 
# 
# We can make changes to either limit how much is shown or include more
# using describe. One useful argument is `include` and a value we can give
# to that is `all`.

# In[4]:


cereal.describe(include='all')


# This expands the output so we get summary statistics for both
# categorical and numerical columns now.
# 
# Adding `include='all'` within the brackets adds some additional
# statistics about categorical columns including:
# 
# - `unique`: which indicates the number of unique observations
# - `top`: which tells up the observation value that is most occurring
# - `freq`: which informs us of the frequency of the most occurring
#   observation
# 
# 
# We can also get single statistics of each column using functions like:
# `.mean()`,`.std()`, `.count()`, `.median()`, `.sum()`.
# 
# To do this, we first have to grab the column that we are interested in
# exploring, and then we add the verb.
# 
# Here are some examples of things that we can calculate. First we
# calculate the mean of the ratings, then we calculate sum of the ratings,
# and finally the median of the ratings.

# In[5]:


ratings = cereal[['rating']]
ratings.mean()


# In[6]:


ratings.sum()


# In[7]:


ratings.median()


# We can also use these summary statistic verbs on the entire dataframe.
# This now shows the mean value of each column in the dataframe.
# 
# You’ll notice that only the numerical variables are calculated which
# makes sense since we would not be able to calculate the mean of
# categorical data.

# In[8]:


cereal.mean()


# ```out
# calories    106.883117
# protein       2.545455
# fat           1.012987
# sodium      159.675325
# fiber         2.151948
# carbo        14.623377
# sugars        6.948052
# potass       96.129870
# vitamins     28.246753
# shelf         2.207792
# weight        1.029610
# cups          0.821039
# rating       42.665705
# dtype: float64
# ```
# 
# :::{admonition} Let’s apply what we learned!
# 
# Bringing back our Fruit Salad dataframe:
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
# 1\. Which of the following columns contain numerical data?                             
# a) `colour`, `shape`, `water-content`          
# b) `water-content`, `weight`           
# c) `colour`, `seed`, `water-content`, `weight`           
# d) All of the columns are categorical            
# 
# 2\. We need summary statistics of both numerical and categorical columns of the dataframe `fruit_salad`. What code would be suitable for this?        
# a) `df.describe()`        
# b) `fruit_salad.describe()`        
# c) `fruit_salad.describe(include="all")`        
# d) `fruit_salad.summary(include="all")`    
# 
# :::
# 
# ```{admonition} Solutions!
# :class: tip, dropdown
# 
# 1. b) `water-content`, `weight`   
# 2. c) `fruit_salad.describe(include="all")` 
# 
# ```
