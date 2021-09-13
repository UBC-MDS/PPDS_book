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

# Frequency Tables and Writing CSVs

:::{admonition} Watch it
See the accompanied youtube video at <a href="https://www.youtube.com/embed/W88f5DAl9hk?rel=0?start=1775&end=1940" target="_blank">the link here.</a>
:::

## What is Frequency?

Before we explain what a frequency table is, you must know what
frequency means first.

*_Frequency_* is simply put, the number of times a value occurs within
the data. Let’s look at an example using our candybars dataset.

``` python
cereal_mini
```

```out
                        name  weight available_canada_america
0               Coffee Crisp      50                   Canada
1               Butterfinger     184                  America
2                       Skor      39                     Both
3                   Smarties      45                   Canada
4                       Twix      58                     Both
5  Reeses Peanutbutter Cups       43                     Both
6               3 Musketeers      54                  America
```

If we count the number of times the value `Both` appears in the
`available_canada_america` column, we get 3 times. This is the frequency
of the value `both`.

## What is a Frequency Table?

A frequency table is a manner of displaying all the possible values of a
column in our dataframe and the number of occurrences (frequencies) of
each value.

For our sample data, a frequency table for the
`available_canada_america` column would look like this:

```out
Both       3
Canada     2
America    2
Name: available_canada_america, dtype: int64
```

If we want to get a frequency table of a categorical column, there are a
few steps that need to be followed.

Up until now, we discussed getting a single column from a dataframe
using double square brackets - `df[['column name']]`.

For frequency tables, however, we only use single brackets to obtain the
column values.


``` python
mfr_column = cereal['mfr']
mfr_column
```

```out
0     N
1     Q
2     K
3     K
     ..
73    G
74    R
75    G
76    G
Name: mfr, Length: 77, dtype: object
```
We saved the object in this example here to an object named `mfr_column`
in the same way that we have done this before.

Now we can use `.value_counts()` on this `mfr_column` variable to
reference it, and we can obtain the frequency value for the different
categories in that variable.

``` python
mfr_freq = mfr_column.value_counts()
mfr_freq
```

```out
K    23
G    22
P     9
Q     8
R     8
N     6
A     1
Name: mfr, dtype: int64
```

If we did instead use double square brackets with `pd.value_counts()`,
we would get an error. So it is important to take care and remember when
you are using `value_counts()`, you only use one set of square brackets.

``` python
mfr_col_wrong = cereal[['mfr']]
mfr_col_wrong
```

```out
   mfr
0    N
1    Q
2    K
3    K
..  ..
73   G
74   R
75   G
76   G

[77 rows x 1 columns]
```

``` python
mfr_col_wrong.value_counts()
```

``` out
AttributeError: 'DataFrame' object has no attribute 'value_counts'

Detailed traceback: 
  File "<string>", line 1, in <module>
  File "/usr/local/lib/python3.7/site-packages/pandas/core/generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
```


## Saving a dataframe

Sometimes it is useful to save a new dataframe to a file like a csv file
for future use by you or somebody else.

We can do this using a method called `.to_csv()`.

``` python
mfr_freq.to_csv('mfr_frequency.csv', index=False)
```

We put our desired `csv` file name in quotations within the parentheses
and follow it with the argument `index=False` so we don’t export our
index column which is just a column of numbers.

