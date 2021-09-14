#!/usr/bin/env python
# coding: utf-8

# # Slicing and selecting using .iloc\[\]
# 
# :::{admonition} Watch it
# See the accompanied youtube video at <a href="https://www.youtube.com/embed/W88f5DAl9hk?start=1011&end=1456" target="_blank">the link here.</a>
# :::
# 
# Up until point, we have been manipulating our dataframe with column and
# row ***labels*** using `.loc[]`.
# 
# Slicing can also be done by the location position of each row with
# `.iloc[]`.
# 
# `.iloc[]` is very similar to `.loc[]`, however, the “i” in `iloc` refers
# to the index ***integer*** position.
# 
# 
# ## Slicing Dataframe
# 
# We are going to return to our cereal dataset and take a look at the
# first 10 rows.

# In[1]:


import pandas as pd
import numpy as np

pd.set_option('display.width', 400)
np.set_printoptions(linewidth=400)
pd.set_option('display.max_columns', 15)


# In[2]:


cereal = pd.read_csv('cereal.csv')
cereal.head(10)


# Let’s say we want the rows from `All-Bran` to `Apple Cinnamon Cheerios`,
# but we want to slice based on their position instead of their label.
# 
# Using Python’s counting method of starting at zero, we conclude that
# `All-Bran` to be at position to 2.
# 
# We get `Apple Cinnamon Cheerios` position to be 5 in the same way.
# 
# We are lucky with this dataframe because our index labels match the
# position of the rows, and this makes things a little bit simpler.
# 
# 
# We can use the same coding structure we learned with `.loc[]` but this
# time using row positions instead of labels with `.iloc[]`.

# In[3]:


cereal.loc[2:5]


# In[4]:


cereal.iloc[2:5]


# But wait\! Something is missing here\!
# 
# Why doesn’t `Apple Cinnamon Cheerios` appear in the dataframe?
# 
# The reason for this is that when we use slicing with indices, it will
# take all the indices including the lower bound but *EXCLUDING* the upper
# bound.
# 
# If we want to include `Apple Cinnamon Cheerios` we would have to go 1
# index position further.

# In[5]:


cereal.iloc[2:6]


# If we think about this a bit it actually make some sense. Think about
# the calculation `6 - 2 = 4` . We get 4 items remaining which is the
# amount of cereals we want in our in new dataframe.
# 
# 
# The same concept can be applied to the columns of the dataframe.
# 
# Let’s say we want all the rows but we only want the columns starting at
# `name` and ending (and including) at column `fat`.  
# Using the logic we learned in the last section, we would use the
# following code.
# 
# We would need to specify all rows using `:` as we did when we used
# `.loc[]`.
# 
# The column `name` is at index position 0 (we do not include the index
# label as a column) and `fat` is at index position 5.
# 
# Since we want to include the 5th column we need to use the 6th position
# to make sure we get all the columns *BEFORE* the upper bound.

# In[6]:


cereal.iloc[:, 0:6]


# Let’s say we want the rows `All-Bran` to `Apple Cinnamon Cheerios` and
# `name` to `fat`.
# 
# For rows, the lower bound `All-Bran` is located at position 2 and the
# upper bound `Apple Cinnamon Cheerios` is located at position 5.
# 
# Now the column’s lower bound `name` is located at position 0 and the
# upper bound `fat` is located at position 5.
# 
# The same would apply if we only wanted certain rows with certain
# columns.
# 
# Both of our upper bound have been compensated with an added 1 to make
# sure they are included in the new dataframe.
# 
# So the code we have to use to do this is the following:

# In[7]:


cereal.iloc[2:6, 0:6]


# There are multiple different way of writing code when you are selecting
# items from the beginning or end of your data.
# 
# Perhaps you only want the first 3 rows of your data.
# 
# We can use `.head(3)` or we can use `.iloc[]`.

# In[8]:


cereal.head(3)


# In[9]:


