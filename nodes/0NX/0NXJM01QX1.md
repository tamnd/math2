---
tag: 0NXJM01QX1
kind: definition
name: Euclidean isometry
aliases: [rigid-transformation, euclidean-transformation]
msc: [51F20]
defines: 0J1N3WTKM4
uses: [0XPR1E85W0, 0NPPGHQNXQ, 0JF0TVYGWT]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_plane_isometry
    locator: Formal definition
  - url: https://en.wikipedia.org/wiki/Euclidean_group
    locator: Relation to the affine group
---

## Definition

Let $d$ be the [[Euclidean distance|0NPPGHQNXQ]] on the [[Euclidean space|0XPR1E85W0]] $\mathbb{R}^n$.
A Euclidean isometry of $\mathbb{R}^n$ is a map $f \colon \mathbb{R}^n \to \mathbb{R}^n$ with
$$d(f(p), f(q)) = d(p, q) \quad \text{for all } p, q \in \mathbb{R}^n.$$

## Remarks

Each Euclidean isometry is an [[affine map|0JF0TVYGWT]] $f(x) = A x + b$, with an orthogonal $n \times n$ matrix $A$ and a vector $b \in \mathbb{R}^n$. Thus $f$ is a bijection, and its inverse is also an isometry.
The isometry is direct if $\det A = 1$ and indirect if $\det A = -1$. The direct isometries keep the orientation of figures.
Mathlib's `AffineIsometryEquiv` is an affine bijection that keeps distances, between normed affine spaces.

## Explanations

### L1 human

An isometry moves the plane or the space without stretching, bending or tearing it. Lengths and angles do not change. In the plane, examples are a shift, a turn about a point and a mirror image in a line.
