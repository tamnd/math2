---
tag: G3A4S7CSB3
kind: concept
name: Lax pair
msc: [37K10, 35Q53, 37K15]
specializes: []
sources:
  - url: https://en.wikipedia.org/wiki/Lax_pair
same_as:
  wikidata: Q4115796
  wikipedia: Lax pair
---

## Summary

A Lax pair is a pair of operators $L(t)$ and $P(t)$ such that an evolution equation is equivalent to $\frac{dL}{dt} = [P, L] = PL - LP$.
Then $L(t)$ stays similar to $L(0)$, so its spectrum does not change in time.
The eigenvalues of $L$ are thus conserved quantities.
Lax pairs are the starting point of the [[inverse scattering transform|6GY3X4Y8X5]] and a sign that an equation is integrable.

## Explanations

### L1 human

Imagine a matrix that changes in time but whose eigenvalues never move.
A Lax pair writes an equation in exactly this form: the unknown is hidden in the operator $L$, and the equation says $L$ only rotates.
For the [[Korteweg–De Vries equation|KTT75QC72Z]], $L$ is the operator $-\partial_x^2 + u$, and the KdV evolution keeps its eigenvalues fixed.
This gives infinitely many conserved quantities and explains why [[solitons|63D4AXYCT4]] keep their speeds after they collide.
