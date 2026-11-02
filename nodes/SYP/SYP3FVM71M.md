---
tag: SYP3FVM71M
kind: definition
name: Euler characteristic
msc: [55N10, 57N65]
defines: RNDDWDAFJ5
uses: [ST71ZV3FES, M0Q5CFJ7ZH, 5W95QFHXPR, 09HT3P35YP]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_characteristic
---

## Definition

Let $X$ be a topological space whose [[singular homology|M0Q5CFJ7ZH]] groups $H_k(X)$ are finitely generated for all $k$ and zero for all but finitely many $k$.
The *Euler characteristic* of $X$ is
$$\chi(X) = \sum_{k \ge 0} (-1)^k b_k(X),$$
where $b_k(X)$ is the $k$-th [[Betti number|ST71ZV3FES]] of $X$.

## Remarks

If $X$ is a finite [[CW complex|5W95QFHXPR]] with $c_k$ cells of dimension $k$, then $\chi(X) = \sum_k (-1)^k c_k$.
For the boundary of a convex polyhedron this is [[Euler's polyhedron formula|09HT3P35YP]] $V - E + F = 2$.
For any field $F$, $\chi(X) = \sum_k (-1)^k \dim_F H_k(X; F)$ under the same hypothesis.

Example: the torus has $b_0 = 1$, $b_1 = 2$, $b_2 = 1$, so $\chi(T^2) = 1 - 2 + 1 = 0$.
Its usual CW structure has one $0$-cell, two $1$-cells and one $2$-cell, and $1 - 2 + 1 = 0$ again.

Non-example: the wedge of countably many circles has $H_1$ free abelian of infinite rank, so it fails the finiteness hypothesis and has no Euler characteristic in this sense.
