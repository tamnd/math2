---
tag: 5RNGRVFBDM
kind: definition
name: Relativistic Euler equations
msc: [76Y05, 35Q75, 83C55]
defines: A1QC5X6E47
uses: [RW0JK9VDZE, 8RA7AMWSAF, BY4QYYS788]
sources:
  - url: https://en.wikipedia.org/wiki/Relativistic_Euler_equations
---

## Definition

Work in Minkowski space $\R^{1+3}$ with coordinates $x^0 = t, x^1, x^2, x^3$, the metric $\eta = \operatorname{diag}(-1, 1, 1, 1)$ and units with $c = 1$.
Indices are raised and lowered with $\eta$, and repeated indices are summed.
A *perfect fluid* is described by its four-velocity $u^\mu$, with $u^\mu u_\mu = -1$ and $u^0 > 0$, and by three scalar fields.
These are its rest-frame energy density $e$, its pressure $p$ and its particle number density $n$.
Its energy–momentum tensor is
$$T^{\mu\nu} = (e + p) \, u^\mu u^\nu + p \, \eta^{\mu\nu}.$$
The *relativistic Euler equations* are
$$\partial_\mu T^{\mu\nu} = 0 \quad (\nu = 0, 1, 2, 3), \qquad \partial_\mu (n u^\mu) = 0,$$
closed by an equation of state that gives $p$ in terms of $e$ and $n$.

## Remarks

This is a system of [[conservation laws|8RA7AMWSAF]]; on a curved spacetime, a [[Lorentzian manifold|BY4QYYS788]], the partial derivatives are replaced by covariant derivatives.
Example: a fluid at rest, $u^\mu = (1, 0, 0, 0)$, with constant $e$, $p$ and $n$, has $T = \operatorname{diag}(e, p, p, p)$ constant, so it solves the equations.
Non-example: a viscous fluid has a shear stress term in $T^{\mu\nu}$ that is not of the perfect fluid form, so its equations are not these.
For an isentropic flow the speed of sound is $c_s = \sqrt{dp/de}$; for radiation, $p = e/3$ and $c_s = 1/\sqrt{3}$.
In the limit of speeds much smaller than $1$ and $p \ll e$, the equations reduce to the compressible [[Euler equations|RW0JK9VDZE]] with mass density proportional to $n$.
