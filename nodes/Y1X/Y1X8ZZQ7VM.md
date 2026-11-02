---
tag: Y1X8ZZQ7VM
kind: concept
name: q-Pochhammer symbol
msc: [05A30, 33D15]
sources:
  - url: https://en.wikipedia.org/wiki/Q-Pochhammer_symbol
same_as:
  wikidata: Q518706
  wikipedia: Q-Pochhammer symbol
---

## Summary

The $q$-Pochhammer symbol $(a; q)_n = (1 - a)(1 - aq) \cdots (1 - aq^{n-1})$ is a $q$-analogue of the rising factorial.
Its infinite version $(a; q)_\infty$ is a convergent [[infinite product|JYV1Y8XX16]] for $\abs{q} < 1$.
It is the basic building block of $q$-series, basic hypergeometric series and generating functions for integer partitions.
The exact definition is in [[q-Pochhammer symbol|K8PHD2NAW9]].

## Explanations

### L1 human

The $q$-Pochhammer symbol is a product of factors $1 - a$, $1 - aq$, $1 - aq^2$, and so on, each with one more power of $q$.
For example, $(q; q)_3 = (1 - q)(1 - q^2)(1 - q^3)$.
Such products appear when one counts partitions of integers: the coefficients of $1/(q; q)_\infty$, expanded in powers of $q$, are the partition numbers.
