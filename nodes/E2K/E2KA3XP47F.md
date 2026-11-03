---
tag: E2KA3XP47F
kind: concept
name: Lambda-ring
msc: ["19L20", "13D15", "19E08"]
specializes: [0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Λ-ring
same_as:
  wikidata: Q8083988
  wikipedia: Λ-ring
---

## Summary

A lambda-ring is a [[commutative ring|0310REJJY8]] with extra operations $\lambda^n$ that behave like exterior powers of vector spaces.
Grothendieck introduced them to organise the structure of the K-group of vector bundles, where $\lambda^n[E] = [\Lambda^n E]$.
Lambda-rings carry the [[Adams operations|KQP64TH307]] and the [[gamma filtration|EW5PMAGN8F]].
They appear in K-theory, in representation theory and in the theory of symmetric functions.

## Explanations

### L1 human

From a vector space $V$ one can build its exterior powers $\Lambda^0 V, \Lambda^1 V, \Lambda^2 V, \ldots$.
Their dimensions follow fixed rules: for example $\Lambda^n (V \oplus W)$ splits into pieces $\Lambda^i V \otimes \Lambda^{n-i} W$.
A lambda-ring is any commutative ring with operations $\lambda^n$ that obey the same rules.
The simplest example is $\Z$ with $\lambda^n(k) = \binom{k}{n}$, the dimension of the $n$-th exterior power of a $k$-dimensional space.
