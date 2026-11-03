---
tag: RNVHT5BTQS
kind: concept
name: Leslie matrix
msc: [92D25, 15B48]
specializes: [WS9M7HY0FE]
sources:
  - url: https://en.wikipedia.org/wiki/Leslie_matrix
same_as:
  wikidata: Q943800
  wikipedia: Leslie matrix
---

## Summary

A Leslie matrix is the projection matrix of an age-structured [[matrix population model|WS9M7HY0FE]], introduced by Patrick H. Leslie.
Its first row holds the fecundities of the age classes and its subdiagonal holds the survival probabilities from one age class to the next.
Its dominant [[eigenvalue|0BQAA2BK3Q]] gives the long-run growth factor of the population, and its eigenvector gives the stable age distribution.

## Explanations

### L1 human

Group the females of a population by age: $0$ to $1$ year, $1$ to $2$ years, and so on.
Each year, every age group has some daughters, and a fraction of each group survives into the next group.
The Leslie matrix puts the numbers of daughters in its top row and the survival fractions just below the diagonal.
Multiplying the vector of group sizes by the matrix moves everyone one year forward.
For example, with two age groups, fecundities $1$ and $2$, and survival $0.5$, the matrix is $\begin{pmatrix} 1 & 2 \\ 0.5 & 0 \end{pmatrix}$.
