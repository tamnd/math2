---
tag: MXZHMC2P99
kind: definition
name: Perimeter of a set
msc: [49Q15, 28A75, 26B30]
defines: Y68BHXZJBV
uses: [2Z2QVWZ262, 0MWV6ZTK6S]
sources:
  - url: https://en.wikipedia.org/wiki/Caccioppoli_set
---

## Definition

Let $n \ge 1$, let $\Omega \subseteq \R^n$ be an open set, and let $E \subseteq \R^n$ be a [[Lebesgue measurable|2Z2QVWZ262]] set.
Its *perimeter in $\Omega$* is the supremum below.
$$P(E, \Omega) = \sup \set{ \int_E \operatorname{div} \varphi \, dx : \varphi \in C^1_c(\Omega; \R^n), \ \abs{\varphi(x)} \le 1 \text{ for all } x \in \Omega }.$$
Here $\operatorname{div}$ is the [[divergence|0MWV6ZTK6S]].
The set $C^1_c(\Omega; \R^n)$ is the space of continuously differentiable vector fields with compact support in $\Omega$.
The value $P(E, \Omega)$ lies in $[0, \infty]$, and $P(E) = P(E, \R^n)$ is the *perimeter* of $E$.

## Remarks

Example: let $E$ be a bounded open set with $C^1$ boundary and outer unit normal $\nu$.
By the divergence theorem, $\int_E \operatorname{div} \varphi \, dx = \int_{\partial E} \varphi \cdot \nu \, d\mathcal{H}^{n-1} \le \mathcal{H}^{n-1}(\partial E)$.
Extending $\nu$ to a continuous field of norm at most $1$ and smoothing it shows that the supremum equals $\mathcal{H}^{n-1}(\partial E)$, the area of the boundary.
So the unit disc in $\R^2$ has perimeter $2\pi$.

The perimeter is not the size of the topological boundary.
The set $E = \Q^2 \cap [0, 1]^2$ has topological boundary $[0, 1]^2$, of positive area.
But $E$ has Lebesgue measure zero, so every integral above vanishes and $P(E) = 0$.

Equivalently, $P(E, \Omega)$ is the total variation $\abs{D \chi_E}(\Omega)$ of the distributional gradient of the indicator function $\chi_E$.
It is finite exactly when $\chi_E$ has bounded variation in $\Omega$.
Changing $E$ on a set of measure zero does not change $P(E, \Omega)$.
