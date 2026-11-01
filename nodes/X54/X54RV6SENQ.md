---
tag: X54RV6SENQ
kind: concept
name: Rees matrix semigroup
msc: [20M10, 20M17]
specializes: [0XMEM406JM]
sources:
  - url: https://en.wikipedia.org/wiki/Rees_matrix_semigroup
same_as:
  wikidata: Q17099723
  wikipedia: Rees matrix semigroup
---

## Summary

A Rees matrix semigroup is a [[semigroup|0XMEM406JM]] built from a [[group|G5S1M9]] $G$ and two index sets $I$ and $\Lambda$.
It also uses a matrix $P$ with entries in $G$.
Its elements are triples $(i, g, \lambda)$, and the matrix $P$ is inserted in the middle of each product.
Rees's theorem says that the completely simple semigroups are exactly the Rees matrix semigroups over groups.
A variant with a zero element describes the completely $0$-simple semigroups, which are the building blocks of finite semigroups.

## Explanations

### L1 human

A Rees matrix semigroup is like a grid of copies of a group.
The rows are labelled by $I$ and the columns by $\Lambda$.
When you multiply two elements, you keep the row of the first and the column of the second.
You multiply the group parts with a twist taken from the matrix $P$.
If the group is trivial, a product just keeps the row of the left factor and the column of the right factor.
