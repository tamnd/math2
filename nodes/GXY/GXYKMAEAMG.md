---
tag: GXYKMAEAMG
kind: object
name: Klein quartic
msc: [14H45, 14H37, 30F10]
instance_of: [5K0N8QMV6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Klein_quartic
---

## Description

The *Klein quartic* is the plane curve
$$X = \set{ [x : y : z] \in \mathbb{P}^2(\C) : x^3 y + y^3 z + z^3 x = 0 }.$$
It is a smooth curve of degree $4$, so it is a compact [[Riemann surface|5K0N8QMV6Q]] of genus $\frac{(4-1)(4-2)}{2} = 3$ by the genus–degree formula.

Two automorphisms can be checked by hand.
Let $\zeta = e^{2\pi i / 7}$.
The map $[x : y : z] \mapsto [\zeta^4 x : \zeta^2 y : \zeta z]$ preserves $X$, because $x^3 y$ is multiplied by $\zeta^{12+2} = 1$, $y^3 z$ by $\zeta^{6+1} = 1$, and $z^3 x$ by $\zeta^{3+4} = 1$.
The cyclic shift $[x : y : z] \mapsto [y : z : x]$ permutes the three monomials, so it also preserves $X$.

The full group of holomorphic automorphisms of $X$ is isomorphic to $\mathrm{PSL}(2, \F_7)$, of order $168$.
This equals the bound $84(g - 1) = 168$ of Hurwitz's automorphisms theorem for $g = 3$.
Up to isomorphism, $X$ is the only compact Riemann surface of genus $3$ with $168$ automorphisms.

## Explanations

### L1 human

The Klein quartic is a surface with three holes that is as symmetric as a surface of its genus can be.
No compact Riemann surface of genus $3$ has more than $168$ symmetries, and this one has exactly $168$.
It can be built by gluing $24$ regular heptagons, with three at each corner, in the hyperbolic plane.
Its equation $x^3 y + y^3 z + z^3 x = 0$ is short, and one can see some symmetries directly: a cyclic shift of the variables, and a scaling by seventh roots of unity.
