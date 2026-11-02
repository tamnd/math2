---
tag: SVDH9C5MCK
kind: definition
name: Isomonodromic deformation
msc: [34M56, 34M35]
defines: KDZF7E66BT
uses: [C8HD62AB6Q, ZBVH2YE50B, 037ZNY7NAG, 0H1GN6P9R5]
sources:
  - url: https://en.wikipedia.org/wiki/Isomonodromic_deformation
---

## Definition

Let $m \ge 1$ and let $T \subseteq \C^m$ be a simply connected domain of points $t = (t_1, \ldots, t_m)$ with pairwise distinct coordinates.
For each $t \in T$, consider the [[Fuchsian|ZBVH2YE50B]] [[linear system|037ZNY7NAG]]
$$\frac{dY}{dz} = \sum_{i=1}^{m} \frac{A_i(t)}{z - t_i}\, Y,$$
where $A_1, \ldots, A_m \colon T \to \C^{n \times n}$ are holomorphic.
Fix a base point $z_0$ with $z_0 \ne t_i$ for all $t \in T$ and all $i$.
The family is an *isomonodromic deformation* if it has a [[fundamental matrix|0H1GN6P9R5]] $Y(z, t)$ with the following property.
$Y$ is holomorphic in $(z, t)$ for $z$ near $z_0$ and $t \in T$.
Its [[monodromy|C8HD62AB6Q]] matrices along loops around the points $t_i$, moved continuously with $t$, do not depend on $t$.

## Remarks

The family is isomonodromic if the matrices $A_i$ satisfy the Schlesinger equations
$$\frac{\partial A_i}{\partial t_j} = \frac{[A_i, A_j]}{t_i - t_j} \ (j \ne i), \qquad \frac{\partial A_i}{\partial t_i} = - \sum_{j \ne i} \frac{[A_i, A_j]}{t_i - t_j},$$
where $[A, B] = A B - B A$.
For $2 \times 2$ systems with singular points $0$, $1$, $t$ and $\infty$, these equations reduce to the sixth Painlevé equation in the variable $t$.

Example: if all $A_i$ are constant and commute with each other, the Schlesinger equations hold, since all commutators vanish.
For $n = 1$, the system is $y' = \sum_i \frac{a_i}{z - t_i} y$ with solution $\prod_i (z - t_i)^{a_i}$, and the monodromy around $t_i$ is $e^{2 \pi i a_i}$; it does not depend on $t$ when the $a_i$ are constant.

Non-example: for $n = 1$ and $m = 1$, take $a_1(t) = t_1$ on a domain $T \subseteq \C$; the monodromy $e^{2 \pi i t_1}$ around $t_1$ changes with $t_1$, so the family is not isomonodromic.
