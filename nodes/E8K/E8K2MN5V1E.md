---
tag: E8K2MN5V1E
kind: concept
name: Prime ideal in a noncommutative ring
msc: [16N60, 16D25]
specializes: [0CD87SFM2N]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_ideal
---

## Summary

A prime ideal of a noncommutative ring is a proper two-sided ideal $P$ with the following property.
A product $AB$ of two-sided ideals lies in $P$ only when $A$ or $B$ does.
For commutative rings this is the usual [[prime ideal|00MHHZ9SNE]].
Ideals are used instead of elements because, for $n \ge 2$, the matrix ring $M_n(k)$ over a field has no proper ideal with the element-wise property.
Prime ideals define the [[prime radical|WF117EJ2HF]] and are the kernels of maps onto [[prime rings|Z9TJSZZYG1]].

## Explanations

### L1 human

For integers, a prime $p$ divides $ab$ only if it divides $a$ or $b$.
For ideals of a noncommutative ring, this is asked for products of whole ideals, not of single elements.
In the ring $M_2(\Q)$ the zero ideal is prime, because the only ideals are $0$ and the whole ring.
But it is not prime element-wise, since $e_{11} e_{22} = 0$ with $e_{11} \ne 0$ and $e_{22} \ne 0$.
