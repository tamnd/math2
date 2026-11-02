---
tag: 3X9DD9J3CV
kind: concept
name: Subadditive function
msc: [39B62, 26A51]
sources:
  - url: https://en.wikipedia.org/wiki/Subadditivity
same_as:
  wikidata: Q1934099
  wikipedia: Subadditivity
---

## Summary

A subadditive function is a function $f$ with $f(x + y) \le f(x) + f(y)$ for all $x, y$ in its domain.
The triangle inequality says that every [[norm|0V2WP9B1MF]] is subadditive, and every [[sublinear function|K3356N0SAX]] is subadditive.
For subadditive sequences, [[Fekete's lemma|8A4GGX1MEY]] shows that $f(n)/n$ converges to its infimum, which may be $-\infty$.
This makes subadditivity a basic tool for growth rates in analysis, combinatorics and ergodic theory.

## Explanations

### L1 human

A function is subadditive when the whole costs at most the sum of its parts.
Shipping costs are a picture: sending two parcels together usually costs no more than sending them apart.
The square root is subadditive on $[0, \infty)$: for example $\sqrt{9 + 16} = 5 \le 3 + 4$.
The absolute value on $\R$ is subadditive by the triangle inequality.
