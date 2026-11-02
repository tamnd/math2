---
tag: 8M04CT7CCM
kind: definition
name: Tricomi equation
msc: [35M10, 76H05]
defines: 21DD2334NR
uses: [GC5BDZ6QBC, 7WFKPAMQFG, B4TTNHSTRX, 92C3S03AQZ, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Euler–Tricomi_equation
---

## Definition

The *Tricomi equation* is the [[partial differential equation|GC5BDZ6QBC]]
$$y \, u_{xx} + u_{yy} = 0.$$
The unknown is a real function $u(x, y)$ on an open subset of $\R^2$.
Subscripts denote [[partial derivatives|09EGC6F8PT]].

## Remarks

The equation is [[elliptic|B4TTNHSTRX]] where $y > 0$, [[hyperbolic|92C3S03AQZ]] where $y < 0$, and parabolic on the line $y = 0$, so it is of [[mixed type|7WFKPAMQFG]].
In the half-plane $y < 0$ its characteristic curves are $3x \pm 2(-y)^{3/2} = \text{const}$.
Some authors write it as $u_{xx} = x \, u_{yy}$, which is the same equation after renaming and reflecting the variables.

Example: $u(x, y) = x^2 - \tfrac{1}{3} y^3$ is a solution, because $y \, u_{xx} + u_{yy} = 2y - 2y = 0$.

Non-example: $u(x, y) = x^2 + y^2$ is not a solution, because $y \, u_{xx} + u_{yy} = 2y + 2$ is not identically $0$.
