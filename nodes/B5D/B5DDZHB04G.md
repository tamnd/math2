---
tag: B5DDZHB04G
kind: concept
name: Period and index
msc: [16K50, 16K20]
sources:
  - url: https://en.wikipedia.org/wiki/Brauer_group
---

## Summary

The period and the index are two numbers attached to a central simple algebra $A$ over a field $K$.
The index is the [[degree|NNXSP5KKAC]] of the division algebra $D$ with $A \cong M_m(D)$.
The period is the order of the class of $A$ in the [[Brauer group|BEW48TA9WZ]].
The period divides the index, and the two numbers have the same prime divisors.
How far apart they can be is the period-index problem, a central question about Brauer groups of fields.

## Explanations

### L1 human

Every central simple algebra is a matrix algebra over a division algebra, and the index measures the size of that division algebra.
The period counts how many copies of the algebra must be tensored together before the result becomes a plain matrix algebra.
For Hamilton's quaternions over $\R$, both numbers are $2$: the quaternions have degree $2$, and $\mathbb{H} \otimes_\R \mathbb{H}$ is a matrix algebra.
Over number fields the two numbers are always equal, but over other fields the index can be larger.
