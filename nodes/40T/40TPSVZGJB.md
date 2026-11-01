---
tag: 40TPSVZGJB
kind: definition
name: Schwarz–Christoffel mapping
msc: [30C30, 30C20]
defines: 7FTW5Q9GHC
uses: [0VHNKP1N3K, X6XGGH5FPW, 02WHMEG5ZR, AZ6H4ZKK55]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarz%E2%80%93Christoffel_mapping
---

## Definition

Let $P$ be the bounded open region enclosed by a simple polygon with $n \ge 3$ vertices $w_1, \ldots, w_n$, listed in the positive direction.
Let $\pi\alpha_k$ be the interior angle of $P$ at $w_k$, with $0 < \alpha_k < 2$; then $\sum_{k=1}^{n} (\alpha_k - 1) = -2$.
Let $\mathbb{H}$ be the [[upper half-plane|X6XGGH5FPW]].
A *Schwarz–Christoffel mapping* for $P$ is a [[conformal map|0VHNKP1N3K]] $f$ of $\mathbb{H}$ onto $P$.

The *Schwarz–Christoffel formula* gives the form of every such $f$:
$$f(z) = A + C \int_{z_0}^{z} \prod_{k=1}^{n} (\zeta - x_k)^{\alpha_k - 1}\, d\zeta, \qquad z \in \mathbb{H},$$
with real *prevertices* $x_1 < x_2 < \cdots < x_n$, a point $z_0 \in \mathbb{H}$ and constants $A, C \in \C$.
The powers are the branches that are holomorphic on $\mathbb{H}$.
Here $f$ extends continuously to the real axis with $f(x_k) = w_k$.
If one prevertex is placed at $\infty$, its factor is omitted from the product.

## Remarks

Such an $f$ exists by the [[Riemann mapping theorem|02WHMEG5ZR]] composed with a Möbius map from the disc to $\mathbb{H}$, and it extends to the boundary by [[Carathéodory's theorem|AZ6H4ZKK55]].
On each interval $(x_k, x_{k+1})$ the argument of $f'$ is constant, so the interval is mapped onto a straight segment; at $x_k$ the argument jumps by $\pi(1 - \alpha_k)$, the exterior angle.
Three of the prevertices can be chosen freely, because $\mathbb{H}$ has a three-parameter group of conformal automorphisms; the others are determined by $P$ and usually found numerically.
Example: for the right isosceles triangle, one may take prevertices $0, 1, \infty$ with angles $\pi/2, \pi/4, \pi/4$, giving $f(z) = \int_0^z \zeta^{-1/2} (\zeta - 1)^{-3/4}\, d\zeta$ up to the constants.
The same formula, with vertices at infinity allowed, describes maps onto unbounded polygonal regions.
For example, $\arcsin$ maps $\mathbb{H}$ onto the half-strip $\set{w : \abs{\operatorname{Re} w} < \pi/2,\ \operatorname{Im} w > 0}$.
Non-example: a conformal map of $\mathbb{H}$ onto the unit disc is not a Schwarz–Christoffel mapping.
The disc is not bounded by a polygon, and the image of the real axis has no straight pieces.
