---
tag: 0TWPTQ0AD7
kind: definition
name: Incentre
msc: [51M04]
defines: 0M9MX8YW0A
uses: [0CTNFGYMM2, 01AAYNSBN6, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Incenter
    locator: Definition and construction
  - url: https://en.wikipedia.org/wiki/Incenter
    locator: Cartesian coordinates
---

## Definition

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean plane $\mathbb{R}^2$. For a point $X$ and a line $\ell$, let $d(X, \ell)$ be the [[distance from the point to the line|01AAYNSBN6]].
The incentre of $ABC$ is the unique point $I$ in the interior of the triangle with
$$d(I, BC) = d(I, CA) = d(I, AB).$$
This common distance $r$ is the inradius of $ABC$.

## Remarks

The point $I$ lies on each of the three internal angle bisectors of the triangle. Thus the three bisectors meet in one point.
Let $a = d(B, C)$, $b = d(C, A)$ and $c = d(A, B)$ be the side lengths, with $d$ the [[Euclidean distance|0NPPGHQNXQ]]. Then $I = \dfrac{aA + bB + cC}{a + b + c}$.
Outside the triangle there are three more points at the same distance from the three side lines. They are the excentres.
Mathlib's `Affine.Simplex.incenter` defines the incentre of each simplex in a Euclidean affine space.

## Explanations

### L1 human

The incentre is the point inside a triangle that is equally far from the three sides. You find it as the crossing point of two angle bisectors. For the right triangle with the vertices $(0, 0)$, $(3, 0)$ and $(0, 4)$, the incentre is $(1, 1)$.
