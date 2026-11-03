---
tag: 3XQ8W7ZKMB
kind: statement
role: theorem
name: Jeans's theorem
msc: [85A05, 70H33]
uses: [SJH7M2VCTE, 0262JP0NV9, 0EDKGA2FAK, 7147M98XNR, 4V8BT1ZD00]
about: [SJH7M2VCTE, 4V8BT1ZD00]
sources:
  - url: https://en.wikipedia.org/wiki/Jeans%27s_theorem
same_as:
  wikidata: Q6172415
  wikipedia: Jeans's theorem
---

## Statement

Let $\Phi \colon \R^3 \to \R$ be a smooth time-independent potential, and consider the orbits of the [[Hamiltonian system|0EDKGA2FAK]] $\dot x = v$, $\dot v = -\nabla \Phi(x)$ in phase space.
Let $f(x, v)$ be a continuously differentiable function.

1. $f$ is a steady solution of the collisionless Boltzmann equation $v \cdot \nabla_x f - \nabla \Phi \cdot \nabla_v f = 0$ if and only if $f$ is constant along every orbit.
   Equivalently, $f$ is an [[integral of motion|0262JP0NV9]].
2. If $I_1, \dots, I_k$ are continuously differentiable integrals of motion and $F \colon \R^k \to \R$ is continuously differentiable, then $f = F(I_1, \dots, I_k)$ is a steady solution.

## Remarks

The left-hand side of the equation is the derivative of $f$ along the flow, $\frac{d}{dt} f(x(t), v(t))$, so it vanishes exactly when $f$ is constant along orbits.
Part 2 follows from the chain rule, since each $I_m$ is constant along orbits.

Example: the energy $E = \frac{1}{2}\abs{v}^2 + \Phi(x)$ is always an integral, so every $f = F(E)$ with $F \ge 0$ is a steady solution; its velocity distribution is isotropic at each point.
In a spherical potential the size $L = \abs{x \times v}$ of the [[angular momentum|7147M98XNR]] is also an integral, and $f = F(E, L)$ gives spherical systems with anisotropic velocities.
For the Vlasov–Poisson system one must in addition choose $F$ so that the density $\int f \, dv$ generates $\Phi$ through Poisson's equation.

A stronger form holds for systems whose orbits are almost all regular.
It says that a steady $f$ is a function of the isolating integrals only, and it can fail when orbits are chaotic.

## Explanations

### L1 human

A galaxy that does not change shape must have the same number of stars at each point of each orbit, since stars just move along their orbits.
So the density of stars in positions and velocities can depend only on quantities that stay fixed along an orbit, such as the energy.
This turns the hard problem of finding steady galaxies into the easier problem of choosing a function of the energy and of a few other conserved quantities.

### L2 human

Jeans's theorem is the basic method to construct equilibrium models in [[stellar dynamics|4V8BT1ZD00]].
Choosing $F(E)$ and solving Poisson's equation for $\Phi$ gives the isotropic spherical models, such as the Plummer model and the isothermal sphere.
It is the special case for the collisionless Boltzmann equation of the general fact that a steady solution of a transport equation is constant along its characteristics.
