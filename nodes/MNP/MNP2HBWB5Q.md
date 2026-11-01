---
tag: MNP2HBWB5Q
kind: concept
name: Group algebra
msc: [20C05, 16S34]
specializes: [0B1261B5ED]
sources:
  - url: https://en.wikipedia.org/wiki/Group_ring
---

## Summary

The group algebra $F[G]$ of a [[group|G5S1M9]] $G$ over a field $F$ is the vector space with basis $G$.
It is a [[ring|0B1261B5ED]], with the group multiplication extended linearly.
Its modules are exactly the [[representations|WYGRXCG2RN]] of $G$ over $F$.
So representation theory of groups becomes module theory of a single ring.
Over a commutative ring $R$ in place of $F$, the same construction gives the group ring $R[G]$.

## Explanations

### L1 human

Take formal sums like $2g + 3h - k$ of group elements with coefficients in a field.
Add them term by term, and multiply them by expanding and using the group law, so $(ag)(bh) = ab \, (gh)$.
For the cyclic group $\set{1, t}$ of order $2$, the product $(1 + t)(1 - t)$ equals $1 - t^2 = 1 - 1 = 0$.
This shows the group algebra can have zero divisors even though the field has none.
