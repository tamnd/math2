---
tag: D1SA8CHJV0
kind: concept
name: Noncommutative ring
msc: [16B99]
specializes: [0B1261B5ED]
sources:
  - url: https://en.wikipedia.org/wiki/Noncommutative_ring
same_as:
  wikidata: Q7049224
  wikipedia: Noncommutative ring
---

## Summary

A noncommutative ring is a [[ring|0B1261B5ED]] in which the order of the factors in a product can matter.
Matrix rings, quaternions, endomorphism rings and group rings of nonabelian groups are the main sources of examples.
Many tools of commutative algebra split into left and right versions in this setting.
The study of these rings is the subject of noncommutative ring theory.

## Explanations

### L1 human

In ordinary arithmetic $ab = ba$, but many natural products do not behave this way.
Doing one rotation of space and then another is in general not the same as doing them in the other order.
Square matrices model this: with
$$A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix},$$
one gets $AB = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $BA = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.
So the ring of $2 \times 2$ real matrices is a noncommutative ring.
