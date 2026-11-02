---
tag: 30GF7TK8YP
kind: definition
name: Meshfree methods
msc: [65N99, 65M99, 65D15]
defines: FR6RA0XF9P
uses: [T0JZN6WP5X, ZBSXSTQM2J, NH739XXVXK, Y5B0PEBKE8]
sources:
  - url: https://en.wikipedia.org/wiki/Meshfree_methods
---

## Definition

Let $\Omega \subset \R^d$ be a domain and let $X = \set{x_1, \ldots, x_n} \subset \overline{\Omega}$ be a finite set of nodes.
A *meshfree method* for a differential equation on $\Omega$ approximates the solution by
$$u_h(x) = \sum_{i=1}^{n} \varphi_i(x) \, c_i,$$
where the functions $\varphi_i$ and the method satisfy two conditions:

1. each $\varphi_i$ is determined by the node set $X$ and fixed weight or kernel functions alone, with no elements or edges between nodes;
2. the coefficients $c_i$ are found by a [[Galerkin|Y5B0PEBKE8]] condition, by collocation at points of $\Omega$, or by a particle evolution law.

Usually each $\varphi_i$ has compact support, a ball of radius $\rho$ around $x_i$.

## Remarks

Common choices of $\varphi_i$ are [[moving least squares|T0JZN6WP5X]] shape functions and [[radial basis functions|ZBSXSTQM2J]] $\varphi_i(x) = \phi(\abs{x - x_i})$.
Moving least squares shape functions of order $m$ reproduce polynomials of degree at most $m$; since they reproduce constants, they form a [[partition of unity|NH739XXVXK]].
Essential boundary conditions need extra care, because these $\varphi_i$ usually do not satisfy $\varphi_i(x_j) = \delta_{ij}$.

Example: Gaussian radial basis function collocation for $-\Delta u = f$ uses $\varphi_i(x) = e^{-\varepsilon^2 \abs{x - x_i}^2}$ with a shape parameter $\varepsilon > 0$.
These functions depend only on the nodes and on $\varepsilon$, which satisfies clause 1.
The $c_i$ solve $-\Delta u_h(x_j) = f(x_j)$ at interior nodes and the boundary condition at boundary nodes, which is clause 2.

Non-example: the hat functions of linear finite elements on a triangulation are not meshfree.
Each hat function depends on which triangles contain its node, so clause 1 fails.
