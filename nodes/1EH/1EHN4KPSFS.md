---
tag: 1EHN4KPSFS
kind: concept
name: Integral element
msc: [13B21]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_element
same_as:
  wikidata: Q1493740
  wikipedia: Integral element
---

## Summary

An element $b$ of a [[commutative ring|0310REJJY8]] $B$ is integral over a subring $A$ if it is a root of a [[monic polynomial|0C3QBCR46M]] over $A$.
It extends to rings the notion of an [[algebraic element|0H628RSGWX]] of a field extension, with the extra demand that the leading coefficient is $1$.
Over $\Z$, the integral elements of $\C$ are the algebraic integers, the basic objects of algebraic number theory.
Integral elements are the starting point of the theory of [[integral extensions|B7X0KFY1S1]], integral closure and normal rings.

## Explanations

### L1 human

An element is integral over $A$ if it satisfies an equation $b^n + a_{n-1} b^{n-1} + \cdots + a_0 = 0$ with all $a_i$ in $A$.
The number $\sqrt{2}$ is integral over $\Z$, since it is a root of $x^2 - 2$.
The golden ratio $(1 + \sqrt{5})/2$ is also integral over $\Z$, since it is a root of $x^2 - x - 1$.
The number $1/2$ is not integral over $\Z$, although it is a root of $2x - 1$: the leading coefficient cannot be made $1$.
Integral elements behave like "integers" inside a larger ring.
