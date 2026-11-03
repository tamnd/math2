---
tag: R3CDET6AT6
kind: definition
name: Hamiltonian optics
msc: [78A05, 70H05]
defines: T56WHM058J
uses: [0EDKGA2FAK, 9VGK0SP6EQ, AQ5ZKPZ88R]
sources:
  - url: https://en.wikipedia.org/wiki/Hamiltonian_optics
---

## Definition

Let an isotropic medium in $\R^3$ have a $C^1$ [[refractive index|9VGK0SP6EQ]] $n(x, y, z) > 0$.
Consider rays that cross each plane $z = \text{const}$ once, and describe such a ray by its position $(x(z), y(z))$.
Let $s$ be arc length along the ray, and define the optical direction cosines
$$p = n \frac{dx}{ds}, \qquad q = n \frac{dy}{ds}.$$
Take $z$ as time, $(x, y)$ as coordinates and $(p, q)$ as momenta.
*Hamiltonian optics* describes rays as solutions of the [[Hamiltonian system|0EDKGA2FAK]] with Hamiltonian
$$H(x, y, p, q; z) = -\sqrt{n(x, y, z)^2 - p^2 - q^2},$$
that is,
$$\frac{dx}{dz} = \frac{\partial H}{\partial p}, \quad \frac{dy}{dz} = \frac{\partial H}{\partial q}, \quad \frac{dp}{dz} = -\frac{\partial H}{\partial x}, \quad \frac{dq}{dz} = -\frac{\partial H}{\partial y}.$$

## Remarks

The equations are equivalent to the ray equation $\dfrac{d}{ds}\Big(n \dfrac{dr}{ds}\Big) = \nabla n$ for $r = (x, y, z)$.
Check: $\sqrt{n^2 - p^2 - q^2} = n \, dz/ds$, so $\partial H / \partial p = p / (n \, dz/ds) = dx/dz$.
Also $\partial H / \partial x = -(\partial n / \partial x) \, ds/dz$, so $dp/dz = (\partial n/\partial x) \, ds/dz$, that is $dp/ds = \partial n / \partial x$.
The Lagrangian $L = n \sqrt{1 + \dot{x}^2 + \dot{y}^2}$, with $\dot{x} = dx/dz$, gives the [[optical path length|AQ5ZKPZ88R]] $\int L \, dz$, and $H$ is its Legendre transform.

Example: in a homogeneous medium, $n$ is constant, so $H$ does not depend on $(x, y)$ and $p, q$ are constant; the rays are straight lines.

Non-example: a ray that runs parallel to the planes $z = \text{const}$ has $dz/ds = 0$, so $p^2 + q^2 = n^2$ and $H$ is not differentiable there; such rays are outside this description.
