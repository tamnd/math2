---
tag: KY7W9E9ECS
kind: concept
name: Next-generation matrix
msc: [92D30, 15B48]
sources:
  - url: https://en.wikipedia.org/wiki/Next-generation_matrix
same_as:
  wikidata: Q17071746
  wikipedia: Next-generation matrix
---

## Summary

The next-generation matrix of a compartmental epidemic model records how many new infections of each type one infected host of each type produces.
Its spectral radius is the [[basic reproduction number|VY4H52692D]] $R_0$ of the model.
It gives a systematic way to compute $R_0$ when there are several infected compartments, such as exposed and infectious stages, or several host groups.

## Explanations

### L1 human

Suppose a disease spreads among children and adults, at different rates within and between the groups.
Make a small table: entry $(i, j)$ is how many people of group $i$ one infected person of group $j$ infects on average.
Applying the table repeatedly predicts the next generations of cases.
In the long run the cases grow or shrink by a fixed factor per generation, and that factor is $R_0$.
For example, the table with rows $(1, 1)$ and $(1, 1)$ gives $R_0 = 2$.
