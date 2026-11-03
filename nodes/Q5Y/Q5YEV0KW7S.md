---
tag: Q5YEV0KW7S
kind: definition
name: Fermi–Walker transport
msc: [83C10, 53B30, 53C50]
defines: NX9NYGFTRV
uses: [63ZKC7AFX2, 5FZDQQHQKM, YG74WHC3S9, J0D8VKDCK2, TVAGN3D6W5]
sources:
  - url: https://en.wikipedia.org/wiki/Fermi–Walker_transport
---

## Definition

Let $(M, g)$ be a [[spacetime|63ZKC7AFX2]] of signature $(-, +, +, +)$ with Levi-Civita connection $\nabla$, in units where $c = 1$.
Let $\gamma$ be a timelike curve parametrised by [[proper time|YG74WHC3S9]] $\tau$, with unit tangent $u = \dot\gamma$ and [[four-acceleration|J0D8VKDCK2]] $a = \nabla_u u$.
For a vector field $X$ along $\gamma$, its *Fermi–Walker derivative* is
$$\frac{D_F X}{d\tau} = \nabla_u X + g(u, X) \, a - g(a, X) \, u,$$
where $\nabla_u X$ is the [[covariant derivative|5FZDQQHQKM]] of $X$ along $\gamma$.
The field $X$ is *Fermi–Walker transported* along $\gamma$ if $D_F X / d\tau = 0$.

## Remarks

The tangent field is always Fermi–Walker transported: since $g(u, u) = -1$ and $g(a, u) = 0$, one gets $\nabla_u u + g(u, u) a - g(a, u) u = a - a - 0 = 0$.
For a given vector at $\gamma(\tau_0)$, the linear equation $D_F X/d\tau = 0$ has a unique solution along $\gamma$, and Fermi–Walker transport preserves the inner products $g(X, Y)$.
So an orthonormal frame with $e_0 = u$ at one point stays orthonormal with $e_0 = u$ along the curve.
If $\gamma$ is a geodesic, then $a = 0$ and Fermi–Walker transport is [[parallel transport|TVAGN3D6W5]].
Non-example: on an accelerated curve, $u$ itself is not parallel transported, since $\nabla_u u = a \ne 0$.
In Minkowski space, for a particle in uniform circular motion, a Fermi–Walker transported spatial vector rotates relative to the axes of the inertial frame, which is Thomas precession.