cereal.iloc[0:3]


# Since we are indicating the beginning of the dataframe, we can omit the
# upper bound `0` just like we did when we learned slicing with `.loc[]`.

# In[10]:


cereal.iloc[:3]


# The same logic can be applied for end of a dataframe. This time we want
# the last 3 rows.
# 
# Since this dataframe has 76 rows we could use our lower bound as 74 and
# upper bound as 77 (76 +1).

# In[11]:


cereal.iloc[74:77]


# A better and easier way to write this, where you don’t even need to know
# the number of rows in the dataframe would be to specify you are counting
# your rows from the bottom with a negative in front of the number of rows
# you want.
# 
# This example takes the last 3 rows of the **bottom** of the dataframe.
# 
# Since we are collecting data to the end of the dataframe, we do not need
# to include the ending row index number.

# In[12]:


cereal.iloc[-3:]


# ## Selecting with .iloc\[\]
# 
# Selecting using `.iloc[]` is done identically to `.loc[]`, however, the
# items within each set of square brackets **MUST** be integers, and not
# in quotation marks.

# In[13]:


cereal.head(10)


# Let’s say we want the rows `Almond Delight`, `Basic 4` and `Apple Jacks`
# with the columns `name`, `calories`, `fat` and `type` and *in that
# specific order*.
# 
# 
# 
# <table id="**Rows**" style="width:50%; float:left">
# 
# <tr>
# 
# <td>
# 
# | **Row**          | **Row Position** |
# | ---------------- | ---------------- |
# | `Almond Delight` | Position 4       |
# | `Basic 4`        | Position 7       |
# | `Apple Jacks`    | Position 6       |
# 
# </td>
# 
# </tr>
# 
# </table>
# 
# <table id="**Columns**" style="width:50%; float:left">
# 
# <tr>
# 
# <td>
# 
# | **Columns** | **Column Position** |
# | ----------- | ------------------- |
# | `name`      | Position 0          |
# | `calories`  | Position 3          |
# | `fat`       | Position 5          |
# | `type`      | Position 2          |
# 
# </td>
# 
# </tr>
# 
# </table>
# 
# `Almond Delight` takes row position 4, `Basic 4` takes row position 7
# and `Apple Jacks` is located at position 6. The desired columns `name`,
# `calories`, `fat`, and `type` take column index positions 0, 5, 3, and 2
# respectively.
# 
# Now let’s put those positions into square backing within `df.iloc[]`.

# In[14]:


cereal.iloc[[4, 7, 6], [0, 3, 5, 2]]


# :::{admonition} Let’s apply what we learned!
# 
# Here is our `fruit_salad` data again:
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
# 
# 1\. If I wanted the rows `elderberry`  to `kiwi` and only columns `seeds`, `shape`, `sweetness` and  `water-content`, what would my code look like if I was using index positions?            
# a) `fruit_salad.iloc[4:9, 3:]`         
# b) `fruit_salad.iloc[4:8, 3:7]`           
# c) `fruit_salad.iloc[4:9, 3:7]`           
# d) `fruit_salad.iloc[5:10, 4:8]`           
# 
# 2\. If I wanted the rows `lemon` and `cantaloupe`  but only the columns `colour`, `weight` and `seeds` in that order, what would my code look like if I was using index position?      
# a) `fruit_salad.iloc[[lemon, cantaloupe], [colour, weight, seeds]]`           
# b) `fruit_salad.iloc[[10, 3], [2, 8, 4]]`           
# c) `fruit_salad.iloc[[9, 2], [1, 7, 3]]`           
# d) `fruit_salad[[9, 2], [1, 7, 3]]`   
# 
# :::
# 
# ```{admonition} Solutions!
# :class: tip, dropdown
# 
# 1. c) `fruit_salad.iloc[4:9, 3:7]`   
# 2. c) `fruit_salad.iloc[[9, 2], [1, 7, 3]]`  
# 
# ```
