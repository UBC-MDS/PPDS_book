#!/usr/bin/env python
# coding: utf-8

# # Selecting using .loc\[\]
# 
# :::{admonition} Watch it
# See the accompanied youtube video at <a href="https://www.youtube.com/embed/W88f5DAl9hk?rel=0?start=763&end=825" target="_blank">the link here.</a>
# :::
# 
# ## Unordered Indexing
# 
# Here we have our trusty `cereal` dataframe.
# 
# What would we do if we wanted to select columns and rows that don’t fall
# consecutively or if we wanted to rearrange them?
# 
# 
# ``` python
# cereal
# ```
# 
# ```out
#                          name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
# 0                   100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3     1.0  0.33  68.402973
# 1           100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3     1.0  1.00  33.983679
# 2                    All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3     1.0  0.33  59.425505
# 3   All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3     1.0  0.50  93.704912
# 4              Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3     1.0  0.75  34.384843
# ..                        ...  ..   ...       ...      ...  ...     ...  ...     ...     ...       ...    ...     ...   ...        ...
# 72                    Triples   G  Cold       110        2    1     250  ...       3      60        25      3     1.0  0.75  39.106174
# 73                       Trix   G  Cold       110        1    1     140  ...      12      25        25      2     1.0  1.00  27.753301
# 74                 Wheat Chex   R  Cold       100        3    1     230  ...       3     115        25      1     1.0  0.67  49.787445
# 75                   Wheaties   G  Cold       100        3    1     200  ...       3     110        25      1     1.0  1.00  51.592193
# 76        Wheaties Honey Gold   G  Cold       110        2    1     200  ...       8      60        25      1     1.0  0.75  36.187559
# 
# [77 rows x 16 columns]
# ```
# 
# Let’s say we want only the rows labelled:
# 
#   - `Clusters` (13)
#   - `Trix` (73), and
#   - `Wheaties` (75)
# 
# And the columns:
# 
#   - `name`
#   - `type`
#   - `sugars`, and
#   - `rating`
# 
# How would we obtain them?
# 
# We need to specify each column and row label that we want between square
# brackets `[]`, that follow `.loc[]` and we separate the items that we
# list in the square brackets with commas.
# 
# 
# ``` python
# cereal.loc[[13,73,75], ['name', 'type', 'sugars', 'rating']]
# ```
# 
# ```out
#         name  type  sugars     rating
# 13  Clusters  Cold       7  40.400208
# 73      Trix  Cold      12  27.753301
# 75  Wheaties  Cold       3  51.592193
# ```
# 
# ## Ordered Indexing
# 
# What if we wanted the rows to be in the order `Wheaties` (75), `Trix`
# (73) and `Clusters` (13) and columns in the order `name`, `type`,
# `rating` and `sugars`.
# 
# How would we obtain that?
# 
# We would just have to rearranging the order in which we list our rows
# and columns.
# 
# 
# ``` python
# cereal.loc[[75, 73, 13], ['name', 'type', 'rating', 'sugars']]
# ```
# 
# ```out
#         name  type     rating  sugars
# 75  Wheaties  Cold  51.592193       3
# 73      Trix  Cold  27.753301      12
# 13  Clusters  Cold  40.400208       7
# ```
# 
# :::{admonition} Let’s apply what we learned!
# 
# Using my `fruit_salad` dataframe from earlier...
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
# 1\. If I wanted to make a tropical salad and the recipe calls for `kiwi`, `cantaloupe` and `guava` in this order and I am only interested in columns ordered as `sweetness`, `weight`, `seed` and  `location`, what would my code look like?         
# a) `fruit_salad.loc[8, 2, 6:"sweetness", "weight", "seed", "location"]`          
# b) `fruit_salad.loc[[8, 2, 6]:["sweetness", "weight", "seed", "location"]]`        
# c) `fruit_salad.loc[[8, 2, 6], ["sweetness", "weight", "seed", "location"]]`    
# d) `fruit_salad.loc[[2, 6, 8], ["location", "seed”, “sweetness", "weight"]]`    
# 
# :::
# 
# ```{admonition} Solutions!
# :class: tip, dropdown
# 
# 1. c) `fruit_salad.loc[[8, 2, 6], ["sweetness", "weight", "seed", "location"]]`             
# 
# ```
