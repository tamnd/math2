---
tag: JB02WZSDDW
kind: definition
name: Hilbert dimension
msc: [46C05]
defines: 40SV748R64
uses: [HM2HHE3J51, 0RW9TNNT87, 0G0ASKNA6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_space
---

## Definition

Let $H$ be a real or complex [[Hilbert space|HM2HHE3J51]].
An *orthonormal basis* of $H$ is an [[orthonormal family|0RW9TNNT87]] $(e_i)_{i \in I}$ in $H$ that is maximal: no nonzero vector of $H$ is orthogonal to all $e_i$.
All orthonormal bases of $H$ have the same [[cardinality|0G0ASKNA6Z]].
The *Hilbert dimension* of $H$ is this cardinality $\abs{I}$.

## Remarks

Example: in $\ell^2$, the unit vectors $e_n$, $n \ge 1$, form an orthonormal basis.
They are orthonormal, and if $\ip{x}{e_n} = x_n = 0$ for all $n$ then $x = 0$.
So the Hilbert dimension of $\ell^2$ is $\aleph_0$, the cardinality of $\N$.

Non-example: the family $(e_n)_{n \ge 2}$ in $\ell^2$ is orthonormal but not maximal, since $e_1$ is orthogonal to all of it.
So it is not an orthonormal basis, though its cardinality is also $\aleph_0$.

For every orthonormal basis, each $x \in H$ is the sum $x = \sum_{i \in I} \ip{x}{e_i} e_i$, with only countably many nonzero terms.
For finite-dimensional $H$, the Hilbert dimension is the usual dimension.
For $H = L^2([0, 2\pi])$, the functions $e^{inx} / \sqrt{2\pi}$, $n \in \Z$, form an orthonormal basis, so $L^2([0, 2\pi])$ and $\ell^2$ are isometrically isomorphic.
