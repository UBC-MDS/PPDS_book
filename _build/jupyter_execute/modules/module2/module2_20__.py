#!/usr/bin/env python
# coding: utf-8

# # Conditional value replacement and assignment
# 
# :::{admonition} Watch it
# See the accompanied youtube video at <a href="https://www.youtube.com/embed/WCWi1R2CQsY?start=1224&end=1590" target="_blank">the link here.</a>
# :::

# In[1]:


import pandas as pd
import numpy as np

pd.set_option('display.width', 350)
np.set_printoptions(linewidth=400)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 20)


# # Building on things we know

# In[2]:


cereal = pd.read_csv('cereal.csv',
                  usecols=['name', 'mfr', 'type', 'calories', 'protein', 'weight', 'rating'])
cereal.head()


# Notes:
# 
# So far, we have accumulated many different skills to wrangle our data.
# 
# One type of transformation that you may use often is replacing values
# within a column depending on a certain condition.
# 
# Let’s bring in a smaller version of our cereal dataset.
# 
# In the dataframe, the manufacturer value “Q” isn’t that informative and
# it might be easier to understand our data if we change all these values
# to something more clear like “Quaker”.
# 
# This leads us to our task:
# 
# ***Replace the `Q` manufacturer values with a new value of `Quaker`.***
# 
# ---

# In[3]:


q_cereal = cereal[cereal['mfr'] == 'Q']
q_cereal.assign(mfr = 'Quaker')


# Notes:
# 
# Our first instinct may be to first filter those rows using the technique
# we learned in our last section.
# 
# From our new filtered selection, perhaps we could assign values of
# “Quaker” to column `mfr` using similar code to this.
# 
# The output looks like it did what we wanted, but what happened to the
# rest of our dataframe?
# 
# Remember that we only want to replace the values in our existing
# dataframe and not create a new one.
# 
# When we use the `.assign()` verb like this, it creates a new dataframe
# with only the rows that meet the condition `cereal['mfr'] == 'Q'` .
# 
# This is problematic since we still want the original dataframe and the
# rows with `mfr` values not equal `Q`.
# 
# So what do we do?
# 
# ---
# 
# # Building on more things we know

# In[4]:


cereal.loc[73] 


# In[5]:


cereal.loc[cereal['mfr'] == 'Q']


# Notes:
# 
# Remember our friend `.loc[]`? We are going to get reacquainted with it.
# 
# Similarly, to how `.loc[]` can select and return specified columns and
# rows of the dataframe, it can filter on conditions too.
# 
# We are used to seeing code involving `.loc[]` like this.
# 
# But now we’ll get introduced to a new side of it when we use it to
# filter as well.
# 
# We can use the same syntax, `cereal['mfr'] == 'Q'`, we normally would
# when filtering. However, this time we wrap the whole thing within
# `.loc[]`.
# 
# ---

# In[6]:


cereal.loc[cereal['mfr'] == 'Q', 'mfr']


# In[7]:


cereal.loc[cereal['mfr'] == 'Q', 'mfr'] = 'Quaker'


# Notes:
# 
# Some people may be asking, “Why don’t we do all our filtering like this
# then?” Well, the answer is, you can, but we prefer not to.
# 
# Filtering without `.loc[]` is a bit more readable.
# 
# Let’s concentrate back on our task of only replacing `mfr` values equal
# to `Q` to `Quaker`.
# 
# How can `.loc[]` help us with this?
# 
# Unlike our earlier approach, `.loc[]` accepts more arguments within it.
# 
# We have the ability to specify not only the target rows matching a
# specific condition but our column of interest as well.
# 
# Once we have that, we can then assign these rows the new values `Quaker`
# in the `mfr` column.
# 
# Wait\! Nothing was outputted with our code\! What happened?
# 
# ---

# In[8]:


cereal


# Notes:
# 
# Let’s take a look at the original dataframe.
# 
# We can now see that the `Q` manufacturer values have changed to
# `Quaker`.
# 
# When we use this syntax, we do not need to save the results in a new
# object like we had to with `.assign()` and `.drop()`.
# 
# Let’s discuss what really is happening behind the scenes.
# 
# ---

# In[9]:


cereal['mfr'] == 'Q'


# Notes:
# 
# Remember what the condition `cereal['mfr'] == 'Q'` returns?
# 
# It produces an object containing all the rows with True/False values
# depending on whether or not the row meets the condition.
# 
# ---
# 
# <img src='/module2/tf_quaker.png'  alt="404 image" />
# 
# Notes:
# 
# Essentially our code is finding the rows with `True` values and
# replacing the values in the `mfr` colum with the new value of `Quaker`.
# 
# ---
# 
# 1.  
# <!-- end list -->

# In[10]:


cereal.loc[cereal['mfr'] == 'Q']


# <br>
# 
# 2.  
# <!-- end list -->

# In[11]:


cereal.loc[cereal['mfr'] == 'Q', 'mfr'] 


# <br>
# 
# 3.  
# <!-- end list -->

# In[12]:


cereal.loc[cereal['mfr'] == 'Q', 'mfr'] = 'Quaker'


# Notes:
# 
# You can split up how this code works into 3 steps:
# 
# 1.  We use `.loc[]` to find the rows meeting certain conditions.
# 
# 2.  We next indicate which column we wish to access.
# 
# 3.  Once we have obtained our desired rows and the column which we are
#     editing, we assign a value.
# 
# ---

# In[13]:


cereal[cereal['mfr'] == 'Q', 'mfr'] = 'Quaker'


# Notes:
# 
# Does this work without using `.loc[]`?
# 
# Let’s give it a try.
# 
# Unfortunately, we are not able to replace values in this manner and it
# results in an error since filtering this way does not allow us to
# specify a column.
# 
# ---
# 
# # Replacing with inequalities

# In[14]:


cereal.loc[cereal['protein'] >= 3, 'protein_level']  = 'high' 


# In[15]:


cereal.loc[cereal['protein'] < 3, 'protein_level']  = 'low' 


# Notes:
# 
# This syntax using `.loc[]` also works for inequality conditions.
# 
# If we are replacing numerical values with characters or words (or vice
# versa) we need to assign our desired values to a **new column** and not
# the existing one, because the column type will be different.
# 
# Perhaps we want just two categories for protein levels - “high” and
# “low”.
# 
# Any cereal above 3 grams of protein will be considered a “high” protein
# level and anything less, as a “low” protein level.
# 
# Let’s assign the “high” protein values first.
# 
# The only difference here from earlier is we now use an inequality for
# our condition and we designate a new column name instead of an existing
# one.
# 
# Let’s save the values in a column named `protein_level`.
# 
# Next by the “low” values.
# 
# ---

# In[16]:


cereal


# Notes:
# 
# Let’s take a look at the dataframe now.
# 
# ---
# 
# ## Creating new columns

# In[17]:


oz_to_g = 28.3495
cereal['weight_g'] = cereal['weight'] * oz_to_g
cereal


# Notes:
# 
# You may have noticed we did not use `.assign()` to create our new
# column.
# 
# That’s because as we mentioned earlier, when we use `.assign()` it
# creates a brand new dataframe.
# 
# When we are replacing values, we don’t want a new dataframe and instead,
# we just want to alter the current values in the existing dataframe.
# 
# When we are not doing conditional value replacement, we could create new
# columns with a similar syntax. Take the example of converting the weight
# from ounces into grams and making a new column named `weight_g`.
# 
# This code edits the existing dataframe `cereal` instead of creating a
# new one.
# 
# We prefer to use `.assign()` where possible as it can help avoid
# unexpected errors and performance issues.
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
