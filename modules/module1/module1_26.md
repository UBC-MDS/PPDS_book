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

# Summary Statistics

:::{admonition} Watch it
See the accompanied youtube video at <a href="https://www.youtube.com/embed/W88f5DAl9hk?rel=0?start=1518&end=1770" target="_blank">the link here.</a>
:::

Now we’ve learned about how to get the data in to the shape and size
that we desire, now we ca have some fun with it\!

We usually like to learn from it. One place we can start is summary
statistics, so we can calculate interesting values for each of the
variables or columns in our dataframe.

Let’s start by doing this for the cereal dataset again.

``` python
cereal = pd.read_csv('cereal.csv')
cereal.head(15)
```

```out
                         name mfr  type  calories  protein  fat  sodium  ...  sugars  potass  vitamins  shelf  weight  cups     rating
0                   100% Bran   N  Cold        70        4    1     130  ...       6     280        25      3    1.00  0.33  68.402973
1           100% Natural Bran   Q  Cold       120        3    5      15  ...       8     135         0      3    1.00  1.00  33.983679
2                    All-Bran   K  Cold        70        4    1     260  ...       5     320        25      3    1.00  0.33  59.425505
3   All-Bran with Extra Fiber   K  Cold        50        4    0     140  ...       0     330        25      3    1.00  0.50  93.704912
4              Almond Delight   R  Cold       110        2    2     200  ...       8       1        25      3    1.00  0.75  34.384843
5     Apple Cinnamon Cheerios   G  Cold       110        2    2     180  ...      10      70        25      1    1.00  0.75  29.509541
6                 Apple Jacks   K  Cold       110        2    0     125  ...      14      30        25      2    1.00  1.00  33.174094
7                     Basic 4   G  Cold       130        3    2     210  ...       8     100        25      3    1.33  0.75  37.038562
8                   Bran Chex   R  Cold        90        2    1     200  ...       6     125        25      1    1.00  0.67  49.120253
9                 Bran Flakes   P  Cold        90        3    0     210  ...       5     190        25      3    1.00  0.67  53.313813
10               Cap'n'Crunch   Q  Cold       120        1    2     220  ...      12      35        25      2    1.00  0.75  18.042851
11                   Cheerios   G  Cold       110        6    2     290  ...       1     105        25      1    1.00  1.25  50.764999
12      Cinnamon Toast Crunch   G  Cold       120        1    3     210  ...       9      45        25      2    1.00  0.75  19.823573
13                   Clusters   G  Cold       110        3    2     140  ...       7     105        25      3    1.00  0.50  40.400208
14                Cocoa Puffs   G  Cold       110        1    1     180  ...      13      55        25      2    1.00  1.00  22.736446

[15 rows x 16 columns]
```

## Numerical and Categorical Columns

Before we go further, let’s quickly discuss the 2 different types of
data.

### Categorical data

Categorical data consists of qualitative observations such as
characteristics - things generally containing names or words.

**Examples**

  - Colours
  - Names

<br>

### Numerical data

These data are usually expressed with numbers.

**Examples**

  - Measurements
  - Quantities



Our columns in our dataframe are considered one of the two of these.

## Pandas describe()

Pandas has a lot up its sleeve but one of the most useful methods is
called `.describe()` and it does exactly that. it *describes* our data.

Let’s try it out on our cereal dataset.

By default `df.describe()` only shows numerical columns.


``` python
cereal.describe()
```

```out
         calories    protein        fat      sodium      fiber      carbo     sugars      potass    vitamins      shelf     weight       cups     rating
count   77.000000  77.000000  77.000000   77.000000  77.000000  77.000000  77.000000   77.000000   77.000000  77.000000  77.000000  77.000000  77.000000
mean   106.883117   2.545455   1.012987  159.675325   2.151948  14.623377   6.948052   96.129870   28.246753   2.207792   1.029610   0.821039  42.665705
std     19.484119   1.094790   1.006473   83.832295   2.383364   4.188138   4.403635   71.215823   22.342523   0.832524   0.150477   0.232716  14.047289
min     50.000000   1.000000   0.000000    0.000000   0.000000   1.000000   0.000000    1.000000    0.000000   1.000000   0.500000   0.250000  18.042851
25%    100.000000   2.000000   0.000000  130.000000   1.000000  12.000000   3.000000   40.000000   25.000000   1.000000   1.000000   0.670000  33.174094
50%    110.000000   3.000000   1.000000  180.000000   2.000000  14.000000   7.000000   90.000000   25.000000   2.000000   1.000000   0.750000  40.400208
75%    110.000000   3.000000   2.000000  210.000000   3.000000  17.000000  11.000000  120.000000   25.000000   3.000000   1.000000   1.000000  50.828392
max    160.000000   6.000000   5.000000  320.000000  14.000000  23.000000  15.000000  330.000000  100.000000   3.000000   1.500000   1.500000  93.704912
```

