---
tag: EH6K8VP1C3
kind: statement
role: theorem
name: Ertel's theorem on potential vorticity
msc: [76U05, 86A10, 76B47]
uses: [B3SXT9TWFA, CJW50K5HZB, ZJH90RWYQ5]
about: [B3SXT9TWFA]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_vorticity
---

## Statement

Consider a smooth flow in a frame rotating with constant angular velocity $\Omega \in \R^3$ (possibly $\Omega = 0$), with velocity $u$, density $\rho > 0$ and pressure $p$.
Assume the flow is [[inviscid|ZJH90RWYQ5]], so that
$$\frac{Du}{Dt} + 2 \Omega \times u = -\frac{1}{\rho} \nabla p - \nabla \Phi, \qquad \frac{D\rho}{Dt} + \rho \, \nabla \cdot u = 0,$$
for a body force potential $\Phi$, where $D/Dt$ is the [[material derivative|CJW50K5HZB]].
Let $\psi$ be a smooth scalar field that is conserved by each parcel, $D\psi/Dt = 0$.
Assume that $\nabla \psi \cdot (\nabla \rho \times \nabla p) = 0$.
This holds for instance when $\psi$ is a function of $\rho$ and $p$ only, or when the fluid is barotropic.
Let $\omega_a = \nabla \times u + 2\Omega$ be the absolute [[vorticity|B3SXT9TWFA]].
Then the potential vorticity
$$q = \frac{\omega_a \cdot \nabla \psi}{\rho}$$
is conserved by each parcel: $Dq/Dt = 0$.

## Remarks

The proof combines the vorticity equation for $\omega_a / \rho$, which reads $D(\omega_a/\rho)/Dt = ((\omega_a/\rho) \cdot \nabla) u + \nabla \rho \times \nabla p / \rho^3$, with the identity $D(\partial_i \psi)/Dt = \partial_i (D\psi/Dt) - \sum_j \partial_i u_j \, \partial_j \psi$.
The stretching terms cancel in the dot product, and the baroclinic term vanishes by the hypothesis on $\psi$.

Example: in the atmosphere one takes $\psi$ to be the potential temperature, which is conserved in adiabatic motion and is a function of $p$ and $\rho$.
A column of air between two surfaces of constant potential temperature that is stretched vertically must then spin faster.
This helps explain why cyclones tend to form on the lee side of mountain ranges.

Without the hypothesis on $\psi$, the baroclinic term $\nabla \psi \cdot (\nabla \rho \times \nabla p)/\rho^3$ in general makes $q$ change.

## Explanations

### L1 human

Potential vorticity combines how fast a parcel of fluid spins with how thick it is between two surfaces of some conserved property.
Ertel's theorem says that in a frictionless flow this combination stays fixed for each parcel.
So if a parcel is squeezed flat, it spins slower, and if it is stretched, it spins faster.

### L2 human

The theorem is a local consequence of [[Kelvin's circulation theorem|BWMB87Q6DM]] applied to small loops on surfaces of constant $\psi$.
In meteorology and oceanography, potential vorticity is the main conserved quantity of large-scale flows.
Together with an inversion principle, which recovers the flow from $q$, it reduces the dynamics of rotating stratified fluids to the transport of one scalar.
