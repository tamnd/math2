---
tag: 0VHNKP1N3K
kind: definition
name: Conformal map
msc: [30C35]
defines: 0YYT36R4YD
uses: [0CTE7A31XQ]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_map
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Conformal_map
    locator: In two dimensions
---

## Definition

Let $U$ be an open subset of the [[complex plane|0CTE7A31XQ]], identified with $\mathbb{R}^2$, and let $z_0 \in U$.
Let $f : U \to \mathbb{C}$ be differentiable at $z_0$ as a map from an open subset of $\mathbb{R}^2$ to $\mathbb{R}^2$, with Jacobian matrix $J$ at $z_0$.
The map $f$ is conformal at $z_0$ if $J = \lambda Q$ for a real number $\lambda > 0$ and a rotation matrix $Q$, that is, an orthogonal $2 \times 2$ matrix with determinant $1$.
The map $f$ is conformal on $U$ if it is conformal at each point of $U$.

## Remarks

Equivalently, $f$ is conformal at $z_0$ when its real derivative at $z_0$ is the map $h \mapsto a h$ for a complex number $a \neq 0$.
A map that is conformal at $z_0$ preserves the angles between curves through $z_0$, and their orientation.
Some authors also allow orientation-reversing maps, such as $z \mapsto \bar{z}$, whose Jacobian is a positive number times an orthogonal matrix.
Other authors use "conformal map" for an injective holomorphic map on an open set.

## Explanations

### L1 human

A conformal map can stretch and turn a small figure, but it does not distort its shape.
If two curves cross at an angle of $30$ degrees, then their images cross at the same angle, in the same direction.
For example, $z \mapsto 2z$ and $z \mapsto iz$ are conformal at each point.
