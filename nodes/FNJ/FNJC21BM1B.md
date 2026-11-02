---
tag: FNJC21BM1B
kind: definition
name: Self-distributive operation
msc: [20N02, 08A62]
defines: VEFE5WZMS3
uses: [0SJ3RX9TXA, 0M418FE7BB, 63JGSKKF7J]
sources:
  - url: https://en.wikipedia.org/wiki/Distributive_property
---

## Definition

Let $X$ be a [[set|0SJ3RX9TXA]] and let $*$ be a [[binary operation|0M418FE7BB]] on $X$.
The operation $*$ is *left self-distributive* if
$$x * (y * z) = (x * y) * (x * z) \quad \text{for all } x, y, z \in X.$$
It is *right self-distributive* if
$$(y * z) * x = (y * x) * (z * x) \quad \text{for all } x, y, z \in X.$$
It is *self-distributive* if it is left or right self-distributive, as fixed by the context, and in other texts if it is both.

## Remarks

Left self-distributivity says that $*$ has the [[distributive property|63JGSKKF7J]] over itself from the left.
Equivalently, each left translation $L_x \colon y \mapsto x * y$ is an endomorphism of $(X, *)$.

Example: on $\Z$ let $x * y = 2x - y$.
Then $x * (y * z) = 2x - (2y - z) = 2x - 2y + z$ and $(x * y) * (x * z) = 2(2x - y) - (2x - z) = 2x - 2y + z$, so $*$ is left self-distributive.

Example: in a group, $x * y = x y x^{-1}$ is left self-distributive, since both sides equal $x y z y^{-1} x^{-1}$.

Non-example: addition on $\Z$.
Here $x + (y + z) = x + y + z$ while $(x + y) + (x + z) = 2x + y + z$, which differ when $x \ne 0$.
