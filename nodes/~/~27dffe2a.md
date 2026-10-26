---
tag: ~27dffe2a
kind: definition
name: Reflection in a line or plane
aliases: [reflection, mirror-isometry]
msc: [51F15]
defines: ~a69c90b5
uses: [~44bd4f3a, ~e430bb1b, ~fea4f31a]
sources:
  - url: https://en.wikipedia.org/wiki/Reflection_(mathematics)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Reflection_(mathematics)
    locator: Reflection across a line in the plane
  - url: https://en.wikipedia.org/wiki/Reflection_(mathematics)
    locator: Properties
---

## Definition

Let $a \in \mathbb{R}^n$ be a nonzero vector and $c$ a real number, and let $\cdot$ be the dot product. Let $H = \{\, x \in \mathbb{R}^n : x \cdot a = c \,\}$ be the hyperplane with the [[normal vector|~44bd4f3a]] $a$.
The reflection in $H$ is the map
$$\sigma_H \colon \mathbb{R}^n \to \mathbb{R}^n, \qquad \sigma_H(x) = x - 2\, \frac{x \cdot a - c}{a \cdot a}\, a.$$
For $n = 2$, $H$ is a line; for $n = 3$, $H$ is a plane.

## Remarks

The map $\sigma_H$ is an indirect [[Euclidean isometry|~e430bb1b]]. Its fixed points are the points of $H$, and $\sigma_H \circ \sigma_H$ is the identity.
For $x \notin H$, the hyperplane $H$ is the [[perpendicular bisector|~fea4f31a]] of $x$ and $\sigma_H(x)$.
The linear part of $\sigma_H$ is an orthogonal matrix with determinant $-1$ and the eigenvalues $-1, 1, \dots, 1$.
Reflections in hyperplanes generate the Euclidean group.

## Explanations

### L1 human

A reflection is a mirror image. Each point goes to the point on the other side of the mirror, at the same distance from it. The reflection in the line $y = x$ in the plane sends $(x, y)$ to $(y, x)$.
