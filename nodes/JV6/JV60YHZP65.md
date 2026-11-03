---
tag: JV60YHZP65
kind: definition
name: Alternative algebra
msc: [17D05]
defines: N8K9SSVMRN
uses: [60W3THKGA7, RT4YV20367]
sources:
  - url: https://en.wikipedia.org/wiki/Alternative_algebra
---

## Definition

Let $A$ be a [[nonassociative algebra|60W3THKGA7]] over a commutative ring $R$.
$A$ is *alternative* if for all $x, y \in A$:

1. $x(xy) = (xx)y$ (left alternative law).
2. $(yx)x = y(xx)$ (right alternative law).

## Remarks

In terms of the [[associator|RT4YV20367]], the laws say $(x, x, y) = 0$ and $(y, x, x) = 0$.
Replacing $x$ by $x + z$ gives $(x, z, y) = -(z, x, y)$ and $(y, x, z) = -(y, z, x)$.
So the associator is alternating: it changes sign under any swap of two arguments and vanishes when two arguments are equal.
In particular $(x, y, x) = 0$, so an alternative algebra is [[flexible|R1Z4P70285]].
Example: every associative algebra is alternative, and so are the [[octonions|1HRMT3DSX2]].
Non-example: $\R^3$ with the cross product is not alternative, since $(e_1 \times e_1) \times e_2 = 0$ but $e_1 \times (e_1 \times e_2) = -e_2$.
