---
tag: ARAGG36S9N
kind: statement
role: theorem
name: Sign rules for integer multiplication and subtraction
msc: [11A99]
uses: [0C4JS9RF5M, 0BXA4Q0JHW]
about: [0C4JS9RF5M]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_background_prop-integers.ptx#L73
    locator: source/s_background_prop-integers.ptx:73
---

## Statement

Let $x$, $y$ and $z$ be any [[integers|0C4JS9RF5M]]. Then three identities hold:

1. $x \cdot (-y) = -(x y)$;
2. $x (y - z) = x y - x z$;
3. $-(x - y) = y - x$.

## Remarks

All three identities follow from the axioms of the [[ring of integers|0BXA4Q0JHW]], in particular the distributive law and the existence of additive inverses.
The first says that the product of $x$ with the opposite of $y$ is the opposite of the product.
The second says that multiplication distributes over subtraction.
The third says that the opposite of a difference is the difference taken in the other order.
