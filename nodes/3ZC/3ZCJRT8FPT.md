---
tag: 3ZCJRT8FPT
kind: definition
name: Hyperkähler manifold
msc: [53C26, 53C29]
defines: 87AWY7NQS0
uses: [7CBT4SM83Y, 9SYWRGVTRS, CAZYGE1T4E, CK1DCPC3D3, WHDZ3MK56B]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperk%C3%A4hler_manifold
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] with [[Levi-Civita connection|CAZYGE1T4E]] $\nabla$.
The manifold $M$ is *hyperkähler* if it carries three [[almost complex structures|9SYWRGVTRS]] $I$, $J$, $K$ such that:

1. $g(IX, IY) = g(JX, JY) = g(KX, KY) = g(X, Y)$ for all tangent vectors $X, Y$;
2. $\nabla I = \nabla J = \nabla K = 0$;
3. $IJ = K$.

## Remarks

From $I^2 = J^2 = -\id$ and $IJ = K$ with $K^2 = -\id$ one gets the quaternion relations $IJ = -JI = K$.
Clauses 1 and 2 say that $(M, g)$ is [[Kähler|CK1DCPC3D3]] for each of $I$, $J$, $K$, and in fact for $aI + bJ + cK$ whenever $a^2 + b^2 + c^2 = 1$.
Equivalently, the [[holonomy|WHDZ3MK56B]] group of $g$ is contained in $Sp(n)$, where $\dim M = 4n$.

Example: $\mathbb{H}^n = \R^{4n}$ with the flat metric and $I, J, K$ given by left multiplication by the quaternions $i, j, k$ on each coordinate.
These maps are orthogonal, have constant coefficients so they are parallel, and satisfy $ij = k$.

Non-example: $\C P^2$ with the Fubini–Study metric is Kähler of real dimension $4$, but it is not hyperkähler.
A hyperkähler metric is Ricci-flat, while the Fubini–Study metric has positive Ricci curvature.
