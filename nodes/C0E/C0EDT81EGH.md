---
tag: C0EDT81EGH
kind: concept
name: Polynomial identity ring
msc: [16R10, 16R20]
specializes: [0B1261B5ED]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_identity_ring
same_as:
  wikidata: Q7226641
  wikipedia: Polynomial identity ring
---

## Summary

A polynomial identity ring, or PI ring, is a [[ring|0B1261B5ED]] in which some nonzero noncommutative polynomial vanishes for all choices of elements.
Commutative rings are PI rings, because $xy - yx$ vanishes on them, and so are matrix rings over commutative rings by the [[Amitsur–Levitzki theorem|YDH60KPTWT]].
PI rings form the class of noncommutative rings that are closest to commutative rings, and many results of commutative algebra extend to them.
Their theory is built on [[free algebras|2P3Y2FRCSZ]], [[central polynomials|667YZTHE96]] and [[generic matrices|GJGEVMZ828]].

## Explanations

### L1 human

In a commutative ring the rule $xy = yx$ holds for all elements.
A PI ring is a ring where some other, more complicated rule of this kind holds for all elements.
For $2 \times 2$ matrices, $xy$ and $yx$ differ, but the rule $(xy - yx)^2 z = z (xy - yx)^2$ always holds.
Such a rule is called a polynomial identity, and its presence forces the ring to behave much like a commutative ring or a ring of matrices.
