---
tag: CGQT9BB4Q9
kind: statement
role: theorem
name: Taylor's constraint
msc: [76U05, 76W05, 86A25]
uses: [6HZRX3WSQD, TXQQQG9T2S, T8JWCBK9M6, 19AESAFHF9, RQKS2ACV95, SCYK4FMY59]
about: [19AESAFHF9]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamo_theory
---

## Statement

Let a sphere of radius $r_0$ be filled with an incompressible, electrically conducting fluid of constant density $\rho$, rotating with constant angular velocity $\boldsymbol{\Omega} = \Omega \hat{\mathbf{z}}$.
Use cylindrical coordinates $(s, \phi, z)$ with axis along $\boldsymbol{\Omega}$.
Assume the flow $\mathbf{u}$ satisfies $\nabla \cdot \mathbf{u} = 0$ in the sphere and $\mathbf{u} \cdot \mathbf{n} = 0$ on its boundary.
Let $p$ be the pressure, $\mathbf{J} \times \mathbf{B}$ the Lorentz force density, $\vartheta$ a scalar buoyancy field and $\mathbf{g}$ a radial gravity field.
Neglect inertia and viscosity, and assume the magnetostrophic balance
$$2 \rho \, \boldsymbol{\Omega} \times \mathbf{u} = -\nabla p + \mathbf{J} \times \mathbf{B} + \rho \, \vartheta \, \mathbf{g}.$$
For $0 < s < r_0$, let $C(s)$ be the part of the cylinder of radius $s$ about the axis that lies inside the sphere.
Then for every $s$,
$$\int_{C(s)} (\mathbf{J} \times \mathbf{B})_\phi \, dS = 0.$$

## Remarks

Proof idea: take the $\phi$-component of the balance and integrate over $C(s)$.
The pressure term integrates to zero because $p$ is single-valued around each circle.
The buoyancy term vanishes because a radial vector has no $\phi$-component.
The [[Coriolis|6HZRX3WSQD]] term gives $2\rho\Omega \int_{C(s)} u_s \, dS$, which is the net mass flux through the cylinder, and it is zero by incompressibility and the boundary condition.
Taylor proved this in 1963 for the Earth's core, where the [[Rossby number|SCYK4FMY59]] and the Ekman number are very small.
A field that satisfies the constraint is called a Taylor state.
Without the magnetic field, the same balance leads to the [[Taylor–Proudman theorem|RQKS2ACV95]].

## Explanations

### L1 human

Imagine the liquid core cut into nested cylinders around the rotation axis, like the layers of an onion turned on its side.
In a fast-rotating fluid without friction, each cylinder can be pushed sideways only if fluid crosses the cylinder, and incompressibility forbids a net crossing.
So the total twist that the magnetic force applies to each cylinder must be zero.
This is a strong condition on any magnetic field in the core.

### L2 human

In the [[geodynamo|19AESAFHF9]], Taylor's constraint is the starting point of the magnetostrophic theory of the core.
When a field departs from a Taylor state, the cylinders are free to rotate about the axis, and small inertia lets them oscillate.
These torsional oscillations are used to explain decadal changes in the length of day.
Numerical geodynamo models, which keep viscosity and inertia much larger than in the real core, satisfy the constraint only approximately.
The balance uses the [[Boussinesq approximation|TXQQQG9T2S]] of [[magnetohydrodynamics|T8JWCBK9M6]].
