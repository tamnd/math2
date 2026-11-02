---
tag: VF17XWCK8Z
kind: definition
name: Isogeometric analysis
msc: [65N30, 65D07, 74S22]
defines: AQ4CNCXAJ0
uses: [Y8B2N9ERPE, 62AFX32JGT, Y5B0PEBKE8, 98GZ9DVHTA]
sources:
  - url: https://en.wikipedia.org/wiki/Isogeometric_analysis
---

## Definition

Let $\hat\Omega = (0, 1)^d$ be the parameter domain.
Let $R_1, \ldots, R_n \colon \hat\Omega \to \R$ be [[NURBS|Y8B2N9ERPE]] basis functions, built from [[B-splines|62AFX32JGT]] on given knot vectors with positive weights.
Let $P_1, \ldots, P_n \in \R^d$ be control points.
Assume the geometry map $\mathbf{F}(\xi) = \sum_{i=1}^{n} R_i(\xi) P_i$ is a bijection from $\hat\Omega$ onto the physical domain $\Omega$, with a smooth inverse.
*Isogeometric analysis* is the [[Galerkin method|Y5B0PEBKE8]] for a boundary value problem on $\Omega$ with the discrete space
$$V_h = \operatorname{span} \set{ R_i \circ \mathbf{F}^{-1} : 1 \le i \le n }.$$
Refinement is done by knot insertion and degree elevation, which leave $\mathbf{F}$ unchanged.

## Remarks

The same functions $R_i$ define the geometry and the solution, as in isoparametric [[finite elements|98GZ9DVHTA]], hence the name.
With $p$ the spline degree and knots of multiplicity one, the basis functions are $C^{p-1}$ across knots.

Example: the quarter circle $\set{(x, y) : x^2 + y^2 = 1, \ x, y \ge 0}$ is the quadratic NURBS curve with control points $(1, 0)$, $(1, 1)$, $(0, 1)$ and weights $1$, $\tfrac{\sqrt{2}}{2}$, $1$.
A quarter annulus is then given exactly by a geometry map that is quadratic in the angular parameter and linear in the radial one.

Non-example: a standard finite element method on a mesh of straight-sided triangles approximates the annulus by a polygon.
Its geometry is not given by the solution basis of a NURBS map from $\hat\Omega$, so it is not isogeometric.
