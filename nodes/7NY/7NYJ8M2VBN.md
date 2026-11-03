---
tag: 7NYJ8M2VBN
kind: definition
name: Prandtl stress function
msc: [74B05, 74K10]
defines: Z2CC465YXA
uses: [HWW08Q7372, J2GWW1NPTC]
sources:
  - url: https://en.wikipedia.org/wiki/Stress_functions
---

## Definition

Consider the [[torsion of a prismatic bar|HWW08Q7372]] with simply connected cross-section $\Omega \subset \R^2$.
Let $G$ be the [[shear modulus|J2GWW1NPTC]] and $\theta$ the twist per unit length.
The only nonzero stresses are the shear stresses $\sigma_{xz}$ and $\sigma_{yz}$, which are functions of $(x, y)$.
A *Prandtl stress function* is a function $\phi \colon \overline{\Omega} \to \R$ such that
$$\sigma_{xz} = \frac{\partial \phi}{\partial y}, \qquad \sigma_{yz} = -\frac{\partial \phi}{\partial x}.$$
For the torsion solution it satisfies
$$\Delta \phi = -2 G \theta \text{ in } \Omega, \qquad \phi = 0 \text{ on } \partial \Omega,$$
and the torque is $T = 2 \int_\Omega \phi \, dA$.

## Remarks

The equilibrium equation $\partial_x \sigma_{xz} + \partial_y \sigma_{yz} = 0$ holds automatically for any smooth $\phi$.
The Poisson equation comes from compatibility, and the boundary condition from the traction-free lateral surface, which makes $\phi$ constant on $\partial \Omega$.
Example: for a disc of radius $a$, $\phi = \frac{G\theta}{2}(a^2 - x^2 - y^2)$.
Then $\Delta \phi = -2G\theta$, $\phi = 0$ on the circle, $\sigma_{yz} = G\theta x$ and $T = G\theta \cdot \pi a^4/2$.
Non-example: $\phi = \frac{G\theta}{2}(a^2 - x^2 - y^2) + 1$ gives the same stresses but is not zero on the boundary, so it violates the normalisation and gives the wrong torque from $2\int \phi$.
For a multiply connected cross-section, $\phi$ is constant on each boundary curve, with different constants.

## Explanations

### L1 human

The stress function packs two shear stresses into one function: each stress is a slope of the function.
Solving one Poisson equation then gives the whole stress field of a twisted bar.
