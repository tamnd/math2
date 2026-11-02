---
tag: 237KR6FRCK
kind: concept
name: Lagrange interpolation
msc: [41A05, 65D05]
specializes: [SS1YMS2NPC]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_polynomial
close_to:
  - system: wikipedia
    id: Lagrange polynomial
    note: This node is a duplicate of node Y7KSGE97GK, which holds the same_as link. The two nodes wait for a merge.
  - system: wikidata
    id: Q861606
    note: This node is a duplicate of node Y7KSGE97GK, which holds the same_as link. The two nodes wait for a merge.
---

## Summary

Lagrange interpolation is an explicit formula for the polynomial of least degree through given points.
It writes the [[interpolation polynomial|SS1YMS2NPC]] as a combination of basis polynomials, each equal to $1$ at one node and $0$ at the others.
The formula works over every field and shows at once that the interpolation polynomial exists.
It is used in numerical analysis, in coding theory and in secret sharing.

## Explanations

### L1 human

Suppose you want a polynomial that takes chosen values at chosen points.
First build, for each point, a polynomial that is $1$ there and $0$ at all other points.
Then multiply each of them by the wanted value and add.
For the points $(0, 1)$, $(1, 3)$ and $(2, 7)$ this gives $x^2 + x + 1$.
The [[definition|QGQTYT6YZR]] gives the formula.
