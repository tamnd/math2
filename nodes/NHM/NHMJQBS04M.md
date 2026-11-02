---
tag: NHMJQBS04M
kind: concept
name: Gosper's algorithm
msc: [33F10, 68W30, 39A10]
sources:
  - url: https://en.wikipedia.org/wiki/Gosper%27s_algorithm
same_as:
  wikidata: Q5587427
  wikipedia: Gosper's algorithm
---

## Summary

Gosper's algorithm decides, for a hypergeometric term $t_k$, whether its partial sums $\sum_{j < k} t_j$ are a hypergeometric term plus a constant.
When they are, it finds that term.
This is the discrete analogue of deciding whether an integral can be done in closed form.
It reduces the question to finding a polynomial solution of a linear recurrence with polynomial coefficients.
It is a building block of [[Zeilberger's algorithm|VA7MH05Z3B]] and of the search for [[WZ pairs|WC0QNABPZ4]].

## Explanations

### L1 human

Some sums have a neat closed form, such as $\sum_{j=0}^{k-1} j\cdot j! = k! - 1$.
Others, such as the partial sums $1 + \frac12 + \cdots + \frac1k$ of the harmonic series, have none of the same kind.
Gosper's algorithm looks for an answer $T_k$ that is the term $t_k$ times a rational function of $k$, with $T_{k+1} - T_k = t_k$.
It either finds such a $T_k$ or proves that none exists.
