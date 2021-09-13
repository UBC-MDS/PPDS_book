#!/usr/bin/env python
# coding: utf-8

# # Frequency Tables and Writing CSVs
# 
# :::{admonition} Watch it
# See the accompanied youtube video at <a href="https://www.youtube.com/embed/W88f5DAl9hk?rel=0?start=1775&end=1940" target="_blank">the link here.</a>
# :::
# 
# ## What is Frequency?
# 
# Before we explain what a frequency table is, you must know what
# frequency means first.
# 
# *_Frequency_* is simply put, the number of times a value occurs within
# the data. Let’s look at an example using our candybars dataset.

# In[1]:


import pandas as pd
import numpy as np

pd.set_option('display.width', 400)
np.set_printoptions(linewidth=400)
pd.set_option('display.max_columns', 15)

cereal = pd.read_csv('cereal.csv')
cereal2 = pd.read_csv('candybars.csv')
candybars_mini = cereal2.head(7).loc[:, ['name', 'weight', 'available_canada_america' ]]


# In[2]:


candybars_mini


# If we count the number of times the value `Both` appears in the
# `available_canada_america` column, we get 3 times. This is the frequency
# of the value `both`.
# 
# ## What is a Frequency Table?
# 
# A frequency table is a manner of displaying all the possible values of a
# column in our dataframe and the number of occurrences (frequencies) of
# each value.
# 
# For our sample data, a frequency table for the
# `available_canada_america` column would look like this:

# In[3]:


candybars_mini['available_canada_america'].value_counts()


# If we want to get a frequency table of a categorical column, there are a
# few steps that need to be followed.
# 
# Up until now, we discussed getting a single column from a dataframe
# using double square brackets - `df[['column name']]`.
# 
# For frequency tables, however, we only use single brackets to obtain the
# column values.

# In[4]:


mfr_column = cereal['mfr']
mfr_column


# We saved the object in this example here to an object named `mfr_column`
# in the same way that we have done this before.
# 
# Now we can use `.value_counts()` on this `mfr_column` variable to
# reference it, and we can obtain the frequency value for the different
# categories in that variable.

# In[5]:


mfr_freq = mfr_column.value_counts()
mfr_freq


# If we did instead use double square brackets with `pd.value_counts()`,
# we would get an error. So it is important to take care and remember when
# you are using `value_counts()`, you only use one set of square brackets.

# In[6]:


mfr_col_wrong = cereal[['mfr']]
mfr_col_wrong


# In[7]:


mfr_col_wrong.value_counts()


# ## Saving a dataframe
# 
# Sometimes it is useful to save a new dataframe to a file like a csv file
# for future use by you or somebody else.
# 
# We can do this using a method called `.to_csv()`.

# In[8]:


mfr_freq.to_csv('mfr_frequency.csv', index=False)


# We put our desired `csv` file name in quotations within the parentheses
# and follow it with the argument `index=False` so we don’t export our
# index column which is just a column of numbers.
