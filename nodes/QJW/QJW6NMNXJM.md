---
tag: QJW6NMNXJM
kind: problem
name: Boussinesq problem
msc: [74B05, 74M15, 74G05]
uses: [GQ3K59MRJP, 6W00ZECYT0, NWYZ9QBA84]
about: [T0R3FBPTJ2, GQ3K59MRJP]
sources:
  - url: https://en.wikipedia.org/wiki/Contact_mechanics
history:
  posed_by: Joseph Boussinesq
  first_stated: "1885"
---

## Problem

Let a homogeneous isotropic linear elastic material with shear modulus $\mu > 0$ and [[Poisson's ratio|NWYZ9QBA84]] $\nu \in (-1, 1/2)$ fill the half-space $\set{(x, y, z) \in \R^3 : z > 0}$.
A force of magnitude $P > 0$ acts at the origin, normal to the boundary plane and pointing into the body.
The rest of the boundary is free of traction.
Find the displacement field $u$ and the stress field, solutions of the static [[Lamé equations|GQ3K59MRJP]] without body force, that tend to $0$ at infinity.

## Remarks

The problem is solved in closed form.
With $r = \sqrt{x^2 + y^2}$ and $R = \sqrt{r^2 + z^2}$, the vertical displacement is
$$u_z = \frac{P}{4 \pi \mu R} \left( 2 (1 - \nu) + \frac{z^2}{R^2} \right),$$
the radial displacement is $u_r = \frac{P}{4 \pi \mu R} \left( \frac{r z}{R^2} - \frac{(1 - 2\nu) r}{R + z} \right)$, and the vertical normal stress is $\sigma_{zz} = -\frac{3 P z^3}{2 \pi R^5}$.
On the surface $z = 0$ this gives the settlement $u_z = \frac{(1 - \nu) P}{2 \pi \mu r}$, which is singular at the loaded point.
The vertical stress does not depend on the elastic constants.
By superposition, the solution for a distributed normal pressure on the surface is an integral of this one.
It is a starting point of the Hertz theory of [[contact mechanics|T0R3FBPTJ2]].
It is also used to compute stresses under foundations in soil mechanics.

## Explanations

### L1 human

Press a pencil point straight down onto a large, thick block of rubber.
The Boussinesq problem asks how every point of the block moves and how the pressure spreads into it.
The answer shows that the surface sinks most near the pencil, with a dent that falls off like one over the distance.
Engineers use it to estimate how much the ground settles under a building.