Let’s talk a little bit about the output of `.describe()`.

On the left-hand side we see a new column. This column contains the
names of the different summary statistics that `.describes()` gives us
back for our dataset. Let’s talk about them each individually:

- `count`: The number of non-NA/null observations.
- `mean`: The mean of column
- `std` : The standard deviation of a column
- `min`: The min value for a column
- `max`: The max value for a column
- By default the 25, 50 and 75 percentile of the observations



We can make changes to either limit how much is shown or include more
using describe. One useful argument is `include` and a value we can give
to that is `all`.

``` python
cereal.describe(include='all')
```

```out
               name  mfr  type    calories    protein        fat      sodium  ...     sugars      potass    vitamins      shelf     weight       cups     rating
count            77   77    77   77.000000  77.000000  77.000000   77.000000  ...  77.000000   77.000000   77.000000  77.000000  77.000000  77.000000  77.000000
unique           77    7     2         NaN        NaN        NaN         NaN  ...        NaN         NaN         NaN        NaN        NaN        NaN        NaN
top     Corn Flakes    K  Cold         NaN        NaN        NaN         NaN  ...        NaN         NaN         NaN        NaN        NaN        NaN        NaN
freq              1   23    74         NaN        NaN        NaN         NaN  ...        NaN         NaN         NaN        NaN        NaN        NaN        NaN
mean            NaN  NaN   NaN  106.883117   2.545455   1.012987  159.675325  ...   6.948052   96.129870   28.246753   2.207792   1.029610   0.821039  42.665705
std             NaN  NaN   NaN   19.484119   1.094790   1.006473   83.832295  ...   4.403635   71.215823   22.342523   0.832524   0.150477   0.232716  14.047289
min             NaN  NaN   NaN   50.000000   1.000000   0.000000    0.000000  ...   0.000000    1.000000    0.000000   1.000000   0.500000   0.250000  18.042851
25%             NaN  NaN   NaN  100.000000   2.000000   0.000000  130.000000  ...   3.000000   40.000000   25.000000   1.000000   1.000000   0.670000  33.174094
50%             NaN  NaN   NaN  110.000000   3.000000   1.000000  180.000000  ...   7.000000   90.000000   25.000000   2.000000   1.000000   0.750000  40.400208
75%             NaN  NaN   NaN  110.000000   3.000000   2.000000  210.000000  ...  11.000000  120.000000   25.000000   3.000000   1.000000   1.000000  50.828392
max             NaN  NaN   NaN  160.000000   6.000000   5.000000  320.000000  ...  15.000000  330.000000  100.000000   3.000000   1.500000   1.500000  93.704912

[11 rows x 16 columns]
```

This expands the output so we get summary statistics for both
categorical and numerical columns now.

Adding `include='all'` within the brackets adds some additional
statistics about categorical columns including:

- `unique`: which indicates the number of unique observations
- `top`: which tells up the observation value that is most occurring
- `freq`: which informs us of the frequency of the most occurring
  observation


We can also get single statistics of each column using functions like:
`.mean()`,`.std()`, `.count()`, `.median()`, `.sum()`.

To do this, we first have to grab the column that we are interested in
exploring, and then we add the verb.

Here are some examples of things that we can calculate. First we
calculate the mean of the ratings, then we calculate sum of the ratings,
and finally the median of the ratings.


``` python
ratings = cereal[['rating']]
ratings.mean()
```

```out
rating    42.665705
dtype: float64
```

``` python
ratings.sum()
```

```out
rating    3285.259284
dtype: float64
```

``` python
ratings.median()
```

```out
rating    40.400208
dtype: float64
```

We can also use these summary statistic verbs on the entire dataframe.
This now shows the mean value of each column in the dataframe.

You’ll notice that only the numerical variables are calculated which
makes sense since we would not be able to calculate the mean of
categorical data.

``` python
cereal.mean()
```

```out
calories    106.883117
protein       2.545455
fat           1.012987
sodium      159.675325
fiber         2.151948
carbo        14.623377
sugars        6.948052
potass       96.129870
vitamins     28.246753
shelf         2.207792
weight        1.029610
cups          0.821039
rating       42.665705
dtype: float64
```

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

```
