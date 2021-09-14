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

# Obtaining dataframe values

:::{admonition} Watch it
See the accompanied youtube video at <a href="https://www.youtube.com/embed/W88f5DAl9hk?start=830&end=907" target="_blank">the link here.</a>
:::

At this point of the module, we now know how to get a subset of an
existing dataframe, but what if we just want to get a single value from
it?

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
cereal.loc[[63]]
```

For example, what if we wanted to save the calorie content of `Shredded
Wheat` by extracting it from the dataframe manually instead of typing
the number in Python?

To do this we use again our `.loc` notation and we specify the row we
are targeting which is 63, followed by the column, here `calories`. This
goes in the square brackets.

```{code-cell} ipython3
cereal.loc[63, 'calories']
```

When we do this, it displays the the value contained in the cell, which
in this case, is 80.

What about if we want just the rating of `Smacks` which is located at index
66?

```{code-cell} ipython3
cereal.loc[[66]]
```

Again we use `.loc[]` notation, and we specify the row and the column
location separated by a comma.

So here we write `cereal.loc` and the inside the brackets we write `[66,
'rating']`.


```{code-cell} ipython3
cereal.loc[66, 'rating']
```


