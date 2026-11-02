---
tag: KFW9841GQK
kind: definition
name: Spherical function
msc: [43A90, "22E30"]
defines: BKZNC76RC8
uses: [W38ZDXDVYC, VY0HXD3GC4, 0P27W9RW0G]
sources:
  - url: https://en.wikipedia.org/wiki/Zonal_spherical_function
---

## Definition

Let $(G, K)$ be a [[Gelfand pair|W38ZDXDVYC]], and let $dk$ be the [[Haar measure|VY0HXD3GC4]] on $K$ of total mass $1$.
A *spherical function* for $(G, K)$ is a [[continuous function|0P27W9RW0G]] $\varphi \colon G \to \C$ such that:

1. $\varphi(k_1 g k_2) = \varphi(g)$ for all $g \in G$ and $k_1, k_2 \in K$;
2. $\varphi(e) = 1$;
3. $\int_K \varphi(x k y) \, dk = \varphi(x) \varphi(y)$ for all $x, y \in G$.

## Remarks

Example: $G = \R$ and $K = \set{0}$, a Gelfand pair since $\R$ is abelian.
Clause 1 is empty, and clause 3 reads $\varphi(x + y) = \varphi(x)\varphi(y)$.
So the spherical functions are $\varphi(x) = e^{s x}$ with $s \in \C$, and clause 2 holds since $e^0 = 1$.
The positive-definite ones are the unitary characters $e^{i \xi x}$ with $\xi \in \R$.

Non-example: $\varphi(x) = 2 e^{x}$ on $\R$ fails clause 2, and also clause 3, since $\varphi(x + y) \ne \varphi(x)\varphi(y)$.

For $(\mathrm{SO}(3), \mathrm{SO}(2))$, the spherical functions are $g \mapsto P_\ell(\cos \theta(g))$, where $\theta(g)$ is the angle between $g e_3$ and $e_3$.
Here $P_\ell$ is the Legendre polynomial of degree $\ell \ge 0$.

Equivalent form: a continuous $K$-bi-invariant $\varphi \ne 0$ is spherical exactly when $f \mapsto \int_G f(g) \varphi(g^{-1}) \, dg$ is multiplicative on $C_c(K \backslash G / K)$.
If $\pi$ is an irreducible unitary representation with a unit $K$-fixed vector $v$, then $\varphi(g) = \ip{\pi(g) v}{v}$ is a positive-definite spherical function.
