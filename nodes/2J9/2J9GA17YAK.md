---
tag: 2J9GA17YAK
kind: definition
name: Harmonic functions on Riemannian manifolds
msc: [31C12, 58J05]
defines: PK2KNMWNW3
uses: [7CBT4SM83Y, F4NWZNTRMD, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace%E2%80%93Beltrami_operator
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] and let $U \subseteq M$ be an open set.
In local coordinates $x^1, \dots, x^n$, write $g_{ij}$ for the metric, $g^{ij}$ for its inverse matrix and $\abs{g} = \det(g_{ij})$.
The [[Laplace–Beltrami operator|F4NWZNTRMD]] of a function $u \in C^2(U)$ is
$$\Delta_g u = \frac{1}{\sqrt{\abs{g}}}\, \partial_i \Big( \sqrt{\abs{g}}\, g^{ij}\, \partial_j u \Big),$$
with summation over repeated indices; it equals $\operatorname{div}_g \operatorname{grad}_g u$ and does not depend on the coordinates.
A function $u \in C^2(U)$ is *harmonic* on $U$ if $\Delta_g u = 0$ on $U$.

## Remarks

For $M = \R^n$ with the Euclidean metric, $\Delta_g$ is the usual Laplacian, and the definition gives the classical [[harmonic functions|0DEB0JMN0W]].
Example: on the upper half-plane $\set{(x, y) : y > 0}$ with the hyperbolic metric $g = y^{-2}(dx^2 + dy^2)$, one has $\Delta_g = y^2(\partial_x^2 + \partial_y^2)$.
So the function $u(x, y) = x$ is harmonic, and so is the bounded function $\arctan(x/y)$.
Non-example: on the unit sphere $S^2 \subset \R^3$ with the round metric, the height function $z$ satisfies $\Delta_g z = -2z$, so it is not harmonic.
On a connected closed manifold every harmonic function is constant, since $\int_M \abs{\nabla u}^2 \, dV_g = -\int_M u\, \Delta_g u \, dV_g = 0$.
The definition depends on the metric: a function harmonic for one metric need not be harmonic for another.
In dimension $2$, however, harmonicity is unchanged under conformal changes of metric.
