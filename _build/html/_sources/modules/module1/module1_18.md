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

# Selecting a Single Column

:::{admonition} Watch it
See the accompanied youtube video at <a href="https://www.youtube.com/embed/W88f5DAl9hk?rel=0?start=913&end=1005" target="_blank">the link here.</a>
:::

Something we often do in data analysis is obtain a single column from
a dataframe. We can again use `.loc[]` to do this which would look
something like this in general:

`dataframe.loc[:, ['column name']]`

So if we here want the column named `type` from our cereal dataframe we
could use the syntax:

``` python
cereal.loc[:, ['type']]
```

```out
    type
0   Cold
1   Cold
2   Cold
3   Cold
4   Cold
..   ...
72  Cold
73  Cold
74  Cold
75  Cold
76  Cold

[77 rows x 1 columns]
```

This seems a bit long winded and since we do this type of thing often.
Luckily, Pandas has provided a quicker syntax to use to do the same
thing.


<br>



Instead, selecting a single column can be done without using `.loc[]`
and we can just specify the dataframe name, followed by double square
brackets containing the column of interest (`df[['column name']]`).

``` python
cereal[['type']]
```

```out
    type
0   Cold
1   Cold
2   Cold
3   Cold
4   Cold
..   ...
72  Cold
73  Cold
74  Cold
75  Cold
76  Cold

[77 rows x 1 columns]
```

This makes the syntax for selecting the column `type` from the `cereal`
dataframe very easy.


