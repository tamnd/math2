---
tag: 87EFGXB17V
kind: definition
name: Constant-mean-curvature surface
msc: [53A10]
defines: RPBKZ7E9VE
uses: [6080X3FAD4, PA78NFEPCF]
sources:
  - url: https://en.wikipedia.org/wiki/Constant-mean-curvature_surface
---

## Definition

Let $S \subset \R^3$ be an orientable [[regular surface|6080X3FAD4]] with a chosen unit normal, and let $H \colon S \to \R$ be its [[mean curvature|PA78NFEPCF]].
The surface $S$ is a *constant-mean-curvature surface* if there is a real number $H_0$ with $H(p) = H_0$ for every $p \in S$.

## Remarks

The sphere of radius $r$ is a CMC surface: for the inward normal both principal curvatures are $1/r$, so $H = 1/r$ everywhere.
The paraboloid $z = x^2 + y^2$ is not: its mean curvature is $2$ at the origin and tends to $0$ far from the origin.

The case $H_0 = 0$ gives the [[minimal surfaces|41X0YW2R9N]].
Changing the normal changes the sign of $H$, so the condition does not depend on the choice of normal.
The same definition applies to immersed surfaces, where self-intersections are allowed.
By a theorem of Alexandrov, a compact embedded CMC surface is a round sphere, but compact immersed CMC tori exist, such as the [[Wente torus|E5NNY7XM44]].

## Explanations

### L1 human

A CMC surface is a surface whose mean curvature is the same number at every point.
