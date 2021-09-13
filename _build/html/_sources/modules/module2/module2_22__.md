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


# Chaining notation

:::{admonition} Watch it
See the accompanied youtube video at <a href="https://www.youtube.com/embed/WCWi1R2CQsY?rel=0?start=1591&end=1748" target="_blank">the link here.</a>
:::


<br>

---

## What is Chaining?

<br>

<br>

<img src='/module2/chainsfinal.png' width="110%" alt="404 image" />  
[Attribution](https://unsplash.com/photos/42ui88Qrxhw)

Notes:

Up until now, when we perform multiple actions on an object, we have
been saving the results with the `=` operator after each line.

Chaining allows us to do multiple actions in a single line of code
without the need to save each action in an intermediate object.

You can imagine that we are linking verbs together with a chain.

---

``` python
manufacturer_column = cereal['mfr']
manufacturer_column.value_counts()
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

``` python
cereal['mfr'].value_counts()
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

Notes:

When we made our frequency table in Module 1, we first saved the single
column as an object before we used `value_counts()` like we show you
here.

Instead of saving the column as an intermediate value, we can skip this
step and make the frequency table in one line, with chaining.

The convenience doesn’t stop there either.

---

``` python
mfr_k = cereal[cereal['mfr'] == 'K']
csr_df = mfr_k.loc[:, ["calories", "sugars", "rating"]]
cereal_mean = csr_df.mean()
cereal_mean
```

```out
calories    108.695652
sugars        7.565217
rating       44.038462
dtype: float64
```

``` python
cereal_mean = cereal[cereal['mfr'] == 'K'].loc[:, ["calories", "sugars", "rating"]].mean()
cereal_mean
```

```out
calories    108.695652
sugars        7.565217
rating       44.038462
dtype: float64
```

Notes:

Let’s say we want to perform three actions:

1.  Filter the dataframe for cereals only from manufacturer “K”.

2.  Select the columns `calories`, `sugars` and `rating` using the verb
    `loc`.

3.  Find the mean of each column using `.mean()`.

Previous we would need 3 different lines to code this.

Instead we can chain them, as shown here.

This chain avoided the use of the intermediate objects; `mfr_k` and
`csr_df`.

We cut out creating intermediate variables which is great but now we
have a really long line of code and it’s a bit hard to read.

How can we make this easier to read?

---

``` python
cereal_mean = cereal[cereal['mfr'] == 'K'].loc[:, ["calories", "sugars", "rating"]].mean()

cereal_mean
```

```out
calories    108.695652
sugars        7.565217
rating       44.038462
dtype: float64
```

``` python
cereal_mean = (cereal[cereal['mfr'] == 'K'].loc[:, ["calories", "sugars", "rating"]]
                                           .mean()
              )
              
cereal_mean.head()
```

```out
calories    108.695652
sugars        7.565217
rating       44.038462
dtype: float64
```

Notes:

In this course, we suggest using a new line for each verb.

We can do this by wrapping our all code (to the right of the equals
sign) in parentheses and inserting a new line before each period (`.`).

It’s a good habit to indent and have the verbs lined up for additional
clarity.

---

## Coding Preferences

  - Chaining has advantages and disadvantages.
  - Increases the readability of our code.
  - Comments are extremely important with of without chaining.

Notes:

Although we have seen how chaining has advantages, it’s a coding style
that is adopted by the person writing the code.

Someone else (or more often, future you) must be able to understand what
is being accomplished.

This is why comments (`#`) are so important. If a lot is going on in
your code, it’s a good habit to explain it whether it’s with chaining,
or without.

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
