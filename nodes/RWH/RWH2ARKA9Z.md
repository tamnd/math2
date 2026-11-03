---
tag: RWH2ARKA9Z
kind: definition
name: Perfect fluid
msc: ["83C55", "76Y05"]
defines: H4FNPG6ZY1
uses: [BY4QYYS788, REDZ92MKXX, Y59V040THG]
sources:
  - url: https://en.wikipedia.org/wiki/Perfect_fluid
---

## Definition

Let $(M, g)$ be a four-dimensional [[Lorentzian manifold|BY4QYYS788]] with signature $(-, +, +, +)$, and use units with $c = 1$.
A *perfect fluid* on $M$ is given by three data.
The first is a future-directed timelike vector field $u$ with $g(u, u) = -1$, the [[four-velocity|Y59V040THG]] of the fluid.
The others are two real functions $\rho$ and $p$ on $M$, the energy density and the pressure in the rest frame of the fluid.
Its [[stress–energy tensor|REDZ92MKXX]] is
$$T^{ab} = (\rho + p)\, u^a u^b + p\, g^{ab}.$$

## Remarks

In an orthonormal frame whose time vector is $u$, the components are $T = \mathrm{diag}(\rho, p, p, p)$.
Its trace is $g_{ab} T^{ab} = 3p - \rho$.
Often an equation of state $p = f(\rho)$ is added to close the equations of motion $\nabla_a T^{ab} = 0$.

Example: radiation, with $p = \rho/3$, is a perfect fluid with traceless stress–energy tensor, since $3p - \rho = 0$.
Dust is the case $p = 0$, with $T^{ab} = \rho\, u^a u^b$.

Non-example: take a uniform magnetic field of strength $B$ along the $z$ axis in flat space, in Heaviside–Lorentz units.
Its energy density is $\rho = B^2/2$, its pressures in the $x$ and $y$ directions are $B^2/2$, but its pressure in the $z$ direction is $-B^2/2$.
The pressure is not isotropic, so it is not a perfect fluid.
