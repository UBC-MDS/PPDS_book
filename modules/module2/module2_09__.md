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


# Column renaming and column dropping

:::{admonition} Watch it
See the accompanied youtube video at <a href="https://www.youtube.com/embed/WCWi1R2CQsY?rel=0?start=573&end=589" target="_blank">the link here.</a>
:::


<br>

---

``` python
candy = pd.read_csv('candybars.csv')
candy
```

```out
                 name  weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi available_canada_america
0        Coffee Crisp      50          1        0        0       0                  1        0                0      0                   Canada
1        Butterfinger     184          1        1        1       0                  0        0                0      0                  America
2                Skor      39          1        0        1       0                  0        0                0      0                     Both
3            Smarties      45          1        0        0       0                  0        0                0      1                   Canada
..                ...     ...        ...      ...      ...     ...                ...      ...              ...    ...                      ...
21   Whatchamacallits      45          1        1        0       0                  1        0                0      0                  America
22         Almond Joy      46          1        0        0       0                  0        1                0      0                  America
23           Oh Henry      51          1        1        1       0                  0        0                0      0                     Both
24  Cookies and Cream      43          0        0        0       0                  1        0                1      0                     Both

[25 rows x 11 columns]
```

Notes:

Remember our `candybars.csv` dataframe?

Let’s bring it back and save it as object named `candy`.

---

## Column Renaming

``` python
candy = candy.rename(columns={'available_canada_america':'availability'})
candy
```

```out
                 name  weight  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability
0        Coffee Crisp      50          1        0        0       0                  1        0                0      0       Canada
1        Butterfinger     184          1        1        1       0                  0        0                0      0      America
2                Skor      39          1        0        1       0                  0        0                0      0         Both
3            Smarties      45          1        0        0       0                  0        0                0      1       Canada
..                ...     ...        ...      ...      ...     ...                ...      ...              ...    ...          ...
21   Whatchamacallits      45          1        1        0       0                  1        0                0      0      America
22         Almond Joy      46          1        0        0       0                  0        1                0      0      America
23           Oh Henry      51          1        1        1       0                  0        0                0      0         Both
24  Cookies and Cream      43          0        0        0       0                  1        0                1      0         Both

[25 rows x 11 columns]
```

``` python
 columns={'old column name':'new column name'}
```

Notes:

There will be times where you are unsatisfied with the column names and
you may want to change them.

The proper syntax to do that is with `.rename()`.

The column name `available_canada_america` is a bit long.

Perhaps it would be a good idea to change it to something shorter like
`availability`.

Here is how we can accomplish that.

This code uses something we’ve never seen before - `{}` curly braces,
also called curly brackets.

These have a special meaning but for now, you only need to concentrate
your attention on the fact that the argument `columns` needs to have the
format shown on the slide.

---

``` python
candy = candy.rename(columns={'available_canada_america':'availability',
                        'weight':'weight_g'})
candy.head()
```

```out
           name  weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability
0  Coffee Crisp        50          1        0        0       0                  1        0                0      0       Canada
1  Butterfinger       184          1        1        1       0                  0        0                0      0      America
2          Skor        39          1        0        1       0                  0        0                0      0         Both
3      Smarties        45          1        0        0       0                  0        0                0      1       Canada
4          Twix        58          1        0        1       0                  1        0                0      1         Both
```

Notes:

You can also rename multiple columns at once by adding a comma between
the new and old column pairs within the curly brackets.

It’s important that we always save the dataframe to an object when
making column changes or the changes will not be saved in our dataframe.

---

## Column Dropping

``` python
candy.drop(columns='coconut')
```

```out
                 name  weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  white_chocolate  multi availability
0        Coffee Crisp        50          1        0        0       0                  1                0      0       Canada
1        Butterfinger       184          1        1        1       0                  0                0      0      America
2                Skor        39          1        0        1       0                  0                0      0         Both
3            Smarties        45          1        0        0       0                  0                0      1       Canada
..                ...       ...        ...      ...      ...     ...                ...              ...    ...          ...
21   Whatchamacallits        45          1        1        0       0                  1                0      0      America
22         Almond Joy        46          1        0        0       0                  0                0      0      America
23           Oh Henry        51          1        1        1       0                  0                0      0         Both
24  Cookies and Cream        43          0        0        0       0                  1                1      0         Both

[25 rows x 10 columns]
```

Notes:

`.drop()` is the verb we use to delete columns in a dataframe.

Let’s delete the column `coconut` by specifying it in the `columns`
argument of the `drop` verb.

---

``` python
candy.drop(columns='coconut')
```

``` python
candy.head()
```

```out
           name  weight_g  chocolate  peanuts  caramel  nougat  cookie_wafer_rice  coconut  white_chocolate  multi availability
0  Coffee Crisp        50          1        0        0       0                  1        0                0      0       Canada
1  Butterfinger       184          1        1        1       0                  0        0                0      0      America
2          Skor        39          1        0        1       0                  0        0                0      0         Both
3      Smarties        45          1        0        0       0                  0        0                0      1       Canada
4          Twix        58          1        0        1       0                  1        0                0      1         Both
```

``` python
candy = candy.drop(columns=['nougat', 'coconut'])
candy.head()
```

```out
           name  weight_g  chocolate  peanuts  caramel  cookie_wafer_rice  white_chocolate  multi availability
0  Coffee Crisp        50          1        0        0                  1                0      0       Canada
1  Butterfinger       184          1        1        1                  0                0      0      America
2          Skor        39          1        0        1                  0                0      0         Both
3      Smarties        45          1        0        0                  0                0      1       Canada
4          Twix        58          1        0        1                  1                0      1         Both
```

Notes:

If you look again at the code we just wrote you’ll notice we didn’t save
over the dataframe object, so the dataframe `candy` still will contain
the `coconut` column.

Let’s overwrite the dataframe and remove multiple columns at the same
time.

Let’s drop `nougat` and `coconut` together.

We put the columns we want to drop in square brackets and this time we
will remember to overwrite over the `candy` object.

Now when we call `candy.head()` it reflects the dropped columns. They’re
no longer there.

:::{admonition} Let’s apply what we learned!

Bringing back our Fruit Salad dataframe:

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
 
1\. Which of the following columns contain numerical data?                             
a) `colour`, `shape`, `water-content` 
b) `water-content`, `weight`      
c) `colour`, `seed`, `water-content`, `weight`           
d) All of the columns are categorical            

2\. We need summary statistics of both numerical and categorical columns of the dataframe `fruit_salad`. What code would be suitable for this?        
a) `df.describe()`        
b) `fruit_salad.describe()`        
c) `fruit_salad.describe(include="all")`        
d) `fruit_salad.summary(include="all")`    

:::

```{admonition} Solutions!
:class: tip, dropdown

1. b) `water-content`, `weight`   
2. c) `fruit_salad.describe(include="all")` 
