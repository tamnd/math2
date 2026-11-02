---
tag: F3DXBJZAME
kind: definition
name: Lamé equations of elasticity
msc: [74B05, 35Q74]
defines: GQ3K59MRJP
uses: [GC5BDZ6QBC, 0299VCW1TH, 0E0B6RA8K0, 0ABK9V9Y64, 0MWV6ZTK6S]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_elasticity
---

## Definition

Let $\Omega \subseteq \R^3$ be an open set, and let $\lambda, \mu$ be real constants, the Lamé parameters, with $\mu > 0$ and $3\lambda + 2\mu > 0$.
Let $f \colon \Omega \to \R^3$ be a given body force.
The *Lamé equations* of static linear elasticity are the system
$$\mu \Delta u + (\lambda + \mu) \nabla (\nabla \cdot u) + f = 0 \quad \text{in } \Omega$$
for an unknown [[vector field|0299VCW1TH]] $u \colon \Omega \to \R^3$, the displacement.
Here $\Delta$ is the [[Laplacian|0E0B6RA8K0]] acting on each component, $\nabla \cdot u$ is the [[divergence|0MWV6ZTK6S]] and $\nabla$ is the [[gradient|0ABK9V9Y64]].
For a body of constant density $\rho > 0$, the *dynamic Lamé equations* are $\rho \, \partial_t^2 u = \mu \Delta u + (\lambda + \mu) \nabla (\nabla \cdot u) + f$.

## Remarks

The conditions $\mu > 0$ and $3\lambda + 2\mu > 0$ make the elastic energy positive definite on symmetric strains.
They imply $\lambda + 2\mu > 0$, so the system is strongly elliptic.

Example: for $a, b \in \R^3$ and $f = 0$, the rigid displacement $u(x) = a + b \times x$ is a solution.
Each component of $u$ is affine, so $\Delta u = 0$, and $\nabla \cdot u = 0$.

Non-example: for $f = 0$, $u(x) = (x_1^2, 0, 0)$ is not a solution.
Here $\Delta u = (2, 0, 0)$ and $\nabla(\nabla \cdot u) = (2, 0, 0)$, so the left side is $(2(\lambda + 2\mu), 0, 0) \ne 0$.

The equations come from the balance of forces $\nabla \cdot \sigma + f = 0$ with Hooke's law $\sigma = \lambda (\nabla \cdot u) I + \mu (\nabla u + \nabla u^T)$ for the stress $\sigma$.
In the dynamic equations, pressure waves travel at speed $\sqrt{(\lambda + 2\mu)/\rho}$ and shear waves at speed $\sqrt{\mu / \rho}$.
