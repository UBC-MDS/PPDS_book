---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Selecting using .loc\[\]

:::{admonition} Watch it
See the accompanied youtube video at <a href="https://www.youtube.com/embed/W88f5DAl9hk?rel=0?start=763&end=825" target="_blank">the link here.</a>
:::

## Unordered Indexing

Here we have our trusty `cereal` dataframe.

What would we do if we wanted to select columns and rows that don’t fall
consecutively or if we wanted to rearrange them?

```{code-cell} ipython3
:tags: ["remove-cell"]
import pandas as pd
import numpy as np
pd.set_option('display.width', 400)

np.set_printoptions(linewidth=400)

pd.set_option('display.max_columns', 15)
cereal = pd.read_csv('cereal.csv')
```


```{code-cell} ipython3
cereal
```


Let’s say we want only the rows labelled:

  - `Clusters` (13)
  - `Trix` (73), and
  - `Wheaties` (75)

And the columns:

  - `name`
  - `type`
  - `sugars`, and
  - `rating`

How would we obtain them?

We need to specify each column and row label that we want between square
brackets `[]`, that follow `.loc[]` and we separate the items that we
list in the square brackets with commas.


```{code-cell} ipython3
cereal.loc[[13,73,75], ['name', 'type', 'sugars', 'rating']]
```


## Ordered Indexing

What if we wanted the rows to be in the order `Wheaties` (75), `Trix`
(73) and `Clusters` (13) and columns in the order `name`, `type`,
`rating` and `sugars`.

How would we obtain that?

We would just have to rearranging the order in which we list our rows
and columns.


```{code-cell} ipython3
cereal.loc[[75, 73, 13], ['name', 'type', 'rating', 'sugars']]
```


:::{admonition} Let’s apply what we learned!

Using my `fruit_salad` dataframe from earlier...

```out
           name    colour    location    seed   shape  sweetness   water-content  weight
0         apple       red     canada    True   round     True          84         100
1        banana    yellow     mexico   False    long     True          75         120
2    cantaloupe    orange      spain    True   round     True          90        1360
3  dragon-fruit   magenta      china    True   round    False          96         600
4    elderberry    purple    austria   False   round     True          80           5
5           fig    purple     turkey   False    oval    False          78          40
6         guava     green     mexico    True    oval     True          83         450
7   huckleberry      blue     canada    True   round     True          73           5
8          kiwi     brown      china    True   round     True          80          76
9         lemon    yellow     mexico   False    oval    False          83          65
```

1\. If I wanted to make a tropical salad and the recipe calls for `kiwi`, `cantaloupe` and `guava` in this order and I am only interested in columns ordered as `sweetness`, `weight`, `seed` and  `location`, what would my code look like?         
a) `fruit_salad.loc[8, 2, 6:"sweetness", "weight", "seed", "location"]`          
b) `fruit_salad.loc[[8, 2, 6]:["sweetness", "weight", "seed", "location"]]`        
c) `fruit_salad.loc[[8, 2, 6], ["sweetness", "weight", "seed", "location"]]`    
d) `fruit_salad.loc[[2, 6, 8], ["location", "seed”, “sweetness", "weight"]]`    

:::

```{admonition} Solutions!
:class: tip, dropdown

1. c) `fruit_salad.loc[[8, 2, 6], ["sweetness", "weight", "seed", "location"]]`             

```
