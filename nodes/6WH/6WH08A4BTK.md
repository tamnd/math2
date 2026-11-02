---
tag: 6WH08A4BTK
kind: concept
name: Determinantal variety
msc: [14M12]
sources:
  - url: https://en.wikipedia.org/wiki/Determinantal_variety
same_as:
  wikidata: Q5265691
  wikipedia: Determinantal variety
---

## Summary

A determinantal variety is the set of matrices of a fixed size whose [[rank|0ZC9YTXZRY]] is at most a given number.
It is cut out by the vanishing of all [[minors|0BT9BYWVRY]] of one size larger, which generate a [[determinantal ideal|SXD7X0WQH1]].
These varieties are irreducible, normal and Cohen–Macaulay, and they are basic examples of singular varieties.
Many varieties in geometry, such as secant varieties and rational normal curves, are described by determinantal equations.

## Explanations

### L1 human

A $2 \times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ has rank at most $1$ exactly when $ad - bc = 0$.
This one equation defines a three-dimensional cone in the four-dimensional space of matrices, with its tip at the zero matrix.
For larger matrices, "rank at most $r$" is expressed by the vanishing of all $(r + 1) \times (r + 1)$ minors.
The resulting sets are the determinantal varieties, and their only singular points are the matrices of rank smaller than $r$.
