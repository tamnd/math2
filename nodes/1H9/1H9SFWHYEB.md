---
tag: 1H9SFWHYEB
kind: concept
name: Incidence algebra
msc: [06A11, 16S99]
sources:
  - url: https://en.wikipedia.org/wiki/Incidence_algebra
same_as:
  wikidata: Q371133
  wikipedia: Incidence algebra
---

## Summary

The incidence algebra of a locally finite [[partially ordered set|0QV2JS9RJ3]] is the algebra of functions on its intervals, multiplied by a convolution.
Its most important elements are the zeta function, which is $1$ on every interval, and its inverse, the Möbius function of the poset.
It gives a common setting for inclusion–exclusion, the number-theoretic [[Möbius inversion formula|07Q4TBTFVB]] and the calculus of finite differences, through [[Möbius inversion on posets|B8XJSJ517Q]].

## Explanations

### L1 human

Take a poset in which every interval $[x, y]$ has finitely many elements.
Attach a number to each pair $x \le y$, and multiply two such functions by summing over all the points $z$ between $x$ and $y$.
This is matrix multiplication in disguise.
For the chain $1 < 2 < \dots < n$ the incidence algebra is the algebra of upper triangular $n \times n$ matrices.
