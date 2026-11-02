---
tag: F2JX0R86WQ
kind: definition
name: Curve of constant width
msc: [52A10]
defines: B4YD1ZXRVH
uses: [437FSG3419, 1H92CYA4ZC, K7N565NKCV, 05D5EGMFYV]
sources:
  - url: https://en.wikipedia.org/wiki/Curve_of_constant_width
---

## Definition

Let $K \subseteq \R^2$ be a [[convex body|437FSG3419]] with [[support function|1H92CYA4ZC]] $h_K$, and let $w > 0$.
For a unit vector $u$, the *width* of $K$ in the direction $u$ is $w_K(u) = h_K(u) + h_K(-u)$.
It is the distance between the two [[supporting lines|K7N565NKCV]] of $K$ orthogonal to $u$.
The body $K$ has *constant width* $w$ if $w_K(u) = w$ for every unit vector $u$.
A *curve of constant width* $w$ is the [[boundary|05D5EGMFYV]] of a plane convex body of constant width $w$.

## Remarks

Example: the circle of radius $r$ centred at $c$ bounds the disc with $h(u) = c \cdot u + r$, so $w(u) = 2r$ for all $u$, and the circle has constant width $2r$.
Non-example: the square $[0, 1]^2$ has width $1$ in the direction $(1, 0)$ and width $\sqrt{2}$ in the direction $(1, 1)/\sqrt{2}$, so its boundary is not a curve of constant width.
A body of constant width $w$ has diameter $w$.
The same definition in $\R^n$ gives bodies of constant width.
