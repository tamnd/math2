---
tag: 6T5GT2RMWB
kind: definition
name: Optical vortex
msc: [78A10, 78A60]
defines: 23MDMTZT5X
uses: [0NQSV2EWDR, 8YGCTX64MT]
sources:
  - url: https://en.wikipedia.org/wiki/Optical_vortex
---

## Definition

Let $U \colon \Omega \to \C$ be a continuous complex scalar field on an open set $\Omega \subseteq \R^2$, the transverse plane of a beam.
Let $p \in \Omega$ be an isolated zero of $U$.
Take a small circle $C$ around $p$ inside $\Omega$ on which $U$ has no zero.
Let $\ell$ be the [[winding number|0NQSV2EWDR]] around $0$ of the closed curve $U \circ C$.
So $2\pi\ell$ is the total change of $\arg U$ along $C$.
The point $p$ is an *optical vortex* if $\ell \ne 0$, and $\ell$ is its *topological charge*.

## Remarks

The integer $\ell$ does not depend on the choice of the small circle, by continuity of the winding number.
A continuous field with a nonzero winding number around $p$ must vanish at $p$, which is why vortices are dark points.
In space, the zeros of a field $U(x, y, z)$ generically form lines, called vortex lines.

Example: $U(x, y) = (x + iy)^\ell e^{-(x^2 + y^2)}$ with $\ell \ge 1$ equals $r^\ell e^{-r^2} e^{i\ell\varphi}$ in polar coordinates.
Its only zero is the origin, and $\arg U = \ell\varphi$ increases by $2\pi\ell$ around it, so the origin is a vortex of charge $\ell$.
The [[Laguerre–Gaussian mode|8YGCTX64MT]] $\mathrm{LG}_{p\ell}$ with $\ell \ne 0$ has a vortex of charge $\ell$ on its axis.

Non-example: $U(x, y) = x^2 + y^2$ vanishes at the origin, but it is real and positive elsewhere.
Its phase is constant, so the winding number is $0$ and the origin is not a vortex.
