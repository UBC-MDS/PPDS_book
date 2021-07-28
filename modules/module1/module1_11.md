# Slicing only columns using .loc\[\]

```{seealso}

See the accompanied youtube video at <a href="https://www.youtube.com/embed/W88f5DAl9hk?rel=0?start=651&end=758" target="_blank">the link here.</a>

```

What happens now if we wanted all the rows of the dataframe but only the
columns `calories` to `fiber`?

We can use `:` in the row postion of the `.loc[]` call to indicate we
want all the rows. So here we write `cereal.loc[:, 'calories':'fiber']`.

``` python
cereal.loc[:, 'calories':'fiber']
```

```out
    calories  protein  fat  sodium  fiber
0         70        4    1     130   10.0
1        120        3    5      15    2.0
2         70        4    1     260    9.0
3         50        4    0     140   14.0
4        110        2    2     200    1.0
..       ...      ...  ...     ...    ...
72       110        2    1     250    0.0
73       110        1    1     140    0.0
74       100        3    1     230    3.0
75       100        3    1     200    3.0
76       110        2    1     200    1.0

[77 rows x 5 columns]
```

## So Far

Let’s talk about what we have covered so far.

- `.loc[]` is used to slice columns and rows by **label** and within
    an interval.

- We always specify **row** indexing first, then **columns**.


``` python
cereal.loc['row name start':'row name end', 'column name start':'column name end']
```

- If we aren’t slicing any columns, but we are slicing rows we can
    shorten that to:

``` python
df.loc[ 'row name start':'row name end']
```

- However, the reverse is not true. If we want all the rows with only
    specific columns, we specify we want all the row first with just a
    colon `:` followed by interval of the columns:

``` python
df.loc[:, 'column name start':'column name end']
```

- We can read `:` as **“to”**.

- If the indices are labeled with numbers, we do not need “quotations”
    when calling them. This is only when the labels are using letters.

## Let’s apply what we learned!

Using my dataframe object named `fruit_salad`, let's answer some slicing questions.

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

1\. If you wanted all the rows and only columns `seeds`, `shape`, `sweetness` and `water-content,` what would your code look like using index labels?                     
a) `fruit_salad.loc[:, "seed":"weight"]`            
b) `fruit_salad[:, "seed":"water-content"]`            
c) `fruit_salad[0:9, "seed":"water-content"]`             
d) `fruit_salad.loc[:, "seed":"water-content"]`                        


```{admonition} Solutions!
:class: dropdown

1. d) `fruit_salad.loc[:, "seed":"water-content"]`           

That's correct! Good job! This has both .loc[] and includes the columns we wish to slice here.

```
