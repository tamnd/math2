---
tag: V365PW1HNE
kind: definition
name: Caccioppoli set
msc: [49Q15, 28A75, 26B30]
defines: W6R7QNEAF1
uses: [Y68BHXZJBV, 2Z2QVWZ262, 9YQ999QHHT, HZNEQQBCW4]
sources:
  - url: https://en.wikipedia.org/wiki/Caccioppoli_set
---

## Definition

Let $n \ge 1$ and let $\Omega \subseteq \R^n$ be an open set.
A [[Lebesgue measurable|2Z2QVWZ262]] set $E \subseteq \R^n$ is a *Caccioppoli set*, or a *set of finite perimeter*, in $\Omega$ if its [[perimeter|Y68BHXZJBV]] $P(E, \Omega)$ is finite.
The set $E$ has *locally finite perimeter* in $\Omega$ if $P(E, U) < \infty$ for every open set $U$ whose closure is a compact subset of $\Omega$.

## Remarks

Example: the unit ball $B \subseteq \R^n$ is a Caccioppoli set in $\R^n$.
Its boundary is smooth, so $P(B) = \mathcal{H}^{n-1}(\partial B)$, the area of the unit sphere, which is finite.

Non-example: the half-space $H = \set{x \in \R^n : x_n > 0}$ with $n \ge 2$ has $P(H) = \infty$, since its boundary is a whole hyperplane.
It still has locally finite perimeter, since $P(H, U)$ is the area of the part of the hyperplane inside $U$.

Equivalently, $E$ has finite perimeter in $\Omega$ exactly when the indicator function $\chi_E$ is a function of [[bounded variation|9YQ999QHHT]] in $\Omega$.
Then the distributional gradient $D \chi_E$ is a vector-valued [[Radon measure|HZNEQQBCW4]], and $P(E, \Omega) = \abs{D\chi_E}(\Omega)$.
