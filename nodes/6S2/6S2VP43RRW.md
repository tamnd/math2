---
tag: 6S2VP43RRW
kind: definition
name: Slip-line field theory
msc: [74C05, 74G05]
defines: PSBT777WYE
uses: [K8BBMTN0KV, KG2XWEMJ30, V82XMG8WPE, 92C3S03AQZ]
sources:
  - url: https://en.wikipedia.org/wiki/Slip_line_field
---

## Definition

Consider a plane strain deformation in the $(x, y)$-plane of a rigid–perfectly plastic isotropic material with shear yield stress $k > 0$.
In the plastic region the in-plane [[Cauchy stress|KG2XWEMJ30]] components satisfy the yield condition below.
$$\frac{(\sigma_{xx} - \sigma_{yy})^2}{4} + \sigma_{xy}^2 = k^2$$
It is the plane strain form of the [[von Mises|V82XMG8WPE]] and Tresca criteria.
Then there are a function $p$, the hydrostatic pressure, and an angle $\phi$ with
$$\sigma_{xx} = -p - k \sin 2\phi, \quad \sigma_{yy} = -p + k \sin 2\phi, \quad \sigma_{xy} = k \cos 2\phi.$$
The *$\alpha$-lines* are the curves whose tangent makes the angle $\phi$ with the $x$-axis, and the *$\beta$-lines* are their orthogonal trajectories.
These two orthogonal families of curves are the directions of maximum shear stress, and together they form the *slip-line field*.
*Slip-line field theory* is the solution of plane strain plasticity problems by constructing this field.
It uses that the slip lines are the characteristics of the [[hyperbolic|92C3S03AQZ]] system formed by equilibrium and the yield condition.

## Remarks

Example: in a uniform state with $p = p_0$ and $\phi = \pi/4$, the stress is $\sigma_{xx} = -p_0 - k$, $\sigma_{yy} = -p_0 + k$, $\sigma_{xy} = 0$.
It satisfies the yield condition, since $(\sigma_{xx} - \sigma_{yy})^2/4 = k^2$, and the slip lines are the two families of straight lines at $45^\circ$ to the axes.
Non-example: the stress $\sigma_{xx} = \sigma_{yy} = -p_0$, $\sigma_{xy} = 0$ violates the yield condition, because the left side is $0 < k^2$; such a region is rigid and carries no slip-line field.
Along slip lines, equilibrium reduces to the Hencky equations: $p + 2k\phi$ is constant along each $\alpha$-line and $p - 2k\phi$ is constant along each $\beta$-line (with the sign conventions above).
