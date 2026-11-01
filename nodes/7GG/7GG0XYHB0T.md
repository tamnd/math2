---
tag: 7GG0XYHB0T
kind: problem
name: Serre's problem on projective modules
msc: [13C10, 19A13]
uses: [0SDC934R52, BFFA03GE3V, 05QY1VEBYD, 0DZ9DKAKZR]
about: [BFFA03GE3V, 0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Quillen%E2%80%93Suslin_theorem
history:
  posed_by: "Jean-Pierre Serre"
  first_stated: "1955"
---

## Problem

Let $k$ be a field, let $n \ge 1$, and let $R = k[x_1, \ldots, x_n]$ be the [[polynomial ring|0SDC934R52]] in $n$ variables over $k$.
Is every [[finitely generated|05QY1VEBYD]] [[projective|BFFA03GE3V]] $R$-module [[free|0DZ9DKAKZR]]?

## Remarks

The problem is solved: the answer is yes, by the [[Quillen–Suslin theorem|7N50GA46W1]].
For $n = 1$, the ring $k[x]$ is a principal ideal domain, so the answer is yes by the structure theorem for modules over such rings.
Serre showed that every finitely generated projective $R$-module $P$ is stably free: $P \oplus R^m$ is free for some $m \ge 0$.

## History

Jean-Pierre Serre raised the question in his 1955 paper on coherent algebraic sheaves.
C. S. Seshadri proved the case $n = 2$ in 1958.
Daniel Quillen and Andrei Suslin solved the general case independently in 1976.

## Explanations

### L1 human

Serre asked whether every vector bundle on affine space is trivial, in the language of algebra.
The question is easy to state: does every finitely generated projective module over a polynomial ring have a basis?
It was known to be true for one and two variables, but the general case stayed open for about twenty years.
Quillen and Suslin both proved that the answer is yes, in 1976.
