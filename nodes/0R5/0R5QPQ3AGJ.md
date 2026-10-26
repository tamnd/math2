---
tag: 0R5QPQ3AGJ
kind: definition
name: Translation
msc: [51F20]
defines: 087VJM5Q77
uses: [0QN3D80AWP, 0J1N3WTKM4]
sources:
  - url: https://en.wikipedia.org/wiki/Translation_(geometry)
    locator: As a function
  - url: https://en.wikipedia.org/wiki/Translation_(geometry)
    locator: As a group
---

## Definition

Let $v$ be a [[vector|0QN3D80AWP]] of $\mathbb{R}^n$. The translation by $v$ is the map
$$T_v \colon \mathbb{R}^n \to \mathbb{R}^n, \qquad T_v(p) = p + v.$$

## Remarks

Each translation is a [[Euclidean isometry|0J1N3WTKM4]], and it is direct. For $v \neq 0$, it has no fixed point.
$T_v \circ T_w = T_{v + w}$ and $T_v^{-1} = T_{-v}$. So the translations form an abelian group, isomorphic to $\mathbb{R}^n$.
In the plane, the composite of the reflections in two parallel lines is a translation.
Mathlib's `AffineEquiv.constVAdd` is the translation by a vector in an affine space.

## Explanations

### L1 human

A translation slides every point by the same arrow. Shapes keep their size, their form and their direction. The translation by $(2, 1)$ sends the point $(0, 0)$ to $(2, 1)$ and the point $(3, -1)$ to $(5, 0)$.
