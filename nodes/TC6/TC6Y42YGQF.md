---
tag: TC6Y42YGQF
kind: definition
name: Discrete Laplace operator
msc: [39A12, 39A14, 05C50]
defines: ZN30Y1ZDB6
uses: [0EPAT51DXQ, TN6M6DVZRP]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_Laplace_operator
---

## Definition

Let $d \ge 1$ and let $e_1, \dots, e_d$ be the standard unit vectors of $\Z^d$.
The *discrete Laplace operator* sends a [[function|0EPAT51DXQ]] $u \colon \Z^d \to \R$ to the function $\Delta u \colon \Z^d \to \R$ given by
$$(\Delta u)(m) = \sum_{i=1}^{d} \big( u(m + e_i) - 2u(m) + u(m - e_i) \big) = \sum_{\abs{m' - m} = 1} \big( u(m') - u(m) \big).$$
More generally, let a graph have vertex set $V$, and let every vertex have finitely many neighbours.
Then the operator sends $u \colon V \to \R$ to
$$(\Delta u)(v) = \sum_{w \sim v} \big( u(w) - u(v) \big), \qquad v \in V,$$
where $w \sim v$ means that $w$ and $v$ are joined by an edge.

## Remarks

Example: on $\Z^2$, the function $u(m, n) = m^2 + n^2$ has $(\Delta u)(m, n) = 2 + 2 = 4$ everywhere, matching $\Delta(x^2 + y^2) = 4$ in the plane.
The function $u(m, n) = mn$ has $\Delta u = 0$, so it is *discrete harmonic*.

Non-example of a discrete harmonic function: $u(m) = 2^m$ on $\Z$ has $(\Delta u)(m) = 2^{m+1} - 2^{m+1} + 2^{m-1} = 2^{m-1} \ne 0$.

On a grid of mesh $h > 0$ one uses $h^{-2} \Delta$, which tends to the Laplacian of $u$ as $h \to 0$ when $u$ is a smooth function sampled on the grid.
On a finite graph with [[Laplacian matrix|TN6M6DVZRP]] $L = D - A$, one has $\Delta u = -L u$ when $u$ is written as a column vector.
Some authors use the opposite sign or divide by the degree.
