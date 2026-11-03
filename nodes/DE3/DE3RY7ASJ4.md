---
tag: DE3RY7ASJ4
kind: definition
name: Hele-Shaw flow
msc: [76D27, 76S05]
defines: CM1R6CSHAA
uses: [13CB7V2YM4, NM5Q4845Z4, DF0M8YNQ3D, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Hele-Shaw_flow
---

## Definition

Let a fluid of [[viscosity|NM5Q4845Z4]] $\mu > 0$ fill the gap $0 < z < b$ between two parallel plates, over a region $\Omega \subset \R^2$ of the $(x, y)$-plane.
Assume that $b$ is small compared with the lengths over which the flow varies in $\Omega$.
Assume that inertia is negligible, so that the flow is a [[Stokes flow|13CB7V2YM4]], and that the [[no-slip condition|DF0M8YNQ3D]] holds on both plates.
A *Hele-Shaw flow* is the resulting flow in which the pressure $p(x, y)$ does not depend on $z$ and the horizontal velocity is
$$u(x, y, z) = -\frac{z(b - z)}{2\mu}\nabla p(x, y).$$
Its average across the gap, $\bar u = \frac{1}{b}\int_0^b u\,dz$, satisfies
$$\bar u = -\frac{b^2}{12\mu}\nabla p, \qquad \nabla \cdot \bar u = 0 \quad \text{in } \Omega,$$
so $p$ is a [[harmonic function|0DEB0JMN0W]] on $\Omega$.

## Remarks

Example: in the strip $\Omega = \R \times (0, L)$ with $p = -Gx$ and $G > 0$, the gap-averaged velocity is the uniform flow $\bar u = \left(\frac{b^2G}{12\mu}, 0\right)$, and $p$ is harmonic.
Check of the profile: $\mu\,\partial_z^2 u = -\mu \cdot \frac{-2}{2\mu}\nabla p = \nabla p$, which is the horizontal Stokes equation, and $u = 0$ at $z = 0$ and $z = b$.
Non-example: a flow between plates with a gap comparable to the size of the obstacles is not a Hele-Shaw flow.
There the velocity varies in the plane on the scale of $b$, and the profile is not parabolic.
The equations for $\bar u$ are [[Darcy's law|DX8RV2XG6H]] with permeability $b^2/12$.
The averaged velocity has the potential $-\frac{b^2}{12\mu}p$, so the streamlines are those of a two-dimensional potential flow, although the real flow is viscous and has no slip on the plates.
