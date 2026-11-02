---
tag: J1E6BEFAPZ
kind: problem
name: Illumination problem
msc: [52A20, 52C17]
uses: [437FSG3419, 05D5EGMFYV, 0RZH6W98HK, SVP75YY386]
about: [437FSG3419]
sources:
  - url: https://en.wikipedia.org/wiki/Hadwiger_conjecture_(combinatorial_geometry)
history:
  posed_by: "Vladimir Boltyansky"
  first_stated: "1960"
---

## Problem

Let $n \ge 1$, and let $K \subseteq \R^n$ be a [[convex body|437FSG3419]].
A nonzero vector $u$ *illuminates* a [[boundary|05D5EGMFYV]] point $x$ of $K$ if the ray $\set{x + t u : t > 0}$ meets the [[interior|0RZH6W98HK]] of $K$.
The *illumination number* $I(K)$ is the least number of vectors such that every boundary point of $K$ is illuminated by one of them.
Show that $I(K) \le 2^n$, with equality only when $K$ is a parallelotope.

## Remarks

Boltyanski proved that $I(K)$ equals the least number of smaller homothetic copies $x_i + \lambda K$, with $0 < \lambda < 1$, that cover $K$.
So the problem is equivalent to the [[Hadwiger covering conjecture|SVP75YY386]], and it is open for $n \ge 3$.
Example: for a disc, a vector $u$ illuminates the boundary point with outer normal $\nu$ exactly when $u \cdot \nu < 0$.
Three vectors at angles $2\pi/3$ illuminate every boundary point, while two vectors never suffice, so $I = 3$.
For the square, each corner needs its own direction, so $I = 4 = 2^2$.

## Explanations

### L1 human

Imagine a convex solid lit by floodlights placed very far away, each shining in one fixed direction.
A point of the surface counts as lit if the light, coming in, can pass through it into the solid.
How many floodlights are needed to light the whole surface?
A round ball needs few, a cube needs one for each corner, and the conjecture says that no convex body in $n$ dimensions needs more than $2^n$.
