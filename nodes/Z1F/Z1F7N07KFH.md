---
tag: Z1F7N07KFH
kind: concept
name: Difference algebra
msc: [12H10, 39A05]
sources:
  - url: https://en.wikipedia.org/wiki/Difference_algebra
same_as:
  wikidata: Q5275270
  wikipedia: Difference algebra
---

## Summary

Difference algebra studies [[rings|0B1261B5ED]] and [[fields|04C5ZBG1WT]] equipped with a distinguished endomorphism, called difference rings and difference fields.
It is the algebraic theory of difference equations, such as $f(x+1) - f(x) = g(x)$, in the same way that differential algebra is the algebraic theory of differential equations.
The endomorphism plays the role that the [[derivation|3J89REV9WQ]] plays in a [[differential field|GA5PTQGC6G]].

## Explanations

### L1 human

A difference equation relates the values of an unknown function at shifted points, such as $f(x+1)$ and $f(x)$.
The shift $f(x) \mapsto f(x+1)$ respects sums and products of functions, so it is a ring homomorphism.
Difference algebra keeps only this structure: a ring together with one such map.
For example, on the rational functions $\C(x)$ the shift sends $x^2$ to $x^2 + 2x + 1$.
Questions such as "can this sum be written in closed form?" then become questions about difference fields.
